import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {

	console.log('C Code Audit Tool is now active!');

	const disposable = vscode.commands.registerCommand(
		'ai-powered-c-c---static-code-analyzer.analyzeCode',
		() => {

			const editor = vscode.window.activeTextEditor;

			if (!editor) {
				vscode.window.showErrorMessage("No file is open.");
				return;
			}

			const text = editor.document.getText();

			let issues: string[] = [];

			// Simple static checks
			if (text.includes("gets(")) {
				issues.push("❌ Avoid using gets() - It is unsafe.");
			}

			if (text.includes("strcpy(")) {
				issues.push("⚠ strcpy() can cause buffer overflow.");
			}

			if (text.includes("scanf(") && !text.includes("&")) {
				issues.push("⚠ scanf() might be missing & operator.");
			}

			if (issues.length === 0) {
				vscode.window.showInformationMessage("✅ No obvious security issues found.");
			} else {
				vscode.window.showWarningMessage(issues.join("\n"));
			}
		}
	);

	context.subscriptions.push(disposable);
}

export function deactivate() {}
