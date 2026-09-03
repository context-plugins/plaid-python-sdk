from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthVerifyNumbersAch(SdkBaseModel):
    """ACH numbers for verification via Database Auth"""

    account: str
    """Account's account number"""

    routing: str
    """Account's routing number"""


class AuthVerifyNumbersAchDict(TypedDict):
    account: str
    routing: str
