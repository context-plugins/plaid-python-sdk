from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .scopes_nullable import ScopesNullable, ScopesNullableDict


class ConnectedApplication(SdkBaseModel):
    """Describes the connected application for a particular end user."""

    application_id: str
    """This field will map to the application ID that is returned from ``/item/application/list``, or provided to the
    institution in an oauth redirect."""

    name: str
    """The name of the application"""

    display_name: OptionalNullable[str] = UNSET
    """A human-readable name of the application for display purposes"""

    logo_url: OptionalNullable[str] = UNSET
    """A URL that links to the application logo image."""

    application_url: OptionalNullable[str] = UNSET
    """The URL for the application's website"""

    reason_for_access: OptionalNullable[str] = UNSET
    """A string provided by the connected app stating why they use their respective enabled products."""

    created_at: RFC3339DateTime
    """The date and time this application was linked, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format in
    UTC (e.g. ``"2020-01-01T00:00:00Z"``). Note that older, legacy integrations instead receive this value as a date
    only, in ``YYYY-MM-DD`` format (e.g. ``"2020-01-01"``)."""

    scopes: OptionalNullable[ScopesNullable] = UNSET
    """The scopes object"""


class ConnectedApplicationDict(TypedDict):
    application_id: str
    name: str
    display_name: NotRequired[str | None]
    logo_url: NotRequired[str | None]
    application_url: NotRequired[str | None]
    reason_for_access: NotRequired[str | None]
    created_at: RFC3339DateTime
    scopes: NotRequired[ScopesNullable | ScopesNullableDict | None]
