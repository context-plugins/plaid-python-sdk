from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .business_account import BusinessAccount, BusinessAccountDict
from .cashflow_account_insights import CashflowAccountInsights, CashflowAccountInsightsDict
from .item import Item, ItemDict


class CashflowReportInsightsGetResponse(SdkBaseModel):
    """CashflowReportInsightsGetResponse defines the response schema for ``/cashflow_report/insights/get``"""

    item: Item
    """Metadata about the Item."""

    accounts: list[BusinessAccount]
    """An array containing the ``accounts`` associated with the Item for which transactions are being returned. Each
    transaction can be mapped to its corresponding account via the ``account_id`` field."""

    account_insights: CashflowAccountInsights
    """Insights on the account level. These are only returned for Credit and Depository type accounts."""

    last_generated_time: RFC3339DateTime
    """Datetime of last Cashflow Report generation in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` )"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CashflowReportInsightsGetResponseDict(TypedDict):
    item: Item | ItemDict
    accounts: list[BusinessAccount | BusinessAccountDict]
    account_insights: CashflowAccountInsights | CashflowAccountInsightsDict
    last_generated_time: RFC3339DateTime
    request_id: str
