from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HostedLinkDeliveryMethod(str, Enum):
    """How Plaid should deliver the Plaid Link session to the customer. Only available to customers enabled for Link
    Delivery (beta). To request Link Delivery access, contact your account manager. 'sms' will deliver via SMS. Must
    pass ``user.phone_number``. 'email' will deliver via email. Must pass ``user.email_address``. In the Sandbox
    environment, this field will be ignored; use the Production environment to test Link Delivery instead."""

    SMS = "sms"
    EMAIL = "email"

    __str__ = str.__str__


HostedLinkDeliveryMethodOrStr: TypeAlias = Annotated[
    HostedLinkDeliveryMethod | str, open_enum_validator(HostedLinkDeliveryMethod)
]
