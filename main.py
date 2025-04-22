# Imports
import flet as ft
import requests 
import os
from murf import Murf
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
# Load environment variables
if API_KEY is None:
    raise ValueError("API_KEY not found. Please set the API_KEY environment variable.")


# API Client
client = Murf(api_key=API_KEY)

voices = client.text_to_speech.get_voices()
# for voice in voices:
#     print(f"Voice ID: {voice.voice_id}, Name: {voice.display_name}, Moods: {voice.available_styles}")

# Voice Settings
VOICE_MOODS = {
  "Samantha": { 
      "voice_id": "en-US-samantha",
      "moods": ['Conversational', 'Luxury', 'Promo', 'Angry', 'Sad', 'Newscast'],
     },

  "Miles": { 
      "voice_id": "en-US-miles",
      "moods": ['Conversational', 'Promo', 'Sports Commentary', 'Narration', 'Newscast', 'Sad', 'Angry', 'Calm', 'Terrified', 'Inspirational', 'Pirate'],
     },

    "Natalie": { 
      "voice_id": "en-US-natalie",
      "moods": ['Promo', 'Narration', 'Newscast Formal', 'Meditative', 'Sad', 'Angry', 'Conversational', 'Newscast Casual', 'Furious', 'Sorrowful', 'Terrified', 'Inspirational']
     }
}

# Build the Flet App
def main(page: ft.Page):
    page.title = "Text to Speech"
    page.padding = 40
    page.bgcolor = "#1E1E2F"


    # Create UI Elements
    title = ft.Text("Text to Speech", size=42, weight=ft.FontWeight.BOLD, color="#FFD700")

    text_input = ft.TextField(
        label="Enter text to convert to speech",
        width=350,
        bgcolor="#2A2A3B",
        color="#FFF",
        border_color="#FFD700",
        border_radius=15,
    )

    # voice_selection
    voice_selection = ft.Dropdown(
        label="Choose Voice",
        options=[ft.dropdown.Option(voice) for voice in VOICE_MOODS.keys()],
        width=350,
        bgcolor="#2A2A3B",
        color="#ffffff",
        value="Miles"
    )

    # mood_selection
    mood_selection = ft.Dropdown(
        label="Choose Mood",
        width=350,
        bgcolor="#2A2A3B",
        color="#ffffff"
    )

    # enter_button

    # Build a UI Container (return everything we created as a container)

    input_container = ft.Container (   
        content=ft.Column(
        controls = [title, text_input],
        spacing=15,
        alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=20,
        bgcolor="#2A2A3B",
        shadow=ft.BoxShadow(blur_radius=12,spread_radius=2, color="#FFD700")
    )

    page.add(
        ft.Column(
            controls = [title, input_container],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    
    page.update()

# Run the App
if __name__ == "__main__":
    ft.app(target=main)