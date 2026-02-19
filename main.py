import argparse
from analyzer.scanner import read_all_c_files
from analyzer.rules_engine import check_rules
from analyzer.reporter import generate_report


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

    args = parser.parse_args()

    # Read files
    files_data = read_all_c_files(args.path)

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
