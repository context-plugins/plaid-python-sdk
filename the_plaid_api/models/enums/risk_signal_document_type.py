from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskSignalDocumentType(str, Enum):
    """Type of a document for risk signal analysis"""

    UNKNOWN = "UNKNOWN"
    BANK_STATEMENT = "BANK_STATEMENT"
    BENEFITS_STATEMENT = "BENEFITS_STATEMENT"
    BUSINESS_FILING = "BUSINESS_FILING"
    CHECK = "CHECK"
    DRIVING_LICENSE = "DRIVING_LICENSE"
    FINANCIAL_STATEMENT = "FINANCIAL_STATEMENT"
    INVOICE = "INVOICE"
    PAYSLIP = "PAYSLIP"
    SOCIAL_SECURITY_CARD = "SOCIAL_SECURITY_CARD"
    TAX_FORM = "TAX_FORM"
    UTILITY_BILL = "UTILITY_BILL"

    __str__ = str.__str__


RiskSignalDocumentTypeOrStr: TypeAlias = Annotated[
    RiskSignalDocumentType | str, open_enum_validator(RiskSignalDocumentType)
]
