"""
Money Tracker Telegram Bot
Tracks meal expenses via natural language parsing with Gemini 3 Flash

Usage:
    python bot.py
"""

import json
import os
from datetime import datetime
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Load environment variables
load_dotenv()

# Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DATABASE_FILE = os.getenv("DATABASE_FILE", "transactions.json")

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def load_system_prompt() -> str:
    """Load the optimized system prompt from file."""
    try:
        with open("best_system_prompt.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("best_system_prompt.txt not found. Cannot proceed.")


def parse_expense(user_input: str, system_prompt: str) -> dict:
    """
    Parse user input to extract food name, amount, and timestamp.
    Uses Gemini Pro with deterministic temperature.

    Args:
        user_input: User message (e.g., "nasi lemak 12")
        system_prompt: System instructions for parsing

    Returns:
        {"food": str, "amount": float, "timestamp": str, "confidence": float, "status": str}
    """
    try:
        prompt = f"{system_prompt}\n\nUser input: {user_input}"
        response = model.generate_content(prompt)
        response_text = response.text.strip()

        # Extract JSON from response (handle case where model returns extra text)
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        
        if json_start == -1 or json_end == 0:
            raise ValueError("No JSON found in response")
        
        json_str = response_text[json_start:json_end]
        result = json.loads(json_str)
        
        # Ensure required fields exist
        result.setdefault("status", "success")
        result.setdefault("confidence", 0.9)
        result.setdefault("error_message", None)
        
        return result

    except json.JSONDecodeError as e:
        return {
            "food": None,
            "amount": None,
            "timestamp": None,
            "confidence": 0.0,
            "status": "error",
            "error_message": f"JSON parse error: {str(e)[:50]}",
        }
    except Exception as e:
        error_msg = str(e)[:100]
        return {
            "food": None,
            "amount": None,
            "timestamp": None,
            "confidence": 0.0,
            "status": "error",
            "error_message": f"Parse error: {error_msg}",
        }


def load_transactions() -> list:
    """Load transactions from JSON file."""
    if Path(DATABASE_FILE).exists():
        try:
            with open(DATABASE_FILE, "r") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_transaction(expense: dict) -> None:
    """Save a single transaction to database."""
    # Don't save failed parses
    if expense.get("status") != "success" or not expense.get("food"):
        return
    
    transactions = load_transactions()
    transactions.append(
        {
            "food": expense["food"],
            "amount": expense["amount"],
            "timestamp": expense["timestamp"],
            "created_at": datetime.now().isoformat(),
        }
    )
    with open(DATABASE_FILE, "w") as f:
        json.dump(transactions, f, indent=2)


def format_response(expense: dict) -> str:
    """Format bot response for user."""
    if expense["status"] == "error" or expense.get("food") is None:
        # Humanized error messages with helpful guidance
        error_msg = expense.get("error_message", "").lower()
        
        # Missing both or missing food
        if "food" in error_msg or "missing" in error_msg:
            return (
                "🍽️ I need both the food name AND amount!\n\n"
                "Please tell me:\n"
                "• What did you eat?\n"
                "• How much did it cost?\n\n"
                "Examples:\n"
                "✓ nasi lemak 12\n"
                "✓ laksa 15.50\n"
                "✓ chicken rice RM10\n"
                "✓ teh tarik 5"
            )
        # Missing amount
        elif "amount" in error_msg or "price" in error_msg:
            return (
                "💰 I need the price in RM!\n\n"
                "Format: [Food Name] [Amount]\n\n"
                "Examples:\n"
                "✓ mee goreng 8\n"
                "✓ roti canai 3.50\n"
                "✓ coffee 5 RM"
            )
        # Generic fallback
        else:
            return (
                "🤔 I didn't catch that!\n\n"
                "Please tell me what you ate and how much:\n"
                "✓ nasi lemak 12\n"
                "✓ laksa 15.50\n"
                "✓ chicken rice RM10\n\n"
                "Or use /stats to see your spending"
            )

    return (
        f"✅ Expense Recorded\n"
        f"🍽️ Food: {expense['food']}\n"
        f"💰 Amount: RM {expense['amount']:.2f}\n"
        f"🕐 Time: {expense['timestamp']}\n"
        f"📊 Confidence: {expense['confidence']:.0%}"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start command handler."""
    await update.message.reply_text(
        "🍽️ Money Tracker Bot Started!\n\n"
        "Tell me what you ate and how much you spent:\n"
        "Examples:\n"
        "• nasi lemak 12\n"
        "• laksa 15.50\n"
        "• chicken rice RM10\n\n"
        "Commands:\n"
        "/stats - View spending summary\n"
        "/reset - Clear all transactions"
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show spending statistics."""
    transactions = load_transactions()

    if not transactions:
        await update.message.reply_text("📊 No transactions recorded yet.")
        return

    total = sum(t["amount"] for t in transactions)
    count = len(transactions)
    average = total / count if count > 0 else 0

    stats_text = (
        f"📊 Spending Summary\n\n"
        f"Total Spent: RM {total:.2f}\n"
        f"Meals: {count}\n"
        f"Average: RM {average:.2f}\n\n"
        f"Recent Meals:\n"
    )

    for t in transactions[-5:]:  # Show last 5
        stats_text += f"• {t['food']}: RM {t['amount']:.2f} ({t['timestamp']})\n"

    await update.message.reply_text(stats_text)


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reset all transactions (confirm first)."""
    await update.message.reply_text(
        "⚠️ Clear all transactions? Reply with 'YES' to confirm."
    )
    context.user_data["awaiting_reset"] = True


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Main message handler - parse expense and save."""
    user_input = update.message.text.strip()

    # Handle reset confirmation
    if context.user_data.get("awaiting_reset"):
        if user_input.upper() == "YES":
            with open(DATABASE_FILE, "w") as f:
                json.dump([], f)
            await update.message.reply_text("✅ All transactions cleared.")
        else:
            await update.message.reply_text("❌ Reset cancelled.")
        context.user_data["awaiting_reset"] = False
        return

    # Parse expense
    system_prompt = load_system_prompt()
    expense = parse_expense(user_input, system_prompt)

    # Save if successful
    if expense["status"] == "success":
        save_transaction(expense)

    # Reply to user
    response = format_response(expense)
    await update.message.reply_text(response)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log and handle errors."""
    print(f"Update {update} caused error {context.error}")


def main() -> None:
    """Start the bot."""
    # Validate environment
    if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
        raise ValueError(
            "FATAL: Missing TELEGRAM_TOKEN or GEMINI_API_KEY in .env"
        )
    
    print("✅ Environment validated")
    print(f"📁 Database: {DATABASE_FILE}")

    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Error handler
    application.add_error_handler(error_handler)

    # Start polling
    print("🤖 Bot is running... (Press Ctrl+C to stop)")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
