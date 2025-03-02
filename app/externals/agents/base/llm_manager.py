from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts.base import BasePromptTemplate
from pydantic import BaseModel


class BaseLLMManager:
    """Manages the interaction between a language model and prompts."""

    def __init__(self, llm: BaseChatModel):
        self.llm = llm

    def get_runnable(
        self,
        prompt: BasePromptTemplate,
        pydantic_parser: BaseModel | None = None,
        tools: list | None = None,
    ):
        """
        Configure and return a runnable LLM pipeline.

        Args:
            prompt (BasePromptTemplate): The prompt template.
            pydantic_parser (BaseModel, optional):Parser for structured output.
            tools (list, optional): List of tools to bind to the model.

        Returns:
            Runnable: A composed pipeline of the prompt and LLM.
        """
        llm = self.llm
        if tools:
            llm = llm.bind_tools(tools)
        if pydantic_parser:
            llm = llm.with_structured_output(pydantic_parser)
        return prompt | llm
