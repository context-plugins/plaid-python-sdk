from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.signal_schedule_default_payment_method import SignalScheduleDefaultPaymentMethodOrStr


class SignalScheduleRequest(SdkBaseModel):
    """SignalScheduleRequest defines the request schema for ``/signal/schedule``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    account_id: str
    """The Plaid ``account_id`` of the account that is the funding source for the proposed transaction. The
    ``account_id`` is returned in the ``/accounts/get`` endpoint as well as the
    https://plaid.com/docs/link/ios/#link-ios-onsuccess-linkSuccess-metadata-accounts-id callback metadata.

    This will return an https://plaid.com/docs/errors/invalid-input/#invalid_account_id error if the account has been
    removed at the bank or if the ``account_id`` is no longer valid."""

    client_transaction_id: str
    """The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal
    data, you could use your internal ID/identifier for this transaction. The max length for this field is 36
    characters."""

    amount: float
    """The transaction amount, in USD (e.g. ``102.05``)"""

    default_payment_method: Optional[SignalScheduleDefaultPaymentMethodOrStr] = UNSET
    """The payment method specified in the ``default_payment_method`` field directly impacts the timing recommendations
    provided by the API for submitting the debit entry to your processor or ODFI. If unspecified, defaults to
    ``STANDARD_ACH``.

    ``SAME_DAY_ACH``: Same Day ACH (as defined by Nacha). The API assumes the settlement will occur on the same business
    day if the ``/signal/schedule`` request is submitted by 6:00 PM UTC. Note: The actual cutoff time can vary depending
    on your payment processor or ODFI. Nacha has established three processing windows for Same Day ACH (Eastern Time):
    10:30 AM, 2:45 PM, and 4:45 PM.

    ``STANDARD_ACH``: Standard ACH (as defined by Nacha), typically settled one to three business days after submission.

    ``MULTIPLE_PAYMENT_METHODS``: Indicates that there is no default debit rail or multiple payment methods are
    available, and the transaction could use any of them based on customer policy or availability."""


class SignalScheduleRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    account_id: str
    client_transaction_id: str
    amount: float
    default_payment_method: NotRequired[SignalScheduleDefaultPaymentMethodOrStr]
