from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type2(str, Enum):
    """The status type of the student loan"""

    CANCELLED = "cancelled"
    CHARGED_OFF = "charged off"
    CLAIM = "claim"
    CONSOLIDATED = "consolidated"
    DEFERMENT = "deferment"
    DELINQUENT = "delinquent"
    DISCHARGED = "discharged"
    EXTENSION = "extension"
    FORBEARANCE = "forbearance"
    IN_GRACE = "in grace"
    IN_MILITARY = "in military"
    IN_SCHOOL = "in school"
    NOT_FULLY_DISBURSED = "not fully disbursed"
    OTHER = "other"
    PAID_IN_FULL = "paid in full"
    REFUNDED = "refunded"
    REPAYMENT = "repayment"
    TRANSFERRED = "transferred"
    PENDING_IDR = "pending idr"

    __str__ = str.__str__


Type2OrStr: TypeAlias = Annotated[Type2 | str, open_enum_validator(Type2)]
