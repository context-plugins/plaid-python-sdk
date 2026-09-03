from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_status import PartnerEndCustomerStatusOrStr


class PartnerEndCustomer(SdkBaseModel):
    """The details for an end customer."""

    client_id: Optional[str] = UNSET
    """The ``client_id`` of the end customer."""

    company_name: Optional[str] = UNSET
    """The company name associated with the end customer."""

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


class PartnerEndCustomerDict(TypedDict):
    client_id: NotRequired[str]
    company_name: NotRequired[str]
    status: NotRequired[PartnerEndCustomerStatusOrStr]
