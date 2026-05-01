# Git Workflow Guide - Money Tracker Bot

## Branch Structure

```
main (Production)
  ↑
  └─ Pull Requests (tested features only)
  
testing (Testing/Staging)
  ↑
  └─ Feature branches (develop here)

feature/* (Development)
develop/* (Work in progress)
bugfix/* (Bug fixes)
hotfix/* (Production patches)
```

---

## Workflow: Local Development → Testing → Production

### **Step 1: Create Feature Branch**

```bash
# Update testing branch first
git checkout testing
git pull origin testing

# Create feature branch FROM testing
git checkout -b feature/your-feature-name

# Or for bugs
git checkout -b bugfix/fix-parse-error
```

### **Step 2: Make Changes & Commit**

```bash
# Edit files
git add .
git commit -m "feat: add humanized responses

- Smart error detection
- User-friendly prompts"

# Can commit multiple times
git add bot.py
git commit -m "fix: improve error message formatting"
```

### **Step 3: Push to Feature Branch**

```bash
# First push (creates remote branch)
git push -u origin feature/your-feature-name

# Subsequent pushes
git push origin feature/your-feature-name
```

### **Step 4: Test on Railway (Testing Environment)**

1. **Push to testing branch to test**:
   ```bash
   # Merge feature into testing locally
   git checkout testing
   git pull origin testing
   git merge feature/your-feature-name
   git push origin testing
   ```

2. **Railway will auto-deploy to testing** (different from production)
3. **Test on Telegram**:
   - Message the bot with test cases
   - Verify all features work
   - Check error handling

4. **If issues found**:
   ```bash
   git checkout feature/your-feature-name
   # Make fixes
   git add .
   git commit -m "fix: resolve edge case"
   git push origin feature/your-feature-name
   # Then merge back to testing and test again
   ```

### **Step 5: Merge to Main (Production)**

Once testing is complete:

```bash
# Ensure main is up to date
git checkout main
git pull origin main

# Merge tested feature
git merge feature/your-feature-name

# Push to production
git push origin main
```

**Railway will auto-deploy to PRODUCTION** 🚀

### **Step 6: Cleanup Feature Branch**

```bash
# Delete local feature branch
git branch -d feature/your-feature-name

# Delete remote feature branch
git push origin --delete feature/your-feature-name
```

---

## Quick Reference

| Task | Commands |
|------|----------|
| **Start new feature** | `git checkout testing && git checkout -b feature/name` |
| **Push changes** | `git add . && git commit -m "..."` + `git push origin feature/name` |
| **Test on staging** | `git checkout testing && git merge feature/name && git push origin testing` |
| **Deploy to production** | `git checkout main && git merge feature/name && git push origin main` |
| **Delete feature** | `git branch -d feature/name && git push origin --delete feature/name` |
| **See all branches** | `git branch -a` |
| **Switch branch** | `git checkout branch-name` |

---

## Branch-Specific Naming Conventions

### **Feature Branches**
```
feature/humanized-responses
feature/add-stats-command
feature/database-optimization
```

### **Bugfix Branches**
```
bugfix/fix-parse-error
bugfix/resolve-timezone-issue
bugfix/handle-empty-input
```

### **Hotfix Branches** (Production only)
```
hotfix/fix-critical-bug
hotfix/security-patch
```

---

## Workflow Example: Adding New Feature

### **Scenario: Add export to CSV feature**

```bash
# 1. Create feature branch from testing
git checkout testing
git pull origin testing
git checkout -b feature/export-csv

# 2. Develop & commit
echo "csv export code" > export.py
git add export.py
git commit -m "feat: add CSV export functionality

- Exports all transactions to file
- Includes timestamp and totals"
git push -u origin feature/export-csv

# 3. Test on staging
git checkout testing
git merge feature/export-csv
git push origin testing
# [Wait for Railway to deploy to testing]
# [Test on Telegram with test account]

# 4. If all good, merge to main
git checkout main
git pull origin main
git merge feature/export-csv
git push origin main
# [Railway auto-deploys to production]

# 5. Cleanup
git branch -d feature/export-csv
git push origin --delete feature/export-csv
```

---

## Important Rules

✅ **DO:**
- Always branch from `testing` for new features
- Test on staging branch before merging to main
- Use descriptive branch names
- Commit frequently with clear messages
- Delete branches after merging

❌ **DON'T:**
- Push directly to `main` (only merge PR)
- Commit to `testing` directly (use feature branches)
- Delete `main` or `testing` branches
- Use vague commit messages ("fix stuff", "update")

---

## Current Branch Status

| Branch | Status | Use Case |
|--------|--------|----------|
| **main** | ✅ Production | Live on Railway |
| **testing** | ✅ Staging | Test new features |
| **feature/*** | 📝 Development | Work on features here |

---

## Next Steps

1. **Always start with**: `git checkout testing && git pull origin testing`
2. **Create feature branch**: `git checkout -b feature/your-feature`
3. **Make changes** and commit
4. **Test on staging** (merge to testing)
5. **If good**, merge to main → Auto-deploy to production

---

**Example: Your next feature**

```bash
# You want to add a "delete transaction" feature
git checkout testing
git pull origin testing
git checkout -b feature/delete-transaction

# Make your code changes...

git add bot.py
git commit -m "feat: add delete transaction command

- Users can delete last transaction
- Confirmation required"

git push -u origin feature/delete-transaction

# Test it
git checkout testing
git merge feature/delete-transaction
git push origin testing

# Once tested and working
git checkout main
git merge feature/delete-transaction
git push origin main

# Cleanup
git branch -d feature/delete-transaction
git push origin --delete feature/delete-transaction
```

That's it! 🎉
