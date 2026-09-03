from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel


class StatementsStatement(SdkBaseModel):
    """A statement's metadata associated with an account"""

    statement_id: str
    """Plaid's unique identifier for the statement."""

    date_posted: OptionalNullable[Date] = UNSET
    """Date when the statement was posted by the FI, if known"""

    month: int
    """Month of the year. Possible values: 1 through 12 (January through December)."""

    year: int
    """The year of the statement, e.g. 2024."""


class StatementsStatementDict(TypedDict):
    statement_id: str
    date_posted: NotRequired[Date | None]
    month: int
    year: int
