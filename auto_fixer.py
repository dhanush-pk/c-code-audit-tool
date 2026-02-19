import re
import os

def fix_file(file_path):
    """
    Automatically fixes simple unsafe C/C++ functions.
    Currently supports:
    - gets()  -> fgets()
    - strcpy() -> strncpy()
    """

    # Only process C/C++ files
    if not file_path.endswith((".c", ".cpp")):
        return False

    if not os.path.exists(file_path):
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified = False

    for i in range(len(lines)):

        # Fix gets()
        if "gets(" in lines[i]:
            lines[i] = re.sub(
                r'gets\((.*?)\)',
                r'fgets(\1, sizeof(\1), stdin)',
                lines[i]
            )
            modified = True

        # Fix strcpy()
        if "strcpy(" in lines[i]:
            lines[i] = re.sub(
                r'strcpy\((.*?),(.*?)\)',
                r'strncpy(\1,\2,sizeof(\1))',
                lines[i]
            )
            modified = True

    # Write changes back if modified
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    return modified
