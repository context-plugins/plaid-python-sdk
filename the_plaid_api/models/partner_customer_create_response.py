from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_with_secrets import PartnerEndCustomerWithSecrets, PartnerEndCustomerWithSecretsDict


class PartnerCustomerCreateResponse(SdkBaseModel):
    """Response schema for ``/partner/customer/create``."""

    end_customer: Optional[PartnerEndCustomerWithSecrets] = UNSET
    """The details for the newly created end customer, including secrets for non-Production environments."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PartnerCustomerCreateResponseDict(TypedDict):
    end_customer: NotRequired[PartnerEndCustomerWithSecretsDict]
    request_id: NotRequired[str]
