from __future__ import annotations

from langchain_core.prompts import PromptTemplate
from loguru import logger

from .llm_manager import LLMManager
from .prompts import DETAIL_DATA_TABLE
from .states import TableGetDetailState
from app.utils.datatable.table_info import get_column_descriptions
from app.utils.datatable.table_info import get_table_data


class TableGetDetailAgent:
    def __init__(self):
        self.llm_manager = LLMManager()
        self.mapping_name_node = {
            'get_schema': self.get_schema,
            'get_detail': self.get_detail,
        }

    async def get_schema(
        self,
        state: TableGetDetailState,
    ) -> TableGetDetailState:
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

    async def get_detail(
        self,
            state: TableGetDetailState,
    ) -> TableGetDetailState:
        prompt_template = PromptTemplate.from_template(DETAIL_DATA_TABLE)
        runnable = self.llm_manager.get_runnable(prompt=prompt_template)
        detail_info = await runnable.ainvoke(
            {
                'question': state.get('question'),
                'schema_info': state.get('schema_info'),
                'table': state.get('table'),
            },
        )
        state.update({
            'response': detail_info,
        })
        return state
