from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class PartnerEndCustomerBankAddendumAcceptance(SdkBaseModel):
    """The bank addendum acceptance for the end customer."""

    customer_accepted: Optional[bool] = UNSET
    """Denotes whether the end customer has accepted the bank addendum terms."""

    customer_ip_address: Optional[str] = UNSET
    """The IP address of the end customer when they accepted the bank addendum."""

    customer_agreement_timestamp: Optional[RFC3339DateTime] = UNSET
    """The timestamp of when the end customer accepted the bank addendum in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``)."""


class PartnerEndCustomerBankAddendumAcceptanceDict(TypedDict):
    customer_accepted: NotRequired[bool]
    customer_ip_address: NotRequired[str]
    customer_agreement_timestamp: NotRequired[RFC3339DateTime]
