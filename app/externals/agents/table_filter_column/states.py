from __future__ import annotations

from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from typing_extensions import NotRequired
from typing_extensions import TypedDict


class TableFilterColumnState(TypedDict):
    # input
    question: str

    # internal
    schema_info: NotRequired[dict[str, object] | None]
    table: NotRequired[dict[str, object] | None]

    # flow control
    flow: NotRequired[Literal['continue', 'end'] | None]

    # output
    response: NotRequired[str | None]


class TableFilterColumnOutput(BaseModel):
    list_column_name: list[str] = Field(
        description='List of column names of data table, make sure the name is correct and have the same case as the data table',
        example=['column1', 'column2', 'column3'],
    )
