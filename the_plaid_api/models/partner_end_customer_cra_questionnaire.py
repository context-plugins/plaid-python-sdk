from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_cra_purposes import PartnerEndCustomerCraPurposes, PartnerEndCustomerCraPurposesDict


class PartnerEndCustomerCraQuestionnaire(SdkBaseModel):
    """The CRA questionnaire for the end customer."""

    purposes: Optional[PartnerEndCustomerCraPurposes] = UNSET
    """A map of permissible purposes to their corresponding use cases."""

    is_third_party_involved: Optional[bool] = UNSET
    """Denotes whether the third party is involved."""

    is_technical_service_provider_involved: Optional[bool] = UNSET
    """Denotes whether the technical service provider is involved."""


class PartnerEndCustomerCraQuestionnaireDict(TypedDict):
    purposes: NotRequired[PartnerEndCustomerCraPurposesDict]
    is_third_party_involved: NotRequired[bool]
    is_technical_service_provider_involved: NotRequired[bool]
