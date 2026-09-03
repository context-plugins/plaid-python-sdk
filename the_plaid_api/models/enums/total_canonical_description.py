from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TotalCanonicalDescription(str, Enum):
    """Commonly used term to describe the line item."""

    BONUS = "BONUS"
    COMMISSION = "COMMISSION"
    OVERTIME = "OVERTIME"
    PAID_TIME_OFF = "PAID TIME OFF"
    REGULAR_PAY = "REGULAR PAY"
    VACATION = "VACATION"
    EMPLOYEE_MEDICARE = "EMPLOYEE MEDICARE"
    FICA = "FICA"
    SOCIAL_SECURITY_EMPLOYEE_TAX = "SOCIAL SECURITY EMPLOYEE TAX"
    MEDICAL = "MEDICAL"
    VISION = "VISION"
    DENTAL = "DENTAL"
    NET_PAY = "NET PAY"
    TAXES = "TAXES"
    NOT_FOUND = "NOT_FOUND"
    OTHER = "OTHER"

    __str__ = str.__str__


TotalCanonicalDescriptionOrStr: TypeAlias = Annotated[
    TotalCanonicalDescription | str, open_enum_validator(TotalCanonicalDescription)
]
