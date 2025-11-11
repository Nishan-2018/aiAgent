# ✅ **README.md (Complete End-to-End Guide)**

````markdown
# ✅ AI Todo Agent using Llama 3.2 & Python

This project is a simple **AI-powered Todo Agent** built using **Llama 3.2**, **Ollama**, and **Python**.  
It takes a task from the user and automatically generates:

✅ A structured **todo list**  
✅ Step-by-step instructions on how to complete it  
✅ Extendable logic to build more automation later

This README contains a complete **end-to-end setup**, from installation to running the agent.

---

# 📌 1. Prerequisites

### ✅ macOS (Mac M1/M2/M3/M4)  
You already have everything needed: Python, Homebrew support, Apple Silicon optimization.

### ✅ Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
````

---

# 📌 2. Install Ollama (Required for Llama Model)

Ollama lets you run Llama locally.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Check installation:

```bash
ollama --version
```

---

# 📌 3. Pull Llama 3.2 Model

```bash
ollama pull llama3.2
```

Verify model:

```bash
ollama list
```

---

# 📌 4. Create a Python Virtual Environment

Inside your project folder:

```bash
python3 -m venv venv
source venv/bin/activate
```

Deactivate anytime:

```bash
deactivate
```

---

# 📌 5. Install Python Dependencies

```bash
pip install ollama
```

---

# 📌 6. Create `agent.py` (Main Todo Agent File)

```python
from ollama import Client

client = Client(host='http://localhost:11434')

def todo_agent(task):
    prompt = f"""
    You are an AI Todo Agent. Your job:
    - Understand the given task
    - Convert it into a structured TODO list
    - Provide clear step-by-step instructions

    Task: {task}

    Output Format:
    ✅ Todo List
    ✅ Steps to complete the task
    """

    response = client.generate(model='llama3.2', prompt=prompt)
    return response['response']


if __name__ == "__main__":
    user_task = input("Enter your task: ")
    print("\n--- AI Todo Agent Output ---\n")
    result = todo_agent(user_task)
    print(result)
```

---

# 📌 7. Run the Agent

Start Ollama server (runs automatically usually):

```bash
ollama serve
```

Then run your script:

```bash
python agent.py
```

Enter any task, for example:

```
Prepare for DevOps interview
```

And the agent will generate a full todo plan.

---

# 📌 8. GitHub Setup (Push Your Code)

### Initialize Git

```bash
git init
```

### Add All Files

```bash
git add .
```

### Commit

```bash
git commit -m "Initial commit with AI todo agent"
```

### Add GitHub Remote

```bash
git remote add origin https://github.com/USERNAME/REPO.git
```

### Push to GitHub

```bash
git push -u origin main
```

---

# 📌 9. Project Structure

```
/todo-agent
    ├── agent.py
    ├── README.md
    ├── venv/
```

---

# 📌 10. How It Works (Short Explanation for Interviews)

This project uses:

✅ **Ollama** → Runs the Llama 3.2 model locally
✅ **Llama 3.2** → Processes the text and generates todo steps
✅ **Python Ollama Client** → Connects Python to the local LLM server
✅ **Custom Prompting** → Converts tasks into todo lists

**Flow:**
User Input → Python → Ollama (Llama Model) → AI Creates Todo List → Output Displayed

This shows strong knowledge of **LLM integration**, **prompt engineering**, and **local AI execution** (important for interviews).


