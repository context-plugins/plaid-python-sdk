from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_credit_funds_source import TransferCreditFundsSourceOrStr
from .enums.transfer_network import TransferNetworkOrStr
from .enums.transfer_type import TransferTypeOrStr
from .transfer_authorization_device import TransferAuthorizationDevice, TransferAuthorizationDeviceDict
from .transfer_authorization_user_in_request import (
    TransferAuthorizationUserInRequest,
    TransferAuthorizationUserInRequestDict,
)
from .transfer_wire_details import TransferWireDetails, TransferWireDetailsDict


class TransferAuthorizationCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/authorization/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    account_id: str
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    funding_account_id: OptionalNullable[str] = UNSET
    """Specify the account used to fund the transfer. Should be specified if using legacy funding methods only. If using
    Plaid Ledger, leave this field blank. Customers can find a list of ``funding_account_id``s in the Accounts page of
    your Plaid Dashboard, under the "Account ID" column. If this field is left blank and you are using legacy funding
    methods, this will default to the default ``funding_account_id`` specified during onboarding. Otherwise, Plaid
    Ledger will be used."""

    ledger_id: OptionalNullable[str] = UNSET
    """Specify which ledger balance should be used to fund the transfer. You can find a list of ``ledger_id``s in the
    Accounts page of your Plaid Dashboard. If this field is left blank, this will default to the id of the default
    ledger balance."""

    payment_profile_token: Optional[str] = UNSET
    """The payment profile token associated with the Payment Profile that will be debited or credited. Required if not
    using ``access_token``."""

    type_: TransferTypeOrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    network: TransferNetworkOrStr
    """The network or rails used for the transfer.

    For transfers submitted as ``ach`` or ``same-day-ach``, the Standard ACH cutoff is 8:30 PM Eastern Time.

    For transfers submitted as ``same-day-ach``, the Same Day ACH cutoff is 3:00 PM Eastern Time. It is recommended to
    send the request 15 minutes prior to the cutoff to ensure that it will be processed in time for submission before
    the cutoff. If the transfer is processed after this cutoff but before the Standard ACH cutoff, it will be sent over
    Standard ACH rails and will not incur same-day charges; this will apply to both legs of the transfer if applicable.
    The transaction limit for a Same Day ACH transfer is $1,000,000. Authorization requests sent with an amount greater
    than $1,000,000 will fail.

    For transfers submitted as ``rtp``, Plaid will automatically route between the Real-Time Payments (RTP) rail by TCH
    or FedNow rails as necessary. If a transfer is submitted as ``rtp`` and the counterparty account is not eligible for
    RTP, the ``/transfer/authorization/create`` request will fail with an ``INVALID_FIELD`` error code. To pre-check to
    determine whether a counterparty account can support RTP, call ``/transfer/capabilities/get`` before calling
    ``/transfer/authorization/create``.

    Wire transfers are currently in early availability. To request access to ``wire`` as a payment network, contact your
    account manager. For transfers submitted as ``wire``, the ``type`` must be ``credit``; wire debits are not
    supported. The cutoff to submit a wire payment is 6:30 PM Eastern Time on a business day; wires submitted after that
    time will be processed on the next business day. The transaction limit for a wire is $999,999.99. Authorization
    requests sent with an amount greater than $999,999.99 will fail.

    Support for ``rfp`` (request for payment) is currently in closed beta. To learn more, contact your Plaid account
    manager. For transfers submitted as ``rfp``, the ``type`` must be ``debit``."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

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

    wire_details: OptionalNullable[TransferWireDetails] = UNSET
    """Information specific to wire transfers."""

    user: TransferAuthorizationUserInRequest
    """The legal name and other information for the account holder. If the account has multiple account holders, provide
    the information for the account holder on whose behalf the authorization is being requested. The ``user.legal_name``
    field is required. Other fields are not currently used and are present to support planned future functionality."""

    device: Optional[TransferAuthorizationDevice] = UNSET
    """Information about the device being used to initiate the authorization. These fields are not currently
    incorporated into the risk check."""

    origination_account_id: Optional[str] = UNSET
    """Plaid's unique identifier for the origination account for this authorization. If not specified, the default
    account will be used."""

    iso_currency_code: Optional[str] = UNSET
    """The currency of the transfer amount. The default value is "USD"."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A random key provided by the client, per unique authorization, which expires after 48 hours. Maximum of 50
    characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    For example, if a request to create an authorization fails due to a network connection error, you can retry the
    request with the same idempotency key to guarantee that only a single authorization is created.

    Idempotency does not apply to authorizations whose decisions are ``user_action_required``. Therefore you may
    re-attempt the authorization after completing the required user action without changing ``idempotency_key``.

    This idempotency key expires after 48 hours, after which the same key can be reused. Failure to provide this key may
    result in duplicate charges."""

    user_present: OptionalNullable[bool] = UNSET
    """If the end user is initiating the specific transfer themselves via an interactive UI, this should be ``true``;
    for automatic recurring payments where the end user is not actually initiating each individual transfer, it should
    be ``false``. This field is not currently used and is present to support planned future functionality."""

    with_guarantee: OptionalNullable[bool] = UNSET
    """If set to ``false``, Plaid will not offer a ``guarantee_decision`` for this request (Guarantee customers only).
    This field is deprecated in favor of ``guarantee``."""

    request_guarantee: OptionalNullable[bool] = UNSET
    """Indicates whether the transfer should be evaluated for guarantee coverage. When set to ``true``, Plaid assesses
    the transfer for guarantee coverage and returns a decision in the authorization response. When omitted or set to
    ``false``, the authorization is evaluated without guarantee coverage."""

    beacon_session_id: OptionalNullable[str] = UNSET
    """The unique identifier returned by Plaid's `beacon <https://plaid.com/docs/transfer/guarantee/#using-a-beacon>`__
    when it is run on your webpage."""

    originator_client_id: OptionalNullable[str] = UNSET
    """The Plaid client ID that is the originator of this transfer. Only needed if creating transfers on behalf of
    another client as a `Platform customer
    <https://plaid.com/docs/transfer/application/#originators-vs-platforms>`__."""

    credit_funds_source: OptionalNullable[TransferCreditFundsSourceOrStr] = UNSET
    test_clock_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a test clock. This field may only be used when using ``sandbox`` environment. If
    provided, the ``authorization`` is created at the ``virtual_time`` on the provided test clock."""

    ruleset_key: OptionalNullable[str] = UNSET
    """The key of the Ruleset for the transaction. If not provided, Signal will use the ``default`` ruleset."""

    custom_attributes: Optional[dict[str, str | None]] = UNSET
    """A free-form map of client-supplied risk-relevant context for this authorization. Plaid may use these attributes
    to inform future versions of our risk models.

    The following limitations apply: Keys must match the regular expression ``^[A-Za-z0-9_.-]{1,40}$`` Values must be
    strings (no nested objects, arrays, numbers, or booleans allowed; stringify non-string values client-side) Maximum
    of 50 key/value pairs Maximum value length of 500 characters

    Do not include personally identifiable information or other sensitive data."""


class TransferAuthorizationCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    account_id: str
    funding_account_id: NotRequired[str | None]
    ledger_id: NotRequired[str | None]
    payment_profile_token: NotRequired[str]
    type_: TransferTypeOrStr
    network: TransferNetworkOrStr
    amount: str
    ach_class: NotRequired[AchclassOrStr]
    wire_details: NotRequired[TransferWireDetails | TransferWireDetailsDict | None]
    user: TransferAuthorizationUserInRequest | TransferAuthorizationUserInRequestDict
    device: NotRequired[TransferAuthorizationDevice | TransferAuthorizationDeviceDict]
    origination_account_id: NotRequired[str]
    iso_currency_code: NotRequired[str]
    idempotency_key: NotRequired[str | None]
    user_present: NotRequired[bool | None]
    with_guarantee: NotRequired[bool | None]
    request_guarantee: NotRequired[bool | None]
    beacon_session_id: NotRequired[str | None]
    originator_client_id: NotRequired[str | None]
    credit_funds_source: NotRequired[TransferCreditFundsSourceOrStr | None]
    test_clock_id: NotRequired[str | None]
    ruleset_key: NotRequired[str | None]
    custom_attributes: NotRequired[dict[str, str | None]]
