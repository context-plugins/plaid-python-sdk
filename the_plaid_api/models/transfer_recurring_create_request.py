from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_recurring_network import TransferRecurringNetworkOrStr
from .enums.transfer_type import TransferTypeOrStr
from .transfer_device import TransferDevice, TransferDeviceDict
from .transfer_recurring_schedule import TransferRecurringSchedule, TransferRecurringScheduleDict
from .transfer_user_in_request import TransferUserInRequest, TransferUserInRequestDict


class TransferRecurringCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/recurring/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    idempotency_key: str
    """A random key provided by the client, per unique recurring transfer. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    For example, if a request to create a recurring transfer fails due to a network connection error, you can retry the
    request with the same idempotency key to guarantee that only a single recurring transfer is created."""

    account_id: str
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Specify the account used to fund the transfer. Customers can find a list of ``funding_account_id``s in the
    Accounts page of your Plaid Dashboard, under the "Account ID" column. If this field is left blank, it will default
    to the default ``funding_account_id`` specified during onboarding."""

    type_: TransferTypeOrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    network: TransferRecurringNetworkOrStr
    """Networks eligible for recurring transfers."""

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

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

    user_present: OptionalNullable[bool] = UNSET
    """If the end user is initiating the specific transfer themselves via an interactive UI, this should be ``true``;
    for automatic recurring payments where the end user is not actually initiating each individual transfer, it should
    be ``false``."""

    iso_currency_code: Optional[str] = UNSET
    """The currency of the transfer amount. The default value is "USD"."""

    description: str
    """The description of the recurring transfer."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. This field may only be used when using the ``sandbox`` environment.
    If provided, the created ``recurring_transfer`` is associated with the ``test_clock``. New originations are
    automatically generated when the associated ``test_clock`` advances. For more details, see `Simulating recurring
    transfers <https://plaid.com/docs/transfer/sandbox/#simulating-recurring-transfers>`__."""

    schedule: TransferRecurringSchedule
    """The schedule that the recurring transfer will be executed on."""

    user: TransferUserInRequest
    """The legal name and other information for the account holder."""

    device: Optional[TransferDevice] = UNSET
    """Information about the device being used to initiate the authorization."""


class TransferRecurringCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    idempotency_key: str
    account_id: str
    funding_account_id: NotRequired[str | None]
    type_: TransferTypeOrStr
    network: TransferRecurringNetworkOrStr
    ach_class: NotRequired[AchclassOrStr]
    amount: str
    user_present: NotRequired[bool | None]
    iso_currency_code: NotRequired[str]
    description: str
    test_clock_id: NotRequired[str | None]
    schedule: TransferRecurringSchedule | TransferRecurringScheduleDict
    user: TransferUserInRequest | TransferUserInRequestDict
    device: NotRequired[TransferDevice | TransferDeviceDict]
