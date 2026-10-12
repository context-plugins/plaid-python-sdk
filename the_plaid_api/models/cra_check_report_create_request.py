from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cra_check_report_create_base_report_options import (
    CraCheckReportCreateBaseReportOptions,
    CraCheckReportCreateBaseReportOptionsDict,
)
from .cra_check_report_create_cashflow_insights_options import (
    CraCheckReportCreateCashflowInsightsOptions,
    CraCheckReportCreateCashflowInsightsOptionsDict,
)
from .cra_check_report_create_income_insights_options import (
    CraCheckReportCreateIncomeInsightsOptions,
    CraCheckReportCreateIncomeInsightsOptionsDict,
)
from .cra_check_report_create_lend_score_options import (
    CraCheckReportCreateLendScoreOptions,
    CraCheckReportCreateLendScoreOptionsDict,
)
from .cra_check_report_create_network_insights_options import (
    CraCheckReportCreateNetworkInsightsOptions,
    CraCheckReportCreateNetworkInsightsOptionsDict,
)
from .cra_check_report_create_partner_insights_options import (
    CraCheckReportCreatePartnerInsightsOptions,
    CraCheckReportCreatePartnerInsightsOptionsDict,
)
from .enums.consumer_report_permissible_purpose import ConsumerReportPermissiblePurposeOrStr
from .enums.products import ProductsOrStr


class CraCheckReportCreateRequest(SdkBaseModel):
    """CraCheckReportCreateRequest defines the request schema for ``/cra/check_report/create``."""

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

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    webhook: str
    """The destination URL to which webhooks will be sent"""

    days_requested: int
    """The number of days of data to request for the report. Default value is 365; maximum is 731; minimum is 180. If a
    value lower than 180 is provided, a minimum of 180 days of history will be requested."""

    days_required: Optional[int] = UNSET
    """The minimum number of days of data required for the report to be successfully generated."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    products: OptionalNullable[list[ProductsOrStr]] = UNSET
    """Specifies a list of products to generate when creating the report (in addition to the Base Report, which is
    always generated). These products will be made available before a success webhook is sent. Note that specifying
    ``cra_partner_insights`` in this field will trigger a billable event. Other products are not billed until the
    respective reports are retrieved via their product-specific ``/get`` endpoints."""

    base_report: OptionalNullable[CraCheckReportCreateBaseReportOptions] = UNSET
    """Defines configuration options to generate a Base Report"""

    cashflow_insights: OptionalNullable[CraCheckReportCreateCashflowInsightsOptions] = UNSET
    """Defines configuration options to generate Cashflow Insights"""

    partner_insights: OptionalNullable[CraCheckReportCreatePartnerInsightsOptions] = UNSET
    """Defines configuration to generate Partner Insights."""

    lend_score: OptionalNullable[CraCheckReportCreateLendScoreOptions] = UNSET
    """Defines configuration options to generate the LendScore"""

    network_insights: OptionalNullable[CraCheckReportCreateNetworkInsightsOptions] = UNSET
    """Defines configuration options to generate Network Insights"""

    include_investments: OptionalNullable[bool] = UNSET
    """Indicates that investment data should be extracted from the linked account(s)."""

    income_insights: OptionalNullable[CraCheckReportCreateIncomeInsightsOptions] = UNSET
    """Defines configuration options to generate Income Insights."""

    consumer_report_permissible_purpose: ConsumerReportPermissiblePurposeOrStr
    """Describes the reason you are generating a Consumer Report for this user. When calling ``/link/token/create``,
    this field is required when using Plaid Check (CRA) products; invalid if not using Plaid Check (CRA) products.

    ``ACCOUNT_REVIEW_CREDIT``: In connection with a consumer credit transaction for the review or collection of an
    account pursuant to FCRA Section 604(a)(3)(A).

    ``ACCOUNT_REVIEW_NON_CREDIT``: For a legitimate business need of the information to review a non-credit account
    provided primarily for personal, family, or household purposes to determine whether the consumer continues to meet
    the terms of the account pursuant to FCRA Section 604(a)(3)(F)(2).

    ``EXTENSION_OF_CREDIT``: In connection with a credit transaction initiated by and involving the consumer pursuant to
    FCRA Section 604(a)(3)(A).

    ``LEGITIMATE_BUSINESS_NEED_TENANT_SCREENING``: For a legitimate business need in connection with a business
    transaction initiated by the consumer primarily for personal, family, or household purposes in connection with a
    property rental assessment pursuant to FCRA Section 604(a)(3)(F)(i).

    ``LEGITIMATE_BUSINESS_NEED_OTHER``: For a legitimate business need in connection with a business transaction made
    primarily for personal, family, or household initiated by the consumer pursuant to FCRA Section 604(a)(3)(F)(i).

    ``WRITTEN_INSTRUCTION_PREQUALIFICATION``: In accordance with the written instructions of the consumer pursuant to
    FCRA Section 604(a)(2), to evaluate an application's profile to make an offer to the consumer.

    ``WRITTEN_INSTRUCTION_OTHER``: In accordance with the written instructions of the consumer pursuant to FCRA Section
    604(a)(2), such as when an individual agrees to act as a guarantor or assumes personal liability for a consumer,
    business, or commercial loan.

    ``ELIGIBILITY_FOR_GOVT_BENEFITS``: In connection with an eligibility determination for a government benefit where
    the entity is required to consider an applicant's financial status pursuant to FCRA Section 604(a)(3)(D)."""


class CraCheckReportCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    user_token: NotRequired[str]
    webhook: str
    days_requested: int
    days_required: NotRequired[int]
    client_report_id: NotRequired[str | None]
    products: NotRequired[list[ProductsOrStr] | None]
    base_report: NotRequired[CraCheckReportCreateBaseReportOptionsDict | None]
    cashflow_insights: NotRequired[CraCheckReportCreateCashflowInsightsOptionsDict | None]
    partner_insights: NotRequired[CraCheckReportCreatePartnerInsightsOptionsDict | None]
    lend_score: NotRequired[CraCheckReportCreateLendScoreOptionsDict | None]
    network_insights: NotRequired[CraCheckReportCreateNetworkInsightsOptionsDict | None]
    include_investments: NotRequired[bool | None]
    income_insights: NotRequired[CraCheckReportCreateIncomeInsightsOptionsDict | None]
    consumer_report_permissible_purpose: ConsumerReportPermissiblePurposeOrStr
