# Contributing to Money Tracker Bot

Thanks for your interest in contributing! This guide will help you get started.

---

## Quick Start

1. **Read the skills**: [DEVELOPMENT_SKILLS.md](./DEVELOPMENT_SKILLS.md)
2. **Follow Git workflow**: Create feature branch → test on staging → merge to main
3. **Use simple commits**: `feat: description` or `fix: description`
4. **Test before pushing**: Run locally, then test on staging branch

---

## Development Environment

### Setup

```bash
# Clone repo
git clone https://github.com/khairulrezz4/moneyFlow_Tracker.git
cd money_Tracker_via_TelegramAPI

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add TELEGRAM_TOKEN and GEMINI_API_KEY
```

### Run Locally

```bash
python bot.py
```

Bot will output: `🤖 Bot is running... (Press Ctrl+C to stop)`

---

## Git Workflow

### Development Flow

```
1. Create feature branch from testing
   git checkout testing && git pull
   git checkout -b feature/your-feature

2. Code and commit
   git add .
   git commit -m "feat: your feature"
   git push origin feature/your-feature

3. Test on staging
   git checkout testing
   git merge feature/your-feature
   git push origin testing
   # Wait 2-3 minutes for Railway to deploy
   # Test on @moneytrackerMayal_bot

4. Deploy to production
   git checkout main
   git merge feature/your-feature
   git push origin main
   # Live! 🚀

5. Cleanup
   git branch -d feature/your-feature
   git push origin --delete feature/your-feature
```

### Branch Naming

- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `hotfix/description` - Urgent fixes for production

---

## Commit Messages

### Format

```
type: short description
```

### Types

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code improvement
- `test:` - Add tests
- `chore:` - Maintenance

### Examples

```bash
git commit -m "feat: add transaction export"
git commit -m "fix: resolve timeout error"
git commit -m "docs: update deployment guide"
```

See [DEVELOPMENT_SKILLS.md](./DEVELOPMENT_SKILLS.md) for more details.

---

## Testing

### Local Testing

```bash
python bot.py

# Test these:
# 1. /start
# 2. Send: "nasi lemak 12"
# 3. /stats
# 4. /reset
```

### Staging Testing

After merging to `testing` branch:
- Wait 2-3 minutes for Railway deployment
- Test on Telegram: @moneytrackerMayal_bot
- Verify all features work

### Before Committing

```bash
# Check syntax
python -m py_compile bot.py
```

---

## Code Standards

- Follow **PEP 8**
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused and small

---

## Reporting Issues

Create an issue if you find a bug:
1. Describe the bug clearly
2. Steps to reproduce
3. Expected vs actual behavior
4. Screenshots if applicable

---

## Feature Requests

Have an idea? Create an issue:
1. Describe the feature
2. Why it's useful
3. Possible implementation approach

---

## Questions?

Refer to:
- [DEVELOPMENT_SKILLS.md](./DEVELOPMENT_SKILLS.md) - Complete guide
- [GUIDES/](../../GUIDES/) - Detailed documentation
- [README.md](../../README.md) - Project overview

---

## Review Process

1. **Code review** - Maintainers review your changes
2. **Testing** - Verified on staging branch
3. **Merge** - Merged to main and deployed

Thanks for contributing! 🚀
