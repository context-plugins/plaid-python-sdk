from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cra_check_report_verification_get_employment_refresh_options import (
    CraCheckReportVerificationGetEmploymentRefreshOptions,
    CraCheckReportVerificationGetEmploymentRefreshOptionsDict,
)
from .enums.cra_check_report_verification_get_report_type import CraCheckReportVerificationGetReportTypeOrStr


class CraCheckReportVerificationGetRequest(SdkBaseModel):
    """CraCheckReportVerificationGetRequest defines the request schema for ``/cra/check_report/verification/get``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    reports_requested: list[CraCheckReportVerificationGetReportTypeOrStr]
    """Specifies which types of home lending reports are expected in the response"""

    employment_refresh_options: OptionalNullable[CraCheckReportVerificationGetEmploymentRefreshOptions] = UNSET
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``employment_refresh_options``."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class CraCheckReportVerificationGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    reports_requested: list[CraCheckReportVerificationGetReportTypeOrStr]
    employment_refresh_options: NotRequired[CraCheckReportVerificationGetEmploymentRefreshOptionsDict | None]
    user_token: NotRequired[str]
