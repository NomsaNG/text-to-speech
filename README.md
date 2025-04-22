# 🎙️ Text to Speech App with Flet & Murf AI

This is a simple yet powerful Text-to-Speech (TTS) application built using [Flet](https://flet.dev/) and [Murf AI](https://murf.ai/). It allows users to input text, select a voice and mood, adjust pitch, and generate lifelike AI audio.


---

## Features

- 🎤 Convert text into high-quality speech using Murf.ai voices
- 🗣️ Choose from multiple voices like *Samantha*, *Miles*, and *Natalie*
- 😃 Customize tone with various moods (Conversational, Promo, Angry, etc.)
- 🎚️ Adjust pitch using an intuitive slider
- 💾 Save and playback the generated audio within the app
- 🖤 Stylish dark-themed UI with smooth interactions

---

## Technologies Used

- [Flet](https://flet.dev/) - for building the interactive UI
- [Murf Python SDK](https://pypi.org/project/murf/) - for text-to-speech generation
- [Python dotenv](https://pypi.org/project/python-dotenv/) - for handling environment variables
- [Requests](https://pypi.org/project/requests/) - for downloading audio files

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/NomsaNG/text-to-speech-app.git
   cd text-to-speech-app
    ```

2. **Create a virtual environment and activate it**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your .env file**
    ```bash
    API_KEY=your_murf_api_key_here
    ```

5. **Run the app**
    ```bash
    python main.py
    ```

6. **Voice & Mood Settings**
Each voice supports different moods. Some examples:

- Samantha: Conversational, Luxury, Angry, Newscast

- Miles: Promo, Sad, Sports Commentary, Pirate

- Natalie: Meditative, Inspirational, Furious

You can preview available moods in the terminal by uncommenting this section:
    ```bash
    # for voice in voices:
    #     print(f"Voice ID: {voice.voice_id}, Name: {voice.display_name}, Moods: {voice.available_styles}")
    ```





