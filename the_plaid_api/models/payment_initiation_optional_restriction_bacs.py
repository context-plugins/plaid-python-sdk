from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentInitiationOptionalRestrictionBacs(SdkBaseModel):
    """An optional object used to restrict the accounts used for payments. If provided, the end user will be able to
    send payments only from the specified bank account."""

    account: Optional[str] = UNSET
    """The account number of the account. Maximum of 10 characters."""

    sort_code: Optional[str] = UNSET
    """The 6-character sort code of the account."""


class PaymentInitiationOptionalRestrictionBacsDict(TypedDict):
    account: NotRequired[str]
    sort_code: NotRequired[str]
