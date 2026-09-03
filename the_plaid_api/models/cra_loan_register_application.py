from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class CraLoanRegisterApplication(SdkBaseModel):
    """Contains loan application data to register."""

    application_id: Optional[str] = UNSET
    """A unique identifier for the loan application. Personally identifiable information, such as an email address or
    phone number, should not be used in the ``application_id``."""

    application_date: Optional[Date] = UNSET
    """The date the user applied for the loan. The date should be in ISO 8601 format (YYYY-MM-DD)."""


class CraLoanRegisterApplicationDict(TypedDict):
    application_id: NotRequired[str]
    application_date: NotRequired[Date]
