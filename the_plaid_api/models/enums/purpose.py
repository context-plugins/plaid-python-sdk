from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Purpose(str, Enum):
    """Specifies the purpose of the uploaded file.

    ``"DUE_DILIGENCE"`` - The transfer due diligence document of the originator."""

    DUE_DILIGENCE = "DUE_DILIGENCE"

    __str__ = str.__str__


PurposeOrStr: TypeAlias = Annotated[Purpose | str, open_enum_validator(Purpose)]
