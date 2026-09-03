from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AssetReportUser(SdkBaseModel):
    """The user object allows you to provide additional information about the user to be appended to the Asset Report.
    All fields are optional. The ``first_name``, ``last_name``, and ``ssn`` fields are required if you would like the
    Report to be eligible for Fannie Mae's Day 1 Certainty™ program."""

    client_user_id: OptionalNullable[str] = UNSET
    """An identifier you determine and submit for the user."""

    first_name: OptionalNullable[str] = UNSET
    """The user's first name. Required for the Fannie Mae Day 1 Certainty™ program."""

    middle_name: OptionalNullable[str] = UNSET
    """The user's middle name"""

    last_name: OptionalNullable[str] = UNSET
    """The user's last name. Required for the Fannie Mae Day 1 Certainty™ program."""

    ssn: OptionalNullable[str] = UNSET
    """The user's Social Security Number. Required for the Fannie Mae Day 1 Certainty™ program.

    Format: "ddd-dd-dddd"
    """

    phone_number: OptionalNullable[str] = UNSET
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567". Phone numbers
    provided in other formats will be parsed on a best-effort basis."""

    email: OptionalNullable[str] = UNSET
    """The user's email address."""


class AssetReportUserDict(TypedDict):
    client_user_id: NotRequired[str | None]
    first_name: NotRequired[str | None]
    middle_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    ssn: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    email: NotRequired[str | None]
