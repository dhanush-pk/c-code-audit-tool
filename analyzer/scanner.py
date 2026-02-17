import os

def read_all_c_files(folder_path):
    files_data = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".c"):
                full_path = os.path.join(root, file)
                with open(full_path, "r") as f:
                    files_data[full_path] = f.readlines()

    return files_data
