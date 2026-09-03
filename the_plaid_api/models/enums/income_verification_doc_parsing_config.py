from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IncomeVerificationDocParsingConfig(str, Enum):
    """Analysis options to enable for document parsing"""

    OCR = "ocr"
    RISK_SIGNALS = "risk_signals"

    __str__ = str.__str__


IncomeVerificationDocParsingConfigOrStr: TypeAlias = Annotated[
    IncomeVerificationDocParsingConfig | str, open_enum_validator(IncomeVerificationDocParsingConfig)
]
