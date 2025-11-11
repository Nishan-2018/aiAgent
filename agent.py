import subprocess
import json
import re

MODEL = "llama3.1:latest"   # change if you're using another model

def call_ollama(prompt):
    """Call Ollama and return raw text output."""
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout

def extract_json(text):
    """Extract JSON from text safely using regex."""
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        else:
            return {"error": "No JSON found", "raw_output": text}
    except Exception as e:
        return {"error": f"JSON parse error: {str(e)}", "raw_output": text}

def create_todo_agent(goal):
    prompt = f"""
You are an AI task planner.

Break down the following goal into a structured to-do list with steps.

Respond ONLY in pure JSON in this format:

{{
  "goal": "...",
  "tasks": [
    {{
      "task": "...",
      "steps": ["...", "..."]
    }}
  ]
}}

Goal: "{goal}"
Return only valid JSON — no explanation.
    """

    raw_output = call_ollama(prompt)
    return extract_json(raw_output)

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    result = create_todo_agent(goal)

    print("\n✅ Final Parsed TODO JSON:\n")
    print(json.dumps(result, indent=2))

