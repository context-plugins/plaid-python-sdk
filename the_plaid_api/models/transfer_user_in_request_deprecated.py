from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_user_address_in_request import TransferUserAddressInRequest, TransferUserAddressInRequestDict


class TransferUserInRequestDeprecated(SdkBaseModel):
    """The legal name and other information for the account holder."""

    legal_name: Optional[str] = UNSET
    """The user's legal name."""

    phone_number: Optional[str] = UNSET
    """The user's phone number."""

    email_address: Optional[str] = UNSET
    """The user's email address."""

    address: Optional[TransferUserAddressInRequest] = UNSET
    """The address associated with the account holder."""


class TransferUserInRequestDeprecatedDict(TypedDict):
    legal_name: NotRequired[str]
    phone_number: NotRequired[str]
    email_address: NotRequired[str]
    address: NotRequired[TransferUserAddressInRequestDict]
