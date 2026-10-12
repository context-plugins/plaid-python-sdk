from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .auth_verify_numbers_ach import AuthVerifyNumbersAch, AuthVerifyNumbersAchDict


class AuthVerifyRequestNumbers(SdkBaseModel):
    """An object containing identifying account numbers for verification via Database Auth"""

    ach: AuthVerifyNumbersAch
    """ACH numbers for verification via Database Auth"""


class AuthVerifyRequestNumbersDict(TypedDict):
    ach: AuthVerifyNumbersAchDict
