from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecisionOrStr
from .enums.transfer_credit_funds_source import TransferCreditFundsSourceOrStr
from .enums.transfer_network import TransferNetworkOrStr
from .enums.transfer_status import TransferStatusOrStr
from .enums.transfer_sweep_status import TransferSweepStatusOrStr
from .enums.transfer_type import TransferTypeOrStr
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
    TransferAuthorizationGuaranteeDecisionRationaleDict,
)
from .transfer_expected_sweep_settlement_schedule_item import (
    TransferExpectedSweepSettlementScheduleItem,
    TransferExpectedSweepSettlementScheduleItemDict,
)
from .transfer_failure import TransferFailure, TransferFailureDict
from .transfer_guarantee_details import TransferGuaranteeDetails, TransferGuaranteeDetailsDict
from .transfer_refund import TransferRefund, TransferRefundDict
from .transfer_user_in_response import TransferUserInResponse, TransferUserInResponseDict
from .transfer_wire_details import TransferWireDetails, TransferWireDetailsDict


class Transfer(SdkBaseModel):
    """Represents a transfer within the Transfers API."""

    id: str
    """Plaid's unique identifier for a transfer."""

    authorization_id: str
    """Plaid's unique identifier for a transfer authorization."""

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

    account_id: Optional[str] = UNSET
    """The Plaid ``account_id`` corresponding to the end-user account that will be debited or credited."""

    funding_account_id: str | None
    """The id of the associated funding account, available in the Plaid Dashboard. If present, this indicates which of
    your business checking accounts will be credited or debited."""

    ledger_id: OptionalNullable[str] = UNSET
    """Plaid's unique identifier for a Plaid Ledger Balance."""

    type_: TransferTypeOrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

    description: str
    """The description of the transfer."""

    created: RFC3339DateTime
    """The datetime when this transfer was created. This will be of the form ``2006-01-02T15:04:05Z``"""

    status: TransferStatusOrStr
    """The status of the transfer.

    ``pending``: A new transfer was created; it is in the pending state. ``posted``: The transfer has been successfully
    submitted to the payment network. ``settled``: The transfer was successfully completed by the payment network. Note
    that funds from received debits are not available to be moved out of the Ledger until the transfer reaches
    ``funds_available`` status. For credit transactions, ``settled`` means the funds have been delivered to the
    receiving bank account. This is the terminal state of a successful credit transfer. ``funds_available``: Funds from
    the transfer have been released from hold and applied to the ledger's available balance. (Only applicable to ACH
    debits.) This is the terminal state of a successful debit transfer. ``cancelled``: The transfer was cancelled by the
    client. This is the terminal state of a cancelled transfer. ``failed``: The transfer failed, no funds were moved.
    This is the terminal state of a failed transfer. ``returned``: A posted transfer was returned. This is the terminal
    state of a returned transfer."""

    sweep_status: OptionalNullable[TransferSweepStatusOrStr] = UNSET
    """The status of the sweep for the transfer.

    ``unswept``: The transfer hasn't been swept yet. ``swept``: The transfer was swept to the sweep account.
    ``swept_settled``: Credits are available to be withdrawn or debits have been deducted from the customer's business
    checking account. ``return_swept``: The transfer was returned, funds were pulled back or pushed back to the sweep
    account. ``null``: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being
    swept)"""

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

    wire_details: OptionalNullable[TransferWireDetails] = UNSET
    """Information specific to wire transfers."""

    cancellable: bool
    """When ``true``, you can still cancel this transfer."""

    failure_reason: TransferFailure | None
    """The failure reason if the event type for a transfer is ``"failed"`` or ``"returned"``. Null value otherwise."""

    metadata: dict[str, str | None]
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of
    50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters"""

    origination_account_id: str
    """Plaid's unique identifier for the origination account that was used for this transfer."""

    guarantee_decision: TransferAuthorizationGuaranteeDecisionOrStr | None
    guarantee_decision_rationale: TransferAuthorizationGuaranteeDecisionRationale | None
    """The rationale for Plaid's decision to not guarantee a transfer. Will be ``null`` unless ``guarantee_decision`` is
    ``NOT_GUARANTEED``."""

    guarantee_details: OptionalNullable[TransferGuaranteeDetails] = UNSET
    """Adaptive guarantee details for a transfer, including the guaranteed amount and settlement schedule. Omitted when
    no guarantee was attempted."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD"
    """

    standard_return_window: Date | None
    """The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01,
    R02, R03, R29. This will be of the form YYYY-MM-DD."""

    unauthorized_return_window: Date | None
    """The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05,
    R07, R10, R11, R51, R33, R37, R38, R52, R53. This will be of the form YYYY-MM-DD."""

    expected_settlement_date: Date | None
    """Deprecated for Plaid Ledger clients, use ``expected_funds_available_date`` instead."""

    expected_funds_available_date: OptionalNullable[Date] = UNSET
    """The expected date when funds from a transfer will be made available and can be withdrawn from the associated
    ledger balance, assuming the debit does not return before this date. If the transfer does return before this date,
    this field will be null. Only applies to debit transfers. This will be of the form YYYY-MM-DD."""

    originator_client_id: str | None
    """The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client
    as a `Platform customer <https://plaid.com/docs/transfer/application/#originators-vs-platforms>`__."""

    refunds: list[TransferRefund]
    """A list of refunds associated with this transfer."""

    recurring_transfer_id: str | None
    """The id of the recurring transfer if this transfer belongs to a recurring transfer."""

    expected_sweep_settlement_schedule: Optional[list[TransferExpectedSweepSettlementScheduleItem]] = UNSET
    """The expected sweep settlement schedule of this transfer, assuming this transfer is not ``returned``. Only applies
    to ACH debit transfers."""

    credit_funds_source: TransferCreditFundsSourceOrStr | None
    facilitator_fee: Optional[str] = UNSET
    """The amount to deduct from ``transfer.amount`` and distribute to the platform's Ledger balance as a facilitator
    fee (decimal string with two digits of precision e.g. "10.00"). The remainder will go to the end-customer's Ledger
    balance. This must be value greater than 0 and less than or equal to the ``transfer.amount``."""

    network_trace_id: OptionalNullable[str] = UNSET
    """The trace identifier for the transfer based on its network. This will only be set after the transfer has posted.

    For ``ach`` or ``same-day-ach`` transfers, this is the ACH trace number. For ``rtp`` transfers, this is the
    Transaction Identification number. For ``wire`` transfers, this is the IMAD (Input Message Accountability Data)
    number."""


