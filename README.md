# 3D-Brain

A Python toolkit for processing and visualizing brain MRI data in 3D. This project provides utilities for converting DICOM files to NIfTI format, performing skull stripping, and creating 3D visualizations of brain scans.

## Overview

This project contains a set of scripts for working with brain MRI data:

- **DICOM to NIfTI conversion** with proper spatial affine matrix handling
- **Skull stripping** using deep learning (deepbrain library)
- **3D visualization** of brain surfaces using marching cubes algorithm
- **DICOM metadata exploration** for scan series identification

## Features

- Convert DICOM scan series to NIfTI format with correct spatial orientation
- Automatically identify and organize multiple scan series from DICOM directories
- Strip skull and non-brain tissue from MRI scans
- Generate smooth 3D surface meshes from brain volumes
- Interactive 3D visualization of brain structures

## Requirements

The project requires the following Python libraries:

```
nibabel
numpy
pydicom
scikit-image
pyvista
deepbrain
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/menzynski-biskup/3D-Brain.git
cd 3D-Brain
```

2. Install the required dependencies:
```bash
pip install nibabel numpy pydicom scikit-image pyvista deepbrain
```

## Usage

### 1. Explore DICOM Metadata

Use `dicom_meta.py` to examine the metadata of a single DICOM file:

```python
# Edit the file to set your DICOM path
dicom_path = "path/to/dicom/file.dcm"
python dicom_meta.py
```

### 2. Identify Scan Series

Use `scan_series_identifier.py` to identify and list all scan series in a DICOM directory:

```python
# Edit the file to set your DICOM directory
dicom_dir = "path/to/dicom"
python scan_series_identifier.py
```

This will output all available series with their descriptions and slice counts.

### 3. Convert DICOM to NIfTI

Use `NIfTI_converter.py` to convert a specific DICOM series to NIfTI format:

```python
# Edit the file to set:
# - target_uid: The Series Instance UID you want to convert
# - dicom_dir: The directory containing DICOM files
python NIfTI_converter.py
```

This script will:
- Load all DICOM slices from the specified series
- Build a proper spatial affine matrix from DICOM metadata
- Stack slices into a 3D volume
- Save as a NIfTI file with correct spatial orientation

### 4. Skull Stripping

Use `skull_stripping.py` to remove skull and non-brain tissue:

```python
# Edit the file to set your NIfTI input path
img = nib.load("path/to/NIfTI/file.nii.gz")
python skull_stripping.py
```

This uses the deepbrain library to create a brain mask and extract only brain tissue.

### 5. 3D Visualization

Use `3D_plotter.py` to create an interactive 3D visualization of the brain surface:

```python
# Edit the file to set your skull-stripped NIfTI path
img = nib.load("MRI/NIfTI/T1_brain_good_bet.nii.gz")
python 3D_plotter.py
```

This script will:
- Load the skull-stripped brain volume
- Apply the marching cubes algorithm to extract the brain surface
- Smooth the mesh for better visualization
- Display an interactive 3D view

## Workflow

A typical workflow for processing brain MRI data:

1. **Identify series**: Run `scan_series_identifier.py` to find available scan series
2. **Convert to NIfTI**: Use `NIfTI_converter.py` to convert your desired series
3. **Strip skull**: Process the NIfTI file with `skull_stripping.py`
4. **Visualize in 3D**: Create a 3D mesh and visualize with `3D_plotter.py`

## Notes

- Make sure to update file paths in each script before running
- The project assumes T1-weighted MRI scans but can be adapted for other modalities
- 3D visualization quality can be adjusted by modifying the marching cubes threshold and smoothing parameters

## License

This project is available for educational and research purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
