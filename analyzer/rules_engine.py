import json
import re


def check_rules(files_data):
    with open("rules/rules.json") as f:
        rules = json.load(f)["rules"]

    issues = []

    for file_path, lines in files_data.items():
        for line_no, line in enumerate(lines, start=1):
            for rule in rules:

                # Use regex word boundary to avoid matching fgets/strncpy etc.
                pattern = r'\b' + re.escape(rule["pattern"]) + r'\b'

                if re.search(pattern, line):
                    issues.append({
                        "file": file_path,
                        "line": line_no,
                        "message": rule["message"],
                        "severity": rule["severity"],
                        "category": rule["category"],
                        "suggestion": rule["suggestion"]
                    })

    return issues
