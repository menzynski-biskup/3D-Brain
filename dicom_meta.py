import pydicom

dicom_path = "path/to/dicom/file.dcm"  # Replace with your DICOM file path

# Load a DICOM file
ds = pydicom.dcmread(dicom_path)

# Print all available DICOM metadata
print(ds)