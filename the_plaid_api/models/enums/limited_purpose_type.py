from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LimitedPurposeType(str, Enum):
    """A specific use case for a limited purpose checking account. Limited purpose checking accounts will reject or
    return ACH transactions that aren't for eligible use cases. For example, a ``RENT_MORTGAGE`` limited purpose
    checking account will reject ACH transactions that are not specifically rent or mortgage payments."""

    RENT_MORTGAGE = "RENT_MORTGAGE"

    __str__ = str.__str__


LimitedPurposeTypeOrStr: TypeAlias = Annotated[LimitedPurposeType | str, open_enum_validator(LimitedPurposeType)]
