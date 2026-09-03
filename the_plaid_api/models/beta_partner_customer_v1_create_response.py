from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .beta_partner_end_customer_with_secrets import (
    BetaPartnerEndCustomerWithSecrets,
    BetaPartnerEndCustomerWithSecretsDict,
)


class BetaPartnerCustomerV1CreateResponse(SdkBaseModel):
    """Response schema for ``/beta/partner/customer/v1/create``."""

    end_customer: Optional[BetaPartnerEndCustomerWithSecrets] = UNSET
    """The details for the newly created end customer, including secrets for non-Production environments."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BetaPartnerCustomerV1CreateResponseDict(TypedDict):
    end_customer: NotRequired[BetaPartnerEndCustomerWithSecrets | BetaPartnerEndCustomerWithSecretsDict]
    request_id: NotRequired[str]
