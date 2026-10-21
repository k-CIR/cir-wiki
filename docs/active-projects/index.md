# Active Projects

This page shows an overview of active research projects at CIR and the researchers involved. The graph below maps researchers to the projects they contribute to.

<div class="researcher-graph-wrapper">
  <div class="researcher-graph-controls">
    <input type="text" id="graph-filter" class="researcher-graph-filter" placeholder="Filter by researcher or project…">
    <div class="researcher-graph-legend">
      <span><span class="rg-legend-dot rg-legend-dot--researcher"></span>Researcher</span>
      <span><span class="rg-legend-dot rg-legend-dot--active"></span>Active project</span>
      <span><span class="rg-legend-dot rg-legend-dot--planning"></span>Planning</span>
      <span><span class="rg-legend-dot rg-legend-dot--completed"></span>Completed</span>
    </div>
  </div>
  <div id="modality-filter" class="researcher-graph-modalities">
    <span class="researcher-graph-modalities__label">Modality:</span>
    <button type="button" class="rg-modality-chip" data-modality="EEG">EEG</button>
    <button type="button" class="rg-modality-chip" data-modality="MEG">MEG</button>
    <button type="button" class="rg-modality-chip" data-modality="3T MRI">3T MRI</button>
    <button type="button" class="rg-modality-chip" data-modality="7T MRI">7T MRI</button>
    <button type="button" class="rg-modality-chip" data-modality="PET-CT">PET-CT</button>
  </div>
  <div id="researcher-graph-tooltip" class="researcher-graph-tooltip"></div>
  <svg id="researcher-graph-svg" height="560"></svg>
  <div class="researcher-graph-hint">
    Hover for details &nbsp;·&nbsp; Click a node to highlight connections &nbsp;·&nbsp; Drag to rearrange &nbsp;·&nbsp; Scroll to zoom
  </div>
</div>

<div class="project-list-section">
  <h2>Projects</h2>
  <div id="project-list" class="project-list"></div>
</div>

