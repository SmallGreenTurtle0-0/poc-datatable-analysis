from __future__ import annotations

import pandas as pd
from langchain_core.prompts import PromptTemplate
from loguru import logger

from .llm_manager import LLMManager
from .prompts import KEY_COLUMNS_TABLE
from .states import TableFilterColumnOutput
from .states import TableFilterColumnState
from app.utils.datatable.table_info import get_column_descriptions
from app.utils.datatable.table_info import get_table_data


class TableFilterColumnAgent:
    def __init__(self):
        self.llm_manager = LLMManager()
        self.mapping_name_node = {
            'get_schema': self.get_schema,
            'filter_column': self.filter_column,
        }

    async def get_schema(
        self,
        state: TableFilterColumnState,
    ) -> TableFilterColumnState:
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

    async def filter_column(
        self,
        state: TableFilterColumnState,
    ) -> TableFilterColumnState:
        prompt_template = PromptTemplate.from_template(KEY_COLUMNS_TABLE)
        runnable = self.llm_manager.get_runnable(
            prompt=prompt_template, pydantic_parser=TableFilterColumnOutput,
        )
        detail_info = await runnable.ainvoke(
            {
                'question': state.get('question'),
                'schema_info': state.get('schema_info'),
                'table': state.get('table'),
            },
        )

        # Retrieve the necessary column names returned from the LLM
        necessary_columns = detail_info.list_column_name

        # Retrieve the data table (assuming it's a pandas DataFrame)

        df = state.get('table')
        df = pd.DataFrame(df)

        # Compute the intersection between the returned column names and the DataFrame's columns,
        # preserving the order from the LLM output.
        filtered_columns = [col for col in necessary_columns if col in df.columns]

        # Filter the DataFrame with the necessary columns
        filtered_df = df[filtered_columns]

        # Update the state with the filtered DataFrame as the response.
        state.update({
            'response': filtered_df,
        })
        return state
