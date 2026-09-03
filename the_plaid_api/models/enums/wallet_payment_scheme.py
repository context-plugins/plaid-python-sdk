from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletPaymentScheme(str, Enum):
    """The payment scheme used to execute this transaction. This is present only for transaction types ``PAYOUT`` and
    ``REFUND``.

    ``FASTER_PAYMENTS``: The standard payment scheme within the UK.

    ``SEPA_CREDIT_TRANSFER``: The standard payment to a beneficiary within the SEPA area.

    ``SEPA_CREDIT_TRANSFER_INSTANT``: Instant payment to a beneficiary within the SEPA area."""

    FASTER_PAYMENTS = "FASTER_PAYMENTS"
    SEPA_CREDIT_TRANSFER = "SEPA_CREDIT_TRANSFER"
    SEPA_CREDIT_TRANSFER_INSTANT = "SEPA_CREDIT_TRANSFER_INSTANT"

    __str__ = str.__str__


WalletPaymentSchemeOrStr: TypeAlias = Annotated[WalletPaymentScheme | str, open_enum_validator(WalletPaymentScheme)]
