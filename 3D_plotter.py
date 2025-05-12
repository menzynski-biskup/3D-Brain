import nibabel as nib
import numpy as np
from skimage import measure
import pyvista as pv
from NIfTI_converter import build_affine_from_dicom

# Load skull-stripped brain image
img = nib.load("MRI/NIfTI/T1_brain_good_bet.nii.gz") # Replace with your NIfTI file path
data = img.get_fdata()

# Optional: smooth or threshold if needed
data = np.clip(data, 0, np.percentile(data, 99))  # clip outliers

spacing = (1.0, 1.0, 0.498)
verts, faces, _, _ = measure.marching_cubes(data, level=np.percentile(data, 70), spacing=spacing)

# Create mesh and plot
faces_pv = np.hstack([np.full((faces.shape[0], 1), 3), faces]).astype(np.int32)
mesh = pv.PolyData(verts, faces_pv)
mesh = mesh.smooth(n_iter=100, relaxation_factor=0.01)
plotter = pv.Plotter()
plotter.add_mesh(mesh, color="lightgray", opacity=1.0)
plotter.add_axes()
plotter.show()