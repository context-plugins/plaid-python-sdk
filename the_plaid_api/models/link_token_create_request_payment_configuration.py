from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateRequestPaymentConfiguration(SdkBaseModel):
    """Specifies options for initializing Link for use with the Pay By Bank flow. This is an optional field to configure
    the user experience, and currently requires the amount field to be set."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00")."""

    description: Optional[str] = UNSET
    """The description of the transfer that provides the payment context. The max length is 256."""


class LinkTokenCreateRequestPaymentConfigurationDict(TypedDict):
    amount: str
    description: NotRequired[str]
