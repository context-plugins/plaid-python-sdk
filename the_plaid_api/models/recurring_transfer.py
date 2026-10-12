from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_recurring_network import TransferRecurringNetworkOrStr
from .enums.transfer_recurring_status import TransferRecurringStatusOrStr
from .enums.transfer_type import TransferTypeOrStr
from .transfer_recurring_schedule import TransferRecurringSchedule, TransferRecurringScheduleDict
from .transfer_user_in_response import TransferUserInResponse, TransferUserInResponseDict


class RecurringTransfer(SdkBaseModel):
    """Represents a recurring transfer within the Transfers API."""

    recurring_transfer_id: str
    """Plaid's unique identifier for a recurring transfer."""

    created: RFC3339DateTime
    """The datetime when this transfer was created. This will be of the form ``2006-01-02T15:04:05Z``"""

    next_origination_date: Date | None
    """A date in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD).

    The next transfer origination date after bank holiday adjustment."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock."""

    type_: TransferTypeOrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

    status: TransferRecurringStatusOrStr
    """The status of the recurring transfer.

    ``active``: The recurring transfer is currently active. ``cancelled``: The recurring transfer was cancelled by the
    client or Plaid. ``expired``: The recurring transfer has completed all originations according to its recurring
    schedule."""

    ach_class: Optional[AchclassOrStr] = UNSET
    """Specifies the use case of the transfer. Required for transfers on an ACH network. For more details, see `ACH SEC
    codes <https://plaid.com/docs/transfer/creating-transfers/#ach-sec-codes>`__.

    Codes supported for credits: ``ccd``, ``ppd`` Codes supported for debits: ``ccd``, ``ppd``, ``tel``, ``web``

    ``"ccd"`` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    ``"ppd"`` - Prearranged Payment or Deposit - The transfer is part of a pre-existing relationship with a consumer.
    Authorization was obtained in writing either in person or via an electronic document signing, e.g. Docusign, by the
    consumer. Can be used for credits or debits.

    ``"web"`` - Internet-Initiated Entry. The transfer debits a consumer's bank account. Authorization from the consumer
    is obtained over the Internet (e.g. a web or mobile application). Can be used for single debits or recurring debits.

    ``"tel"`` - Telephone-Initiated Entry. The transfer debits a consumer. Debit authorization has been received orally
    over the telephone via a recorded call."""

    network: TransferRecurringNetworkOrStr
    """Networks eligible for recurring transfers."""

    origination_account_id: str
    """Plaid's unique identifier for the origination account that was used for this transfer."""

    account_id: str
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    funding_account_id: str
    """The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business
    checking accounts will be credited or debited."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD"
    """

    description: str
    """The description of the recurring transfer."""

    transfer_ids: list[str]
    """The created transfer instances associated with this ``recurring_transfer_id``. If the recurring transfer has been
    newly created, this array will be empty."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    schedule: TransferRecurringSchedule
    """The schedule that the recurring transfer will be executed on."""


class RecurringTransferDict(TypedDict):
    recurring_transfer_id: str
    created: RFC3339DateTime
    next_origination_date: Date | None
    test_clock_id: NotRequired[str | None]
    type_: TransferTypeOrStr
    amount: str
    status: TransferRecurringStatusOrStr
    ach_class: NotRequired[AchclassOrStr]
    network: TransferRecurringNetworkOrStr
    origination_account_id: str
    account_id: str
    funding_account_id: str
    iso_currency_code: str
    description: str
    transfer_ids: list[str]
    user: TransferUserInResponseDict
    schedule: TransferRecurringScheduleDict
