from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .signal_evaluate_device import SignalEvaluateDevice, SignalEvaluateDeviceDict
from .signal_user import SignalUser, SignalUserDict


class SignalEvaluateRequest(SdkBaseModel):
    """SignalEvaluateRequest defines the request schema for ``/signal/evaluate``"""

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
    """The unique ID that you would like to use to refer to this evaluation attempt - for example, a payment attempt ID.
    You will use this later to debug this evaluation, and/or report an ACH return, etc. The max length for this field is
    36 characters. The ``client_transaction_id`` also functions as an idempotency key; calling ``/signal/evaluate`` with
    a previously used ``client_transaction_id`` will return the results of the previous evaluation rather than
    triggering a fresh evaluation."""

    amount: float
    """The transaction amount, in USD (e.g. ``102.05``)"""

    user_present: OptionalNullable[bool] = UNSET
    """``true`` if the end user is present while initiating the ACH transfer and the endpoint is being called; ``false``
    otherwise (for example, when the ACH transfer is scheduled and the end user is not present, or you call this
    endpoint after the ACH transfer but before submitting the Nacha file for ACH processing). When using a Balance-only
    ruleset, this field is ignored. This field is not currently used as part of Signal Transaction Score evaluations,
    but may be used in the future."""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with
    multiple Items. Personally identifiable information, such as an email address or phone number, should not be used in
    the ``client_user_id``."""

    is_recurring: OptionalNullable[bool] = UNSET
    """Use ``true`` if the ACH transaction is a part of recurring schedule (for example, a monthly repayment); ``false``
    otherwise. When using a Balance-only ruleset, this field is ignored."""

    default_payment_method: OptionalNullable[str] = UNSET
    """The default ACH payment method to complete the transaction. When using a Balance-only ruleset, this field is
    ignored. ``SAME_DAY_ACH``: Same Day ACH by Nacha. The debit transaction is processed and settled on the same day.
    ``STANDARD_ACH``: Standard ACH by Nacha. ``MULTIPLE_PAYMENT_METHODS``: If there is no default debit rail or there
    are multiple payment methods. Possible values: ``SAME_DAY_ACH``, ``STANDARD_ACH``, ``MULTIPLE_PAYMENT_METHODS``"""

    user: Optional[SignalUser] = UNSET
    """Details about the end user initiating the transaction (i.e., the account holder). These fields are optional, but
    strongly recommended to increase the accuracy of results when using Signal Transaction Scores. When using a
    Balance-only ruleset, if the Signal Addendum has been signed, these fields are ignored; if the Addendum has not been
    signed, using these fields will result in an error."""

    device: Optional[SignalEvaluateDevice] = UNSET
    """Details about the end user's device. These fields are optional, but strongly recommended to increase the accuracy
    of results when using Signal Transaction Scores. When using a Balance-only Ruleset, these fields are ignored if the
    Signal Addendum has been signed; if it has not been signed, using these fields will result in an error."""

    risk_profile_key: OptionalNullable[str] = UNSET
    """Specifying ``risk_profile_key`` is deprecated. Please provide ``ruleset`` instead."""

    ruleset_key: OptionalNullable[str] = UNSET
    """The key of the ruleset to use for evaluating this transaction. You can create a ruleset using the Plaid
    Dashboard, under https://dashboard.plaid.com/signal/risk-profiles. If not provided, for all new customers as of
    October 15, 2025, the ``default`` ruleset will be used. For existing Signal Transaction Scores customers as of
    October 15, 2025, by default, no ruleset will be used if the ``ruleset_key`` is not provided. For more information,
    or to opt out of using rulesets, see `Signal Rules <https://plaid.com/docs/signal/signal-rules/>`__."""


class SignalEvaluateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    account_id: str
    client_transaction_id: str
    amount: float
    user_present: NotRequired[bool | None]
    client_user_id: NotRequired[str]
    is_recurring: NotRequired[bool | None]
    default_payment_method: NotRequired[str | None]
    user: NotRequired[SignalUserDict]
    device: NotRequired[SignalEvaluateDeviceDict]
    risk_profile_key: NotRequired[str | None]
    ruleset_key: NotRequired[str | None]
