# Contributing to SailPoint Session Manager

Thank you for your interest in contributing!

## Ways to Contribute

- Add support for new applications
- Improve session discovery mechanisms
- Enhance approval workflows
- Add new metrics and reporting
- Improve documentation
- Report bugs and suggest features

## Getting Started

### 1. Fork & Clone

```bash
git clone https://github.com/YOUR-USERNAME/sailpoint-session-manager.git
cd sailpoint-session-manager
```

### 2. Create Development Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Guidelines

### Code Style

- Follow PEP 8
- Use type hints where possible
- Write docstrings for all public functions

### Testing

```bash
pytest tests/
pytest --cov=sailpoint_session_manager tests/
```

### Commit Guidelines

- Use clear, descriptive commit messages
- Reference issues when relevant: `Fix #123: Add ServiceNow connector`
- Keep commits focused on a single change

```bash
git commit -m "Add ServiceNow session connector

- Implement session discovery for ServiceNow
- Add session revocation via REST API
- Include comprehensive error handling

Closes #45"
```

## Pull Request Process

1. Update README.md if adding features
2. Add or update tests for new functionality
3. Ensure all tests pass: `pytest`
4. Create pull request with clear description
5. Reference related issues

## Reporting Bugs

Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, SailPoint version)
- Error messages and logs

## Questions?

- [GitHub Discussions](https://github.com/xamitgupta/sailpoint-session-manager/discussions)
- [GitHub Issues](https://github.com/xamitgupta/sailpoint-session-manager/issues)
- Email: apphelp.csw@gmail.com

Thank you for contributing! 🙏
