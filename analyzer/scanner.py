import os

# Supported C / C++ file extensions
SUPPORTED_EXTENSIONS = (".c", ".cpp", ".h", ".hpp", ".cc", ".cxx")

def is_c_cpp_file(filename):
    return filename.endswith(SUPPORTED_EXTENSIONS)


def read_all_c_files(folder_path):
    files_data = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            if is_c_cpp_file(file):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        files_data[full_path] = f.readlines()
                except Exception as e:
                    print(f"Could not read file: {full_path} -> {e}")

    return files_data
