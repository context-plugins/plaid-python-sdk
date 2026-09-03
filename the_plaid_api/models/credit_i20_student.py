from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel


class CreditI20Student(SdkBaseModel):
    """An object representing the student named on a Form I-20."""

    given_name: OptionalNullable[str] = UNSET
    """Given name of the student."""

    surname_primary_name: OptionalNullable[str] = UNSET
    """Surname or primary name of the student."""

    passport_name: OptionalNullable[str] = UNSET
    """Name of the student as it appears on their passport."""

    preferred_name: OptionalNullable[str] = UNSET
    """Preferred name of the student."""

    school_name: OptionalNullable[str] = UNSET
    """Name of the school issuing the Form I-20."""

    program_start_date: OptionalNullable[Date] = UNSET
    """Start date of the program in ISO 8601 format (YYYY-MM-DD)."""

    program_end_date: OptionalNullable[Date] = UNSET
    """End date of the program in ISO 8601 format (YYYY-MM-DD)."""


class CreditI20StudentDict(TypedDict):
    given_name: NotRequired[str | None]
    surname_primary_name: NotRequired[str | None]
    passport_name: NotRequired[str | None]
    preferred_name: NotRequired[str | None]
    school_name: NotRequired[str | None]
    program_start_date: NotRequired[Date | None]
    program_end_date: NotRequired[Date | None]