class TransferDict(TypedDict):
    id: str
    authorization_id: str
    ach_class: NotRequired[AchclassOrStr]
    account_id: NotRequired[str]
    funding_account_id: str | None
    ledger_id: NotRequired[str | None]
    type_: TransferTypeOrStr
    user: TransferUserInResponse | TransferUserInResponseDict
    amount: str
    description: str
    created: RFC3339DateTime
    status: TransferStatusOrStr
    sweep_status: NotRequired[TransferSweepStatusOrStr | None]
    network: TransferNetworkOrStr
    wire_details: NotRequired[TransferWireDetails | TransferWireDetailsDict | None]
    cancellable: bool
    failure_reason: TransferFailure | TransferFailureDict | None
    metadata: dict[str, str | None]
    origination_account_id: str
    guarantee_decision: TransferAuthorizationGuaranteeDecisionOrStr | None
    guarantee_decision_rationale: (
        TransferAuthorizationGuaranteeDecisionRationale | TransferAuthorizationGuaranteeDecisionRationaleDict | None
    )
    guarantee_details: NotRequired[TransferGuaranteeDetails | TransferGuaranteeDetailsDict | None]
    iso_currency_code: str
    standard_return_window: Date | None
    unauthorized_return_window: Date | None
    expected_settlement_date: Date | None
    expected_funds_available_date: NotRequired[Date | None]
    originator_client_id: str | None
    refunds: list[TransferRefund | TransferRefundDict]
    recurring_transfer_id: str | None
    expected_sweep_settlement_schedule: NotRequired[
        list[TransferExpectedSweepSettlementScheduleItem | TransferExpectedSweepSettlementScheduleItemDict]
    ]
    credit_funds_source: TransferCreditFundsSourceOrStr | None
    facilitator_fee: NotRequired[str]
    network_trace_id: NotRequired[str | None]
