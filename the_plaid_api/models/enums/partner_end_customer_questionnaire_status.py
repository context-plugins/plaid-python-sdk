from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerQuestionnaireStatus(str, Enum):
    """The status of the end customer's security questionnaire."""

    NOT_STARTED = "NOT_STARTED"
    RECEIVED = "RECEIVED"
    COMPLETE = "COMPLETE"

    __str__ = str.__str__


PartnerEndCustomerQuestionnaireStatusOrStr: TypeAlias = Annotated[
    PartnerEndCustomerQuestionnaireStatus | str, open_enum_validator(PartnerEndCustomerQuestionnaireStatus)
]
