from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StatementsRefreshCompleteResult(str, Enum):
    """The result of the statement refresh extraction

    ``SUCCESS``: The statements were successfully extracted and can be listed via ``/statements/list`` and downloaded
    via ``/statements/download``.

    ``FAILURE``: The statements failed to be extracted."""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    __str__ = str.__str__


StatementsRefreshCompleteResultOrStr: TypeAlias = Annotated[
    StatementsRefreshCompleteResult | str, open_enum_validator(StatementsRefreshCompleteResult)
]
