from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraPartnerInsightsBureau(str, Enum):
    """The credit bureau that provided the base FICO score."""

    EQUIFAX = "EQUIFAX"
    EXPERIAN = "EXPERIAN"
    TRANSUNION = "TRANSUNION"

    __str__ = str.__str__


CraPartnerInsightsBureauOrStr: TypeAlias = Annotated[
    CraPartnerInsightsBureau | str, open_enum_validator(CraPartnerInsightsBureau)
]
