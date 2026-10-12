from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.credit_bank_income_category import CreditBankIncomeCategoryOrStr


class CraMonitoringInsightsSubscribeRequest(SdkBaseModel):
    """CraMonitoringInsightsSubscribeRequest defines the request schema for ``/cra/monitoring_insights/subscribe``"""

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

    item_id: Optional[str] = UNSET
    """The Item ID to subscribe for Cash Flow Updates."""

    webhook: str
    """URL to which Plaid will send Cash Flow Updates webhooks, for example when the requested Cash Flow Updates report
    is ready."""

    income_categories: OptionalNullable[list[CreditBankIncomeCategoryOrStr]] = UNSET
    """Income categories to include in Cash Flow Updates. If empty or ``null``, this field will default to including all
    possible categories."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""


class CraMonitoringInsightsSubscribeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    item_id: NotRequired[str]
    webhook: str
    income_categories: NotRequired[list[CreditBankIncomeCategoryOrStr] | None]
    user_token: NotRequired[str]
