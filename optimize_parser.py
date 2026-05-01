import os
import json
from gepa import optimize
from typing import Dict, Any

# --- CONFIGURATION ---
# Replace with your actual Gemini API Key or set it in your environment
# os.environ["GOOGLE_API_KEY"] = "your-api-key-here"

def parse_expense(instructions: str, user_message: str) -> str:
    """
    Simulates calling an LLM with instructions to parse a message.
    """
    # Placeholder for the actual LLM call logic
    return f"SIMULATED_LLM_OUTPUT using prompt: {instructions[:20]}... for message: {user_message}"

def evaluation_metric(example: Dict[str, Any], prediction: str) -> tuple[float, str]:
    """
    Evaluates if the 'prediction' correctly parsed the 'example'.
    Returns (score, feedback).
    """
    if "SIMULATED" in prediction:
        score = 1.0
        feedback = "The format is correct."
    else:
        score = 0.0
        feedback = "The model failed to follow instructions."
        
    return score, feedback

# --- DATASET ---
trainset = [
    {
        "input": "Spent 15 euros on pizza today",
        "answer": '{"amount": 15, "currency": "EUR", "category": "food", "item": "pizza"}'
    },
    {
        "input": "bought a coffee for $5",
        "answer": '{"amount": 5, "currency": "USD", "category": "drinks", "item": "coffee"}'
    }
]

def run_optimization():
    print("🚀 Starting GEPA optimization...")
    
    initial_prompt = (
        "Extract the expense details from the user message. "
        "Return JSON with keys: amount, currency, category, item."
    )

    result = optimize(
        fn=parse_expense,
        initial_instructions=initial_prompt,
        trainset=trainset,
        reflection_lm="google/gemini-3-flash-preview", 
        max_iterations=3
    )

    print(f"\n✅ Best Prompt Generated:\n{result.best_candidate}")
    
    with open("best_system_prompt.txt", "w") as f:
        f.write(result.best_candidate)
    print("\n💾 Saved to 'best_system_prompt.txt'")

if __name__ == "__main__":
    run_optimization()
