from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Form1099Type(str, Enum):
    """Form 1099 Type"""

    FORM_1099_TYPE_UNKNOWN = "FORM_1099_TYPE_UNKNOWN"
    FORM_1099_TYPE_MISC = "FORM_1099_TYPE_MISC"
    FORM_1099_TYPE_K = "FORM_1099_TYPE_K"

    __str__ = str.__str__


Form1099TypeOrStr: TypeAlias = Annotated[Form1099Type | str, open_enum_validator(Form1099Type)]
