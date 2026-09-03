from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.cra_check_report_permissible_purpose import CraCheckReportPermissiblePurposeOrStr
from .enums.cra_user_tier import CraUserTierOrStr


class CraCheckReportBaseReportGetRequest(SdkBaseModel):
    """CraCheckReportBaseReportGetRequest defines the request schema for ``/cra/check_report/base_report/get``"""

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

    item_ids: Optional[list[str | None]] = UNSET
    """The Item IDs to include in the Base Report. If not provided, all Items associated with the user will be
    included."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    user_tier: OptionalNullable[CraUserTierOrStr] = UNSET
    """The tier of the user."""

    report_id: Optional[str] = UNSET
    """The CRA report token (formatted ``cra-report-<env>-<uuid>``) identifying a specific consumer report. When
    provided alongside ``consumer_report_permissible_purpose``, pins retrieval to that report and stamps its permissible
    purpose. If omitted, the most recently generated report for the user is returned."""

    consumer_report_permissible_purpose: Optional[CraCheckReportPermissiblePurposeOrStr] = UNSET


class CraCheckReportBaseReportGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    third_party_user_token: NotRequired[str]
    item_ids: NotRequired[list[str | None]]
    user_token: NotRequired[str]
    user_tier: NotRequired[CraUserTierOrStr | None]
    report_id: NotRequired[str]
    consumer_report_permissible_purpose: NotRequired[CraCheckReportPermissiblePurposeOrStr]
