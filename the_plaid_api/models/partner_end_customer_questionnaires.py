from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_craquestionnaire import (
    PartnerEndCustomerCraquestionnaire,
    PartnerEndCustomerCraquestionnaireDict,
)


class PartnerEndCustomerQuestionnaires(SdkBaseModel):
    """The questionnaires for the end customer."""

    cra: Optional[PartnerEndCustomerCraquestionnaire] = UNSET
    """The CRA questionnaire for the end customer."""


class PartnerEndCustomerQuestionnairesDict(TypedDict):
    cra: NotRequired[PartnerEndCustomerCraquestionnaireDict]
