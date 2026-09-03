from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerCustomerEnableResponse(SdkBaseModel):
    """Response schema for ``/partner/customer/enable``."""

    production_secret: Optional[str] = UNSET
    """The end customer's secret key for the Production environment."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PartnerCustomerEnableResponseDict(TypedDict):
    production_secret: NotRequired[str]
    request_id: NotRequired[str]
