import argparse
from analyzer.scanner import read_all_c_files
from analyzer.rules_engine import check_rules
from analyzer.reporter import generate_report
from auto_fixer import fix_file


def main():
    parser = argparse.ArgumentParser(
        description="Automated C/C++ Code Audit Tool"
    )

    parser.add_argument(
        "--path",
        type=str,
        default="sample_code",
        help="Path to scan (default: sample_code)"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Generate JSON report"
    )

    parser.add_argument(
        "--fail-on",
        type=str,
        choices=["HIGH", "MEDIUM", "LOW", "NONE"],
        default="HIGH",
        help="Fail build on severity level (default: HIGH)"
    )

    # ✅ ADD THIS
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically fix simple unsafe patterns"
    )

    args = parser.parse_args()

    # Read files
    files_data = read_all_c_files(args.path)

    # -------- AUTO FIX SECTION --------
    if args.fix:
        print("\n========== AUTO FIX MODE ENABLED ==========\n")

        fixed_any = False

        for file_path in files_data.keys():
            if fix_file(file_path):
                print(f"Fixed issues in {file_path}")
                fixed_any = True

        if fixed_any:
            print("\nRe-scanning after auto-fix...\n")
            files_data = read_all_c_files(args.path)
        else:
            print("No auto-fixable issues found.\n")
    # -----------------------------------

    # Check rules
    issues = check_rules(files_data)

    # Generate report
    generate_report(
        issues,
        export_json=args.json,
        fail_on=args.fail_on
    )


if __name__ == "__main__":
    main()
