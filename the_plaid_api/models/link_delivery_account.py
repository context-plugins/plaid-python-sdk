from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.link_delivery_verification_status import LinkDeliveryVerificationStatusOrStr


class LinkDeliveryAccount(SdkBaseModel):
    """Information related to account attached to the connected Item"""

    id: Optional[str] = UNSET
    """The Plaid ``account_id``"""

    name: Optional[str] = UNSET
    """The official account name"""

    mask: Optional[str] = UNSET
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts. It may also not match the mask that the bank displays to the user."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The account type. See the `Account schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a
    full list of possible values"""

    subtype: Optional[str] = UNSET
    """The account subtype. See the `Account schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a
    full list of possible values"""

    verification_status: Optional[LinkDeliveryVerificationStatusOrStr] = UNSET
    """Indicates an Item's micro-deposit-based verification or database verification status."""

    class_type: Optional[str] = UNSET
    """If micro-deposit verification is being used, indicates whether the account being verified is a ``business`` or
    ``personal`` account."""


class LinkDeliveryAccountDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    mask: NotRequired[str]
    type_: NotRequired[str]
    subtype: NotRequired[str]
    verification_status: NotRequired[LinkDeliveryVerificationStatusOrStr]
    class_type: NotRequired[str]
