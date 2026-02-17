import json

def load_rules():
    with open("rules/rules.json", "r") as f:
        return json.load(f)["rules"]

def check_rules(files_data):
    rules = load_rules()
    issues = []

    for file_path, lines in files_data.items():
        for line_no, line in enumerate(lines, start=1):
            for rule in rules:
                if rule["pattern"] in line:
                    issues.append({
                        "file": file_path,
                        "line": line_no,
                        "issue": rule["message"]
                    })

    return issues
