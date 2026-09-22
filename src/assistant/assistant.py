from api.api import API
from listen.listen import ListenMic
from voice.speak import Voice


class Assistant:
    def __init__(self, api_url: str):
        self.listen = ListenMic()
        self.voice = Voice(API(api_url))
        self.api = API(api_url)

    def ia_speak(self, stream: str):
        buffer = ""

        for chunk in self.api.request_stream(stream):
            print(chunk, end="", flush=True)

            buffer += chunk

            # fala a cada frase (melhor que palavra por palavra)
            if any(p in buffer for p in [".", "!", "?"]):
                self.voice.speak(buffer)
                buffer = ""

        # fala resto
        if buffer.strip():
            self.voice.speak(buffer)

    def send_to_ai(self):
        self.voice.speak("Pode falar, estou ouvindo")
        text = self.listen.listen_and_transcribe()
        if text:
            self.ia_speak(text)
        else:
            self.voice.speak("Desculpe, não entendi. Pode repetir?")

    def start_listen(self):
        self.listen.listen_and_wait(self.send_to_ai)
