from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class LinkTokenCreateRequestStatements(SdkBaseModel):
    """Specifies options for initializing Link for use with the Statements product. This field is required for the
    statements product."""

    start_date: Date
    """The start date for statements, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ "YYYY-MM-DD" format, e.g.
    "2020-10-30"."""

    end_date: Date
    """The end date for statements, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ "YYYY-MM-DD" format, e.g.
    "2020-10-30". You can request up to two years of data."""


class LinkTokenCreateRequestStatementsDict(TypedDict):
    start_date: Date
    end_date: Date
