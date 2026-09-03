from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.risk_check_linked_service import RiskCheckLinkedServiceOrStr
from .enums.risk_level import RiskLevelOrStr


class RiskCheckPhone(SdkBaseModel):
    """Result summary object specifying values for ``phone`` attributes of risk check."""

    linked_services: list[RiskCheckLinkedServiceOrStr]
    """A list of online services where this phone number has been detected to have accounts or other activity."""

    risk_level: Optional[RiskLevelOrStr] = UNSET
    """Risk level for the given risk check type."""

    factors: Optional[list[str]] = UNSET
    """List of factors, when available, that contribute towards the risk level of the given risk check type."""


class RiskCheckPhoneDict(TypedDict):
    linked_services: list[RiskCheckLinkedServiceOrStr]
    risk_level: NotRequired[RiskLevelOrStr]
    factors: NotRequired[list[str]]
