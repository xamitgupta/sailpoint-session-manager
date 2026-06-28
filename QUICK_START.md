# 🚀 Quick Start Guide

Get SailPoint Session Manager up and running in 5 minutes.

## Installation

```bash
pip install sailpoint-session-manager
```

Or from source:

```bash
git clone https://github.com/xamitgupta/sailpoint-session-manager.git
cd sailpoint-session-manager
pip install -e .
```

## Configuration

Create `config.yml`:

```yaml
sailpoint:
  base_url: "https://your-sailpoint.com"
  api_username: "admin"
  api_token: "your_token"

okta:
  base_url: "https://company.okta.com"
  api_token: "your_okta_token"

google_workspace:
  admin_email: "admin@company.com"
  service_account_json: "/path/to/service-account.json"
```

## Basic Commands

### View Sessions

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

## Common Use Cases

### Offboarding an Employee

```bash
# Step 1: Review sessions
session-manager list-user-sessions john.doe

# Step 2: Terminate all sessions
session-manager terminate-sessions john.doe --reason "Employee separation"

# Step 3: Check metrics
session-manager org-metrics
```

### Emergency Security Response

```bash
session-manager terminate-sessions suspicious.user --reason "Security incident"
```

## Troubleshooting

### Connection Error

Verify `base_url` and credentials in `config.yml`.

### No Sessions Found

Check that the username is correct and user exists in SailPoint.

## Next Steps

- Read [README.md](README.md) for full documentation
- Review example configuration in `examples/`
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to add new features

## Getting Help

- Issues: [GitHub Issues](https://github.com/xamitgupta/sailpoint-session-manager/issues)
- Questions: [GitHub Discussions](https://github.com/xamitgupta/sailpoint-session-manager/discussions)
- Email: apphelp.csw@gmail.com

---

**Happy session managing!** 🎉
