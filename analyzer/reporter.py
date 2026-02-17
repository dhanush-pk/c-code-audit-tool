import sys

def generate_report(issues):
    print("----- AUTOMATED C CODE AUDIT REPORT -----")

    if not issues:
        print("No issues found. Build PASSED.")
        sys.exit(0)

    for issue in issues:
        print(f"{issue['file']} | Line {issue['line']} | {issue['issue']}")

    print("Build FAILED due to coding standard violations.")
    sys.exit(1)
