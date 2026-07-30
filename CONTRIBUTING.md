# 🤝 Contributing to Machine Learning Journey

First off, thank you for considering contributing to this repository! It's people like you that make learning more collaborative and fun.

## 🚀 Welcome Message
I welcome contributions of all kinds, whether it's fixing a typo, updating resources, optimizing code, or submitting a new project. Let's learn together!

## 🛠️ How to Contribute
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name` or `bugfix/issue-name`.
3. Make your changes and commit them following the conventions below.
4. Push your branch to your fork: `git push origin feature/your-feature-name`.
5. Open a Pull Request!

## ⚙️ Development Setup
To set up your local development environment:

```bash
# Clone your fork
git clone https://github.com/YourUsername/machine-learning-journey.git
cd machine-learning-journey

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
```

## 🎨 Code Style
We enforce consistent code formatting:
- **Black** for Python code formatting.
- **isort** for import sorting.
- **Ruff** for fast linting.

Our pre-commit hooks will automatically run these checks on your commits!

## 📝 Commit Message Conventions
We follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` for new features or projects
- `fix:` for bug fixes
- `docs:` for documentation updates (README, docs folder)
- `style:` for formatting changes (Black, isort)
- `refactor:` for code restructuring
- `chore:` for updating dependencies or CI/CD

Example: `feat: add Random Forest model to house price project`

## 🔄 Pull Request Process
1. Ensure your code passes all pre-commit checks and tests.
2. Update the README or documentation if applicable.
3. Describe your changes thoroughly in the PR template.
4. Request a review from maintainers.

## 🐛 Issue Guidelines
- Search existing issues before creating a new one.
- Use the provided issue templates.
- Be descriptive and provide clear steps to reproduce if it's a bug.

## 🔍 Code Review Process
- Reviews are meant to be constructive and collaborative.
- Maintainers will review PRs as soon as possible.
- Please address review comments by pushing new commits to your branch.

## 🛡️ Community Guidelines Reference
Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
