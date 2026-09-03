from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletTransactionFailureReason(str, Enum):
    """The error code of a failed transaction. Error codes include: ``EXTERNAL_SYSTEM``: The transaction was declined by
    an external system. ``EXPIRED``: The transaction request has expired. ``CANCELLED``: The transaction request was
    rescinded. ``INVALID``: The transaction did not meet certain criteria, such as an inactive account or no valid
    counterparty, etc. ``ACCOUNT_INVALID``: The transaction could not be processed because the wallet account is invalid
    or inactive. ``AUTHENTICATION_FAILED``: The transaction could not be processed because authentication with the
    wallet provider failed. ``UNKNOWN``: The transaction was unsuccessful, but the exact cause is unknown."""

    EXTERNAL_SYSTEM = "EXTERNAL_SYSTEM"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"
    INVALID = "INVALID"
    ACCOUNT_INVALID = "ACCOUNT_INVALID"
    AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


WalletTransactionFailureReasonOrStr: TypeAlias = Annotated[
    WalletTransactionFailureReason | str, open_enum_validator(WalletTransactionFailureReason)
]
