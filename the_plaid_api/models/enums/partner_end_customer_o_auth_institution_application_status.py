from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerOAuthInstitutionApplicationStatus(str, Enum):
    """The registration status for the end customer's application."""

    NOT_STARTED = "NOT_STARTED"
    PROCESSING = "PROCESSING"
    APPROVED = "APPROVED"
    ENABLED = "ENABLED"
    ATTENTION_REQUIRED = "ATTENTION_REQUIRED"

    __str__ = str.__str__


PartnerEndCustomerOAuthInstitutionApplicationStatusOrStr: TypeAlias = Annotated[
    PartnerEndCustomerOAuthInstitutionApplicationStatus | str,
    open_enum_validator(PartnerEndCustomerOAuthInstitutionApplicationStatus),
]
