import json

import requests


class API:
    def __init__(self, url: str):
        self.prompt =  """
    Você é um assistente que responde APENAS em texto simples (plain text).
    Não use markdown.
    Não use símbolos como #, *, _, -, >, listas ou formatação.
    Não use emojis.
    Responda apenas com frases normais, como fala natural.
    """
        self.url = url

    def request(self, question: str) -> str:
        payload = {
            "model": "local-model",
            "messages": [
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": question}
            ],
            "temperature": 0.7
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def request_stream(self, question: str):
        payload = {
            "model": "local-model",
            "messages": [
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": question}
            ],
            "temperature": 0.7,
            "stream": True,
        }

        with requests.post(self.url, json=payload, stream=True) as response:
            response.raise_for_status()

            for line in response.iter_lines():
                if not line:
                    continue

                if line.startswith(b"data: "):
                    data = line[len(b"data: "):]

                    if data == b"[DONE]":
                        break

                    chunk = json.loads(data)
                    content = chunk["choices"][0]["delta"].get("content")

                    if content:
                        yield content