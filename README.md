# 🍽️ Money Tracker Telegram Bot

A smart Telegram bot that tracks meal expenses using **Gemini 3 Flash** for natural language parsing and **GEPA** for automatic prompt optimization.

## Features

✅ **Natural Language Processing**: Just tell the bot what you ate and how much it cost  
✅ **Auto-Parsing**: Extracts food name, amount (RM), and timestamp automatically  
✅ **Spending Stats**: View total spent, average per meal, and recent transactions  
✅ **Self-Optimizing**: GEPA automatically improves parsing accuracy over time  
✅ **Cloud-Ready**: Deploy to Railway, Heroku, or any VPS in minutes  

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.10+ |
| Bot Framework | python-telegram-bot |
| LLM | Google Gemini 3 Flash |
| Parsing | Gemini + GEPA optimization |
| Hosting | Railway / Heroku / Digital Ocean |

## Quick Start

### 1. Prerequisites

- Python 3.10+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Google Gemini API Key (from [Google AI Studio](https://aistudio.google.com))

### 2. Clone & Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/money_tracker_bot.git
cd money_tracker_bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Create .env file
echo "TELEGRAM_TOKEN=your_token_here" > .env
echo "GEMINI_API_KEY=your_api_key_here" >> .env
echo "DATABASE_FILE=transactions.json" >> .env
```

### 4. Run Locally

```bash
python bot.py
```

Open Telegram and message your bot:
- `/start` - Initialize bot
- `nasi lemak 12` - Log expense
- `/stats` - View spending summary
- `/reset` - Clear all transactions

## Usage Examples

```
User: Hi
Bot: 🍽️ Money Tracker Bot Started! Tell me what you ate and how much you spent...

User: nasi lemak 12
Bot: ✅ Expense Recorded
     🍽️ Food: Nasi Lemak
     💰 Amount: RM 12.00
     🕐 Time: 2026-05-01T14:32:15Z
     📊 Confidence: 98%

User: /stats
Bot: 📊 Spending Summary
     Total Spent: RM 27.50
     Meals: 2
     Average: RM 13.75
     Recent Meals:
     • Nasi Lemak: RM 12.00 (2026-05-01T14:32:15Z)
     • Laksa: RM 15.50 (2026-05-01T14:35:42Z)
```

## Deployment

### Option 1: Railway (Recommended - Easiest)

1. Push to GitHub
2. Connect repo to [Railway](https://railway.app)
3. Add environment variables in Railway dashboard
4. Railway auto-deploys on push ✅

### Option 2: Heroku

```bash
# Install Heroku CLI
brew install heroku  # or download from heroku.com

# Login
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set TELEGRAM_TOKEN=your_token
heroku config:set GEMINI_API_KEY=your_key

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Option 3: Digital Ocean (Most Reliable)

```bash
# SSH to your server
ssh root@your_server_ip

# Clone repo
git clone https://github.com/YOUR_USERNAME/money_tracker_bot.git
cd money_tracker_bot

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup environment
cat > .env << EOF
TELEGRAM_TOKEN=your_token_here
GEMINI_API_KEY=your_api_key_here
DATABASE_FILE=transactions.json
EOF

# Install PM2 for auto-restart
sudo apt update
sudo apt install npm
npm install -g pm2

# Start bot with PM2
pm2 start bot.py --name "money-tracker"
pm2 startup
pm2 save

# Setup auto-deploy from GitHub (optional)
pm2 install pm2-auto-pull
```

## Project Structure

```
money_tracker_bot/
├── bot.py                      # Main Telegram handler
├── optimize_parser.py          # GEPA optimization (provided)
├── best_system_prompt.txt      # Gemini parsing instructions
├── transactions.json           # Transaction database
├── requirements.txt            # Python dependencies
├── .env                        # Secrets (not committed)
├── .gitignore                  # Git exclusions
├── README.md                   # This file
└── .github/workflows/
    └── deploy.yml              # Auto-deploy on push
```

## File Descriptions

### `bot.py`
Main bot logic:
- Receives Telegram messages
- Calls Gemini to parse expenses
- Saves to JSON database
- Returns formatted response to user

### `best_system_prompt.txt`
System prompt for Gemini:
- Defines parsing rules (extract food name, amount, time)
- Sets output format (JSON)
- Provides examples and edge cases
- Automatically optimized by GEPA over time

### `optimize_parser.py`
GEPA optimization script:
- Tracks parsing failures
- Runs reflection loop to improve prompt
- Saves optimized version to `best_system_prompt.txt`
- Run manually: `python optimize_parser.py --reflect`

## API Keys

### Telegram Bot Token

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot`
3. Follow prompts to create bot
4. Copy token to `.env`

### Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Create API Key"
3. Copy key to `.env`
4. **Note**: Free tier allows 15 requests/minute

## Troubleshooting

### Bot doesn't respond
- Check `.env` has valid tokens
- Run `python bot.py` and look for errors
- Verify bot has internet access

### "No module named 'telegram'"
```bash
pip install -r requirements.txt
```

### High API costs
- Use Gemini 3 Flash (cheapest option)
- Keep prompts short (fewer tokens)
- Set `max_tokens=200` in bot.py

### Parsing errors
- Check error message in bot response
- Add example to `optimize_parser.py` trainset
- Run `python optimize_parser.py --reflect` to auto-improve

## Development

### Run with debugging
```bash
export DEBUG=True
python bot.py
```

### Run tests (if you add tests)
```bash
pytest tests/
```

### Update GEPA prompt
```bash
# After adding examples to trainset in optimize_parser.py
python optimize_parser.py --reflect
```

## Contributing

1. Fork repository
2. Create branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "feat: your feature"`
4. Push to branch: `git push origin feature/your-feature`
5. Open Pull Request

## License

MIT License - see LICENSE file for details

## Support

- Issues: [GitHub Issues](https://github.com/YOUR_USERNAME/money_tracker_bot/issues)
- Discussions: [GitHub Discussions](https://github.com/YOUR_USERNAME/money_tracker_bot/discussions)

---

**Created**: May 2026  
**Maintained By**: Your Name  
**Status**: ✅ Active
