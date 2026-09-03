from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailDomainIsCustom(str, Enum):
    """Indicates whether the email address domain is custom if known, i.e. a company domain and not free or
    disposable."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailDomainIsCustomOrStr: TypeAlias = Annotated[
    RiskCheckEmailDomainIsCustom | str, open_enum_validator(RiskCheckEmailDomainIsCustom)
]
