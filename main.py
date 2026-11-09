
import os
import json
import re
import urllib.request
import urllib.error
from pathlib import Path

# Get API key
def get_api_key():
    key = os.getenv("GROQ_API_KEY")

    if key:
        return key

    env_file = Path(".env")

    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("GROQ_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")

    raise ValueError("Groq API key not found in .env")


# AI system instructions
SYSTEM_PROMPT = """
You are an expert Python coding assistant.

Convert the user's task into working Python code.

Rules:
1. Return ONLY Python code.
2. No explanations.
3. No Markdown code fences.
4. Write clean and readable Python.
5. Include necessary functions and examples.
"""


# Generate code using Groq API
def generate_code(task):

    api_key = get_api_key()

    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": task}
        ],
        "temperature": 0.2,
        "max_completion_tokens": 2000
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "ai-coding-agent/1.0"
        },
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))

    code = result["choices"][0]["message"]["content"]

    # Remove Markdown code fences
    code = re.sub(r"^```(?:python)?\s*", "", code.strip())
    code = re.sub(r"\s*```$", "", code.strip())

    return code


# Save generated Python code
def save_code(code):

    output_dir = Path("generated")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / "generated_code.py"

    file_path.write_text(code + "\n", encoding="utf-8")

    return file_path


# Main application
def main():

    print("===== AI CODING AGENT =====")

    task = input("\nEnter your coding task: ").strip()

    if not task:
        print("Please enter a task.")
        return

    try:
        print("\nGenerating Python code...")

        code = generate_code(task)

        print("\n===== GENERATED CODE =====")
        print(code)

        file_path = save_code(code)

        print("\nCode saved successfully!")
        print("File location:", file_path)

    except urllib.error.HTTPError as error:
        print("\nHTTP Error:", error.code)
        print(error.read().decode("utf-8", errors="replace"))

    except urllib.error.URLError as error:
        print("\nNetwork error:", error.reason)

    except Exception as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()
