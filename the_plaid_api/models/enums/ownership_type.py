from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OwnershipType(str, Enum):
    """How an asset is owned.

    ``association``: Ownership by a corporation, partnership, or unincorporated association, including for-profit and
    not-for-profit organizations. ``individual``: Ownership by an individual. ``joint``: Joint ownership by multiple
    parties. ``trust``: Ownership by a revocable or irrevocable trust."""

    INDIVIDUAL = "individual"
    JOINT = "joint"
    ASSOCIATION = "association"
    TRUST = "trust"

    __str__ = str.__str__


OwnershipTypeOrStr: TypeAlias = Annotated[OwnershipType | str, open_enum_validator(OwnershipType)]
