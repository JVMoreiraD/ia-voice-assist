
from assistant.assistant import Assistant
from config import load_settings

if __name__ == "__main__":
    configuration = load_settings()
    assistant = Assistant(configuration.api_url)
    assistant.start_listen()