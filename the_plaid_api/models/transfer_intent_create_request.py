from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_intent_create_mode import TransferIntentCreateModeOrStr
from .enums.transfer_intent_create_network import TransferIntentCreateNetworkOrStr
from .transfer_user_in_request import TransferUserInRequest, TransferUserInRequestDict


class TransferIntentCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/intent/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    account_id: OptionalNullable[str] = UNSET
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Specify the account used to fund the transfer. Should be specified if using legacy funding methods only. If using
    Plaid Ledger, leave this field blank. Customers can find a list of ``funding_account_id``s in the Accounts page of
    your Plaid Dashboard, under the "Account ID" column. If this field is left blank and you are using legacy funding
    methods, this will default to the default ``funding_account_id`` specified during onboarding. Otherwise, Plaid
    Ledger will be used."""

    mode: TransferIntentCreateModeOrStr
    """The direction of the flow of transfer funds.

    ``PAYMENT``: Transfers funds from an end user's account to your business account.

    ``DISBURSEMENT``: Transfers funds from your business account to an end user's account."""

    network: Optional[TransferIntentCreateNetworkOrStr] = UNSET
    """The network or rails used for the transfer. Defaults to ``same-day-ach``.

    For transfers submitted using ``ach``, the Standard ACH cutoff is 8:30 PM Eastern Time.

    For transfers submitted using ``same-day-ach``, the Same Day ACH cutoff is 3:00 PM Eastern Time. It is recommended
    to send the request 15 minutes prior to the cutoff to ensure that it will be processed in time for submission before
    the cutoff. If the transfer is processed after this cutoff but before the Standard ACH cutoff, it will be sent over
    Standard ACH rails and will not incur same-day charges.

    For transfers submitted using ``rtp``, in the case that the account being credited does not support RTP, the
    transfer will be sent over ACH as long as an ``ach_class`` is provided in the request. If RTP isn't supported by the
    account and no ``ach_class`` is provided, the transfer will fail to be submitted."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

    description: str
    """A description for the underlying transfer. Maximum of 15 characters."""

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

    origination_account_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for the origination account for the intent. If not provided, the default account will
    be used."""

    user: TransferUserInRequest
    """The legal name and other information for the account holder."""

    metadata: Optional[dict[str, str | None]] = UNSET
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of
    50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters"""

    iso_currency_code: Optional[str] = UNSET
    """The currency of the transfer amount, e.g. "USD"
    """

    require_guarantee: OptionalNullable[bool] = UNSET
    """When ``true``, the transfer requires a ``GUARANTEED`` decision by Plaid to proceed (Guarantee customers only)."""


class TransferIntentCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    account_id: NotRequired[str | None]
    funding_account_id: NotRequired[str | None]
    mode: TransferIntentCreateModeOrStr
    network: NotRequired[TransferIntentCreateNetworkOrStr]
    amount: str
    description: str
    ach_class: NotRequired[AchclassOrStr]
    origination_account_id: NotRequired[str | None]
    user: TransferUserInRequest | TransferUserInRequestDict
    metadata: NotRequired[dict[str, str | None]]
    iso_currency_code: NotRequired[str]
    require_guarantee: NotRequired[bool | None]
