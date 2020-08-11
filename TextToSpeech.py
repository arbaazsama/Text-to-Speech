""" Text to Speach """
""" Environment: talk_program """

import io
import pygame
from gtts import gTTS

def speak(text_to_speak):
    with io.BytesIO() as file:
        gTTS(text=text_to_speak, lang='en').write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

if __name__ == "__main__":
    text = str(input("What would like me to say?: "))
    speak(text)
    
