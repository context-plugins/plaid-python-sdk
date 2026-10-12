from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_document_metadata import CreditDocumentMetadata, CreditDocumentMetadataDict
from .credit_pay_stub_employee import CreditPayStubEmployee, CreditPayStubEmployeeDict
from .credit_pay_stub_employer import CreditPayStubEmployer, CreditPayStubEmployerDict
from .w2_box12 import W2Box12, W2Box12Dict
from .w2_state_and_local_wages import W2StateAndLocalWages, W2StateAndLocalWagesDict


class CreditW2(SdkBaseModel):
    """W2 is an object that represents income data taken from a W2 tax document."""

    document_metadata: CreditDocumentMetadata
    """Object representing metadata pertaining to the document."""

    document_id: str
    """An identifier of the document referenced by the document metadata."""

    employer: CreditPayStubEmployer
    """Information about the employer on the pay stub."""

    employee: CreditPayStubEmployee
    """Data about the employee."""

    tax_year: str | None
    """The tax year of the W2 document."""

    employer_id_number: str | None
    """An employer identification number or EIN."""

    wages_tips_other_comp: str | None
    """Wages from tips and other compensation."""

    federal_income_tax_withheld: str | None
    """Federal income tax withheld for the tax year."""

    social_security_wages: str | None
    """Wages from Social Security."""

    social_security_tax_withheld: str | None
    """Social Security tax withheld for the tax year."""

    medicare_wages_and_tips: str | None
    """Wages and tips from medicare."""

    medicare_tax_withheld: str | None
    """Medicare tax withheld for the tax year."""

    social_security_tips: str | None
    """Tips from Social Security."""

    allocated_tips: str | None
    """Allocated tips."""

    box_9: str | None
    """Contents from box 9 on the W2."""

    dependent_care_benefits: str | None
    """Dependent care benefits."""

    nonqualified_plans: str | None
    """Nonqualified plans."""

    box_12: list[W2Box12]
    statutory_employee: str | None
    """Statutory employee."""

    retirement_plan: str | None
    """Retirement plan."""

    third_party_sick_pay: str | None
    """Third party sick pay."""

    other: str | None
    """Other."""

    state_and_local_wages: list[W2StateAndLocalWages]


class CreditW2Dict(TypedDict):
    document_metadata: CreditDocumentMetadataDict
    document_id: str
    employer: CreditPayStubEmployerDict
    employee: CreditPayStubEmployeeDict
    tax_year: str | None
    employer_id_number: str | None
    wages_tips_other_comp: str | None
    federal_income_tax_withheld: str | None
    social_security_wages: str | None
    social_security_tax_withheld: str | None
    medicare_wages_and_tips: str | None
    medicare_tax_withheld: str | None
    social_security_tips: str | None
    allocated_tips: str | None
    box_9: str | None
    dependent_care_benefits: str | None
    nonqualified_plans: str | None
    box_12: list[W2Box12Dict]
    statutory_employee: str | None
    retirement_plan: str | None
    third_party_sick_pay: str | None
    other: str | None
    state_and_local_wages: list[W2StateAndLocalWagesDict]
