from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .transfer_platform_person_address import TransferPlatformPersonAddress, TransferPlatformPersonAddressDict
from .transfer_platform_person_idnumber import TransferPlatformPersonIdnumber, TransferPlatformPersonIdnumberDict
from .transfer_platform_person_name import TransferPlatformPersonName, TransferPlatformPersonNameDict


class TransferPlatformPersonCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/platform/person/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: str
    """The client ID of the originator"""

    name: Optional[TransferPlatformPersonName] = UNSET
    """The person's legal name"""

    email_address: Optional[str] = UNSET
    """A valid email address. Must not have leading or trailing spaces."""

    phone_number: Optional[str] = UNSET
    """A valid phone number in E.164 format. Phone number input may be validated against valid number ranges; number
    strings that do not match a real-world phone numbering scheme may cause the request to fail, even in the Sandbox
    test environment."""

    address: Optional[TransferPlatformPersonAddress] = UNSET
    """Home address of a person"""

    id_number: Optional[TransferPlatformPersonIdnumber] = UNSET
    """ID number of the person"""

    date_of_birth: Optional[Date] = UNSET
    """The date of birth of the person. Formatted as YYYY-MM-DD."""

    relationship_to_originator: Optional[str] = UNSET
    """The relationship between this person and the originator they are related to."""

    ownership_percentage: Optional[int] = UNSET
    """The percentage of ownership this person has in the onboarding business. Only applicable to beneficial owners with
    25% or more ownership."""

    title: Optional[str] = UNSET
    """The title of the person at the business. Only applicable to control persons - for example, "CEO", "President",
    "Owner", etc."""


class TransferPlatformPersonCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: str
    name: NotRequired[TransferPlatformPersonNameDict]
    email_address: NotRequired[str]
    phone_number: NotRequired[str]
    address: NotRequired[TransferPlatformPersonAddressDict]
    id_number: NotRequired[TransferPlatformPersonIdnumberDict]
    date_of_birth: NotRequired[Date]
    relationship_to_originator: NotRequired[str]
    ownership_percentage: NotRequired[int]
    title: NotRequired[str]
