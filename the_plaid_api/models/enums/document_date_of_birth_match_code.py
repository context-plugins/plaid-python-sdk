from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentDateOfBirthMatchCode(str, Enum):
    """A match summary describing the cross comparison between the subject's date of birth, extracted from the document
    image, and the date of birth they separately provided to the identity verification attempt."""

    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NO_MATCH = "no_match"
    NO_DATA = "no_data"

    __str__ = str.__str__


DocumentDateOfBirthMatchCodeOrStr: TypeAlias = Annotated[
    DocumentDateOfBirthMatchCode | str, open_enum_validator(DocumentDateOfBirthMatchCode)
]
