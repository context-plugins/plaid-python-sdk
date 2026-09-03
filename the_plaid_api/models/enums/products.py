from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Products(str, Enum):
    """A list of products that an institution can support. All Items must be initialized with at least one product. The
    Balance product is always available and does not need to be specified during initialization."""

    ASSETS = "assets"
    AUTH = "auth"
    BALANCE = "balance"
    BALANCE_PLUS = "balance_plus"
    BEACON = "beacon"
    IDENTITY = "identity"
    IDENTITY_MATCH = "identity_match"
    INVESTMENTS = "investments"
    INVESTMENTS_AUTH = "investments_auth"
    LIABILITIES = "liabilities"
    PAYMENT_INITIATION = "payment_initiation"
    IDENTITY_VERIFICATION = "identity_verification"
    TRANSACTIONS = "transactions"
    CREDIT_DETAILS = "credit_details"
    INCOME = "income"
    INCOME_VERIFICATION = "income_verification"
    STANDING_ORDERS = "standing_orders"
    TRANSFER = "transfer"
    EMPLOYMENT = "employment"
    RECURRING_TRANSACTIONS = "recurring_transactions"
    TRANSACTIONS_REFRESH = "transactions_refresh"
    SIGNAL = "signal"
    STATEMENTS = "statements"
    PROCESSOR_PAYMENTS = "processor_payments"
    PROCESSOR_IDENTITY = "processor_identity"
    PROFILE = "profile"
    CRA_BASE_REPORT = "cra_base_report"
    CRA_INCOME_INSIGHTS = "cra_income_insights"
    CRA_PARTNER_INSIGHTS = "cra_partner_insights"
    CRA_NETWORK_INSIGHTS = "cra_network_insights"
    CRA_CASHFLOW_INSIGHTS = "cra_cashflow_insights"
    CRA_MONITORING = "cra_monitoring"
    CRA_LEND_SCORE = "cra_lend_score"
    CRA_PLAID_CREDIT_SCORE = "cra_plaid_credit_score"
    CRA_QUALIFY = "cra_qualify"
    LAYER = "layer"
    PAY_BY_BANK = "pay_by_bank"
    PROTECT_LINKED_BANK = "protect_linked_bank"
    PROTECT_TRANSACTIONS = "protect_transactions"

    __str__ = str.__str__


ProductsOrStr: TypeAlias = Annotated[Products | str, open_enum_validator(Products)]
