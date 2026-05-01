# 🚀 Railway Deployment Guide for moneyFlow_Tracker

Your code is now live on GitHub: **https://github.com/khairulrezz4/moneyFlow_Tracker**

## Deploy to Railway (3 Minutes)

### Step 1: Go to Railway
Open: https://railway.app

### Step 2: Create New Project
1. Click **"New Project"**
2. Click **"Deploy from GitHub repo"**
3. Select **"khairulrezz4/moneyFlow_Tracker"**
4. Click **"Create"**

### Step 3: Add Environment Variables
Once the project is created:

1. Click **"Add Variable"** (in Variables tab)
2. Add these **exactly**:

```
TELEGRAM_TOKEN = 8591313211:AAFGlu2_HYNmJG8XTwFaUN-SMOs6DQRZwpA
GEMINI_API_KEY = AlzaSyAP7wqqhkkgDdy8xjRjABic_Y7HTk4-24
DATABASE_FILE = transactions.json
```

3. Click **"Deploy"**

### Step 4: Wait for Deployment
- Railway will build and deploy automatically
- Status will show **"Deployed"** when complete (usually 2-5 minutes)
- Your bot will now run 24/7 in the cloud ✅

---

## ✅ What You Get Now

| Feature | Status |
|---------|--------|
| Bot 24/7 Uptime | ✅ Running |
| Auto-restart on crash | ✅ Enabled |
| Auto-deploy on GitHub push | ✅ Enabled |
| Transaction storage | ✅ JSON file |

---

## Test Your Cloud Bot

Message **@moneytrackerMalay_bot** on Telegram:

```
/start
→ Bot responds with welcome

nasi lemak 12
→ Bot saves: Nasi Lemak, RM 12.00

/stats
→ Shows spending summary
```

If bot responds, **✅ Deployment successful!**

---

## GitHub Auto-Deploy

Now whenever you push code to GitHub:

```powershell
git add .
git commit -m "your message"
git push origin main
```

Railway **automatically redeploys** within 1 minute ✅

---

## Troubleshooting

### Bot doesn't respond
- Check Railway dashboard for deployment errors
- Verify environment variables are correct
- Try `/start` command again

### "API quota exceeded"
- Gemini free tier: 15 requests/minute
- Wait 60 seconds before retrying

### Want to view logs
- Railway dashboard → "Logs" tab
- Shows real-time bot activity

---

## Next Steps

1. ✅ Go to https://railway.app
2. ✅ Deploy from GitHub
3. ✅ Add environment variables
4. ✅ Test bot on Telegram
5. ✅ Celebrate! 🎉

**Questions?** Check the [README.md](README.md) in the repo for more details.
