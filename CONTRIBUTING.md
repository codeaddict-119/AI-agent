# Contributing to AI-agent

First off, thank you for considering contributing! It’s people like you who make the open-source community such an amazing place to learn, inspire, and create.

## How Can I Contribute?

### 1. Reporting Bugs
* Check the **Issues** tab to see if the bug has already been reported.
* If not, open a new issue. Include steps to reproduce the bug and your Python version.

### 2. Suggesting Enhancements
* We love new ideas! If you want to add a new "Voice Skill" (e.g., "Open Spotify"), please open an issue first to discuss it.

### 3. Pull Requests (PRs)
1. **Fork** the repository.
2. **Create a branch** for your feature (`git checkout -b feature/AmazingFeature`).
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
4. **Push to the branch** (`git push origin feature/AmazingFeature`).
5. **Open a Pull Request**.

## Style Guidelines

* **Code Style:** Please follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) standards.
* **Documentation:** If you add a new function, please add a brief comment explaining what it does.
* **API Safety:** **Do not** include your `config.py` or any private API keys in your Pull Request.

## Project Structure
* `main.py`: The core logic and voice recognition loop.
* `config.py`: (Local only) Stores your OpenAI API key.
* `Openai/`: Folder where AI responses are saved as text files.

## Community and Conduct
By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and kind to other contributors.
