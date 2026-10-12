from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.transfer_authorization_decision import TransferAuthorizationDecisionOrStr
from .recurring_transfer_nullable import RecurringTransferNullable, RecurringTransferNullableDict
from .transfer_authorization_decision_rationale import (
    TransferAuthorizationDecisionRationale,
    TransferAuthorizationDecisionRationaleDict,
)


class TransferRecurringCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/recurring/create``"""

    recurring_transfer: OptionalNullable[RecurringTransferNullable] = UNSET
    """Represents a recurring transfer within the Transfers API."""

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

    decision_rationale: OptionalNullable[TransferAuthorizationDecisionRationale] = UNSET
    """The rationale for Plaid's decision regarding a proposed transfer. It is always set for ``declined`` decisions,
    and may or may not be null for ``approved`` decisions."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferRecurringCreateResponseDict(TypedDict):
    recurring_transfer: NotRequired[RecurringTransferNullableDict | None]
    decision: TransferAuthorizationDecisionOrStr
    decision_rationale: NotRequired[TransferAuthorizationDecisionRationaleDict | None]
    request_id: str
