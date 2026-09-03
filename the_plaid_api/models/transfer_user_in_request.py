from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_user_address_in_request import TransferUserAddressInRequest, TransferUserAddressInRequestDict


class TransferUserInRequest(SdkBaseModel):
    """The legal name and other information for the account holder."""

    legal_name: str
    """The user's legal name."""

    phone_number: Optional[str] = UNSET
    """The user's phone number. Phone number input may be validated against valid number ranges; number strings that do
    not match a real-world phone numbering scheme may cause the request to fail, even in the Sandbox test
    environment."""

    email_address: Optional[str] = UNSET
    """The user's email address."""

    address: Optional[TransferUserAddressInRequest] = UNSET
    """The address associated with the account holder."""


class TransferUserInRequestDict(TypedDict):
    legal_name: str
    phone_number: NotRequired[str]
    email_address: NotRequired[str]
    address: NotRequired[TransferUserAddressInRequest | TransferUserAddressInRequestDict]
