# Quick Start: Feature Testing Workflow

## Your Git Setup is Ready! ✅

You now have **3 branches**:

| Branch | Purpose | Deploy? | Status |
|--------|---------|---------|--------|
| `main` | **Production** | ✅ Yes (Live) | Latest stable |
| `testing` | **Staging** | 🔄 Auto-test | For QA |
| `feature/*` | **Development** | ❌ No | Your workspace |

---

## From Now On: Use This Workflow

### **Every Time You Start Work**

```bash
# 1. Switch to testing
git checkout testing

# 2. Pull latest changes
git pull origin testing

# 3. Create YOUR feature branch
git checkout -b feature/your-feature-name
```

### **While You Code**

```bash
# Make changes...
git add .
git commit -m "feat: your message"

# Repeat as needed...
git add .
git commit -m "fix: another fix"

# Push your branch
git push origin feature/your-feature-name
```

### **When Ready to Test**

```bash
# Merge YOUR feature into testing
git checkout testing
git merge feature/your-feature-name
git push origin testing

# Railway auto-deploys to TESTING environment
# Test on Telegram for 5-10 minutes
# Fix any bugs in your feature branch if needed
```

### **When Tests Pass**

```bash
# Merge into main (production)
git checkout main
git merge feature/your-feature-name
git push origin main

# Railway auto-deploys to PRODUCTION
# Bot goes live 🚀
```

### **Clean Up**

```bash
# Delete your feature branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

---

## Real Example: Fix Parsing Bug

```bash
# 1. Start
git checkout testing && git pull

# 2. Create bugfix branch
git checkout -b bugfix/fix-gemini-response

# 3. Edit files
# [Fix the bug in bot.py]
git add bot.py
git commit -m "fix: improve Gemini response parsing

- Handle edge cases better
- Better error messages"
git push origin bugfix/fix-gemini-response

# 4. Test on staging
git checkout testing
git merge bugfix/fix-gemini-response
git push origin testing
# [Test bot for 5 mins]
# [Works? Continue to 5, Broken? Fix and repeat]

# 5. Deploy to production
git checkout main
git merge bugfix/fix-gemini-response
git push origin main
# [Live! 🎉]

# 6. Cleanup
git branch -d bugfix/fix-gemini-response
git push origin --delete bugfix/fix-gemini-response
```

---

## Command Cheat Sheet

| What You Want | Command |
|---|---|
| See all branches | `git branch -a` |
| Switch branches | `git checkout branch-name` |
| Create feature | `git checkout -b feature/name` |
| Push changes | `git push origin branch-name` |
| Merge branches | `git checkout main && git merge feature/name` |
| See recent commits | `git log --oneline -10` |
| See current branch | `git status` or `git branch` |

---

## Important! 🚨

✅ **Always do this first**: `git checkout testing && git pull`  
✅ **Branch FROM testing**: `git checkout -b feature/name`  
✅ **Test BEFORE deploying**: Merge to testing first  
✅ **Only merge to main when tested**  

❌ **DON'T push directly to main**  
❌ **DON'T commit directly to testing**  
❌ **DON'T delete main or testing branches**  

---

## See Full Workflow Guide

Read [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for detailed examples!

---

## Current Status

```
✅ main         (Production - Live)
✅ testing      (Testing - For QA)
✅ Ready to dev (Create feature/bugfix branches)
```

**Ready to code? Start with:**
```bash
git checkout testing
git pull origin testing
git checkout -b feature/your-feature
```

Good luck! 🚀
