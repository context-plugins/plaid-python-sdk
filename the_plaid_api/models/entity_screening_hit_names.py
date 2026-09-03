from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.weak_alias_determination import WeakAliasDeterminationOrStr


class EntityScreeningHitNames(SdkBaseModel):
    """Name information for the associated entity watchlist hit"""

    full: str
    """The full name of the entity."""

    is_primary: bool
    """Primary names are those most commonly used to refer to this entity. Only one name will ever be marked as
    primary."""

    weak_alias_determination: WeakAliasDeterminationOrStr
    """Names that are explicitly marked as low quality either by their ``source`` list, or by ``plaid`` by a series of
    additional checks done by Plaid. Plaid does not ever surface a hit as a result of a weak name alone. If a name has
    no quality issues, this value will be ``none``."""


class EntityScreeningHitNamesDict(TypedDict):
    full: str
    is_primary: bool
    weak_alias_determination: WeakAliasDeterminationOrStr
