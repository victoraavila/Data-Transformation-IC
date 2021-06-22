import os
import zipfile

def zip_this_folder(path = ""):
    all_files = os.listdir(path)
    csv_files = []

    for file in all_files:
        _, extension = os.path.splitext(file)
        
        if extension == ".csv":
            csv_files.append(file)

    with zipfile.ZipFile("quadros.zip", "w") as zipper:
        for file in csv_files:
            zipper.write(file, compress_type = zipfile.ZIP_DEFLATED)