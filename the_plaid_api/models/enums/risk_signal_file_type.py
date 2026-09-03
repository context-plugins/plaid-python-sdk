from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskSignalFileType(str, Enum):
    """The file type for risk signal analysis"""

    UNKNOWN = "UNKNOWN"
    IMAGE_PDF = "IMAGE_PDF"
    SCAN_OCR = "SCAN_OCR"
    TRUE_PDF = "TRUE_PDF"
    IMAGE = "IMAGE"
    MIXED_PAGE_PDF = "MIXED_PAGE_PDF"
    EMPTY_PDF = "EMPTY_PDF"
    FLATTENED_PDF = "FLATTENED_PDF"

    __str__ = str.__str__


RiskSignalFileTypeOrStr: TypeAlias = Annotated[RiskSignalFileType | str, open_enum_validator(RiskSignalFileType)]
