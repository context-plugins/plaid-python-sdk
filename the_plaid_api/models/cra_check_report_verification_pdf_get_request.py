from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cra_check_report_verification_pdf_report_type import CraCheckReportVerificationPdfReportTypeOrStr


class CraCheckReportVerificationPdfGetRequest(SdkBaseModel):
    """CraCheckReportVerificationPdfGetRequest defines the request schema for
    ``/cra/check_report/verification/pdf/get``."""

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

    third_party_user_token: Optional[str] = UNSET
    """The third-party user token associated with the requested User data."""

    report_requested: Optional[CraCheckReportVerificationPdfReportTypeOrStr] = UNSET
    reports_requested: Optional[list[CraCheckReportVerificationPdfReportTypeOrStr]] = UNSET
    """Specifies which types of verification reports to include in the returned PDF. Supported combinations are:
    ``[voa]``, ``[employment_refresh]``, ``[income]``, or ``[voa, income]``. Other combinations are not supported."""

    hide_gse_details: Optional[bool] = UNSET
    """If ``true``, the GSE identifiers (the Report ID and ``gse_reference_id``) are omitted from the returned Home
    Lending Report PDF. Defaults to ``false``. These identifiers are always present in the
    ``/cra/check_report/verification/get`` JSON response regardless of this field."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class CraCheckReportVerificationPdfGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    third_party_user_token: NotRequired[str]
    report_requested: NotRequired[CraCheckReportVerificationPdfReportTypeOrStr]
    reports_requested: NotRequired[list[CraCheckReportVerificationPdfReportTypeOrStr]]
    hide_gse_details: NotRequired[bool]
    user_token: NotRequired[str]
