from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict


class TableGetDetailState(TypedDict):
    # input
    question: str

    # internal
    schema_info: NotRequired[dict[str, object] | None]
    table: NotRequired[dict[str, object] | None]

    # flow control
    flow: NotRequired[Literal['continue', 'end'] | None]

    # output
    response: NotRequired[str | None]
