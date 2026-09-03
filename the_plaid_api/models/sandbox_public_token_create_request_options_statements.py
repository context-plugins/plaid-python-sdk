from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class SandboxPublicTokenCreateRequestOptionsStatements(SdkBaseModel):
    """An optional set of parameters corresponding to statements options."""

    start_date: Date
    """The earliest date for which to fetch statements history. Dates should be formatted as YYYY-MM-DD."""

    end_date: Date
    """The most recent date for which to fetch statements history. Dates should be formatted as YYYY-MM-DD."""


class SandboxPublicTokenCreateRequestOptionsStatementsDict(TypedDict):
    start_date: Date
    end_date: Date
