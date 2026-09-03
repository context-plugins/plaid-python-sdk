from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class Application(SdkBaseModel):
    """Metadata about the application"""

    application_id: str
    """This field will map to the application ID that is returned from ``/item/application/list``, or provided to the
    institution in an oauth redirect."""

    name: str
    """The name of the application"""

    display_name: str | None
    """A human-readable name of the application for display purposes"""

    join_date: Date
    """The date this application was granted production access at Plaid in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format in UTC."""

    logo_url: str | None
    """A URL that links to the application logo image."""

    application_url: str | None
    """The URL for the application's website"""

    reason_for_access: str | None
    """A string provided by the connected app stating why they use their respective enabled products."""

    use_case: str | None
    """A string representing client's broad use case as assessed by Plaid."""

    company_legal_name: str | None
    """A string representing the name of client's legal entity."""

    city: str | None
    """A string representing the city of the client's headquarters."""

    region: str | None
    """A string representing the region of the client's headquarters."""

    postal_code: str | None
    """A string representing the postal code of the client's headquarters."""

    country_code: str | None
    """A string representing the country code of the client's headquarters."""


class ApplicationDict(TypedDict):
    application_id: str
    name: str
    display_name: str | None
    join_date: Date
    logo_url: str | None
    application_url: str | None
    reason_for_access: str | None
    use_case: str | None
    company_legal_name: str | None
    city: str | None
    region: str | None
    postal_code: str | None
    country_code: str | None
