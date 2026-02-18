import sys

def generate_report(issues):
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

    print("\n============== SUMMARY ==============")
    print(f"HIGH   : {high}")
    print(f"MEDIUM : {medium}")
    print(f"LOW    : {low}")
    print(f"TOTAL  : {len(issues)}")
    print("=====================================\n")

    if high > 0:
        print("Build FAILED due to HIGH severity violations.")
        sys.exit(1)
    else:
        print("Build PASSED (No HIGH severity issues).")
        sys.exit(0)
