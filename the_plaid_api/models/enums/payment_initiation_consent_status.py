from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentInitiationConsentStatus(str, Enum):
    """The status of the payment consent.

    ``UNAUTHORISED``: Consent created, but requires user authorisation.

    ``REJECTED``: Consent authorisation was rejected by the bank.

    ``AUTHORISED``: Consent is active and ready to be used.

    ``REVOKED``: Consent has been revoked and can no longer be used.

    ``EXPIRED``: Consent is no longer valid."""

    UNAUTHORISED = "UNAUTHORISED"
    AUTHORISED = "AUTHORISED"
    REVOKED = "REVOKED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"

    __str__ = str.__str__


PaymentInitiationConsentStatusOrStr: TypeAlias = Annotated[
    PaymentInitiationConsentStatus | str, open_enum_validator(PaymentInitiationConsentStatus)
]
