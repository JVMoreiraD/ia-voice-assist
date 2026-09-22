## IA-VOICE-ASSIST

**Author:** João Vitor Moreira Duarte

---

### About

IA Voice Assist is a Python-based voice assistant that integrates:

* **Speech-to-Text (STT)** — captures and transcribes user audio
* **LLM Processing** — sends the transcription to a language model
* **Text-to-Speech (TTS)** — streams and converts the response back into audio

The goal of this project is to provide a simple assistant that listens, answers questions, and potentially performs tasks using MCP.

---

### Dependencies

This project uses **uv** for dependency management and execution.

To install dependencies:

```sh
(.venv) C:\ia-voice-assist> uv sync
```

---

### Running the Project

```sh
(.venv) C:\ia-voice-assist> uv run ia-voice-assist
```
