from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer import PartnerEndCustomer, PartnerEndCustomerDict


class PartnerCustomerGetResponse(SdkBaseModel):
    """Response schema for ``/partner/customer/get``."""

    end_customer: Optional[PartnerEndCustomer] = UNSET
    """The details for an end customer."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PartnerCustomerGetResponseDict(TypedDict):
    end_customer: NotRequired[PartnerEndCustomer | PartnerEndCustomerDict]
    request_id: NotRequired[str]
