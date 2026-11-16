from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_cra_use_cases import PartnerEndCustomerCraUseCases, PartnerEndCustomerCraUseCasesDict


class PartnerEndCustomerCraPurposes(SdkBaseModel):
    """A map of permissible purposes to their corresponding use cases."""

    written_instruction: Optional[PartnerEndCustomerCraUseCases] = Field(default=UNSET, alias="WRITTEN_INSTRUCTION")
    """The list of use cases associated with a given permissible purpose."""

    extension_of_credit_or_account_review: Optional[PartnerEndCustomerCraUseCases] = Field(
        default=UNSET, alias="EXTENSION_OF_CREDIT_OR_ACCOUNT_REVIEW"
    )
    """The list of use cases associated with a given permissible purpose."""

    employment: Optional[PartnerEndCustomerCraUseCases] = Field(default=UNSET, alias="EMPLOYMENT")
    """The list of use cases associated with a given permissible purpose."""

    insurance_underwriting: Optional[PartnerEndCustomerCraUseCases] = Field(
        default=UNSET, alias="INSURANCE_UNDERWRITING"
    )
    """The list of use cases associated with a given permissible purpose."""

    license_eligibility: Optional[PartnerEndCustomerCraUseCases] = Field(default=UNSET, alias="LICENSE_ELIGIBILITY")
    """The list of use cases associated with a given permissible purpose."""

    risk_assessment: Optional[PartnerEndCustomerCraUseCases] = Field(default=UNSET, alias="RISK_ASSESSMENT")
    """The list of use cases associated with a given permissible purpose."""

    business_need_transaction: Optional[PartnerEndCustomerCraUseCases] = Field(
        default=UNSET, alias="BUSINESS_NEED_TRANSACTION"
    )
    """The list of use cases associated with a given permissible purpose."""

    business_need_account_review: Optional[PartnerEndCustomerCraUseCases] = Field(
        default=UNSET, alias="BUSINESS_NEED_ACCOUNT_REVIEW"
    )
    """The list of use cases associated with a given permissible purpose."""


class PartnerEndCustomerCraPurposesDict(TypedDict):
    written_instruction: NotRequired[PartnerEndCustomerCraUseCasesDict]
    extension_of_credit_or_account_review: NotRequired[PartnerEndCustomerCraUseCasesDict]
    employment: NotRequired[PartnerEndCustomerCraUseCasesDict]
    insurance_underwriting: NotRequired[PartnerEndCustomerCraUseCasesDict]
    license_eligibility: NotRequired[PartnerEndCustomerCraUseCasesDict]
    risk_assessment: NotRequired[PartnerEndCustomerCraUseCasesDict]
    business_need_transaction: NotRequired[PartnerEndCustomerCraUseCasesDict]
    business_need_account_review: NotRequired[PartnerEndCustomerCraUseCasesDict]
