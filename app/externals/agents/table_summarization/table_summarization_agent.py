from __future__ import annotations

from langchain_core.prompts import PromptTemplate
from loguru import logger

from .llm_manager import LLMManager
from .prompts import SUMMARY_DATA_TABLE
from .states import TableSummarizationState
from app.utils.datatable.table_info import get_column_descriptions
from app.utils.datatable.table_info import get_table_data


class TableSummarizationAgent:
    def __init__(self):
        self.llm_manager = LLMManager()
        self.mapping_name_node = {
            'get_schema': self.get_schema,
            'summarize': self.summarize,
        }

    async def get_schema(
        self,
        state: TableSummarizationState,
    ) -> TableSummarizationState:
        try:
            state.update({
                'schema_info': get_column_descriptions(),
                'table': get_table_data(),
                'flow': 'continue',
            })
        except Exception as e:
            logger.exception(e)
            state.update({
                'flow': 'end',
                'response': (
                    'Unable to read the data table and'
                    'its column descriptions.'
                    'This may be because the data table and'
                    'its schema information have not been uploaded.'
                    'Please check and ensure that both are provided.'
                ),
            })
        return state

    async def summarize(
        self,
            state: TableSummarizationState,
    ) -> TableSummarizationState:
        prompt_template = PromptTemplate.from_template(SUMMARY_DATA_TABLE)
        runnable = self.llm_manager.get_runnable(prompt=prompt_template)
        summarization = await runnable.ainvoke(
            {
                'question': state.get('question'),
                'schema_info': state.get('schema_info'),
                'table': state.get('table'),
            },
        )
        state.update({
            'response': summarization,
        })
        return state
