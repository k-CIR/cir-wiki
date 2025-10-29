---
title: Matlab and related tools
---

MATLAB is a proprietary multi-paradigm programming language and numeric computing environment developed by MathWorks. 

## License Activation
- MATLAB is pre-installed on the server
- First-time users must activate their license
- During initial launch, you'll be prompted to:
    1. Enter your MathWorks account credentials
    2. Authenticate your institutional license

## Accessing MATLAB

### Remote Connection
```bash
# Connect with X11 forwarding for GUI support
ssh -X <username>@193.10.16.5
```

### Launching MATLAB
```bash
# Start MATLAB in terminal mode
matlab

# Alternative: Start MATLAB with specific options
matlab -nodesktop    # No desktop environment
matlab -nosplash     # Skip splash screen
```

### Recommended Workflows

1. **Terminal Mode**
   ```bash
   # Ideal for scripting and batch processing
   matlab -nodesktop -r "your_script.m"
   ```

2. **Interactive GUI**
   ```bash
   # Full MATLAB desktop environment
   matlab
   ```

### Performance Optimization
- Use `-nodesktop` for computationally intensive tasks
- Close unnecessary GUI windows
- Utilize server's computational resources efficiently

## Matlab tools: SPM
SPM (Statistical Parametric Mapping) is a widely used MATLAB-based software suite for the analysis of brain imaging data sequences. 
The current release is designed for the analysis of fMRI, PET, SPECT, EEG and MEG.

### Available Versions
The following SPM versions are installed and available on the system:

- SPM12: Located at `/usr/local/spm12`
- SPM25: Located at `/usr/local/spm25`

You can launch SPM from MATLAB by navigating to the corresponding directory or adding it to your MATLAB path.

### Learn More
For full documentation, tutorials, and support, please visit the [official SPM website](https://www.fil.ion.ucl.ac.uk/spm/).

## Workspace Management
- Save your work frequently
- Use `save` command to preserve workspace
- Clear large variables to free memory
  ```matlab
  clear large_variable
  ```

## Advanced Usage

### Running MATLAB Scripts
```bash
# Execute MATLAB script from command line
matlab -batch "run('path/to/your/script.m')"
```

### Parallel Computing
- MATLAB supports server-side parallel processing
- Configure parallel computing toolbox for enhanced performance

## Resources
- [MathWorks Documentation](https://www.mathworks.com/help/matlab/)
- Institutional MATLAB Support Contact
