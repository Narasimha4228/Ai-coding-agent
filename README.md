# AI Coding Agent 🤖

An AI-powered Python command-line tool that converts plain-English instructions into executable Python code using the Groq API.

## 🚀 Features

- Generate Python code from natural-language instructions.
- Uses Groq LLM API.
- Supports string operations, mathematical calculations, lists, and dictionaries.
- Displays generated code in the terminal.
- Automatically saves generated code as a `.py` file.
- Handles API and network errors.
- Uses environment variables to protect API keys.

## 🛠️ Technologies Used

- Python 3.11
- Groq API
- REST API (`urllib`)
- JSON
- Python Standard Library

## 📁 Project Structure

```text
ai-coding-agent/
│
├── main.py
├── .env
├── .gitignore
├── README.md
│
└── generated/
    └── generated_code.py
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/ai-coding-agent.git
cd ai-coding-agent
```

**2. Create a virtual environment (optional)**

```bash
python -m venv venv
```

**3. Configure your Groq API key**

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**4. Run the application**

```bash
python main.py
```

## 💡 Example

**Input:**

```text
Create a Python program to check whether a number is even or odd.
```

**Output:**

The AI generates Python code, displays it in the terminal, and saves it to:

```text
generated/generated_code.py
```

## 🔐 Security

Never upload your `.env` file or expose your API key on GitHub.

## 🎯 Project Objective

To build a simple AI coding assistant that converts natural-language tasks into Python programs, helping developers generate code faster.

## 👨‍💻 Author

Ch. Narasimha Reddy

AI/ML Enthusiast | Python Developer
