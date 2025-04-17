import nibabel as nib
import numpy as np
import pydicom
from scan_series_identifier import series_dict

# Replace with the selected Series UID
target_uid = "T1_MRI_Series_UID"  # Example UID, replace with actual UID

# Get filepaths in this series
dicom_files = [fp for (fp, desc) in series_dict[target_uid]]

# Sort slices based on ImagePositionPatient (z-axis position)
slices = [pydicom.dcmread(fp) for fp in dicom_files]
slices.sort(key=lambda s: float(s.ImagePositionPatient[2]))

# Stack pixel arrays
volume = np.stack([s.pixel_array for s in slices], axis=-1)

# Get affine transform from DICOM metadata
px_spacing = slices[0].PixelSpacing
slice_thickness = slices[0].SliceThickness
affine = np.diag([*px_spacing, slice_thickness, 1])

# Save as NIfTI
nifti_img = nib.Nifti1Image(volume.astype(np.int16), affine)
nib.save(nifti_img, "MRI/NIfTI/T1_brain.nii.gz")
print("NIfTI file saved as: T1_brain.nii.gz")