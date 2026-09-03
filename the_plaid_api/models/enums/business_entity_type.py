from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessEntityType(str, Enum):
    """The legal structure or type of business entity"""

    SOLE_PROPRIETORSHIP = "sole_proprietorship"
    GENERAL_PARTNERSHIP = "general_partnership"
    LLC = "llc"
    LLP = "llp"
    LLLP = "lllp"
    LP = "lp"
    C_CORPORATION = "c_corporation"
    S_CORPORATION = "s_corporation"
    B_CORPORATION = "b_corporation"
    NONPROFIT = "nonprofit"
    COOPERATIVE = "cooperative"
    TRUST = "trust"
    PROFESSIONAL_ASSOCIATION = "professional_association"
    PROFESSIONAL_CORPORATION = "professional_corporation"
    TRADE_NAME = "trade_name"
    BANK = "bank"
    CREDIT_UNION = "credit_union"
    INSURANCE = "insurance"
    OTHER = "other"
    UNKNOWN = "unknown"

    __str__ = str.__str__


BusinessEntityTypeOrStr: TypeAlias = Annotated[BusinessEntityType | str, open_enum_validator(BusinessEntityType)]
