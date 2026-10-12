from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credit_session_bank_employment_status import CreditSessionBankEmploymentStatusOrStr
from .link_session_success_metadata_institution import (
    LinkSessionSuccessMetadataInstitution,
    LinkSessionSuccessMetadataInstitutionDict,
)


class LinkSessionBankEmploymentResult(SdkBaseModel):
    """The details of a bank employment verification in Link."""

    status: CreditSessionBankEmploymentStatusOrStr
    """Status of the Bank Employment Link session.

    ``APPROVED``: User has approved and verified their employment.

    ``NO_EMPLOYERS_FOUND``: We attempted, but were unable to find any employment in the connected account.

    ``EMPLOYER_NOT_LISTED``: The user explicitly indicated that they did not see their current or previous employer in
    the list of employer names found.

    ``STARTED``: The user began the bank employment portion of the link flow.

    ``INTERNAL_ERROR``: The user encountered an internal error."""

    item_id: str
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    institution: LinkSessionSuccessMetadataInstitution | None
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""


class LinkSessionBankEmploymentResultDict(TypedDict):
    status: CreditSessionBankEmploymentStatusOrStr
    item_id: str
    institution: LinkSessionSuccessMetadataInstitutionDict | None
