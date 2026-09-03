from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletTransactionPayeeVerificationStatus(str, Enum):
    """Result of payee verification check for EUR payouts. Payee verification checks whether the payee name provided
    matches the account holder name at the destination institution.

    ``FULL_MATCH``: The payee name fully matches the account holder.

    ``PARTIAL_MATCH``: The payee name partially matches the account holder.

    ``NO_MATCH``: The payee name does not match the account holder.

    ``ERROR``: An error occurred during payee verification.

    ``CHECK_NOT_POSSIBLE``: Payee verification could not be performed.

    This field is only populated for applicable EUR payout transactions and will be ``null`` for other transaction
    types."""

    FULL_MATCH = "FULL_MATCH"
    PARTIAL_MATCH = "PARTIAL_MATCH"
    NO_MATCH = "NO_MATCH"
    ERROR = "ERROR"
    CHECK_NOT_POSSIBLE = "CHECK_NOT_POSSIBLE"

    __str__ = str.__str__


WalletTransactionPayeeVerificationStatusOrStr: TypeAlias = Annotated[
    WalletTransactionPayeeVerificationStatus | str, open_enum_validator(WalletTransactionPayeeVerificationStatus)
]
