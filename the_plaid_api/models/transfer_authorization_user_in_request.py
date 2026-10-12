from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_user_address_in_request import TransferUserAddressInRequest, TransferUserAddressInRequestDict


class TransferAuthorizationUserInRequest(SdkBaseModel):
    """The legal name and other information for the account holder. If the account has multiple account holders, provide
    the information for the account holder on whose behalf the authorization is being requested. The ``user.legal_name``
    field is required. Other fields are not currently used and are present to support planned future functionality."""

    legal_name: str
    """The user's legal name. If the user is a business, provide the business name."""

    phone_number: Optional[str] = UNSET
    """The user's phone number."""

    email_address: Optional[str] = UNSET
    """The user's email address."""

    address: Optional[TransferUserAddressInRequest] = UNSET
    """The address associated with the account holder."""


class TransferAuthorizationUserInRequestDict(TypedDict):
    legal_name: str
    phone_number: NotRequired[str]
    email_address: NotRequired[str]
    address: NotRequired[TransferUserAddressInRequestDict]
