from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class CraPartnerInsightsItemAccountMetadata(SdkBaseModel):
    """An object containing metadata about the extracted account."""

    start_date: Date | None
    """The date of the earliest extracted transaction, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    end_date: Date | None
    """The date of the most recent extracted transaction, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""


class CraPartnerInsightsItemAccountMetadataDict(TypedDict):
    start_date: Date | None
    end_date: Date | None
