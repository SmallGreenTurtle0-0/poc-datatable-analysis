from __future__ import annotations

import pandas as pd

from app.utils.constants.table_info import COLUMNS_DESCRIPTION_PATH
from app.utils.constants.table_info import TABLE_PATH


def get_column_descriptions() -> dict:
    df = pd.read_csv(COLUMNS_DESCRIPTION_PATH)
    column_data = {
        each['Column_Name']: {
            'description': each['Description'],
        }
        for _, each in df.iterrows()
    }
    return {'column_data': column_data}


def get_table_data() -> dict:
    df = pd.read_csv(TABLE_PATH)
    return df.to_dict(orient='records')
