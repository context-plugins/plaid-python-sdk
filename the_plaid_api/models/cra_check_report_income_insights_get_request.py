from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cra_check_report_income_insights_get_options import (
    CraCheckReportIncomeInsightsGetOptions,
    CraCheckReportIncomeInsightsGetOptionsDict,
)
from .enums.cra_check_report_permissible_purpose import CraCheckReportPermissiblePurposeOrStr


class CraCheckReportIncomeInsightsGetRequest(SdkBaseModel):
    """Defines the request schema for ``/cra/check_report/income_insights/get``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    third_party_user_token: Optional[str] = UNSET
    """The third-party user token associated with the requested User data."""

    user_id: Optional[str] = UNSET
    """A unique user identifier, created by ``/user/create``. Integrations that began using ``/user/create`` after
    December 10, 2025 use this field to identify a user instead of the ``user_token``. For more details, see `New User
    APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    options: OptionalNullable[CraCheckReportIncomeInsightsGetOptions] = UNSET
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``options``."""

    report_id: Optional[str] = UNSET
    """The CRA report token (formatted ``cra-report-<env>-<uuid>``) identifying a specific consumer report. When
    provided alongside ``consumer_report_permissible_purpose``, pins retrieval to that report and stamps its permissible
    purpose. If omitted, the most recently generated report for the user is returned."""

    consumer_report_permissible_purpose: Optional[CraCheckReportPermissiblePurposeOrStr] = UNSET


class CraCheckReportIncomeInsightsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_token: NotRequired[str]
    third_party_user_token: NotRequired[str]
    user_id: NotRequired[str]
    options: NotRequired[CraCheckReportIncomeInsightsGetOptionsDict | None]
    report_id: NotRequired[str]
    consumer_report_permissible_purpose: NotRequired[CraCheckReportPermissiblePurposeOrStr]
