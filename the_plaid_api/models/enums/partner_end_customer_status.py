from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerStatus(str, Enum):
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

    UNDER_REVIEW = "UNDER_REVIEW"
    PENDING_ENABLEMENT = "PENDING_ENABLEMENT"
    ACTIVE = "ACTIVE"
    DENIED = "DENIED"
    MORE_INFORMATION_NEEDED = "MORE_INFORMATION_NEEDED"

    __str__ = str.__str__


PartnerEndCustomerStatusOrStr: TypeAlias = Annotated[
    PartnerEndCustomerStatus | str, open_enum_validator(PartnerEndCustomerStatus)
]
