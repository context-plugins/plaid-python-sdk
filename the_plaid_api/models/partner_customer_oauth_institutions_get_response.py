from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_flowdown_status import PartnerEndCustomerFlowdownStatusOrStr
from .enums.partner_end_customer_questionnaire_status import PartnerEndCustomerQuestionnaireStatusOrStr
from .partner_end_customer_oauth_institution import (
    PartnerEndCustomerOauthInstitution,
    PartnerEndCustomerOauthInstitutionDict,
)


class PartnerCustomerOauthInstitutionsGetResponse(SdkBaseModel):
    """Response schema for ``/partner/customer/oauth_institutions/get``."""

    flowdown_status: Optional[PartnerEndCustomerFlowdownStatusOrStr] = UNSET
    """The status of the addendum to the Plaid MSA ("flowdown") for the end customer."""

    questionnaire_status: Optional[PartnerEndCustomerQuestionnaireStatusOrStr] = UNSET
    """The status of the end customer's security questionnaire."""

    institutions: Optional[list[PartnerEndCustomerOauthInstitution]] = UNSET
    """The OAuth institutions with which the end customer's application is being registered."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PartnerCustomerOauthInstitutionsGetResponseDict(TypedDict):
    flowdown_status: NotRequired[PartnerEndCustomerFlowdownStatusOrStr]
    questionnaire_status: NotRequired[PartnerEndCustomerQuestionnaireStatusOrStr]
    institutions: NotRequired[list[PartnerEndCustomerOauthInstitutionDict]]
    request_id: NotRequired[str]
