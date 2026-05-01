# Money Tracker via Telegram API - Project Instructions

## Project Context
This project is a Telegram bot that helps users track their expenses using natural language. It uses **Gemini 3 Flash** as the core LLM and **GEPA** to optimize the parsing prompts.

## Coding Standards
- Use `python-telegram-bot` for the Telegram API.
- Use `litellm` for interacting with Gemini.
- Keep parsing logic optimized via GEPA-generated instructions found in `best_system_prompt.txt`.

## Project Structure
- `optimize_parser.py`: GEPA optimization script to refine bot instructions.
- `bot.py`: Main Telegram bot handler (to be created).
- `best_system_prompt.txt`: The latest optimized prompt for expense extraction.
- `.env`: API keys and project settings.

## GEPA Specifics
When modifying the parsing logic, ensure that the `trainset` in `optimize_parser.py` is updated with any new edge cases encountered in production.

## Chat Workflow – Always Use Skills
All interactions in this chat **must reference the system skills framework**:
- See `CHAT_WORKFLOW.md` for protocol
- See `system_skills.yaml` for skill definitions
- See `skills.md` for quick reference

**Every response must include**:
- Skill ID and name (e.g., "debug_error")
- Token cost estimate
- Skill template applied (request format, input/output format)

This ensures token efficiency and predictable, high-quality answers.
