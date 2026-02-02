# Security Policy

## Supported Versions

We actively provide security updates for the following versions of this project:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

If you discover a potential security flaw, please help us keep the community safe by reporting it privately. 

### How to report
1. Send an email to eamon112009@gmail.com
2. Include a detailed description of the vulnerability.
3. Provide steps to reproduce the issue (proof-of-concept scripts are helpful).
4. Mention the potential impact if the vulnerability is exploited.

### What to expect
* You will receive an acknowledgment of your report as soon as possible.
* We will provide a timeline for the fix and keep you updated on our progress.
* Once the fix is verified, we will release an update and credit you for the discovery (unless you prefer to remain anonymous).

## Known Security Considerations

As this project interacts with local system shells and external APIs, please be aware of the following:

* **API Key Safety:** Never hardcode your OpenAI API key in `config.py` and commit it to a public repository. Use `.gitignore` to exclude your `config.py` file.
* **Command Injection:** This script uses `os.system()` to launch local applications. Ensure that user input is sanitized if you extend the functionality to accept dynamic arguments.
* **Microphone Privacy:** This application listens for voice commands. Ensure you run the script in a secure environment.

---
*Thank you for helping keep this project secure!*
