from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_status import PartnerEndCustomerStatusOrStr


class BetaPartnerCustomerV1EnableResponse(SdkBaseModel):
    """Response schema for ``/beta/partner/customer/v1/enable``."""

    end_customer_client_id: Optional[str] = UNSET
    status: Optional[PartnerEndCustomerStatusOrStr] = UNSET
    """The status of the given end customer.

    ``UNDER_REVIEW``: The end customer has been created and enabled in the Sandbox environment. The end customer must be
    manually reviewed by the Plaid team before it can be enabled in Production, at which point its status will
    automatically transition to ``PENDING_ENABLEMENT`` or ``DENIED``.

    ``PENDING_ENABLEMENT``: The end customer is ready to be fully enabled in the Production environment. Call the
    ``/partner/customer/enable`` endpoint to enable the end customer in full Production.

    ``ACTIVE``: The end customer has been fully enabled in all environments.

    ``DENIED``: The end customer has been created and enabled in the Sandbox environment, but it did not pass review by
    the Plaid team and therefore cannot be enabled for Production access. Talk to your account manager for more
    information."""

    product_statuses: Optional[Any] = UNSET
    """Mapping of product names to their current status."""

    production_secret: Optional[str] = UNSET
    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BetaPartnerCustomerV1EnableResponseDict(TypedDict):
    end_customer_client_id: NotRequired[str]
    status: NotRequired[PartnerEndCustomerStatusOrStr]
    product_statuses: NotRequired[Any]
    production_secret: NotRequired[str]
    request_id: NotRequired[str]
