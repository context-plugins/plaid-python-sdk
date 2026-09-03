from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .beta_partner_end_customer import BetaPartnerEndCustomer, BetaPartnerEndCustomerDict


class BetaPartnerCustomerV1GetResponse(SdkBaseModel):
    """Response schema for ``/beta/partner/customer/v1/get``."""

    end_customer: Optional[BetaPartnerEndCustomer] = UNSET
    """The details for an end customer."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BetaPartnerCustomerV1GetResponseDict(TypedDict):
    end_customer: NotRequired[BetaPartnerEndCustomer | BetaPartnerEndCustomerDict]
    request_id: NotRequired[str]
