from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_cra_questionnaire import (
    PartnerEndCustomerCraQuestionnaire,
    PartnerEndCustomerCraQuestionnaireDict,
)


class PartnerEndCustomerQuestionnaires(SdkBaseModel):
    """The questionnaires for the end customer."""

    cra: Optional[PartnerEndCustomerCraQuestionnaire] = UNSET
    """The CRA questionnaire for the end customer."""


class PartnerEndCustomerQuestionnairesDict(TypedDict):
    cra: NotRequired[PartnerEndCustomerCraQuestionnaireDict]
