from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_crause_cases import PartnerEndCustomerCrauseCases, PartnerEndCustomerCrauseCasesDict


class PartnerEndCustomerCrapurposes(SdkBaseModel):
    """A map of permissible purposes to their corresponding use cases."""

    written_instruction: Optional[PartnerEndCustomerCrauseCases] = Field(default=UNSET, alias="WRITTEN_INSTRUCTION")
    """The list of use cases associated with a given permissible purpose."""

    extension_of_credit_or_account_review: Optional[PartnerEndCustomerCrauseCases] = Field(
        default=UNSET, alias="EXTENSION_OF_CREDIT_OR_ACCOUNT_REVIEW"
    )
    """The list of use cases associated with a given permissible purpose."""

    employment: Optional[PartnerEndCustomerCrauseCases] = Field(default=UNSET, alias="EMPLOYMENT")
    """The list of use cases associated with a given permissible purpose."""

    insurance_underwriting: Optional[PartnerEndCustomerCrauseCases] = Field(
        default=UNSET, alias="INSURANCE_UNDERWRITING"
    )
    """The list of use cases associated with a given permissible purpose."""

    license_eligibility: Optional[PartnerEndCustomerCrauseCases] = Field(default=UNSET, alias="LICENSE_ELIGIBILITY")
    """The list of use cases associated with a given permissible purpose."""

    risk_assessment: Optional[PartnerEndCustomerCrauseCases] = Field(default=UNSET, alias="RISK_ASSESSMENT")
    """The list of use cases associated with a given permissible purpose."""

    business_need_transaction: Optional[PartnerEndCustomerCrauseCases] = Field(
        default=UNSET, alias="BUSINESS_NEED_TRANSACTION"
    )
    """The list of use cases associated with a given permissible purpose."""

    business_need_account_review: Optional[PartnerEndCustomerCrauseCases] = Field(
        default=UNSET, alias="BUSINESS_NEED_ACCOUNT_REVIEW"
    )
    """The list of use cases associated with a given permissible purpose."""


class PartnerEndCustomerCrapurposesDict(TypedDict):
    written_instruction: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
    extension_of_credit_or_account_review: NotRequired[
        PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict
    ]
    employment: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
    insurance_underwriting: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
    license_eligibility: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
    risk_assessment: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
    business_need_transaction: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
    business_need_account_review: NotRequired[PartnerEndCustomerCrauseCases | PartnerEndCustomerCrauseCasesDict]
