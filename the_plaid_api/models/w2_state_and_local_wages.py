from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class W2StateAndLocalWages(SdkBaseModel):
    """W2 state and local wages"""

    state: OptionalNullable[str] = UNSET
    """State associated with the wage."""

    employer_state_id_number: OptionalNullable[str] = UNSET
    """State identification number of the employer."""

    state_wages_tips: OptionalNullable[str] = UNSET
    """Wages and tips from the specified state."""

    state_income_tax: OptionalNullable[str] = UNSET
    """Income tax from the specified state."""

    local_wages_tips: OptionalNullable[str] = UNSET
    """Wages and tips from the locality."""

    local_income_tax: OptionalNullable[str] = UNSET
    """Income tax from the locality."""

    locality_name: OptionalNullable[str] = UNSET
    """Name of the locality."""


class W2StateAndLocalWagesDict(TypedDict):
    state: NotRequired[str | None]
    employer_state_id_number: NotRequired[str | None]
    state_wages_tips: NotRequired[str | None]
    state_income_tax: NotRequired[str | None]
    local_wages_tips: NotRequired[str | None]
    local_income_tax: NotRequired[str | None]
    locality_name: NotRequired[str | None]
