from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .bank_transfer_user import BankTransferUser, BankTransferUserDict
from .enums.achclass import AchclassOrStr
from .enums.bank_transfer_network import BankTransferNetworkOrStr
from .enums.bank_transfer_type import BankTransferTypeOrStr


class BankTransferCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/bank_transfer/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    idempotency_key: str
    """A random key provided by the client, per unique bank transfer. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    For example, if a request to create a bank transfer fails due to a network connection error, you can retry the
    request with the same idempotency key to guarantee that only a single bank transfer is created."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    account_id: str
    """The Plaid ``account_id`` for the account that will be debited or credited."""

    type_: BankTransferTypeOrStr = Field(alias="type")
    """The type of bank transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money
    into the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    network: BankTransferNetworkOrStr
    """The network or rails used for the transfer. Valid options are ``ach``, ``same-day-ach``, or ``wire``."""

    amount: str
    """The amount of the bank transfer (decimal string with two digits of precision e.g. "10.00")."""

    iso_currency_code: str
    """The currency of the transfer amount - should be set to "USD"."""

    description: str
    """The transfer description. Maximum of 10 characters."""

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

    user: BankTransferUser
    """The legal name and other information for the account holder."""

    custom_tag: OptionalNullable[str] = UNSET
    """An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters."""

    metadata: OptionalNullable[dict[str, str]] = UNSET
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of
    50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters"""

    origination_account_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for the origination account for this transfer. If you have more than one origination
    account, this value must be specified. Otherwise, this field should be left blank."""


class BankTransferCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    idempotency_key: str
    access_token: str
    account_id: str
    type_: BankTransferTypeOrStr
    network: BankTransferNetworkOrStr
    amount: str
    iso_currency_code: str
    description: str
    ach_class: NotRequired[AchclassOrStr]
    user: BankTransferUserDict
    custom_tag: NotRequired[str | None]
    metadata: NotRequired[dict[str, str] | None]
    origination_account_id: NotRequired[str | None]
