# Development Skills & Standards

Guidelines for contributing to Money Tracker Bot. These skills ensure consistent, professional development.

---

## 📋 Table of Contents

1. [Git Workflow](#git-workflow)
2. [Commit Message Standards](#commit-message-standards)
3. [Code Standards](#code-standards)
4. [Development Process](#development-process)
5. [Testing Before Deployment](#testing-before-deployment)

---

## Git Workflow

### Branch Strategy

```
main (Production - Auto-deploys to Railway)
  ↓
testing (Staging - For QA before production)
  ↓
feature/* (Development - Your workspace)
```

### Flow: Development → Staging → Production

```
feature/your-feature
    ↓ (merge to)
testing (test 5 mins)
    ↓ (merge to)
main (live!)
```

### Step-by-Step Workflow

#### 1. Start New Feature
```bash
git checkout testing
git pull origin testing
git checkout -b feature/your-feature-name
```

#### 2. Code & Commit
```bash
git add .
git commit -m "feat: description of your feature"
git push origin feature/your-feature-name
```

#### 3. Test on Staging
```bash
git checkout testing
git merge feature/your-feature-name
git push origin testing
# Wait 2-3 minutes for Railway to deploy
# Test on Telegram
```

#### 4. Deploy to Production
If tests pass:
```bash
git checkout main
git merge feature/your-feature-name
git push origin main
# Live on Railway! 🚀
```

#### 5. Cleanup
```bash
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

### Key Rules

✅ **DO:**
- Always branch FROM `testing`
- Test on `testing` BEFORE merging to `main`
- Use descriptive branch names
- Delete branches after merging

❌ **DON'T:**
- Push directly to `main` (only merge)
- Commit directly to `testing` (only merge)
- Delete `main` or `testing` branches
- Mix multiple features in one branch

---

## Commit Message Standards

### Format

```
type: short description
```

### Commit Types

| Type | Use | Example |
|------|-----|---------|
| `feat:` | New feature | `feat: add delete command` |
| `fix:` | Bug fix | `fix: resolve parse error` |
| `docs:` | Documentation | `docs: update README` |
| `refactor:` | Code improvement | `refactor: simplify handler` |
| `test:` | Add/update tests | `test: add parser tests` |
| `style:` | Formatting | `style: format code` |
| `chore:` | Maintenance | `chore: update dependencies` |

### Rules

✅ **DO:**
- Start with lowercase
- Use imperative mood ("add", not "added")
- Keep under 50 characters
- Be specific and clear
- One main change per commit

❌ **DON'T:**
- Use vague titles ("fix stuff")
- Use all caps
- End with period
- Mix multiple changes

### Examples

```bash
# ✅ GOOD
git commit -m "feat: add transaction export to CSV"
git commit -m "fix: handle gemini api timeout"
git commit -m "docs: add deployment guide"
git commit -m "refactor: simplify expense parser"
git commit -m "chore: update python-telegram-bot"

# ❌ BAD
git commit -m "fix: remove markdown parse mode to fix Telegram entity parsing errors"
git commit -m "update stuff"
git commit -m "Fixed things"
```

### With Details (Optional)

If you need to explain more:

```bash
git commit -m "feat: add humanized error responses

- Detect missing food name or amount
- Show friendly prompts with examples
- Guide users to correct format"
```

Keep the first line short!

---

## Code Standards

### Python Style

- Use **PEP 8** formatting
- Descriptive variable names
- Comments for complex logic
- Type hints where helpful

### Project Structure

```
money_Tracker_via_TelegramAPI/
├── bot.py                    # Main bot code
├── best_system_prompt.txt    # Gemini system prompt
├── requirements.txt          # Python dependencies
├── Procfile                  # Railway deployment
├── README.md                 # Project overview
├── .env.example              # Environment template
├── .gitignore
├── GUIDES/                   # Development guides
│   ├── GIT_WORKFLOW.md
│   ├── GIT_QUICK_START.md
│   └── COMMIT_MESSAGE_GUIDE.md
└── .github/
    ├── DEVELOPMENT_SKILLS.md (this file)
    ├── copilot-instructions.md
    └── workflows/
```

### Environment Variables

**Local Development** (`.env`):
```
TELEGRAM_TOKEN=your_token_here
GEMINI_API_KEY=your_key_here
DATABASE_FILE=transactions.json
```

**Production** (Railway Dashboard):
- Same variables stored in Railway environment

**Never commit `.env`** - it's in `.gitignore`

---

## Development Process

### 1. Setup Environment

```bash
# Clone repo
git clone https://github.com/khairulrezz4/moneyFlow_Tracker.git
cd money_Tracker_via_TelegramAPI

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your tokens
```

### 2. Run Bot Locally

```bash
python bot.py
# Output: 🤖 Bot is running... (Press Ctrl+C to stop)
```

### 3. Test Locally

Before pushing, test locally:
- `/start` command
- Send expense: "nasi lemak 12"
- `/stats` command
- `/reset` command

### 4. Syntax Validation

Before committing:
```bash
python -m py_compile bot.py
# No output = ✅ Valid syntax
```

### 5. Git Workflow

See [Git Workflow](#git-workflow) section above.

---

## Testing Before Deployment

### Local Testing (Before Push)

```bash
# 1. Run bot
python bot.py

# 2. Test commands in Telegram
#    - /start
#    - Send: "nasi lemak 12"
#    - /stats
#    - /reset

# 3. Verify responses
#    - Bot sends welcome message
#    - Expense recorded correctly
#    - Stats show proper summary
#    - Reset works with confirmation
```

### Staging Testing (Testing Branch)

```bash
# After merging to testing branch:
# Wait 2-3 minutes for Railway to deploy
# Test same commands on @moneytrackerMayal_bot
# Verify all features work on live bot
```

### Production Testing (Main Branch)

```bash
# After merging to main:
# Wait 2-3 minutes for Railway to deploy
# Final quick test: /start command
# Monitor logs for errors
```

---

## Useful Commands

### Git Commands

```bash
# See all branches
git branch -a

# See current branch
git status

# See recent commits
git log --oneline -10

# Switch branch
git checkout branch-name

# Create branch
git checkout -b feature/name

# Push changes
git push origin branch-name

# Merge branches
git checkout target
git merge source
git push origin target
```

### Python Commands

```bash
# Check syntax
python -m py_compile bot.py

# Run bot
python bot.py

# Install dependencies
pip install -r requirements.txt

# Create virtual environment
python -m venv venv
```

### Railway Commands

Check Railway dashboard: https://railway.app/project/1027849-120b-431a-9022-7eae126cd6b8

---

## Troubleshooting

### Bot not responding on Telegram?

1. Check Railway logs for errors
2. Verify tokens in Railway environment
3. Restart Railway deployment
4. Check internet connection

### Commit failed?

1. Check syntax: `python -m py_compile bot.py`
2. Verify all files are staged: `git status`
3. Ensure branch is up to date: `git pull`

### Merge conflict?

1. Fix conflicts in editor
2. `git add .`
3. `git commit -m "fix: resolve merge conflict"`
4. `git push`

---

## References

For detailed guides, see:
- [GUIDES/GIT_WORKFLOW.md](../../GUIDES/GIT_WORKFLOW.md) - Full workflow examples
- [GUIDES/GIT_QUICK_START.md](../../GUIDES/GIT_QUICK_START.md) - Quick reference
- [GUIDES/COMMIT_MESSAGE_GUIDE.md](../../GUIDES/COMMIT_MESSAGE_GUIDE.md) - Commit standards
- [README.md](../../README.md) - Project overview
- [copilot-instructions.md](./copilot-instructions.md) - Copilot setup

---

## Questions?

Create an issue or refer to the guides above. Welcome to the team! 🚀

---

**Last updated**: May 2026
