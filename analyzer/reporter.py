import sys
import json


def generate_report(issues, export_json=False, fail_on="HIGH"):
    print("========== AUTOMATED C CODE AUDIT REPORT ==========\n")

    high = 0
    medium = 0
    low = 0

    for issue in issues:
        print(f"{issue['file']} | Line {issue['line']}")
        print(f"Category : {issue['category']}")
        print(f"Severity : {issue['severity']}")
        print(f"Issue    : {issue['message']}")
        print(f"Fix      : {issue['suggestion']}")
        print("-" * 55)

        if issue["severity"] == "HIGH":
            high += 1
        elif issue["severity"] == "MEDIUM":
            medium += 1
        elif issue["severity"] == "LOW":
            low += 1

    summary = {
        "HIGH": high,
        "MEDIUM": medium,
        "LOW": low,
        "TOTAL": len(issues)
    }

    print("\n============== SUMMARY ==============")
    print(f"HIGH   : {high}")
    print(f"MEDIUM : {medium}")
    print(f"LOW    : {low}")
    print(f"TOTAL  : {len(issues)}")
    print("=====================================\n")

    # JSON Export (if enabled)
    if export_json:
        report_data = {
            "issues": issues,
            "summary": summary
        }

        with open("audit_report.json", "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)

        print("JSON report generated: audit_report.json\n")

    # Fail logic
    severity_count = {
        "HIGH": high,
        "MEDIUM": medium,
        "LOW": low
    }

    if fail_on != "NONE" and severity_count.get(fail_on, 0) > 0:
        print(f"Build FAILED due to {fail_on} severity violations.")
        sys.exit(1)
    else:
        print("Build PASSED.")
        sys.exit(0)
