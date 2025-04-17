import os
import pydicom
from collections import defaultdict

dicom_dir = "path/to/dicom/files"  # Replace with the directory containing DICOM files
series_dict = defaultdict(list)

for root, _, files in os.walk(dicom_dir):
    for file in sorted(files):
        if file.lower().endswith(".dcm") or file.startswith("IMG"):
            filepath = os.path.join(root, file)
            try:
                dcm = pydicom.dcmread(filepath, stop_before_pixels=True)
                series_uid = dcm.SeriesInstanceUID
                series_desc = getattr(dcm, "SeriesDescription", "No Description")
                series_dict[series_uid].append((filepath, series_desc))
            except Exception:
                continue

# Print summary of available series
for uid, items in series_dict.items():
    print(f"Series: {uid}")
    print(f"  Description: {items[0][1]}")
    print(f"  Slices: {len(items)}\n")