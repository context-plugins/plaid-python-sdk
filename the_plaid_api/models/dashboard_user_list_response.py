from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .dashboard_user import DashboardUser, DashboardUserDict


class DashboardUserListResponse(SdkBaseModel):
    """Paginated list of dashboard users"""

    dashboard_users: list[DashboardUser]
    """List of dashboard users"""

    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class DashboardUserListResponseDict(TypedDict):
    dashboard_users: list[DashboardUser | DashboardUserDict]
    next_cursor: str | None
    request_id: str
