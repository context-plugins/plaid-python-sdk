from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailDomainIsFreeProvider(str, Enum):
    """Indicates whether the email address domain is a free provider such as Gmail or Hotmail if known."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailDomainIsFreeProviderOrStr: TypeAlias = Annotated[
    RiskCheckEmailDomainIsFreeProvider | str, open_enum_validator(RiskCheckEmailDomainIsFreeProvider)
]
