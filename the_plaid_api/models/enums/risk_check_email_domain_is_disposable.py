from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailDomainIsDisposable(str, Enum):
    """Indicates whether the email domain is listed as disposable if known. Disposable domains are often used to create
    email addresses that are part of a fake set of user details."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailDomainIsDisposableOrStr: TypeAlias = Annotated[
    RiskCheckEmailDomainIsDisposable | str, open_enum_validator(RiskCheckEmailDomainIsDisposable)
]
