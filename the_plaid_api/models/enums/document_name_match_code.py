from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentNameMatchCode(str, Enum):
    """A match summary describing the cross comparison between the subject's name, extracted from the document image,
    and the name they separately provided to the identity verification attempt."""

    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NO_MATCH = "no_match"
    NO_DATA = "no_data"

    __str__ = str.__str__


DocumentNameMatchCodeOrStr: TypeAlias = Annotated[
    DocumentNameMatchCode | str, open_enum_validator(DocumentNameMatchCode)
]
