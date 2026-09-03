from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CashflowReportRefreshResponse(SdkBaseModel):
    """CashflowReportRefreshResponse defines the response schema for ``/cashflow_report/refresh``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CashflowReportRefreshResponseDict(TypedDict):
    request_id: str
