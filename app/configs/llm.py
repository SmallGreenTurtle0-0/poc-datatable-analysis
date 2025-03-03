from __future__ import annotations

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from loguru import logger

from .settings import settings


def _init_llm_gpt_4o_mini() -> ChatOpenAI:
    logger.info('Initialize OpenAI Chat GPT')
    if not settings.openai_api_key:
        raise ValueError('Missing OpenAI API key or model in settings.')

    try:
        return ChatOpenAI(
            model='gpt-4o-mini',
            temperature=0.8,
            api_key=settings.openai_api_key,
        )
    except Exception as e:
        logger.error(f'Connect to OpenAI Chat GPT error: {e}')
        raise RuntimeError('Failed to initialize OpenAI Chat GPT') from e


def _init_llm_llama_32() -> ChatOllama:
    logger.info('Initialize Ollama: model Llama 3.2')

    try:
        return ChatOllama(
            model='llama3.2',
            temperature=0.8,
        )
    except Exception as e:
        logger.error(f'Connect to Ollama: model Llama 3.2 error: {e}')
        raise RuntimeError(
            'Failed to initialize Ollama: model Llama 3.2',
        ) from e


def _init_llm_llama_321b() -> ChatOllama:
    logger.info('Initialize Ollama: model Llama 3.2.1b')

    try:
        return ChatOllama(
            model='llama3.2.1b',
            temperature=0.8,
        )
    except Exception as e:
        logger.error(f'Connect to Ollama: model Llama 3.2.1b error: {e}')
        raise RuntimeError(
            'Failed to initialize Ollama: model Llama 3.2.1b',
        ) from e


llm_gpt_4o_mini: ChatOpenAI = _init_llm_gpt_4o_mini()
llm_llama_32: ChatOllama = _init_llm_llama_32()
llm_llama_321b: ChatOllama = _init_llm_llama_321b()
