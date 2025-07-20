# 🤖 Jarvis Voice AI Assistant

Jarvis is a Python-based voice assistant powered by Google Gemini, speech recognition, and intelligent web browsing. Built to respond to voice commands, play music, and answer queries — all with a touch of AI magic.

## 🚀 Features

- Wake word activation: “Jarvis”
- AI-powered responses via Google Gemini
- Voice-controlled web browsing
- Music playback from a custom library
- Text-to-speech using gTTS and pygame
- Saves conversations to timestamped logs

## 🧰 Technologies Used

- `speech_recognition`
- `gtts` + `pygame` for audio output
- `google-generativeai` for AI responses
- `webbrowser` for browsing
- `pyaudio`, `pyttsx3`, `contextlib`

## 📦 Installation

```bash
git clone https://github.com/shamsulhaqcodes/Jarvis-VoiceAI-Assistant.git
cd Jarvis-VoiceAI-Assistant
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Configuration
To activate Gemini AI integration, set your API key in the aiProcess() function within main.py:

```bash
genai.configure(api_key="your_api_key")
```
🔐 Tip: Keep your API key private! Never commit or push it to GitHub.

## 🎵 Music Library
Customize your music experience by editing musicLibrary.py:

```bash
music = {
    "song name": "https://example.com/your-song-link"
}
```
Use voice commands like:

Play [song name]
Jarvis will open the song link in your browser for playback.

## 🗣️ Running Jarvis
Launch your assistant with:

```bash
python main.py
```
Jarvis will:

Listen for the wake word “Jarvis”

Accept spoken commands

Respond using Gemini AI

Speak replies via gTTS and pygame

Save chat logs in timestamped .txt files

## 📁 Project Structure
├── main.py
├── musicLibrary.py
├── requirements.txt
├── README.md
├── temp.mp3
└── jarvis_response_*.txt
## 🙌 Credits
Developed by ShamsulHaq

Grateful for inspiration from the Python and AI developer communities 💡 Voice tech, creative code, and helpful companions — this is the spirit of Jarvis.

## 🛡️ License
This project is licensed under the MIT License
