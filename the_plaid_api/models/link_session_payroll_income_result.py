from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .link_session_success_metadata_institution import (
    LinkSessionSuccessMetadataInstitution,
    LinkSessionSuccessMetadataInstitutionDict,
)


class LinkSessionPayrollIncomeResult(SdkBaseModel):
    """The details of a digital payroll income verification in Link."""

    num_paystubs_retrieved: int
    """The number of paystubs retrieved from a payroll provider."""

    num_w2s_retrieved: int
    """The number of W-2s retrieved from a payroll provider."""

    institution: LinkSessionSuccessMetadataInstitution | None
    """An institution object. If the Item was created via Same-Day or Instant micro-deposit verification, will be
    ``null``."""


class LinkSessionPayrollIncomeResultDict(TypedDict):
    num_paystubs_retrieved: int
    num_w2s_retrieved: int
    institution: LinkSessionSuccessMetadataInstitution | LinkSessionSuccessMetadataInstitutionDict | None
