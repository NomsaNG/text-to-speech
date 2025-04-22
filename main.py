# Imports
import flet as ft
import requests 
import os
from murf import Murf
from api_key import API_KEY


# API Client
client = Murf(api_key=API_KEY)

voices = client.text_to_speech.get_voices()
for voice in voices:
    print(f"Voice ID: {voice.voice_id}, Name: {voice.display_name}, Moods: {voice.available_styles}")

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

    # mood_selection

    # enter_button


# Run the App
if __name__ == "__main__":
    ft.app(target=main)