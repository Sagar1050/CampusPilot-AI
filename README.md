# CampusPilot AI — Your Intelligent Study Companion

CampusPilot AI is an AI-powered study companion that helps students organize academic tasks, plan study time, and get AI-assisted study support.

## Features

- **Task Management:** Add and track academic tasks.
- **Study Planner:** Generate a simple seven-day study plan.
- **AI Study Assistant:** Ask study-related questions and receive AI-generated responses.
- **Task-Aware Assistance:** Get help informed by saved tasks.
- **Conversation History:** Continue a conversation or start a new one.
- **Dashboard:** View task progress and completed tasks.

## Technology Stack

- Python
- Flask
- SQLite
- HTML and CSS
- Google Gemini API

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sagar1050/CampusPilot-AI.git
cd CampusPilot-AI
```

### 2. Create a virtual environment

```cmd
py -3.11 -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

Install Flask, `google-genai`, `python-dotenv`, `Markdown`, and `nh3`.

### 4. Configure environment variables

Create a `.env` file in the project root containing:

```env
GEMINI_API_KEY=your_gemini_api_key
FLASK_SECRET_KEY=your_random_secret_key
```

Replace the example values with your own credentials. Never commit your `.env` file or publish your API key.

### 5. Run the application

```cmd
python app.py
```

Open the local address shown in your terminal.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Hackathon Note

CampusPilot AI demonstrates a simulated Alexa+-style conversational study assistant through a web interface. It is not a native Alexa+ integration unless that integration is implemented separately.
