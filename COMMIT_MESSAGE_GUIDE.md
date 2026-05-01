# Commit Message Guide

## Simple Format

```
type: description
```

## Types

| Type | When to use | Example |
|------|-------------|---------|
| **feat** | New feature | `feat: add humanized responses` |
| **fix** | Bug fix | `fix: resolve parse error` |
| **docs** | Documentation | `docs: update README` |
| **style** | Formatting only | `style: format code` |
| **refactor** | Code improvement | `refactor: simplify error handling` |
| **test** | Add/update tests | `test: add parser tests` |
| **chore** | Maintenance | `chore: update dependencies` |

## Rules

✅ **DO:**
- Start with lowercase
- Use imperative mood ("add", not "added" or "adds")
- Keep under 50 characters
- Be specific and clear
- One main change per commit

❌ **DON'T:**
- Use vague titles ("fix stuff", "update")
- Use all caps
- End with period
- Mix multiple changes

## Examples

### ❌ BAD
```
fix: remove markdown parse_mode to fix Telegram entity parsing errors
fix: use google.generativeai directly instead of litellm for Gemini API
fix: update google-generativeai to valid version (>=0.5.0)
feat: add humanized responses for invalid input
```

### ✅ GOOD
```
fix: resolve telegram entity parsing error
fix: switch to google-generativeai library
fix: update google-generativeai to v0.5.0
feat: add friendly error messages
```

## With Optional Details

If you need more info, add a blank line then details:

```
feat: add humanized error responses

- Detect missing food name or amount
- Show friendly prompts with examples
- Guide users to correct format
```

But keep the first line short!

## Examples for Your Bot

| What You're Doing | Commit Message |
|---|---|
| Add new command | `feat: add delete transaction command` |
| Fix a bug | `fix: resolve gemini parsing timeout` |
| Improve error message | `feat: improve error message clarity` |
| Update documentation | `docs: update deployment guide` |
| Clean up code | `refactor: simplify expense parsing` |
| Add tests | `test: add parser edge case tests` |
| Update dependency | `chore: update telegram-bot to v22` |
| Format code | `style: format bot.py` |

## Your Next Commits

### When adding a feature:
```bash
git commit -m "feat: add feature name here"
```

### When fixing a bug:
```bash
git commit -m "fix: what you fixed"
```

### When updating docs:
```bash
git commit -m "docs: what changed"
```

## Real Examples for Money Tracker

```bash
# Adding stats export
git commit -m "feat: export transactions to CSV"

# Fixing timeout issue
git commit -m "fix: handle gemini api timeout"

# Improving UI
git commit -m "feat: add transaction confirmation"

# Updating docs
git commit -m "docs: add deployment troubleshooting"

# Code cleanup
git commit -m "refactor: simplify transaction handler"

# New test
git commit -m "test: add currency conversion tests"

# Update library
git commit -m "chore: update python-telegram-bot"
```

## Summary

Keep it simple:
1. Type (feat, fix, docs, etc.)
2. Colon and space
3. Short description (under 50 chars)
4. Done! ✅

That's it!
