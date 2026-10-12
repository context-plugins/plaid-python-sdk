from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_employment_verification import CreditEmploymentVerification, CreditEmploymentVerificationDict


class CreditEmploymentItem(SdkBaseModel):
    """The object containing employment items."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    employments: list[CreditEmploymentVerification]
    employment_report_token: Optional[str] = UNSET
    """Token to represent the underlying Employment data"""


class CreditEmploymentItemDict(TypedDict):
    item_id: str
    employments: list[CreditEmploymentVerificationDict]
    employment_report_token: NotRequired[str]
