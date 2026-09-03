from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.transfer_achnetwork import TransferAchnetworkOrStr


class TransferLedgerDepositRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/ledger/deposit``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: OptionalNullable[str] = UNSET
    """Client ID of the customer that owns the Ledger balance. This is so Plaid knows which of your customers to pay out
    to or collect funds from. Only applicable for `Platform customers
    <https://plaid.com/docs/transfer/application/#originators-vs-platforms>`__. Do not include if you're paying out to
    yourself."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Specify which funding account to use. Customers can find a list of ``funding_account_id``s in the Accounts page
    of the Plaid Dashboard, under the "Account ID" column. If this field is left blank, the funding account associated
    with the specified Ledger will be used. If an ``originator_client_id`` is specified, the ``funding_account_id`` must
    belong to the specified originator."""

    ledger_id: OptionalNullable[str] = UNSET
    """Specify which ledger balance to deposit to. Customers can find a list of ``ledger_id``s in the Accounts page of
    your Plaid Dashboard. If this field is left blank, this will default to the id of the default ledger balance."""

    amount: str
    """A positive amount of how much will be deposited into ledger (decimal string with two digits of precision e.g.
    "5.50")."""

    description: OptionalNullable[str] = UNSET
    """The description of the deposit that will be passed to the receiving bank (up to 10 characters). Note that banks
    utilize this field differently, and may or may not show it on the bank statement."""

    idempotency_key: str
    """A unique key provided by the client, per unique ledger deposit. Maximum of 50 characters.

    The API supports idempotency for safely retrying the request without accidentally performing the same operation
    twice. For example, if a request to create a ledger deposit fails due to a network connection error, you can retry
    the request with the same idempotency key to guarantee that only a single deposit is created."""

    network: TransferAchnetworkOrStr
    """The ACH networks used for the funds flow.

    For requests submitted as either ``ach`` or ``same-day-ach`` the cutoff for Same Day ACH is 3:00 PM Eastern Time and
    the cutoff for Standard ACH transfers is 8:30 PM Eastern Time. It is recommended to submit a request at least 15
    minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any request that is
    indicated as ``same-day-ach`` and that misses the Same Day ACH cutoff, but is submitted in time for the Standard ACH
    cutoff, will be sent over Standard ACH rails and will not incur same-day charges."""


class TransferLedgerDepositRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: NotRequired[str | None]
    funding_account_id: NotRequired[str | None]
    ledger_id: NotRequired[str | None]
    amount: str
    description: NotRequired[str | None]
    idempotency_key: str
    network: TransferAchnetworkOrStr
