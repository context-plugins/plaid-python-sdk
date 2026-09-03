from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecisionOrStr
from .enums.transfer_intent_authorization_decision import TransferIntentAuthorizationDecisionOrStr
from .enums.transfer_intent_create_mode import TransferIntentCreateModeOrStr
from .enums.transfer_intent_create_network import TransferIntentCreateNetworkOrStr
from .enums.transfer_intent_status import TransferIntentStatusOrStr
from .transfer_authorization_decision_rationale import (
    TransferAuthorizationDecisionRationale,
    TransferAuthorizationDecisionRationaleDict,
)
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
    TransferAuthorizationGuaranteeDecisionRationaleDict,
)
from .transfer_intent_get_failure_reason import TransferIntentGetFailureReason, TransferIntentGetFailureReasonDict
from .transfer_user_in_response import TransferUserInResponse, TransferUserInResponseDict


class TransferIntentGet(SdkBaseModel):
    """Represents a transfer intent within Transfer UI."""

    id: str
    """Plaid's unique identifier for a transfer intent object."""

    created: RFC3339DateTime
    """The datetime the transfer was created. This will be of the form ``2006-01-02T15:04:05Z``."""

    status: TransferIntentStatusOrStr
    """The status of the transfer intent.

    ``PENDING``: The transfer intent is pending. ``SUCCEEDED``: The transfer intent was successfully created.
    ``FAILED``: The transfer intent was unable to be created."""

    transfer_id: str | None
    """Plaid's unique identifier for the transfer created through the UI. Returned only if the transfer was successfully
    created. Null value otherwise."""

    failure_reason: TransferIntentGetFailureReason | None
    """The reason for a failed transfer intent. Returned only if the transfer intent status is ``failed``. Null
    otherwise."""

    authorization_decision: TransferIntentAuthorizationDecisionOrStr | None
    """A decision regarding the proposed transfer.

    ``APPROVED`` - The proposed transfer has received the end user's consent and has been approved for processing by
    Plaid. The ``decision_rationale`` field is set if Plaid was unable to fetch the account information. You may proceed
    with the transfer, but further review is recommended (i.e., use Link in update mode to re-authenticate your user
    when ``decision_rationale.code`` is ``ITEM_LOGIN_REQUIRED``). Refer to the ``code`` field in the
    ``decision_rationale`` object for details.

    ``DECLINED`` - Plaid reviewed the proposed transfer and declined processing. Refer to the ``code`` field in the
    ``decision_rationale`` object for details."""

    authorization_decision_rationale: TransferAuthorizationDecisionRationale | None
    """The rationale for Plaid's decision regarding a proposed transfer. It is always set for ``declined`` decisions,
    and may or may not be null for ``approved`` decisions."""

    account_id: OptionalNullable[str] = UNSET
    """The Plaid ``account_id`` for the account that will be debited or credited. Returned only if ``account_id`` was
    set on intent creation."""

    origination_account_id: str
    """Plaid's unique identifier for the origination account used for the transfer."""

    funding_account_id: str
    """The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business
    checking accounts will be credited or debited."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. "10.00"). When calling
    ``/transfer/authorization/create``, specify the maximum amount to authorize. When calling ``/transfer/create``,
    specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when
    calling ``/transfer/create``, the maximum amount authorized in the ``authorization_id`` will be sent."""

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

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    description: str
    """A description for the underlying transfer. Maximum of 15 characters."""

    metadata: Optional[dict[str, str | None]] = UNSET
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of
    50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters"""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD"
    """

    require_guarantee: OptionalNullable[bool] = UNSET
    """When ``true``, the transfer requires a ``GUARANTEED`` decision by Plaid to proceed (Guarantee customers only)."""

    guarantee_decision: TransferAuthorizationGuaranteeDecisionOrStr | None
    """Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either
    ``GUARANTEED`` or ``NOT_GUARANTEED`` indicating whether Plaid will guarantee the transfer."""

    guarantee_decision_rationale: TransferAuthorizationGuaranteeDecisionRationale | None
    """The rationale for Plaid's decision to not guarantee a transfer. Will be ``null`` unless ``guarantee_decision`` is
    ``NOT_GUARANTEED``."""


class TransferIntentGetDict(TypedDict):
    id: str
    created: RFC3339DateTime
    status: TransferIntentStatusOrStr
    transfer_id: str | None
    failure_reason: TransferIntentGetFailureReason | TransferIntentGetFailureReasonDict | None
    authorization_decision: TransferIntentAuthorizationDecisionOrStr | None
    authorization_decision_rationale: (
        TransferAuthorizationDecisionRationale | TransferAuthorizationDecisionRationaleDict | None
    )
    account_id: NotRequired[str | None]
    origination_account_id: str
    funding_account_id: str
    amount: str
    mode: TransferIntentCreateModeOrStr
    network: NotRequired[TransferIntentCreateNetworkOrStr]
    ach_class: NotRequired[AchclassOrStr]
    user: TransferUserInResponse | TransferUserInResponseDict
    description: str
    metadata: NotRequired[dict[str, str | None]]
    iso_currency_code: str
    require_guarantee: NotRequired[bool | None]
    guarantee_decision: TransferAuthorizationGuaranteeDecisionOrStr | None
    guarantee_decision_rationale: (
        TransferAuthorizationGuaranteeDecisionRationale | TransferAuthorizationGuaranteeDecisionRationaleDict | None
    )
