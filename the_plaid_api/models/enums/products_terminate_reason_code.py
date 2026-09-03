from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductsTerminateReasonCode(str, Enum):
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

    FRAUD_FIRST_PARTY = "FRAUD_FIRST_PARTY"
    FRAUD_FALSE_IDENTITY = "FRAUD_FALSE_IDENTITY"
    FRAUD_ABUSE = "FRAUD_ABUSE"
    FRAUD_OTHER = "FRAUD_OTHER"
    FRAUD_TRANSACTION = "FRAUD_TRANSACTION"
    CONSUMER_LOAN_PAID_OFF = "CONSUMER_LOAN_PAID_OFF"
    CONSUMER_ACCOUNT_CLOSED = "CONSUMER_ACCOUNT_CLOSED"
    CONSUMER_CHARGE_OFF = "CONSUMER_CHARGE_OFF"
    CONSUMER_PAYMENT_METHOD_SWITCHED = "CONSUMER_PAYMENT_METHOD_SWITCHED"
    USER_OFFBOARDING = "USER_OFFBOARDING"
    DUPLICATE_ITEM = "DUPLICATE_ITEM"
    BILLING_TERMINATION = "BILLING_TERMINATION"
    OTHER = "OTHER"

    __str__ = str.__str__


ProductsTerminateReasonCodeOrStr: TypeAlias = Annotated[
    ProductsTerminateReasonCode | str, open_enum_validator(ProductsTerminateReasonCode)
]
