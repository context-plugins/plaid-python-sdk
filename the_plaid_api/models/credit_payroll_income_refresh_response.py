from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditPayrollIncomeRefreshResponse(SdkBaseModel):
    """CreditPayrollIncomeRefreshResponse defines the response schema for ``/credit/payroll_income/refresh``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    verification_refresh_status: str
    """The verification refresh status. One of the following:

    ``"USER_PRESENCE_REQUIRED"`` User presence is required to refresh an income verification. ``"SUCCESSFUL"`` The
    income verification refresh was successful. ``"NOT_FOUND"`` No new data was found after the income verification
    refresh."""


class CreditPayrollIncomeRefreshResponseDict(TypedDict):
    request_id: str
    verification_refresh_status: str
