from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HumanReviewStatus(str, Enum):
    """The outcome of the human review check, when available. The following values are possible:


    ``success`` - The document passed the check.

    ``failed`` - The document failed the check.

    ``no_data`` - The document was submitted, but the document specialist review was not completed in time."""

    SUCCESS = "success"
    FAILED = "failed"
    NO_DATA = "no_data"

    __str__ = str.__str__


HumanReviewStatusOrStr: TypeAlias = Annotated[HumanReviewStatus | str, open_enum_validator(HumanReviewStatus)]
