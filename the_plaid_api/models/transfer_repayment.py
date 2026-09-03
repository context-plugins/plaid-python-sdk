from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class TransferRepayment(SdkBaseModel):
    """A repayment is created automatically after one or more guaranteed transactions receive a return. If there are
    multiple eligible returns in a day, they are batched together into a single repayment.

    Repayments are sent over ACH, with funds typically available on the next banking day."""

    repayment_id: str
    """Identifier of the repayment."""

    created: RFC3339DateTime
    """The datetime when the repayment occurred, in RFC 3339 format."""

    amount: str
    """Decimal amount of the repayment as it appears on your account ledger."""

    iso_currency_code: str
    """The currency of the repayment, e.g. "USD"."""


class TransferRepaymentDict(TypedDict):
    repayment_id: str
    created: RFC3339DateTime
    amount: str
    iso_currency_code: str
