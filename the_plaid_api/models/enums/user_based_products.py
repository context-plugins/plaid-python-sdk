from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UserBasedProducts(str, Enum):
    """A list of user-based products. User-based products include Financial Management products, Protect products, CRA
    products, and subscription products."""

    CRA_BASE_REPORT = "cra_base_report"
    CRA_INCOME_INSIGHTS = "cra_income_insights"
    CRA_PARTNER_INSIGHTS = "cra_partner_insights"
    CRA_NETWORK_INSIGHTS = "cra_network_insights"
    CRA_CASHFLOW_INSIGHTS = "cra_cashflow_insights"
    CRA_MONITORING = "cra_monitoring"
    CRA_LEND_SCORE = "cra_lend_score"
    CRA_PLAID_CREDIT_SCORE = "cra_plaid_credit_score"
    INVESTMENTS = "investments"
    LIABILITIES = "liabilities"
    PROTECT_LINKED_BANK = "protect_linked_bank"
    PROTECT_TRANSACTIONS = "protect_transactions"
    TRANSACTIONS = "transactions"

    __str__ = str.__str__


UserBasedProductsOrStr: TypeAlias = Annotated[UserBasedProducts | str, open_enum_validator(UserBasedProducts)]
