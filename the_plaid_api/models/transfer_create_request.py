from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_network import TransferNetworkOrStr
from .enums.transfer_type import TransferTypeOrStr
from .transfer_user_in_request_deprecated import TransferUserInRequestDeprecated, TransferUserInRequestDeprecatedDict


class TransferCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    idempotency_key: Optional[str] = UNSET
    """Deprecated. ``authorization_id`` is now used as idempotency instead.

    A random key provided by the client, per unique transfer. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    For example, if a request to create a transfer fails due to a network connection error, you can retry the request
    with the same idempotency key to guarantee that only a single transfer is created."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    account_id: str
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    authorization_id: str
    """Plaid's unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an
    idempotency identifier."""

    type_: Optional[TransferTypeOrStr] = Field(default=UNSET, alias="type")
    network: Optional[TransferNetworkOrStr] = UNSET
    amount: Optional[str] = UNSET
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

    description: str
    """The transfer description, maximum of 15 characters (RTP transactions) or 10 characters (ACH transactions). Should
    represent why the money is moving, not your company name. For recommendations on setting the ``description`` field
    to avoid ACH returns, see `Description field recommendations
    <https://www.plaid.com/docs/transfer/creating-transfers/#description-field-recommendations>`__.

    If reprocessing a returned transfer, the ``description`` field must be ``"Retry 1"`` or ``"Retry 2"``. You may retry
    a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with
    code ``R01`` or ``R09`` may be retried."""

    ach_class: Optional[AchclassOrStr] = UNSET
    user: OptionalNullable[TransferUserInRequestDeprecated] = UNSET
    """The legal name and other information for the account holder."""

    metadata: OptionalNullable[dict[str, str]] = UNSET
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of
    50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters"""

    origination_account_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for the origination account for this transfer. If you have more than one origination
    account, this value must be specified. Otherwise, this field should be left blank."""

    iso_currency_code: Optional[str] = UNSET
    """The currency of the transfer amount. The default value is "USD"."""

    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. This field may only be used when using ``sandbox`` environment. If
    provided, the ``transfer`` is created at the ``virtual_time`` on the provided ``test_clock``."""

    facilitator_fee: Optional[str] = UNSET
    """The amount to deduct from ``transfer.amount`` and distribute to the platform's Ledger balance as a facilitator
    fee (decimal string with two digits of precision e.g. "10.00"). The remainder will go to the end-customer's Ledger
    balance. This must be value greater than 0 and less than or equal to the ``transfer.amount``."""


class TransferCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    idempotency_key: NotRequired[str]
    access_token: str
    account_id: str
    authorization_id: str
    type_: NotRequired[TransferTypeOrStr]
    network: NotRequired[TransferNetworkOrStr]
    amount: NotRequired[str]
    description: str
    ach_class: NotRequired[AchclassOrStr]
    user: NotRequired[TransferUserInRequestDeprecatedDict | None]
    metadata: NotRequired[dict[str, str] | None]
    origination_account_id: NotRequired[str | None]
    iso_currency_code: NotRequired[str]
    test_clock_id: NotRequired[str | None]
    facilitator_fee: NotRequired[str]
