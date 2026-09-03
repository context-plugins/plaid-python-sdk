from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraCreditProfileInquiryType(str, Enum):
    """The inquiry type of credit profile report."""

    SOFT_INQUIRY = "SOFT_INQUIRY"
    STANDARD_INQUIRY = "STANDARD_INQUIRY"

    __str__ = str.__str__


CraCreditProfileInquiryTypeOrStr: TypeAlias = Annotated[
    CraCreditProfileInquiryType | str, open_enum_validator(CraCreditProfileInquiryType)
]
