from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    parser_host: SecretStr
    updates_rate: SecretStr
    busted_chats_pic: SecretStr
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')


config = Settings()
