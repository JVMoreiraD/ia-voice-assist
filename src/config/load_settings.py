import os

from dotenv import dotenv_values

from config.configuration import Configuration


def _require(config: dict, key: str) -> str:
    value = config.get(key)
    if value is None or value == "":
        raise ValueError(
            f"Variável de ambiente obrigatória não definida: {key}")
    return value


def load_settings() -> Configuration:
    env_path = os.environ.get("APP_ENV_FILE", ".env")
    config = dotenv_values(env_path)
    return Configuration(
        api_url=_require(config, "API_URL")
    )