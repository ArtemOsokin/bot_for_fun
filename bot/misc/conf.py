from os import environ
from typing import Final


class Settings:
    DEBUG: bool = environ.get('DEBUG', True)

    TOKEN: Final = environ.get('BOT', 'define me!')

    # webhook settings
    WEBHOOK_HOST = environ.get('WEBHOOK_HOST')
    WEBHOOK_PATH = environ.get('WEBHOOK_PATH', '')
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

    WEBAPP_HOST = environ.get('WEBAPP_HOST', 'localhost')
    WEBAPP_PORT = environ.get('WEBAPP_PORT', 80)

    OPENAPI_KEY: Final = environ.get('OPENAPI_KEY', 'Need openapi_key!')
    OPENAPI_ORG: Final = environ.get('OPENAPI_ORG', 'Need openapi_organisation!')

    DB_URL: Final = environ.get('DB_URL', 'Need sqlite database url')

    ADMINS: list[int] = list(map(int, environ.get('ADMINS').split(',')))


settings = Settings()
