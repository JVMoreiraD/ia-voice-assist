from assistant.assistant import Assistant
from config import load_settings


def main():
    configuration = load_settings()
    assistant = Assistant(configuration.api_url)
    assistant.start_listen()


main()
