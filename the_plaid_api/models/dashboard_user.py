from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.dashboard_user_status import DashboardUserStatusOrStr


class DashboardUser(SdkBaseModel):
    """Account information associated with a team member with access to the Plaid dashboard."""

    id: str
    """ID of the associated user. To retrieve the email address or other details of the person corresponding to this ID,
    use ``/dashboard_user/get``."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    email_address: EmailStr
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    status: DashboardUserStatusOrStr
    """The current status of the user."""


class DashboardUserDict(TypedDict):
    id: str
    created_at: RFC3339DateTime
    email_address: EmailStr
    status: DashboardUserStatusOrStr
