from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type4 import Type4OrStr


class WalletTransactionRelation(SdkBaseModel):
    """Transactions are related when they have a logical connection.

    For example, a ``PAYOUT`` transaction can be returned by the sender, creating a ``RETURN`` transaction. Each
    ``PAYOUT`` transaction can have at most one corresponding ``RETURN`` transaction in case of reversal.

    These relationships are bi-directional, meaning that both entities have references to each other. For instance, when
    a transaction of type RETURN occurs, it is linked to the original transaction being returned. Likewise, the original
    transaction has a reference back to the RETURN transaction that represents the return.

    This field is only populated for transactions of type ``RETURN``, ``FUNDS_SWEEP``, ``REFUND`` and ``PAYOUT``.

    The relationship between a ``PIS_PAY_IN`` payment and its corresponding ``REFUND`` transactions is only available
    through the ``refund_ids`` property in the payment object. See
    https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-get-response-refund-ids."""

    id: Optional[str] = UNSET
    """The ID of the related transaction."""

    type_: Optional[Type4OrStr] = Field(default=UNSET, alias="type")
    """The type of the transaction."""


class WalletTransactionRelationDict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[Type4OrStr]
