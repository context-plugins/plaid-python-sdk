from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CheckReportWarningCode(str, Enum):
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Account-owner information is
    not available. ``TRANSACTIONS_UNAVAILABLE``: Transactions information associated with Credit and Depository accounts
    are unavailable. ``USER_FRAUD_ALERT``: The user has placed a fraud alert on their Plaid Check consumer report due to
    suspected fraud. Please note that when a fraud alert is in place, the recipient of the consumer report has an
    obligation to verify the consumer's identity."""

    IDENTITY_UNAVAILABLE = "IDENTITY_UNAVAILABLE"
    TRANSACTIONS_UNAVAILABLE = "TRANSACTIONS_UNAVAILABLE"
    USER_FRAUD_ALERT = "USER_FRAUD_ALERT"

    __str__ = str.__str__


CheckReportWarningCodeOrStr: TypeAlias = Annotated[
    CheckReportWarningCode | str, open_enum_validator(CheckReportWarningCode)
]
