import time
import pyttsx3


class Speaker:
    def __init__(self, cooldown=2):
        self.engine = pyttsx3.init()
        self.cooldown = cooldown
        self.last_spoken = 0

        self.voices = self.engine.getProperty("voices")

        # Try to map voices
        self.voice_map = {
            "en": None,
            "hi": None,
            "bn": None
        }

        for v in self.voices:
            name = v.name.lower()
            if "english" in name and self.voice_map["en"] is None:
                self.voice_map["en"] = v.id
            elif "hindi" in name and self.voice_map["hi"] is None:
                self.voice_map["hi"] = v.id
            elif "bengali" in name or "bangla" in name:
                self.voice_map["bn"] = v.id

    def say(self, text, language="en"):
        current_time = time.time()
        if current_time - self.last_spoken < self.cooldown:
            return

        voice_id = self.voice_map.get(language)

        if voice_id:
            self.engine.setProperty("voice", voice_id)

        self.engine.say(text)
        self.engine.runAndWait()

        self.last_spoken = current_time
