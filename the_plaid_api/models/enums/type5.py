from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type5(str, Enum):
    """The type of the transaction. The supported transaction types that are returned are: ``BANK_TRANSFER:`` a
    transaction which credits an e-wallet through an external bank transfer.

    ``PAYOUT:`` a transaction which debits an e-wallet by disbursing funds to a counterparty.

    ``PIS_PAY_IN:`` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more
    information see the `Payment Initiation endpoints <https://plaid.com/docs/api/products/payment-initiation/>`__.

    ``REFUND:`` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's
    `PIS APIs <https://plaid.com/docs/api/products/payment-initiation/>`__.

    ``FUNDS_SWEEP``: an automated transaction which debits funds from an e-wallet to a designated client-owned account.

    ``RETURN``: an automated transaction where a debit transaction was reversed and money moved back to originating
    account.

    ``RECALL``: a transaction where the sending bank has requested the return of funds due to a fraud claim, technical
    error, or other issue associated with the payment.

    ``ACCOUNT_FUNDING``: an incoming transfer from an allowlisted account. Not automatically refunded.

    ``AUTO_REFUND``: an outgoing refund automatically initiated by Plaid in response to an unexpected
    ``BANK_TRANSFER``."""

    BANK_TRANSFER = "BANK_TRANSFER"
    PAYOUT = "PAYOUT"
    PIS_PAY_IN = "PIS_PAY_IN"
    REFUND = "REFUND"
    FUNDS_SWEEP = "FUNDS_SWEEP"
    RETURN = "RETURN"
    RECALL = "RECALL"
    ACCOUNT_FUNDING = "ACCOUNT_FUNDING"
    AUTO_REFUND = "AUTO_REFUND"

    __str__ = str.__str__


Type5OrStr: TypeAlias = Annotated[Type5 | str, open_enum_validator(Type5)]
