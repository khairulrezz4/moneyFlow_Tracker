# Setup Steps for GitHub & Railway Deployment

## Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Create repo name: `money_tracker_bot`
3. **DO NOT** initialize with README (we already have files)
4. Click "Create repository"
5. Copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/money_tracker_bot.git`)

## Step 2: Connect Local Repo to GitHub

Run in PowerShell:

```powershell
cd "g:\GitHub Project\money_Tracker_via_TelegramAPI"

# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/money_tracker_bot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Deploy to Railway

1. Go to https://railway.app
2. Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `money_tracker_bot` repository
6. Click "Add variables"
7. Add these environment variables:
   ```
   TELEGRAM_TOKEN=8591313211:AAFGlu2_HYNmJG8XTwFaUN-SMOs6DQRZwpA
   GEMINI_API_KEY=AlzaSyAP7wqqhkkgDdy8xjRjABic_Y7HTk4-24
   DATABASE_FILE=transactions.json
   ```
8. Click "Deploy"
9. Wait for deployment to complete (usually 2-5 minutes)
10. ✅ Your bot will automatically restart on every GitHub push

## Verification

After Railway deployment, your bot will:
- ✅ Run 24/7 in the cloud
- ✅ Auto-restart on crashes
- ✅ Auto-deploy when you push to GitHub
- ✅ Store transactions in Railway's ephemeral storage (for permanent storage, add a database later)

## Next Steps

1. Message @moneytrackerMalay_bot on Telegram to verify it's working
2. Use `/stats` to check stored transactions
3. Push new features to GitHub - Railway will auto-deploy

---

## If Bot Already Deployed
If you've already completed these steps, congratulations! Your bot is live and operational. 🎉
