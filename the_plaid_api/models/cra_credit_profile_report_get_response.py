from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_credit_profile_report import CraCreditProfileReport, CraCreditProfileReportDict
from .cra_report_warning import CraReportWarning, CraReportWarningDict


class CraCreditProfileReportGetResponse(SdkBaseModel):
    """CraCreditProfileReportGetResponse defines the response schema for ``/cra/credit_profile/report/get``."""

    report: CraCreditProfileReport
    """Contains data for the CRA Credit Profile Report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    warnings: list[CraReportWarning]
    """If the report generation was successful but a subset of data could not be retrieved, this array will contain
    information about the errors causing information to be missing"""


class CraCreditProfileReportGetResponseDict(TypedDict):
    report: CraCreditProfileReportDict
    request_id: str
    user_id: NotRequired[str]
    warnings: list[CraReportWarningDict]
