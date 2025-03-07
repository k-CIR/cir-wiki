**Problem:** The various MNE functions for plotting does not work. Especially 3D graphics such as plotting source estimates on cortical surfaces. In Spyder it might even crash the entire Python session.

**Cause:** might be some incompatibility between 3D render function and video drive (or lack thereof on Compute). Possible also inconsistencies in Python dependencies.

**Solution:** run this snippet of code in the terminal before starting Spyder: export MESA_GL_VERSION_OVERRIDE=3.3. Also, make sure that you install MNE according to the [install instructions.](Set-up-MNE-Python-on-Compute).
