# Pygmalion Chatbot

Pygmalion Chatbot is an advanced conversational AI model built upon the Pygmalion-350M model, designed to provide human-like interactions with a focus on roleplay and natural dialogue capabilities. This chatbot is suitable for both developers and users seeking an engaging virtual assistant experience.

## Features

- **Conversational AI:** Supports natural conversations with context understanding.
- **Roleplay Focus:** Designed to handle roleplay scenarios effectively.
- **Lightweight Model:** Utilizes Pygmalion-350M for efficiency and performance.
- **Text-to-Speech Integration:** Realistic voice responses using `pyttsx3`.
- **Speech Recognition:** Voice commands via `speech_recognition`.
- **Jokes & Wikipedia Search:** Light-hearted interactions and quick information retrieval.
- **Weather Updates:** Fetches current weather using OpenWeatherMap API.
- **Real-Time Clock:** Provides current time updates.

## Installation

```bash
# Clone the repository
git clone https://github.com/username/pygmalion-chatbot.git
cd pygmalion-chatbot

# Create virtual environment
python -m venv env
source env/bin/activate # Linux/Mac
env\Scripts\activate # Windows

# Install dependencies
pip install -r requirements.txt
```

## Dependencies

- `torch`
- `transformers`
- `speechrecognition`
- `pyttsx3`
- `pyjokes`
- `wikipedia-api`
- `requests`

## Usage

```bash
python jarvis.py
```

## Example Commands

- "What is the time?"
- "Tell me a joke."
- "Search Wikipedia for Elon Musk."
- "What's the weather in Delhi?"

## API Key Setup

Weather updates require an API key from OpenWeatherMap:

1. Visit [OpenWeatherMap](https://openweathermap.org/).
2. Create an account and get your API key.
3. Replace `api_key` in `jarvis.py` with your key.

## License

This project is licensed under the MIT License.
