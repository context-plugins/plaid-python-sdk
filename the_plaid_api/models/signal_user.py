from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .signal_address_data import SignalAddressData, SignalAddressDataDict
from .signal_person_name import SignalPersonName, SignalPersonNameDict


class SignalUser(SdkBaseModel):
    """Details about the end user initiating the transaction (i.e., the account holder). These fields are optional, but
    strongly recommended to increase the accuracy of results when using Signal Transaction Scores. When using a
    Balance-only ruleset, if the Signal Addendum has been signed, these fields are ignored; if the Addendum has not been
    signed, using these fields will result in an error."""

    name: OptionalNullable[SignalPersonName] = UNSET
    """The user's legal name"""

    phone_number: OptionalNullable[str] = UNSET
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567"
    """

    email_address: OptionalNullable[str] = UNSET
    """The user's email address."""

    address: OptionalNullable[SignalAddressData] = UNSET
    """Data about the components comprising an address."""


class SignalUserDict(TypedDict):
    name: NotRequired[SignalPersonName | SignalPersonNameDict | None]
    phone_number: NotRequired[str | None]
    email_address: NotRequired[str | None]
    address: NotRequired[SignalAddressData | SignalAddressDataDict | None]
