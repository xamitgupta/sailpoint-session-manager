# 🔐 SailPoint Session Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Multi-app session management and revocation tool for SailPoint.**

Quickly terminate user sessions across Google Workspace, Okta, AWS, and other integrated applications when offboarding employees or responding to security incidents.

## 🎯 What It Does

SailPoint Session Manager provides a unified interface for session management across your entire application ecosystem:

- **🔍 Session Discovery** - Find all active and idle sessions for any user across all integrated apps
- **⏹️ Bulk Termination** - Revoke sessions in seconds instead of hours of manual work
- **👤 User-Based Revocation** - Terminate sessions by username with approval workflows
- **📊 Real-time Metrics** - View organization-wide session statistics by app
- **📝 Audit Logging** - Complete audit trail of all session terminations
- **✅ Approval Workflows** - Optional approval requirements before revocation

## ⚡ Quick Start

### Install

```bash
pip install sailpoint-session-manager
```

### Configure

Create a `config.yml` file:

```yaml
sailpoint:
  base_url: "https://your-sailpoint-instance.com"
  api_username: "admin_user"
  api_token: "your_api_token"

google_workspace:
  admin_email: "admin@company.com"

okta:
  base_url: "https://company.okta.com"
  api_token: "your_okta_token"
```

### List Sessions

```bash
session-manager list-user-sessions john.doe
```

### Terminate Sessions

```bash
session-manager terminate-sessions john.doe --reason "Offboarding"
```

### View Metrics

```bash
session-manager org-metrics
```

## 🔌 Supported Applications

| Application | Status | Revocation | Discovery |
|-------------|--------|------------|-----------| 
| Google Workspace | ✅ | ✅ | ✅ |
| Okta | ✅ | ✅ | ✅ |
| AWS | 🟡 | ✅ | ✅ |
| Slack | 🟡 | ❌ | ✅ |

## 📊 Key Features

### Session Management
- Discover all active and idle sessions per user
- Bulk terminate sessions across all apps with one command
- Idle session detection (configurable threshold)
- Session age and duration tracking

### Approval Workflows
- Optional approval requirements before termination
- Integration with SailPoint Workflow engine
- Configurable approver groups
- Approval timeout handling

### Audit Logging
- Complete audit trail of all operations
- Session termination history
- Failed operation logging
- Compliance-ready reports

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 👨‍💻 Author

**Amit Gupta**
- Staff Security Engineer @ Meta
- OSAC Panelist
- [Twitter](https://x.com/_xamitgupta)
- [Email](mailto:apphelp.csw@gmail.com)

---

**Questions?** [Start a discussion](https://github.com/xamitgupta/sailpoint-session-manager/discussions)

**Found an issue?** [Report it](https://github.com/xamitgupta/sailpoint-session-manager/issues)

**Like this tool?** Please ⭐ star the repo!
