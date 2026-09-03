from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferIntentAuthorizationDecision(str, Enum):
    """A decision regarding the proposed transfer.

    ``APPROVED`` - The proposed transfer has received the end user's consent and has been approved for processing by
    Plaid. The ``decision_rationale`` field is set if Plaid was unable to fetch the account information. You may proceed
    with the transfer, but further review is recommended (i.e., use Link in update mode to re-authenticate your user
    when ``decision_rationale.code`` is ``ITEM_LOGIN_REQUIRED``). Refer to the ``code`` field in the
    ``decision_rationale`` object for details.

    ``DECLINED`` - Plaid reviewed the proposed transfer and declined processing. Refer to the ``code`` field in the
    ``decision_rationale`` object for details."""

    APPROVED = "APPROVED"
    DECLINED = "DECLINED"

    __str__ = str.__str__


TransferIntentAuthorizationDecisionOrStr: TypeAlias = Annotated[
    TransferIntentAuthorizationDecision | str, open_enum_validator(TransferIntentAuthorizationDecision)
]
