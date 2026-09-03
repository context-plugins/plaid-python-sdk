from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemRemoveReasonCode(str, Enum):
    """The reason for removing the Item

    ``FRAUD_FIRST_PARTY``: The end user who owns the connected bank account committed fraud ``FRAUD_FALSE_IDENTITY``:
    The end user created the connection using false identity information or stolen credentials ``FRAUD_ABUSE``: The end
    user is abusing the client's service or platform through their connected account ``FRAUD_OTHER``: Other
    fraud-related reasons involving the end user not covered by the specific fraud categories
    ``CONNECTION_IS_NON_FUNCTIONAL``: The connection to the end user's financial institution is broken and cannot be
    restored ``OTHER``: Any other reason for removing the connection not covered by the above categories"""

    FRAUD_FIRST_PARTY = "FRAUD_FIRST_PARTY"
    FRAUD_FALSE_IDENTITY = "FRAUD_FALSE_IDENTITY"
    FRAUD_ABUSE = "FRAUD_ABUSE"
    FRAUD_OTHER = "FRAUD_OTHER"
    CONNECTION_IS_NON_FUNCTIONAL = "CONNECTION_IS_NON_FUNCTIONAL"
    OTHER = "OTHER"

    __str__ = str.__str__


ItemRemoveReasonCodeOrStr: TypeAlias = Annotated[ItemRemoveReasonCode | str, open_enum_validator(ItemRemoveReasonCode)]
