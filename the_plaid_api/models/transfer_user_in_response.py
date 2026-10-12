from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_user_address_in_response import TransferUserAddressInResponse, TransferUserAddressInResponseDict


class TransferUserInResponse(SdkBaseModel):
    """The legal name and other information for the account holder."""

    legal_name: str
    """The user's legal name."""

    phone_number: str | None
    """The user's phone number."""

    email_address: str | None
    """The user's email address."""

    address: TransferUserAddressInResponse | None
    """The address associated with the account holder."""


class TransferUserInResponseDict(TypedDict):
    legal_name: str
    phone_number: str | None
    email_address: str | None
    address: TransferUserAddressInResponseDict | None
