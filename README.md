📌 AI-Powered C/C++ Static Code Analyzer with Auto-Fix

🔍 Overview



This project is an automated C/C++ code audit tool that:



Detects insecure coding patterns



Categorizes issues by severity (HIGH, MEDIUM, LOW)



Blocks commits based on severity



Automatically fixes simple vulnerabilities



Re-validates code after fixing



🚀 Features



✔ Static code scanning

✔ Rule-based security detection

✔ JSON report generation

✔ Severity-based build failure

✔ Auto-remediation (--fix mode)

✔ Git pre-commit integration



🛠 Supported Vulnerabilities



gets() usage



strcpy() usage



Format string risks



Extendable via rules.json



▶ How to Run

Basic Scan

python main.py



Auto Fix Mode

python main.py --fix



Generate JSON Report

python main.py --json



🔒 Pre-Commit Integration



Update:



.git/hooks/pre-commit





Add:



python main.py --fix





This prevents insecure code from being committed.



📊 Example Output

AUTO FIX MODE ENABLED

Fixed issues in sample\_code/test.c

Re-scanning after auto-fix...



Build PASSED.



📈 Future Improvements



Advanced pattern detection



AI-based contextual fixes



VS Code extension integration



CI/CD pipeline support

:

🎯 Problem solved:

C/C++ code has security issues that compilers often miss — this tool finds them automatically.

🧱 Modular Design:
scanner → rule engine → reporter → auto-fix → CI

⚙️ Extensibility:
Rules are JSON, so new checks can be added without changing code.

🧪 CI Integration:
GitHub Actions runs analysis on every push/PR → this helps enforce quality early.

💡 Future Scope:
Add AST-based parsing, improve rule detection, integrate VS Code plugin.

👨‍💻 Author



Dhanush

BCA | AI \& Security Enthusiast

