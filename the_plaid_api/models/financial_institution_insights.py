from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .detected_account import DetectedAccount, DetectedAccountDict


class FinancialInstitutionInsights(SdkBaseModel):
    """Insights surrounding external financial institution counterparties associated with a user."""

    name: str
    """Name of the financial institution counterparty."""

    entity_id: OptionalNullable[str] = UNSET
    """A unique, stable, Plaid-generated id that maps to the counterparty."""

    website: str | None
    """The website associated with the counterparty."""

    detected_accounts: list[DetectedAccount]
    """Associated accounts, detected based on the nature of transfers to/from this institution."""


class FinancialInstitutionInsightsDict(TypedDict):
    name: str
    entity_id: NotRequired[str | None]
    website: str | None
    detected_accounts: list[DetectedAccount | DetectedAccountDict]
