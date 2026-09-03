from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .asset_report_user import AssetReportUser, AssetReportUserDict


class AssetReportRefreshRequestOptions(SdkBaseModel):
    """An optional object to filter ``/asset_report/refresh`` results. If provided, cannot be ``null``. If not
    specified, the ``options`` from the original call to ``/asset_report/create`` will be used."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    webhook: OptionalNullable[str] = UNSET
    """URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready."""

    user: Optional[AssetReportUser] = UNSET
    """The user object allows you to provide additional information about the user to be appended to the Asset Report.
    All fields are optional. The ``first_name``, ``last_name``, and ``ssn`` fields are required if you would like the
    Report to be eligible for Fannie Mae's Day 1 Certainty™ program."""


class AssetReportRefreshRequestOptionsDict(TypedDict):
    client_report_id: NotRequired[str | None]
    webhook: NotRequired[str | None]
    user: NotRequired[AssetReportUser | AssetReportUserDict]
