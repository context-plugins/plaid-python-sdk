from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.transfer_authorization_guarantee_decision_rationale_code import (
    TransferAuthorizationGuaranteeDecisionRationaleCodeOrStr,
)


class TransferAuthorizationGuaranteeDecisionRationale(SdkBaseModel):
    """The rationale for Plaid's decision to not guarantee a transfer. Will be ``null`` unless ``guarantee_decision`` is
    ``NOT_GUARANTEED``."""

    code: TransferAuthorizationGuaranteeDecisionRationaleCodeOrStr
    """A code representing the reason Plaid declined to guarantee this transfer:

    ``RETURN_BANK``: The risk of a bank-initiated return (for example, an R01/NSF) is too high to guarantee this
    transfer.

    ``RETURN_CUSTOMER``: The risk of a customer-initiated return (for example, a R10/Unauthorized) is too high to
    guarantee this transfer.

    ``GUARANTEE_LIMIT_REACHED``: This transfer is low-risk, but Guarantee has exhausted an internal limit on the number
    or rate of guarantees that applies to this transfer.

    ``RISK_ESTIMATE_UNAVAILABLE``: A risk estimate is unavailable for this Item.

    ``REQUIRED_PARAM_MISSING``: Required fields are missing."""

    description: str
    """A human-readable description of why the transfer cannot be guaranteed."""


class TransferAuthorizationGuaranteeDecisionRationaleDict(TypedDict):
    code: TransferAuthorizationGuaranteeDecisionRationaleCodeOrStr
    description: str
