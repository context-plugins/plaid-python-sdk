from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentScheme(str, Enum):
    """Payment scheme. If not specified - the default in the region will be used (e.g. ``SEPA_CREDIT_TRANSFER`` for EU).
    In responses, if the scheme is not explicitly specified in the request, this value will be ``null``. Using
    unsupported values will result in a failed payment.

    ``LOCAL_DEFAULT``: The default payment scheme for the selected market and currency will be used.

    ``LOCAL_INSTANT``: The instant payment scheme for the selected market and currency will be used (if applicable).
    Fees may be applied by the institution.

    ``SEPA_CREDIT_TRANSFER``: The standard payment to a beneficiary within the SEPA area.

    ``SEPA_CREDIT_TRANSFER_INSTANT``: Instant payment within the SEPA area. May involve additional fees and may not be
    available at some banks."""

    LOCAL_DEFAULT = "LOCAL_DEFAULT"
    LOCAL_INSTANT = "LOCAL_INSTANT"
    SEPA_CREDIT_TRANSFER = "SEPA_CREDIT_TRANSFER"
    SEPA_CREDIT_TRANSFER_INSTANT = "SEPA_CREDIT_TRANSFER_INSTANT"

    __str__ = str.__str__


PaymentSchemeOrStr: TypeAlias = Annotated[PaymentScheme | str, open_enum_validator(PaymentScheme)]
