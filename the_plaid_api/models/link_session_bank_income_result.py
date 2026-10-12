from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credit_session_bank_income_status import CreditSessionBankIncomeStatusOrStr
from .link_session_success_metadata_institution import (
    LinkSessionSuccessMetadataInstitution,
    LinkSessionSuccessMetadataInstitutionDict,
)


class LinkSessionBankIncomeResult(SdkBaseModel):
    """The details of a bank income verification in Link."""

    status: CreditSessionBankIncomeStatusOrStr
    """Status of the Bank Income Link session.

    ``APPROVED``: User has approved and verified their income

    ``NO_DEPOSITS_FOUND``: We attempted, but were unable to find any income in the connected account.

    ``USER_REPORTED_NO_INCOME``: The user explicitly indicated that they don't receive income in the connected account.

    ``STARTED``: The user began the bank income portion of the link flow.

    ``INTERNAL_ERROR``: The user encountered an internal error."""

    item_id: str
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    institution: LinkSessionSuccessMetadataInstitution | None
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""


class LinkSessionBankIncomeResultDict(TypedDict):
    status: CreditSessionBankIncomeStatusOrStr
    item_id: str
    institution: LinkSessionSuccessMetadataInstitutionDict | None
