# eq-coach-mvp

real-time emotional intelligence communication app
📘 EQ Coach MVP — README

Welcome to the EQ Coach MVP repository — a modular, emotionally intelligent communication assistant designed to help users improve their tone, empathy, and clarity in real-time conversations. This project blends Firebase, OpenAI Codex, and FlutterFlow to deliver a cross-platform experience for dating, workplace, and family communication.

🧱 Folder Structure

eq-coach-mvp/
├── frontend/         # FlutterFlow export or web UI
├── backend/          # Firebase functions or Node/Python API
├── ai/               # Prompt templates, scoring logic
├── assets/           # Icons, UI elements
├── docs/             # README, roadmap, architecture notes
└── .env              # API keys (OpenAI, Firebase)

🔥 Tech Stack

OpenAI Codex / ChatGPT: Emotional tone analysis, reply generation, scoring

Firebase: Firestore for data storage, Cloud Functions for backend logic

FlutterFlow: UI for Android/iOS deployment

Python: Backend scaffolding and Codex integration

🚀 Key Features

Tone Analysis: Classifies user messages into emotional tones (e.g., warm, assertive, playful)

Reply Suggestions: Generates emotionally intelligent responses tailored to context

Gamified Scoring: Assigns points based on empathy, clarity, and positivity

Real-Time Feedback: Helps users improve communication habits over time

🔧 Setup Instructions

Clone the repo:

git clone https://github.com/shopiers/eq-coach-mvp.git
cd eq-coach-mvp

Install dependencies:

Python: pip install openai firebase-admin

Firebase CLI: npm install -g firebase-tools

Configure .env:

OPENAI\_API\_KEY=your\_openai\_key
FIREBASE\_PROJECT\_ID=your\_project\_id

Deploy Firebase Functions:

firebase deploy --only functions

🧠 Prompt Engineering Workspace

Located in /ai/prompts/:

tone\_classification.txt

reply\_generation.txt

scoring\_model.txt

Use Codex to iterate and refine emotional nuance.

📱 Frontend (FlutterFlow)

UI: Message input → Tone feedback → Suggested replies → Score display

Firebase integration via REST or Cloud Functions

Optional gamification: streaks, badges, scoreboard

🧪 Sample Codex Functions

# analyze\_tone.py

def analyze\_tone(message: str) -> dict:
# Use OpenAI API to classify tone
# Return tone label + confidence score

# generate\_replies.py

def generate\_replies(message: str, tone: str) -> list:
# Generate 3 emotionally intelligent replies

# score\_interaction.py

def score\_interaction(reply: str) -> int:
# Score based on empathy, clarity, positivity

🧩 Integration Notes

Firebase Cloud Functions wrap Codex calls and log results to Firestore

Firestore structure:

users/{userId}/messages/{messageId}

users/{userId}/scores/{date}

🧭 Roadmap

\[ ] Chrome extension for real-time tone coaching

\[ ] Multi-user scoring dashboard

\[ ] Vertical-specific prompt tuning (dating, workplace, family)

🤝 Contributing

Pull requests welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License

MIT License — feel free to remix, extend, and build on this foundation.

Endnote: Adding initial README with vision, modular structure, and onboarding notes on October 03rd, 2025

