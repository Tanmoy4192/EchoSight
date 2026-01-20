import pyttsx3


class Speaker:
    def __init__(self):
        pass  # do NOT keep engine alive

    def say(self, text):
        if not text:
            return

        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 170)

            for voice in engine.getProperty("voices"):
                if "english" in voice.name.lower():
                    engine.setProperty("voice", voice.id)
                    break

            engine.say(text)
            engine.runAndWait()
            engine.stop()

        except Exception as e:
            print("Speaker error:", e)
