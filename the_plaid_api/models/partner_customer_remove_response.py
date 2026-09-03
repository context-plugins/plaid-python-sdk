from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PartnerCustomerRemoveResponse(SdkBaseModel):
    """Response schema for ``/partner/customer/remove``."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PartnerCustomerRemoveResponseDict(TypedDict):
    request_id: NotRequired[str]
