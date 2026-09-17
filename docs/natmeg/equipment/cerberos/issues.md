---
title: Known issues
---

## Issues

??? failure "Cerberos is not starting"
    ## Rocky Linux 8 + NVIDIA
    ### Failure Recovery & Maintenance Manual

    This document covers **reliable recovery and maintenance** of NVIDIA GPUs on
    **Rocky Linux 8 / RHEL 8-derived systems**, specifically for cases where:

    - The GUI fails to start
    - `/dev/dri` is missing
    - `nouveau` reports **"unknown chipset"**
    - NVIDIA breaks after kernel updates
    - RPM Fusion package names appear inconsistent

    This manual is based on real-world recovery and reflects **correct EL8 behavior**.

    ---

    ### 1. Core Facts (Memorize These)

    #### Hardware & Drivers
    - Some NVIDIA GPUs **are not supported by `nouveau`**
    - Message: `nouveau: unknown chipset`
    - `nouveau` will **never work** on this hardware

    ### Graphics Stack
    - GUI requires **DRM**
    - DRM creates `/dev/dri`
    - On unsupported NVIDIA GPUs:
    - Only the **proprietary NVIDIA driver** provides DRM

    ### Kernel Rules (Critical)
    - NVIDIA kernel modules **must exactly match the running kernel**
    - Even minor version differences break the driver
    - EL8 repositories **do not keep old kernel graphics modules forever**

    ---

    ### 2. Golden Rules

    Disable **Secure Boot** (mandatory for NVIDIA)
    Boot into **multi-user.target** for repairs
    Pick **one kernel** and stay on it
    Use **akmod-nvidia**, not `dkms`
    Rebuild NVIDIA only for the **current kernel**

    Do **not** rely on `nouveau` on unsupported GPUs
    Do **not** chase old kernels
    Do **not** mix kernels and drivers
    Do **not** install random NVIDIA package names from blogs

    ---

    ### 3. Emergency: Boot Into Text Mode

    From GRUB, edit the boot entry and append: `systemd.unit=multi-user.target`

    After login, lock it in:

    ```bash
    sudo systemctl set-default multi-user.target
    ```

    ### 4. Verify Secure Boot (Mandatory)

    ```bash
    mokutil --sb-state # verify secure boot state
    ```

    Must show: `SecureBoot disabled`

    If enabled, disable Secure Boot in BIOS. There is no workaround.

    ### 5. Clean NVIDIA Reinstall (Minimal & Correct)

    #### Step 1 - Install a Supported Kernel Stack

    ```bash
    sudo dnf install -y \
    kernel \
    kernel-core \
    kernel-modules \
    kernel-modules-extra
    sudo reboot
    ```

    After reboot:

    ```bash
    uname -r
    ```

    This kernel is now your only supported kernel.

    #### Step 2 - Enable Required Repositories

    ```bash
    sudo dnf config-manager --set-enabled powertools

    sudo dnf install -y \
    https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm \
    https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm

    sudo dnf clean all
    sudo dnf makecache
    ```

    #### Step 3 - Install NVIDIA (Correct Package)

    ```bash
    sudo dnf install -y akmod-nvidia
    ```

    Do not manually install:

    - `xorg-x11-drv-nvidia`
    - `nvidia-driver`
    - `*-cuda`

    RPM Fusion resolves the correct userspace automatically on EL8.

    #### Step 4 - Build NVIDIA for This Kernel Only

    ```bash
    sudo akmods --force --kernel $(uname -r)

    ls /var/cache/akmods/nvidia/ # verify
    ```

    Expected: `kmod-nvidia-<kernel>.rpm`

    #### Step 5 - Install the Built Module Explicitly

    ```bash
    sudo dnf install -y /var/cache/akmods/nvidia/kmod-nvidia-*.rpm

    sudo modprobe nvidia # load driver

    lsmod | grep nvidia # verify
    ```

    Expected:

    ```bash
    nvidia
    nvidia_drm
    nvidia_modeset
    nvidia_uvm
    ```

    ### 6. Validate Graphics Stack

    ```bash
    ls /dev/dri
    ```

    Expected:

    ```bash
    card0
    renderD128
    ```

    Optional verification:

    ```bash
    command -v nvidia-smi
    nvidia-smi
    ```

    (Probably not going to work, but that is fine. GUI works even without `nvidia-smi`, but it is a good confirmation.)

    ### 7. Start the GUI

    ```bash
    sudo systemctl set-default graphical.target
    sudo systemctl start graphical.target
    ```

    You should now get:

    - Graphical login
    - Proper resolution
    - Hardware acceleration

    ### 8. Make the Fix Permanent

    Disable `nouveau` forever.

    ```bash
    sudo nano /etc/default/grub
    ```

    Set `GRUB_CMDLINE_LINUX="rhgb quiet module_blacklist=nouveau"`

    Rebuild:

    ```bash
    sudo grub2-mkconfig -o /boot/grub2/grub.cfg
    sudo dracut --force
    ```

    Pin the working kernel:

    ```bash
    sudo grub2-set-default 0
    sudo grub2-editenv list
    ```

    ### 9. Quick Diagnostic Table

    | Symptom | Meaning | Fix |
    |---|---|---|
    | `/dev/dri` missing | No DRM | Fix kernel / NVIDIA |
    | `nouveau: unknown chipset` | Unsupported GPU | Use NVIDIA |
    | `modprobe nvidia: key not available` | Secure Boot enabled | Disable Secure Boot (SB) |
    | GUI fails, text works | Driver mismatch | Rebuild NVIDIA |
    | akmods builds wrong kernel | Kernel drift | Pin kernel |

    ### 10. Final Takeaway

    On Rocky Linux 8, NVIDIA stability depends on kernel discipline.
    One kernel, one NVIDIA build, Secure Boot off, and the system is stable.

    ### 11. Additional possiblilities
    ### Disable Wayland (recommended on your system)

    Edit GDM configuration:

    ```bash
    sudo nano /etc/gdm/custom.conf
    ```

    Set:

    ```text
    [daemon]
    WaylandEnable=false
    ```

    Save, then restart GDM or reboot:

    ```bash
    sudo systemctl restart gdm
    ```
