import nibabel as nib
import numpy as np
from deepbrain import Extractor

# Load your NIfTI file
img: nib.Nifti1Image = nib.load("path/to/NIfTI/file.nii.gz")  # Replace with your NIfTI file path
img_data = img.get_fdata()

# Run deepbrain mask extraction
ext = Extractor()
probability_mask = ext.run(img_data)

# Threshold the probability map to create binary mask
brain_mask = probability_mask > 0.5

# Apply mask to original image
brain_only = img_data * brain_mask

# Save masked brain image
masked_img = nib.Nifti1Image(brain_only.astype(np.float32), img.affine)
nib.save(masked_img, "T1_brain_stripped.nii.gz")
print("Skull stripped image saved as: T1_brain_stripped.nii.gz")