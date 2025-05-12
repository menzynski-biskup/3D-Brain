import nibabel as nib
import numpy as np
import pydicom
from scan_series_identifier import get_series_dict

def build_affine_from_dicom(slices):
    """Build a spatial affine matrix from DICOM slice metadata."""
    import numpy as np

    orientation = np.array(slices[0].ImageOrientationPatient).reshape(2, 3)
    row_cosine = orientation[0]
    col_cosine = orientation[1]
    slice_cosine = np.cross(row_cosine, col_cosine)

    # Pixel spacing from DICOM: [row_spacing, col_spacing]
    row_spacing, col_spacing = map(float, slices[0].PixelSpacing)

    # Compute slice spacing from adjacent positions, fallback to thickness
    try:
        positions = [np.array(s.ImagePositionPatient, dtype=np.float32) for s in slices]
        spacings = [np.linalg.norm(positions[i+1] - positions[i]) for i in range(len(positions)-1)]
        slice_spacing = np.mean(spacings)
    except Exception:
        slice_spacing = float(getattr(slices[0], 'SpacingBetweenSlices', slices[0].SliceThickness))

    # Build affine
    affine = np.eye(4)
    affine[:3, 0] = col_cosine * col_spacing
    affine[:3, 1] = row_cosine * row_spacing
    affine[:3, 2] = slice_cosine * slice_spacing
    affine[:3, 3] = np.array(slices[0].ImagePositionPatient)

    print("Voxel size (mm):", np.round([col_spacing, row_spacing, slice_spacing], 3))
    print("Affine matrix:\n", np.round(affine, 3))
    return affine

# Replace with the selected Series UID
target_uid = "1.3.12.2.1107.5.2.40.49051.2013112511491513754413626.0.0.0"  # Example UID, replace with actual UID

series_dict = get_series_dict(dicom_dir = "path/to/dicom/files")  # Replace with your DICOM directoryq
# Get filepaths in this series
dicom_files = [fp for (fp, desc) in series_dict[target_uid]]

# Sort slices based on ImagePositionPatient (z-axis position)
slices = [pydicom.dcmread(fp) for fp in dicom_files]
slices.sort(key=lambda s: float(s.ImagePositionPatient[2]))

# Stack pixel arrays
volume = np.stack([s.pixel_array for s in slices], axis=-1)

affine = build_affine_from_dicom(slices)

# Save as NIfTI
nifti_img = nib.Nifti1Image(volume.astype(np.int16), affine)
nib.save(nifti_img, "MRI/NIfTI/T1_brain_good.nii.gz")
print("NIfTI file saved with corrected affine: T1_brain_good.nii.gz")