from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.products_terminate_reason_code import ProductsTerminateReasonCodeOrStr


class ItemProductsTerminateRequest(SdkBaseModel):
    """ItemProductsTerminateRequest defines the request schema for ``/item/products/terminate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    reason_code: ProductsTerminateReasonCodeOrStr
    """The reason for terminating products.

    ``FRAUD_FIRST_PARTY``: The end user who owns the connected bank account committed fraud using their real identity
    ``FRAUD_FALSE_IDENTITY``: The connection was created using a false or stolen identity ``FRAUD_ABUSE``: The end user
    is abusing the client's service or platform (for example, automation or excessive retries) through their connected
    account ``FRAUD_OTHER``: Fraud-related, but not covered by the specific fraud categories above; ``reason_note``
    should clarify ``FRAUD_TRANSACTION``: Fraud occurred at the transaction level, such as an unauthorized transaction,
    card testing, chargeback, ACH return, or dispute ``CONSUMER_LOAN_PAID_OFF``: The end user paid off their loan and no
    longer needs the product ``CONSUMER_ACCOUNT_CLOSED``: The end user closed their account with the client and no
    longer needs the product ``CONSUMER_CHARGE_OFF``: The end user's account has been charged off
    ``CONSUMER_PAYMENT_METHOD_SWITCHED``: The end user switched to a different payment method and no longer needs the
    product ``USER_OFFBOARDING``: The user is offboarding from the client's service or platform ``DUPLICATE_ITEM``: This
    Item is a duplicate of another active Item for the same user ``BILLING_TERMINATION``: The client's billing or
    subscription relationship with the end user has ended ``OTHER``: None of the above; ``reason_note`` should
    clarify"""

    reason_note: OptionalNullable[str] = UNSET
    """Additional context or details about the reason for terminating products on the Item. Personally identifiable
    information, such as an email address or phone number, should not be included in the ``reason_note``."""


class ItemProductsTerminateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    reason_code: ProductsTerminateReasonCodeOrStr
    reason_note: NotRequired[str | None]
