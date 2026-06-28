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

## 📦 Installation

### From PyPI

```bash
pip install sailpoint-session-manager
```

### From Source

```bash
git clone https://github.com/xamitgupta/sailpoint-session-manager.git
cd sailpoint-session-manager
pip install -e .
```

### Docker

```bash
docker build -t sailpoint-session-manager .
docker run --rm -v $(pwd)/config.yml:/app/config.yml sailpoint-session-manager org-metrics
```

## ⚙️ Configuration

Create a `config.yml` file in your working directory:

```yaml
sailpoint:
  base_url: "https://your-sailpoint-instance.com"
  api_username: "api_admin_user"
  api_token: "your_sailpoint_api_token"
  verify_ssl: true
  timeout: 30

google_workspace:
  admin_email: "admin@company.com"
  service_account_json: "/path/to/service-account.json"

okta:
  base_url: "https://company.okta.com"
  api_token: "your_okta_api_token"

approval:
  enabled: true
  approvers:
    - "security-lead@company.com"
    - "hr-manager@company.com"
  approval_required_for_bulk: true
  approval_timeout_hours: 24
```

See `examples/config.example.yml` for all configuration options.

## 🚀 Usage

### List All Sessions for a User

```bash
session-manager list-user-sessions john.doe --config config.yml
```

**Sample Output:**
```
    ╔═══════════════════════════════════════════════════════╗
    ║   🔐 SailPoint Session Manager                        ║
    ║   Multi-app session management and revocation         ║
    ╚═══════════════════════════════════════════════════════╝

Connecting to SailPoint...
Retrieving sessions for: john.doe

📊 Session Summary
Username        john.doe
Total Sessions  12
Active Sessions 8
Idle Sessions   4

🟢 Active Sessions
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ App             ┃ Session ID  ┃ Created  ┃ Duration  ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ Google Workspace│ sess_abc...  │ 2024-06  │ 480 min   │
│ Okta            │ sess_def...  │ 2024-06  │ 240 min   │
│ AWS             │ sess_ghi...  │ 2024-06  │ 120 min   │
└─────────────────┴─────────────┴──────────┴───────────┘

🟡 Idle Sessions
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ App             ┃ Session ID  ┃ Idle (min)┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Slack           │ sess_jkl...  │ 1440      │
│ Google Workspace│ sess_mno...  │ 960       │
│ Okta            │ sess_pqr...  │ 720       │
│ AWS             │ sess_stu...  │ 480       │
└─────────────────┴─────────────┴───────────┘

✓ Session listing complete
```

### Terminate All Sessions for a User

```bash
session-manager terminate-sessions john.doe --reason "Offboarding"
```

**Sample Output:**
```
    ╔═══════════════════════════════════════════════════════╗
    ║   🔐 SailPoint Session Manager                        ║
    ║   Multi-app session management and revocation         ║
    ╚═══════════════════════════════════════════════════════╝

Terminate ALL sessions for john.doe? This cannot be undone. [y/N]: y

Sessions to terminate: 12
  • Google Workspace: sess_abc1234…
  • Okta: sess_def5678…
  • AWS: sess_ghi9012…
  • Slack: sess_jkl3456…

⏳ Awaiting approval...
✓ Approved by security-lead@company.com

Terminating sessions...
  ✓ Google Workspace
  ✓ Okta
  ✓ AWS
  ✗ Slack (API revocation not supported)

📊 Termination Summary
  Total: 12
  Successful: 11
  Failed: 1

✓ Session termination complete
```

### View Organization-Wide Metrics

```bash
session-manager org-metrics
```

**Sample Output:**
```
    ╔═══════════════════════════════════════════════════════╗
    ║   🔐 SailPoint Session Manager                        ║
    ║   Multi-app session management and revocation         ║
    ╚═══════════════════════════════════════════════════════╝

Collecting organization metrics...

    Organization Session Metrics
┌──────────────────────────┬────────┐
│ Metric                   │ Value  │
├──────────────────────────┼────────┤
│ Total Sessions           │ 2,341  │
│ Active Sessions          │ 1,890  │
│ Idle Sessions (>30min)   │   451  │
│ Terminated Today         │    12  │
└──────────────────────────┴────────┘

By Application
┌──────────────────┬───────┬────────┬──────┐
│ Application      │ Total │ Active │ Idle │
├──────────────────┼───────┼────────┼──────┤
│ Google Workspace │ 1,200 │ 1,050  │ 150  │
│ Okta             │   800 │   650  │ 150  │
│ AWS              │   200 │   150  │  50  │
│ Slack            │   141 │    40  │ 101  │
└──────────────────┴───────┴────────┴──────┘

✓ Metrics collected
```

## 🔌 Supported Applications

| Application | Status | Revocation | Discovery |
|-------------|--------|------------|-----------| 
| Google Workspace | ✅ Full | ✅ Yes | ✅ Yes |
| Okta | ✅ Full | ✅ Yes | ✅ Yes |
| AWS | 🟡 Partial | ✅ Yes (STS) | ✅ Yes |
| Slack | 🟡 Partial | ❌ No | ✅ Yes |
| Generic Apps | ⚠️ Limited | ❌ No | ✅ Limited |

## 📋 Available Commands

```bash
# List all sessions for a user
session-manager list-user-sessions USERNAME [--config CONFIG_FILE]

# Terminate all sessions for a user
session-manager terminate-sessions USERNAME \
  --reason "Reason for termination" \
  --config CONFIG_FILE

# View organization-wide metrics
session-manager org-metrics [--config CONFIG_FILE]

# Show version
session-manager version
```

## 📊 Key Features

### Session Discovery
- Real-time session discovery across all integrated applications
- Session status classification (active/idle/terminated)
- Configurable idle detection (default: 30 minutes)
- Device, IP address, and location tracking
- Detailed session metadata

### Session Management
- Bulk terminate sessions for single or multiple users
- Single-click offboarding of user sessions
- Selective session termination per application
- Session termination audit trail
- Failed operation recovery and retry

### Approval Workflows
- Optional approval requirements before termination
- SailPoint Workflow engine integration
- Configurable approver groups
- Approval timeout with automatic cleanup
- Email notifications for approvals

### Metrics & Reporting
- Real-time organization-wide metrics
- Per-application session statistics
- Session distribution analysis
- Idle session reporting
- Termination history tracking

## 🔒 Security

- Credentials stored in local config file (add to .gitignore)
- HTTPS enforcement for all external APIs
- Optional SSL certificate verification
- Complete audit logging of all operations
- Approval workflows for sensitive operations
- No persistent session data storage

## 🛠️ Development

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest tests/
pytest --cov=sailpoint_session_manager tests/
```

### Code Style

```bash
black sailpoint_session_manager/
ruff sailpoint_session_manager/
```

## 📚 Documentation

- [QUICK_START.md](QUICK_START.md) - Get started in 5 minutes
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [examples/config.example.yml](examples/config.example.yml) - Configuration reference

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Adding support for new applications
- Improving session discovery
- Enhancing approval workflows
- Adding new metrics and reporting
- Improving documentation

## ⚖️ License

MIT License - see [LICENSE](LICENSE) for details.

## 📞 Support

- [GitHub Issues](https://github.com/xamitgupta/sailpoint-session-manager/issues) - Report bugs and request features
- [GitHub Discussions](https://github.com/xamitgupta/sailpoint-session-manager/discussions) - Ask questions and discuss ideas

---

**Like this tool?** Please ⭐ star the repo!
