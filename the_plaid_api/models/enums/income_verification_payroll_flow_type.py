from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomeVerificationPayrollFlowType(str, Enum):
    """Flow types to retrieve payroll income data"""

    PAYROLL_DIGITAL_INCOME = "payroll_digital_income"
    PAYROLL_DOCUMENT_INCOME = "payroll_document_income"

    __str__ = str.__str__


IncomeVerificationPayrollFlowTypeOrStr: TypeAlias = Annotated[
    IncomeVerificationPayrollFlowType | str, open_enum_validator(IncomeVerificationPayrollFlowType)
]
