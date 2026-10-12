from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .authorization_guarantee_details import AuthorizationGuaranteeDetails, AuthorizationGuaranteeDetailsDict
from .enums.transfer_authorization_decision import TransferAuthorizationDecisionOrStr
from .enums.transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecisionOrStr
from .transfer_authorization_decision_rationale import (
    TransferAuthorizationDecisionRationale,
    TransferAuthorizationDecisionRationaleDict,
)
from .transfer_authorization_guarantee_decision_rationale import (
    TransferAuthorizationGuaranteeDecisionRationale,
    TransferAuthorizationGuaranteeDecisionRationaleDict,
)
from .transfer_authorization_payment_risk import TransferAuthorizationPaymentRisk, TransferAuthorizationPaymentRiskDict
from .transfer_authorization_proposed_transfer import (
    TransferAuthorizationProposedTransfer,
    TransferAuthorizationProposedTransferDict,
)


class TransferAuthorization(SdkBaseModel):
    """Contains the authorization decision for a proposed transfer."""

    id: str
    """Plaid's unique identifier for a transfer authorization."""

    created: RFC3339DateTime
    """The datetime representing when the authorization was created, in the format ``2006-01-02T15:04:05Z``."""

    decision: TransferAuthorizationDecisionOrStr
    """A decision regarding the proposed transfer.

    ``approved`` - The proposed transfer has received the end user's consent and has been approved for processing by
    Plaid. The ``decision_rationale`` field is set if Plaid was unable to fetch the account information. You may proceed
    with the transfer, but further review is recommended. Refer to the ``code`` field in the ``decision_rationale``
    object for details.

    ``declined`` - Plaid reviewed the proposed transfer and declined processing. Refer to the ``code`` field in the
    ``decision_rationale`` object for details.

    ``user_action_required`` - An action is required before Plaid can assess the transfer risk and make a decision. The
    most common scenario is to update authentication for an Item. To complete the required action, initialize Link by
    setting ``transfer.authorization_id`` in the request of ``/link/token/create``. After Link flow is completed, you
    may re-attempt the authorization request.

    For ``guarantee`` requests, ``approved`` indicates the transfer is eligible for Plaid's guarantee, and ``declined``
    indicates Plaid will not provide guarantee coverage for the transfer. ``user_action_required`` indicates you should
    follow the above guidance before re-attempting."""

    decision_rationale: TransferAuthorizationDecisionRationale | None
    """The rationale for Plaid's decision regarding a proposed transfer. It is always set for ``declined`` decisions,
    and may or may not be null for ``approved`` decisions."""

    guarantee_decision: TransferAuthorizationGuaranteeDecisionOrStr | None
    guarantee_decision_rationale: TransferAuthorizationGuaranteeDecisionRationale | None
    """The rationale for Plaid's decision to not guarantee a transfer. Will be ``null`` unless ``guarantee_decision`` is
    ``NOT_GUARANTEED``."""

    guarantee_details: OptionalNullable[AuthorizationGuaranteeDetails] = UNSET
    """Adaptive guarantee details for a transfer authorization, including the guarantee outcome and settlement schedule.
    Omitted when no guarantee was attempted."""

    payment_risk: TransferAuthorizationPaymentRisk | None
    """This object includes the scores and risk level. This response is offered as an add-on to
    ``/transfer/authorization/create``. To request access to these fields, please contact your Plaid account manager."""

    proposed_transfer: TransferAuthorizationProposedTransfer
    """Details regarding the proposed transfer."""


class TransferAuthorizationDict(TypedDict):
    id: str
    created: RFC3339DateTime
    decision: TransferAuthorizationDecisionOrStr
    decision_rationale: TransferAuthorizationDecisionRationaleDict | None
    guarantee_decision: TransferAuthorizationGuaranteeDecisionOrStr | None
    guarantee_decision_rationale: TransferAuthorizationGuaranteeDecisionRationaleDict | None
    guarantee_details: NotRequired[AuthorizationGuaranteeDetailsDict | None]
    payment_risk: TransferAuthorizationPaymentRiskDict | None
    proposed_transfer: TransferAuthorizationProposedTransferDict
