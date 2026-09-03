from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .refresh_result import RefreshResult, RefreshResultDict


class UserFinancialDataRefreshResponse(SdkBaseModel):
    """UserFinancialDataRefreshResponse defines the response schema for ``/user/financial_data/refresh``"""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    user_id: Optional[str] = UNSET
    """The user ID associated with the refresh request."""

    results: Optional[list[RefreshResult]] = UNSET


class UserFinancialDataRefreshResponseDict(TypedDict):
    request_id: NotRequired[str]
    user_id: NotRequired[str]
    results: NotRequired[list[RefreshResult | RefreshResultDict]]
