from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SenderBacsnullable(SdkBaseModel):
    """An object containing a Bacs account number and sort code. If an IBAN is not provided or if this recipient needs
    to accept domestic GBP-denominated payments, Bacs data is required."""

    account: Optional[str] = UNSET
    """The account number of the account. Maximum of 10 characters."""

    sort_code: Optional[str] = UNSET
    """The 6-character sort code of the account."""


class SenderBacsnullableDict(TypedDict):
    account: NotRequired[str]
    sort_code: NotRequired[str]
