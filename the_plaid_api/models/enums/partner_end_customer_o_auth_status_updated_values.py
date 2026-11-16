from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerOAuthStatusUpdatedValues(str, Enum):
    """The OAuth status of the update"""

    NOT_STARTED = "not-started"
    PROCESSING = "processing"
    APPROVED = "approved"
    ENABLED = "enabled"
    ATTENTION_REQUIRED = "attention-required"

    __str__ = str.__str__


PartnerEndCustomerOAuthStatusUpdatedValuesOrStr: TypeAlias = Annotated[
    PartnerEndCustomerOAuthStatusUpdatedValues | str, open_enum_validator(PartnerEndCustomerOAuthStatusUpdatedValues)
]
