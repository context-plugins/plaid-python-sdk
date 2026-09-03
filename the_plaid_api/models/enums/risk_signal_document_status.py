from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskSignalDocumentStatus(str, Enum):
    """Status of a document for risk signal analysis"""

    PROCESSING = "PROCESSING"
    PROCESSING_COMPLETE = "PROCESSING_COMPLETE"
    PROCESSING_ERROR = "PROCESSING_ERROR"
    PASSWORD_PROTECTED = "PASSWORD_PROTECTED"
    VIRUS_DETECTED = "VIRUS_DETECTED"

    __str__ = str.__str__


RiskSignalDocumentStatusOrStr: TypeAlias = Annotated[
    RiskSignalDocumentStatus | str, open_enum_validator(RiskSignalDocumentStatus)
]
