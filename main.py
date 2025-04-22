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
# Uncomment the following lines to print available voice names, voice id, and their moods on the terminal
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
    page.title = "Text to Speech App"
    page.padding = 40
    page.bgcolor = "#1E1E2F"
    
    
    # Create the UI Widgets
    title = ft.Text("Text to Speech App", size=42, weight=ft.FontWeight.BOLD, color="#8E24AA")
    
    # Text Input field where user can enter text to be converted to speech
    text_input = ft.TextField(
        label="Enter some text here...",
        width=350,
        bgcolor="#2A2A3B",
        color="#ffffff",
        border_radius=15,
        border_color="#8E24AA"
    )
    
    # Dropdown for selecting voice
    voice_selection = ft.Dropdown(
        label="Choose Voice",
        options=[ft.dropdown.Option(voice) for voice in VOICE_MOODS.keys()],
        width=350,
        bgcolor="#2A2A3B",
        color="#ffffff",
        value="Miles"
    )
    
    # Dropdown for selecting mood for the selected voice (each voice has different moods)
    mood_selection = ft.Dropdown(
        label="Choose Mood",
        width=350,
        bgcolor="#2A2A3B",
        color="#ffffff"
    )
    
    # Update the mood dropdown based on the selected voice
    def update_moods(e=None):
        selected_voice = voice_selection.value
        mood_selection.options = [
            ft.dropdown.Option(mood) for mood in VOICE_MOODS.get(selected_voice, {}).get("moods", [])
        ]
        mood_selection.value = mood_selection.options[0].text if mood_selection.options else None
        page.update()
        
    voice_selection.on_change = update_moods
    update_moods()
        
    voice_speed = ft.Slider(
        min=-30, max=30, value=0, divisions=10, label="{value}%", active_color="#8E24AA"
    )
    
    
    # Generate AI Voice
    def generate_audio():
        selected_voice = voice_selection.value 
        voice_id = VOICE_MOODS.get(selected_voice,{}).get("voice_id")
        
        if not text_input.value.strip():
            print("ERROR, you need some text...")
            return None
        
        try:
            response = client.text_to_speech.generate(
                format="MP3",
                sample_rate=48000.0,
                channel_type="STEREO",
                text=text_input.value,
                voice_id=voice_id,
                style=mood_selection.value,
                pitch=voice_speed.value
            )
            return response.audio_file if hasattr(response ,"audio_file") else None 
        except Exception as e:
            print(f"Error: {e}")
            return None 
    # Save and Play the generated audio   
    def save_and_play(e):
        audio_url = generate_audio()
        if not audio_url:
            print("Error: no audio found...")
            return 
        
        try:
            response = requests.get(audio_url, stream=True)
            if response.status_code == 200:
                file_path = os.path.abspath("audio.mp3")
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                        
                print("Audio Saved As:", file_path)
                
                page.overlay.clear()
                page.overlay.append(ft.Audio(src="audio.mp3", autoplay=True))
                page.update()
            else:
                print("Failed to get audio")
        except Exception as e:
            print("ERROR",e)
                
    
    # enter_button 
    btn_enter = ft.ElevatedButton(
        "Generate Voice",
        bgcolor="#8E24AA",
        color="#1E1E2F",
        on_click=save_and_play,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15),
                            bgcolor={
            ft.ControlState.HOVERED: "#6A1B9A",  # Hover color
            ft.ControlState.DEFAULT: "#8E24AA",  # Default color
        } )
        
    )
    
    
    # Build a UI Container
    input_container = ft.Container(
        content=ft.Column(
            controls=[ text_input, voice_selection, mood_selection,
                      ft.Text("Adjust Pitch", size=18, weight=ft.FontWeight.BOLD, color="#8E24AA"),
                      voice_speed, btn_enter],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=20,
        bgcolor="#2A2A3B",
        shadow=ft.BoxShadow(blur_radius=12, spread_radius=2, color="#8E24AA")   
    )
    # Add the title and input container to the page
    page.add(
        ft.Column(
            controls=[title, input_container],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()  # Update the page to reflect changes


# Run the App
if __name__ == "__main__":
    ft.app(target=main, assets_dir=".")