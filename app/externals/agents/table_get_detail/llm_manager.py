from __future__ import annotations

from app.configs.llm import llm_gpt_4o_mini
from app.configs.llm import llm_llama_32
from app.configs.llm import llm_llama_321b
from app.externals.agents.base.llm_manager import BaseLLMManager


class LLMManager(BaseLLMManager):
    def __init__(self) -> None:
        super().__init__(
            llm=llm_gpt_4o_mini.with_fallbacks(
                [llm_llama_321b, llm_llama_32],
            ),
        )
