from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_report_get_report import CraReportGetReport, CraReportGetReportDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraReportGetResponse(SdkBaseModel):
    """CraReportGetResponse defines the response schema for ``/cra/report/get``."""

    report: CraReportGetReport
    """The CRA report returned by ``/cra/report/get``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    user_id: str
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    warnings: list[CraReportWarning]
    """User or report-level errors that affected the overall report but do not map to a specific product failure."""


class CraReportGetResponseDict(TypedDict):
    report: CraReportGetReport | CraReportGetReportDict
    request_id: str
    user_id: str
    warnings: list[CraReportWarning | CraReportWarningDict]
