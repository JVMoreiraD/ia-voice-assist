from collections.abc import Callable

import speech_recognition as sr


class ListenMic:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen_and_transcribe(self) -> str | None:
        """
        Escuta o audio do microfone e transcreve o texto.
        """
        with sr.Microphone() as source:
            audio = self.r.listen(source, timeout=15)
        try:
            # pyrefly: ignore [missing-attribute]
            text = self.r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return None

    def listen_and_wait(self, action: Callable):
        while True:
            r = self.r
            with sr.Microphone() as source:
                audio = r.listen(source)

            try:
                # pyrefly: ignore [missing-attribute]
                fala = r.recognize_google(audio, language="pt-BR")
                if "bonsai" in fala.lower():
                    action()
            except sr.UnknownValueError:
                print("Não consegui entender o que você disse.")
            except sr.RequestError as e:
                # pyrefly: ignore [missing-attribute]
                print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")