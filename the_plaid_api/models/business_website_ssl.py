from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.business_check_boolean_status import BusinessCheckBooleanStatusOrStr


class BusinessWebsiteSsl(SdkBaseModel):
    """SSL status for the business website."""

    is_valid: BusinessCheckBooleanStatusOrStr
    """Tri-state boolean status, where ``no_data`` indicates the check could not determine a value."""


class BusinessWebsiteSslDict(TypedDict):
    is_valid: BusinessCheckBooleanStatusOrStr
