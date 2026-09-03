from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DashboardUserGetRequest(SdkBaseModel):
    """Request input for fetching a dashboard user"""

    dashboard_user_id: str
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""


class DashboardUserGetRequestDict(TypedDict):
    dashboard_user_id: str
    secret: NotRequired[str]
    client_id: NotRequired[str]
