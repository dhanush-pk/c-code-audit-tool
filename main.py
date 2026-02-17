from analyzer.scanner import read_all_c_files
from analyzer.rules_engine import check_rules
from analyzer.reporter import generate_report

def main():
    files_data = read_all_c_files("sample_code")
    issues = check_rules(files_data)
    generate_report(issues)

if __name__ == "__main__":
    main()
