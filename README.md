🛡️ C/C++ Static Code Audit Tool

A lightweight Static Code Analysis Tool designed to detect security vulnerabilities in C and C++ source files.
This tool scans source code, identifies insecure coding patterns, classifies issues by severity levels, and generates structured audit reports with suggested remediation steps.

📌 Project Overview

C and C++ are powerful system-level programming languages but are highly susceptible to memory-related vulnerabilities such as:

Buffer overflows

Unsafe input handling

Insecure standard library usage

Potential memory corruption risks

This project demonstrates how automated static analysis can be integrated into a development workflow to detect security risks before deployment.

The tool simulates a simplified DevSecOps pipeline by:

Performing rule-based code scanning

Categorizing vulnerabilities

Enforcing build failures for critical issues

Supporting automation via CLI

🎯 Objectives

Detect unsafe coding patterns in C/C++ source files

Provide severity-based vulnerability classification

Suggest safer alternatives for insecure functions

Simulate CI/CD security enforcement

Demonstrate modular and extensible tool design

🏗️ Architecture Overview

The system follows a modular architecture:

main.py (CLI Controller)
│
├── analyzer/
│   ├── scanner.py        → Reads all C/C++ files
│   ├── rules_engine.py   → Applies security rules
│   ├── reporter.py       → Generates structured reports
│
├── auto_fixer.py         → Fixes simple unsafe patterns
├── rules.json            → Configurable security rules
└── sample_code/          → Sample vulnerable files
⚙️ How It Works

1️⃣ The CLI accepts user input (--path, --fix, --json, etc.)
2️⃣ The scanner traverses directories and collects .c / .cpp files
3️⃣ Each file is analyzed line-by-line
4️⃣ Rules from rules.json are applied
5️⃣ Matched vulnerabilities are stored with:

File path

Line number

Category

Severity

Suggested fix
6️⃣ A structured report is generated
7️⃣ If HIGH severity issues exist → build fails

🚀 Features

🔍 Recursive directory scanning

📂 Supports .c and .cpp files

🧠 Rule-based detection system

📊 Severity classification:

HIGH

MEDIUM

LOW

🛠 Suggested secure alternatives

🔧 Auto-fix support (for simple patterns)

📄 JSON report export

🛑 Conditional build failure enforcement

💻 Command-line interface support

🖥️ Installation
Requirements

Python 3.8+

No external dependencies required

Clone Repository
git clone https://github.com/dhanush-pk/c-code-audit-tool.git
cd c-code-audit-tool
▶️ Usage
Scan Current Directory
python main.py --path .
Scan Specific Directory
python main.py --path sample_code
Enable Auto-Fix
python main.py --path . --fix
Export JSON Report
python main.py --path . --json
Fail Build Based on Severity
python main.py --path . --fail-on HIGH
📄 Example Output
========== AUTOMATED C CODE AUDIT REPORT ==========

.\analyzer\test.c | Line 5
Category : Security
Severity : HIGH
Issue    : Unsafe function gets() used
Fix      : Use fgets() instead

============== SUMMARY ==============
HIGH   : 1
MEDIUM : 0
LOW    : 0
TOTAL  : 1
=====================================

Build FAILED due to HIGH severity violations.
🧠 Example Rule (rules.json)
{
  "pattern": "gets(",
  "severity": "HIGH",
  "category": "Security",
  "message": "Unsafe function gets() used",
  "suggestion": "Use fgets() instead"
}

Rules are configurable and can be extended without modifying core logic.

🔐 Why gets() is Dangerous

The gets() function does not perform bounds checking.
This can cause buffer overflow vulnerabilities, allowing attackers to overwrite memory and potentially execute malicious code.

🔄 Auto-Fix Capability

The tool can automatically replace simple unsafe patterns such as:

gets() → fgets()

This demonstrates secure remediation workflows.

🛠️ CI/CD Integration

The tool can be integrated into GitHub Actions or other CI pipelines to:

Automatically scan code on every push

Fail builds when HIGH severity issues are detected

Enforce security compliance early in development

📊 Technical Concepts Demonstrated

Static Code Analysis

Rule-Based Pattern Matching

Command-Line Interface Design

Severity Classification Systems

DevSecOps Integration Concepts

Modular Python Architecture

Automated Code Remediation

🚧 Limitations

Pattern-based detection (not AST-based)

May produce false positives

No deep data-flow analysis

Limited auto-fix scope

No cross-file semantic analysis

🔮 Future Improvements

AST-based parsing for better accuracy

Regex-based advanced rule engine

Multi-threaded scanning

Web dashboard visualization

Full IDE plugin integration

Advanced AI-based vulnerability explanation

Test case integration using pytest

📚 Learning Outcomes

Through this project, I gained hands-on experience in:

Designing modular software systems

Implementing static analysis techniques

Applying secure coding principles

Building CLI-based developer tools

Simulating DevSecOps workflows

👤 Author

Dhanush P K
BCA Student | 

GitHub: https://github.com/dhanush-pk

📄 License

This project is developed for educational and demonstration purposes.

⭐ If you find this project useful, consider giving it a star!
