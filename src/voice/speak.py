from typing import cast

import pyttsx3

from api.api import API


class Voice:
    def __init__(self, api: API):
        self.api: API = api

    def speak(self, text: str):
        engine = pyttsx3.init()
        voices = cast(list, engine.getProperty("voices"))
        
        for voice in voices:
                    if "portuguese" in voice.name.lower() or "brazil" in voice.name.lower():
                        engine.setProperty("voice", voice.id)
                        break
        
        engine.setProperty("rate", 200)
        engine.setProperty("volume", 0.8)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
