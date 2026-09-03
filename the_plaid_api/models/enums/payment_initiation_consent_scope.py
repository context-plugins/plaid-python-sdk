from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInitiationConsentScope(str, Enum):
    """This field is deprecated in favor of the consent ``type`` field. Consents are required to have a single type.

    Payment consent scope. Defines possible directions for payments made with the given consent.

    ``ME_TO_ME``: Allows moving money between accounts owned by the same user.

    ``EXTERNAL``: Allows initiating payments from the user's account to third parties."""

    ME_TO_ME = "ME_TO_ME"
    EXTERNAL = "EXTERNAL"

    __str__ = str.__str__


PaymentInitiationConsentScopeOrStr: TypeAlias = Annotated[
    PaymentInitiationConsentScope | str, open_enum_validator(PaymentInitiationConsentScope)
]
