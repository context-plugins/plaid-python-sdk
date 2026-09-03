from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AddressPurposeLabel(str, Enum):
    """Field describing whether the associated address is being used for commercial or residential purposes.

    Note: This value will be ``no_data`` when Plaid does not have sufficient data to determine the address's use."""

    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    NO_DATA = "no_data"

    __str__ = str.__str__


AddressPurposeLabelOrStr: TypeAlias = Annotated[AddressPurposeLabel | str, open_enum_validator(AddressPurposeLabel)]
