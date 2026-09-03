from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DocumentStatus(str, Enum):
    """An outcome status for this specific document submission. Distinct from the overall
    ``documentary_verification.status`` that summarizes the verification outcome from one or more documents."""

    SUCCESS = "success"
    FAILED = "failed"
    MANUALLY_APPROVED = "manually_approved"

    __str__ = str.__str__


DocumentStatusOrStr: TypeAlias = Annotated[DocumentStatus | str, open_enum_validator(DocumentStatus)]
