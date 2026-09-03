from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailTopLevelDomainIsSuspicious(str, Enum):
    """Indicates whether the email address top level domain, which is the last part of the domain, is fraudulent or
    risky if known. In most cases, a suspicious top level domain is also associated with a disposable or high-risk
    domain."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailTopLevelDomainIsSuspiciousOrStr: TypeAlias = Annotated[
    RiskCheckEmailTopLevelDomainIsSuspicious | str, open_enum_validator(RiskCheckEmailTopLevelDomainIsSuspicious)
]
