from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class LinkTokenCreateRequestBaseReport(SdkBaseModel):
    """Specifies options for initializing Link for use with the Base Report product. This field is required if
    ``assets`` is included in the ``products`` array and the client is CRA-enabled."""

    days_requested: int
    """The maximum integer number of days of history to include in the Base Report."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""


class LinkTokenCreateRequestBaseReportDict(TypedDict):
    days_requested: int
    client_report_id: NotRequired[str | None]
