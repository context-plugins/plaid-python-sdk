from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .employee import Employee, EmployeeDict
from .paystub_employer import PaystubEmployer, PaystubEmployerDict
from .w2_box12 import W2Box12, W2Box12Dict
from .w2_state_and_local_wages import W2StateAndLocalWages, W2StateAndLocalWagesDict


class W2(SdkBaseModel):
    """W2 is an object that represents income data taken from a W2 tax document."""

    employer: Optional[PaystubEmployer] = UNSET
    """Information about the employer on the paystub"""

    employee: Optional[Employee] = UNSET
    """Data about the employee."""

    tax_year: OptionalNullable[str] = UNSET
    """The tax year of the W2 document."""

    employer_id_number: OptionalNullable[str] = UNSET
    """An employer identification number or EIN."""

    wages_tips_other_comp: OptionalNullable[str] = UNSET
    """Wages from tips and other compensation."""

    federal_income_tax_withheld: OptionalNullable[str] = UNSET
    """Federal income tax withheld for the tax year."""

    social_security_wages: OptionalNullable[str] = UNSET
    """Wages from Social Security."""

    social_security_tax_withheld: OptionalNullable[str] = UNSET
    """Social Security tax withheld for the tax year."""

    medicare_wages_and_tips: OptionalNullable[str] = UNSET
    """Wages and tips from medicare."""

    medicare_tax_withheld: OptionalNullable[str] = UNSET
    """Medicare tax withheld for the tax year."""

    social_security_tips: OptionalNullable[str] = UNSET
    """Tips from Social Security."""

    allocated_tips: OptionalNullable[str] = UNSET
    """Allocated tips."""

    box_9: OptionalNullable[str] = UNSET
    """Contents from box 9 on the W2."""

    dependent_care_benefits: OptionalNullable[str] = UNSET
    """Dependent care benefits."""

    nonqualified_plans: OptionalNullable[str] = UNSET
    """Nonqualified plans."""

    box_12: Optional[list[W2Box12]] = UNSET
    statutory_employee: OptionalNullable[str] = UNSET
    """Statutory employee."""

    retirement_plan: OptionalNullable[str] = UNSET
    """Retirement plan."""

    third_party_sick_pay: OptionalNullable[str] = UNSET
    """Third party sick pay."""

    other: OptionalNullable[str] = UNSET
    """Other."""

    state_and_local_wages: Optional[list[W2StateAndLocalWages]] = UNSET


class W2Dict(TypedDict):
    employer: NotRequired[PaystubEmployerDict]
    employee: NotRequired[EmployeeDict]
    tax_year: NotRequired[str | None]
    employer_id_number: NotRequired[str | None]
    wages_tips_other_comp: NotRequired[str | None]
    federal_income_tax_withheld: NotRequired[str | None]
    social_security_wages: NotRequired[str | None]
    social_security_tax_withheld: NotRequired[str | None]
    medicare_wages_and_tips: NotRequired[str | None]
    medicare_tax_withheld: NotRequired[str | None]
    social_security_tips: NotRequired[str | None]
    allocated_tips: NotRequired[str | None]
    box_9: NotRequired[str | None]
    dependent_care_benefits: NotRequired[str | None]
    nonqualified_plans: NotRequired[str | None]
    box_12: NotRequired[list[W2Box12Dict]]
    statutory_employee: NotRequired[str | None]
    retirement_plan: NotRequired[str | None]
    third_party_sick_pay: NotRequired[str | None]
    other: NotRequired[str | None]
    state_and_local_wages: NotRequired[list[W2StateAndLocalWagesDict]]
