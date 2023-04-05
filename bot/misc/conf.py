from os import environ
from typing import Final


class Settings:
    DEBUG: bool = environ.get('DEBUG', True)

    TOKEN: Final = environ.get('BOT_TOKEN', 'define me!')

    OPENAPI_KEY: Final = environ.get('OPENAPI_KEY', 'Need openapi_key!')
    OPENAPI_ORG: Final = environ.get('OPENAPI_ORG', 'Need openapi_organisation!')
