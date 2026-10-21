/* Researcher–Project force-directed graph for the Active Projects page.
 * Requires D3 v7 to be loaded before this script.
 * Works with MkDocs Material instant navigation via document$.subscribe().
 */
(function () {
  "use strict";

  function init() {
    var svgEl = document.getElementById("researcher-graph-svg");
    if (!svgEl) return;

    // Clear previous render (triggered again on instant-navigation re-entry)
    d3.select("#researcher-graph-svg").selectAll("*").remove();

    var wrapper = svgEl.closest(".researcher-graph-wrapper");
    var width = (wrapper ? wrapper.clientWidth : 800) || 800;
    var height = 560;

    fetch("./data.json")
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        render(data, width, height);
      })
      .catch(function (err) {
        console.error("[researcher-graph] Failed to load data.json:", err);
      });
  }

  function render(rawData, width, height) {
    // Deep-copy so D3 can mutate freely across re-renders
    var nodes = rawData.nodes.map(function (d) { return Object.assign({}, d); });
    var links = rawData.links.map(function (d) { return Object.assign({}, d); });

    // ── Colour scheme (respects Material light / dark mode) ──────────────────
    var isDark = document.body.getAttribute("data-md-color-scheme") === "slate";
    var C = {
      researcher : isDark ? "#60a5fa" : "#2563eb",
      projectActive   : isDark ? "#fb923c" : "#ea580c",
      projectPlanning : isDark ? "#a78bfa" : "#7c3aed",
      projectCompleted: "#3bb367",
      link       : isDark ? "rgba(255,255,255,0.18)" : "rgba(0,0,0,0.14)",
      label      : isDark ? "#d1d5db" : "#1f2937",
      labelStroke: isDark ? "#0f172a" : "#ffffff",
      dim        : 0.12,
    };

    function nodeColor(d) {
      if (d.type === "researcher") return C.researcher;
      if (d.status === "Planning") return C.projectPlanning;
      if (d.status === "Completed") return C.projectCompleted;
      return C.projectActive;
    }

    // ── SVG setup ─────────────────────────────────────────────────────────────
    var svg = d3
      .select("#researcher-graph-svg")
      .attr("width", "100%")
      .attr("height", height)
      .attr("viewBox", [0, 0, width, height]);

    var g = svg.append("g").attr("class", "rg-zoom-layer");

    svg.call(
      d3.zoom()
        .scaleExtent([0.35, 4])
        .on("zoom", function (event) { g.attr("transform", event.transform); })
    );

    // ── Force simulation ───────────────────────────────────────────────────────
    var simulation = d3.forceSimulation(nodes)
      .force("link",    d3.forceLink(links).id(function (d) { return d.id; }).distance(130))
      .force("charge",  d3.forceManyBody().strength(-420))
      .force("center",  d3.forceCenter(width / 2, height / 2))
      .force("collide", d3.forceCollide(52));

    // ── Links ──────────────────────────────────────────────────────────────────
    var linkSel = g.append("g")
      .attr("class", "rg-links")
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke", C.link)
      .attr("stroke-width", 1.8);

    // ── Nodes ──────────────────────────────────────────────────────────────────
    var drag = d3.drag()
      .on("start", function (event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on("drag", function (event, d) {
        d.fx = event.x; d.fy = event.y;
      })
      .on("end", function (event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null; d.fy = null;
      });

    var nodeSel = g.append("g")
      .attr("class", "rg-nodes")
      .selectAll("g")
      .data(nodes)
      .join("g")
      .attr("class", function (d) { return "rg-node rg-node--" + d.type; })
      .style("cursor", "pointer")
      .call(drag);

    nodeSel.append("circle")
      .attr("r", function (d) { return d.type === "project" ? 26 : 19; })
      .attr("fill", nodeColor)
      .attr("stroke", C.labelStroke)
      .attr("stroke-width", 2);

    nodeSel.append("text")
      .text(function (d) { return d.label; })
      .attr("text-anchor", "middle")
      .attr("dy", function (d) { return d.type === "project" ? 43 : 35; })
      .attr("font-size", "11px")
      .attr("font-family", "var(--md-text-font, sans-serif)")
      .attr("fill", C.label)
      .attr("paint-order", "stroke")
      .attr("stroke", C.labelStroke)
      .attr("stroke-width", 3)
      .attr("stroke-linejoin", "round")
      .call(wrapText, 90); // wrap long labels

    // ── Tooltip ────────────────────────────────────────────────────────────────
    var tooltip = d3.select("#researcher-graph-tooltip");

    nodeSel
      .on("mouseover", function (event, d) {
        var html = "<strong>" + d.label + "</strong>";
        if (d.type === "researcher") {
          html += "<br><em>" + d.role + "</em><br>" + d.department;
        } else {
          html += "<br><em>Status: " + d.status + "</em><br>" + d.description;
          if (Array.isArray(d.modalities) && d.modalities.length) {
            html += "<br><em>Modalities: " + d.modalities.join(", ") + "</em>";
          }
        }
        tooltip.html(html).style("opacity", "1");
      })
      .on("mousemove", function (event) {
        var rect = document.getElementById("researcher-graph-svg").getBoundingClientRect();
        tooltip
          .style("left", (event.clientX - rect.left + 14) + "px")
          .style("top",  (event.clientY - rect.top  - 14) + "px");
      })
      .on("mouseout", function () {
        tooltip.style("opacity", "0");
      });

    // ── Click-to-highlight ─────────────────────────────────────────────────────
    var selectedId = null;

    // Map of project node id -> { item, header, body } DOM refs, populated by buildList()
    var listItemEls = {};
    // Default (data) order of project ids, populated by buildList()
    var projectOrder = [];
    // Active modality filter chips (e.g. "EEG", "MEG", "3T MRI", "7T MRI", "PET-CT")
    var activeModalities = new Set();

    function collapseAllListItems() {
      Object.keys(listItemEls).forEach(function (id) {
        var el = listItemEls[id];
        el.item.classList.remove("is-expanded");
        el.header.setAttribute("aria-expanded", "false");
      });
    }

    function expandListItem(id) {
      var el = listItemEls[id];
      if (!el) return;
      el.item.classList.add("is-expanded");
      el.header.setAttribute("aria-expanded", "true");
    }

    function clearListDim() {
      Object.keys(listItemEls).forEach(function (id) {
        listItemEls[id].item.classList.remove("rg-dim");
      });
    }

    // Reorders the list DOM so `topId` (a project id) is first, or restores the
    // original data order when `topId` is null. List-click driven selection never
    // calls this, so clicking inside the list never shuffles entries.
    function setListOrder(topId) {
      if (!listContainer) return;
      var order = topId
        ? [topId].concat(projectOrder.filter(function (id) { return id !== topId; }))
        : projectOrder.slice();
      order.forEach(function (id) {
        var el = listItemEls[id];
        if (el) listContainer.appendChild(el.item);
      });
    }

    function resetHighlight() {
      selectedId = null;
      nodeSel.style("opacity", 1);
      linkSel.style("opacity", 1);
      collapseAllListItems();
      clearListDim();
      setListOrder(null);
    }

    // `opts.reorder`: when true (graph node clicks) and `d` is a project, the
    // matching list item is moved to the top so it's visible without scrolling.
    // List-item clicks pass no `opts`, so the list order never changes there.
    function highlightNode(d, opts) {
      selectedId = d.id;
      var neighbors = new Set([d.id]);
      links.forEach(function (l) {
        var s = l.source.id !== undefined ? l.source.id : l.source;
        var t = l.target.id !== undefined ? l.target.id : l.target;
        if (s === d.id) neighbors.add(t);
        if (t === d.id) neighbors.add(s);
      });
      nodeSel.style("opacity", function (n) {
        return neighbors.has(n.id) ? 1 : C.dim;
      });
      linkSel.style("opacity", function (l) {
        var s = l.source.id !== undefined ? l.source.id : l.source;
        var t = l.target.id !== undefined ? l.target.id : l.target;
        return (s === d.id || t === d.id) ? 1 : C.dim;
      });

      // Projects related to the selection: the project itself when a project
      // node is selected, or its connected projects when a researcher is
      // selected (links only ever connect a researcher to a project).
      var relatedProjectIds = d.type === "project"
        ? new Set([d.id])
        : new Set(Array.from(neighbors).filter(function (id) { return id !== d.id; }));

      collapseAllListItems();
      Object.keys(listItemEls).forEach(function (id) {
        listItemEls[id].item.classList.toggle("rg-dim", !relatedProjectIds.has(id));
      });

      if (d.type === "project") {
        expandListItem(d.id);
        if (opts && opts.reorder) {
          setListOrder(d.id);
        }
      }
    }

    svg.on("click", resetHighlight);

    nodeSel.on("click", function (event, d) {
      event.stopPropagation();
      if (selectedId === d.id) { resetHighlight(); } else { highlightNode(d, { reorder: true }); }
    });

    // ── Project list (below the graph) ──────────────────────────────────────────
    var listContainer = document.getElementById("project-list");
    if (listContainer) {
      buildList(listContainer);
    }

    function buildList(container) {
      container.innerHTML = "";
      listItemEls = {};
      projectOrder = [];

      var projects = nodes.filter(function (d) { return d.type === "project"; });

      projects.forEach(function (p) {
        projectOrder.push(p.id);

        var item = document.createElement("div");
        item.className = "project-list-item";
        item.dataset.id = p.id;

        var header = document.createElement("button");
        header.type = "button";
        header.className = "project-list-item__header";
        header.setAttribute("aria-expanded", "false");

        var statusClass = p.status === "Planning"
          ? "project-list-item__badge--planning"
          : p.status === "Completed"
          ? "project-list-item__badge--completed"
          : "project-list-item__badge--active";

        var modalitiesHtml = (Array.isArray(p.modalities) ? p.modalities : [])
          .map(function (m) { return '<span class="project-list-item__modality">' + escapeHtml(m) + "</span>"; })
          .join("");

        header.innerHTML =
          '<span class="project-list-item__title">' + escapeHtml(p.label) + "</span>" +
          '<span class="project-list-item__modalities">' + modalitiesHtml + "</span>" +
          '<span class="project-list-item__badge ' + statusClass + '">' + escapeHtml(p.status) + "</span>" +
          '<span class="project-list-item__chevron" aria-hidden="true">\u203A</span>';

        var body = document.createElement("div");
        body.className = "project-list-item__body";

        var contributors = links
          .filter(function (l) {
            var s = l.source.id !== undefined ? l.source.id : l.source;
            var t = l.target.id !== undefined ? l.target.id : l.target;
            return s === p.id || t === p.id;
          })
          .map(function (l) {
            var s = l.source.id !== undefined ? l.source.id : l.source;
            var t = l.target.id !== undefined ? l.target.id : l.target;
            var researcherId = s === p.id ? t : s;
            return nodes.find(function (n) { return n.id === researcherId; });
          })
          .filter(Boolean);

        var contributorsHtml = contributors
          .map(function (r) {
            return "<li>" + escapeHtml(r.label) +
              ' <span class="project-list-item__role">(' + escapeHtml(r.role) + ", " + escapeHtml(r.department) + ")</span></li>";
          })
          .join("");

        body.innerHTML =
          '<p class="project-list-item__description">' + escapeHtml(p.description) + "</p>" +
          '<p class="project-list-item__contributors-label">Contributors:</p>' +
          '<ul class="project-list-item__contributors">' + contributorsHtml + "</ul>";

        item.appendChild(header);
        item.appendChild(body);
        container.appendChild(item);

        listItemEls[p.id] = { item: item, header: header, body: body };

        header.addEventListener("click", function () {
          if (selectedId === p.id) { resetHighlight(); } else { highlightNode(p); }
        });
      });
    }

    function escapeHtml(str) {
      return String(str == null ? "" : str).replace(/[&<>"']/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
      });
    }

    // ── Text filter ────────────────────────────────────────────────────────────
    var filterInput = document.getElementById("graph-filter");
    if (filterInput) {
      filterInput.value = "";
      // Use .oninput (property) to avoid stacking listeners on re-render
      filterInput.oninput = function () {
        var q = this.value.trim().toLowerCase();
        if (!q) { resetHighlight(); return; }
        var matchIds = new Set(
          nodes
            .filter(function (n) { return n.label.toLowerCase().includes(q); })
            .map(function (n) { return n.id; })
        );
        nodeSel.style("opacity", function (n) { return matchIds.has(n.id) ? 1 : C.dim; });
        linkSel.style("opacity", C.dim);
        Object.keys(listItemEls).forEach(function (id) {
          listItemEls[id].item.classList.toggle("rg-dim", !matchIds.has(id));
        });
      };
    }

    // ── Modality filter ─────────────────────────────────────────────────────────
    // Highlights projects (and their connected researchers) whose `modalities`
    // array matches any of the currently active chips, both in the graph and
    // in the list below it. Matching is OR across selected chips.
    function applyModalityFilter() {
      var matchedProjectIds = new Set(
        nodes
          .filter(function (n) {
            return n.type === "project" &&
              Array.isArray(n.modalities) &&
              n.modalities.some(function (m) { return activeModalities.has(m); });
          })
          .map(function (n) { return n.id; })
      );

      var matchedIds = new Set(matchedProjectIds);
      links.forEach(function (l) {
        var s = l.source.id !== undefined ? l.source.id : l.source;
        var t = l.target.id !== undefined ? l.target.id : l.target;
        if (matchedProjectIds.has(s)) matchedIds.add(t);
        if (matchedProjectIds.has(t)) matchedIds.add(s);
      });

      nodeSel.style("opacity", function (n) { return matchedIds.has(n.id) ? 1 : C.dim; });
      linkSel.style("opacity", function (l) {
        var s = l.source.id !== undefined ? l.source.id : l.source;
        var t = l.target.id !== undefined ? l.target.id : l.target;
        return (matchedProjectIds.has(s) || matchedProjectIds.has(t)) ? 1 : C.dim;
      });

      Object.keys(listItemEls).forEach(function (id) {
        listItemEls[id].item.classList.toggle("rg-dim", !matchedProjectIds.has(id));
      });
    }

    var modalityFilterEl = document.getElementById("modality-filter");
    if (modalityFilterEl) {
      var modalityChips = modalityFilterEl.querySelectorAll(".rg-modality-chip");
      modalityChips.forEach(function (btn) {
        btn.setAttribute("aria-pressed", "false");
        // Use .onclick (property) to avoid stacking listeners on re-render
        btn.onclick = function () {
          var modality = btn.dataset.modality;
          if (activeModalities.has(modality)) {
            activeModalities.delete(modality);
            btn.classList.remove("is-active");
            btn.setAttribute("aria-pressed", "false");
          } else {
            activeModalities.add(modality);
            btn.classList.add("is-active");
            btn.setAttribute("aria-pressed", "true");
          }
          if (activeModalities.size === 0) {
            resetHighlight();
          } else {
            applyModalityFilter();
          }
        };
      });
    }

    // ── Tick ───────────────────────────────────────────────────────────────────
    simulation.on("tick", function () {
      linkSel
        .attr("x1", function (d) { return d.source.x; })
        .attr("y1", function (d) { return d.source.y; })
        .attr("x2", function (d) { return d.target.x; })
        .attr("y2", function (d) { return d.target.y; });
      nodeSel.attr("transform", function (d) {
        return "translate(" + d.x + "," + d.y + ")";
      });
    });
  }

  // ── Utility: wrap SVG text to a max pixel width ────────────────────────────
  function wrapText(textSel, maxWidth) {
    textSel.each(function () {
      var text  = d3.select(this);
      var words = text.text().split(/\s+/).reverse();
      var lineHeight = 13; // px
      var dy = parseFloat(text.attr("dy")) || 0;
      var tspan = text.text(null)
        .append("tspan")
        .attr("x", 0)
        .attr("dy", dy + "px");

      var line  = [];
      var lineNum = 0;
      var word;

      while ((word = words.pop())) {
        line.push(word);
        tspan.text(line.join(" "));
        if (tspan.node().getComputedTextLength() > maxWidth && line.length > 1) {
          line.pop();
          tspan.text(line.join(" "));
          line = [word];
          tspan = text.append("tspan")
            .attr("x", 0)
            .attr("dy", (++lineNum * lineHeight) + "px")
            .text(word);
        }
      }
    });
  }

  // ── Bootstrap ─────────────────────────────────────────────────────────────
  if (typeof document$ !== "undefined") {
    // MkDocs Material instant navigation
    document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
