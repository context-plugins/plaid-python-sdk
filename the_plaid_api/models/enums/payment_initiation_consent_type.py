from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInitiationConsentType(str, Enum):
    """Payment consent type. Defines possible use case for payments made with the given consent.

    ``SWEEPING``: Allows moving money between accounts owned by the same user.

    ``COMMERCIAL``: Allows initiating payments from the user's account to third parties."""

    SWEEPING = "SWEEPING"
    COMMERCIAL = "COMMERCIAL"

    __str__ = str.__str__


PaymentInitiationConsentTypeOrStr: TypeAlias = Annotated[
    PaymentInitiationConsentType | str, open_enum_validator(PaymentInitiationConsentType)
]
