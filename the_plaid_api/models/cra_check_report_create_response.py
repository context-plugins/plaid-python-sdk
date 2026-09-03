from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CraCheckReportCreateResponse(SdkBaseModel):
    """CraCheckReportCreateResponse defines the response schema for ``/cra/check_report/create``."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CraCheckReportCreateResponseDict(TypedDict):
    request_id: NotRequired[str]
