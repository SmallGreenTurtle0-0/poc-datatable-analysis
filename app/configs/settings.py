from __future__ import annotations

import os

from dotenv import load_dotenv
from loguru import logger

load_dotenv()


class Settings:
    _instance = None

    def __new__(cls) -> Settings:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        logger.info('Initializing settings')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        logger.info('Settings successfully loaded.')


settings = Settings()
