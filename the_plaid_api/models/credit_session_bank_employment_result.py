from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.credit_session_bank_employment_status import CreditSessionBankEmploymentStatusOrStr


class CreditSessionBankEmploymentResult(SdkBaseModel):
    """The details of a bank employment verification in Link."""

    status: Optional[CreditSessionBankEmploymentStatusOrStr] = UNSET
    """Status of the Bank Employment Link session.

    ``APPROVED``: User has approved and verified their employment.

    ``NO_EMPLOYERS_FOUND``: We attempted, but were unable to find any employment in the connected account.

    ``EMPLOYER_NOT_LISTED``: The user explicitly indicated that they did not see their current or previous employer in
    the list of employer names found.

    ``STARTED``: The user began the bank employment portion of the link flow.

    ``INTERNAL_ERROR``: The user encountered an internal error."""

    item_id: Optional[str] = UNSET
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    institution_id: Optional[str] = UNSET
    """The Plaid Institution ID associated with the Item."""


class CreditSessionBankEmploymentResultDict(TypedDict):
    status: NotRequired[CreditSessionBankEmploymentStatusOrStr]
    item_id: NotRequired[str]
    institution_id: NotRequired[str]
