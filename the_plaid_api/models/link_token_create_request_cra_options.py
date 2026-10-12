from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .link_token_create_request_cra_options_base_report import (
    LinkTokenCreateRequestCraOptionsBaseReport,
    LinkTokenCreateRequestCraOptionsBaseReportDict,
)
from .link_token_create_request_cra_options_cashflow_insights import (
    LinkTokenCreateRequestCraOptionsCashflowInsights,
    LinkTokenCreateRequestCraOptionsCashflowInsightsDict,
)
from .link_token_create_request_cra_options_income_insights import (
    LinkTokenCreateRequestCraOptionsIncomeInsights,
    LinkTokenCreateRequestCraOptionsIncomeInsightsDict,
)
from .link_token_create_request_cra_options_lend_score import (
    LinkTokenCreateRequestCraOptionsLendScore,
    LinkTokenCreateRequestCraOptionsLendScoreDict,
)
from .link_token_create_request_cra_options_network_insights import (
    LinkTokenCreateRequestCraOptionsNetworkInsights,
    LinkTokenCreateRequestCraOptionsNetworkInsightsDict,
)
from .link_token_create_request_cra_options_partner_insights import (
    LinkTokenCreateRequestCraOptionsPartnerInsights,
    LinkTokenCreateRequestCraOptionsPartnerInsightsDict,
)


class LinkTokenCreateRequestCraOptions(SdkBaseModel):
    """Specifies options for initializing Link for use with Plaid Check products"""

    days_requested: int
    """The number of days of history to include in Plaid Check products. Maximum is 731; minimum is 180. If a value
    lower than 180 is provided, a minimum of 180 days of history will be requested."""

    days_required: Optional[int] = UNSET
    """The minimum number of days of data required for the report to be successfully generated."""

    client_report_id: OptionalNullable[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    partner_insights: Optional[LinkTokenCreateRequestCraOptionsPartnerInsights] = UNSET
    """Specifies options for initializing Link for use with the Credit Partner Insights product."""

    base_report: Optional[LinkTokenCreateRequestCraOptionsBaseReport] = UNSET
    """Specifies options for initializing Link for use with the Base Report product, specifically the
    ``client_report_id``."""

    cashflow_insights: Optional[LinkTokenCreateRequestCraOptionsCashflowInsights] = UNSET
    """Specifies options for initializing Link for use with the Cashflow Insights product."""

    lend_score: Optional[LinkTokenCreateRequestCraOptionsLendScore] = UNSET
    """Specifies options for initializing Link for use with the CRA LendScore product."""

    network_insights: Optional[LinkTokenCreateRequestCraOptionsNetworkInsights] = UNSET
    """Specifies options for initializing Link for use with the CRA Network Insights product."""

    include_investments: OptionalNullable[bool] = UNSET
    """Indicates that investment data should be extracted from the linked account(s)."""

    income_insights: Optional[LinkTokenCreateRequestCraOptionsIncomeInsights] = UNSET
    """Specifies options for initializing Link for use with the CRA Income Insights product."""


class LinkTokenCreateRequestCraOptionsDict(TypedDict):
    days_requested: int
    days_required: NotRequired[int]
    client_report_id: NotRequired[str | None]
    partner_insights: NotRequired[LinkTokenCreateRequestCraOptionsPartnerInsightsDict]
    base_report: NotRequired[LinkTokenCreateRequestCraOptionsBaseReportDict]
    cashflow_insights: NotRequired[LinkTokenCreateRequestCraOptionsCashflowInsightsDict]
    lend_score: NotRequired[LinkTokenCreateRequestCraOptionsLendScoreDict]
    network_insights: NotRequired[LinkTokenCreateRequestCraOptionsNetworkInsightsDict]
    include_investments: NotRequired[bool | None]
    income_insights: NotRequired[LinkTokenCreateRequestCraOptionsIncomeInsightsDict]
