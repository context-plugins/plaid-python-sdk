from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExpirationDate(str, Enum):
    """A description of whether the associated document was expired when the verification was performed.

    Note: In the case where an expiration date is not present on the document or failed to be extracted, this value will
    be ``no_data``."""

    NOT_EXPIRED = "not_expired"
    EXPIRED = "expired"
    NO_DATA = "no_data"

    __str__ = str.__str__


ExpirationDateOrStr: TypeAlias = Annotated[ExpirationDate | str, open_enum_validator(ExpirationDate)]
