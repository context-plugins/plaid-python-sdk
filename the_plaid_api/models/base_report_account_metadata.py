from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class BaseReportAccountMetadata(SdkBaseModel):
    """Metadata about the extracted account."""

    start_date: Date | None
    """The beginning of the range of the financial institution provided data for the account, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format ("yyyy-mm-dd")."""

    end_date: Date | None
    """The end of the range of the financial institution provided data for the account, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format ("yyyy-mm-dd")."""


class BaseReportAccountMetadataDict(TypedDict):
    start_date: Date | None
    end_date: Date | None
