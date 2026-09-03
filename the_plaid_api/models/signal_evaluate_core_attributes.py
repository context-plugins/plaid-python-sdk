from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SignalEvaluateCoreAttributes(SdkBaseModel):
    """The core attributes object contains additional data that can be used to assess the ACH return risk.

    If using a Balance-only ruleset, only ``available_balance`` and ``current_balance`` will be returned as core
    attributes. If using a Signal Transaction Scores ruleset, over 80 core attributes will be returned. Examples of
    attributes include:

    ``available_balance`` and ``current_balance``: The balance in the ACH transaction funding account
    ``days_since_first_plaid_connection``: The number of days since the first time the Item was connected to an
    application via Plaid ``plaid_connections_count_7d``: The number of times the Item has been connected to
    applications via Plaid over the past 7 days ``plaid_connections_count_30d``: The number of times the Item has been
    connected to applications via Plaid over the past 30 days ``total_plaid_connections_count``: The number of times the
    Item has been connected to applications via Plaid ``is_savings_or_money_market_account``: Indicates whether the ACH
    transaction funding account is a savings/money market account

    For the full list and detailed documentation of core attributes available, or to request that core attributes not be
    returned, contact sales or your Plaid account manager."""

    unauthorized_transactions_count_7d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 7 days from the account that will be debited."""

    unauthorized_transactions_count_30d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 30 days from the account that will be debited."""

    unauthorized_transactions_count_60d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 60 days from the account that will be debited."""

    unauthorized_transactions_count_90d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 90 days from the account that will be debited."""

    nsf_overdraft_transactions_count_7d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 7 days from the account that will be debited."""

    nsf_overdraft_transactions_count_30d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 30 days from the account that will be debited."""

    nsf_overdraft_transactions_count_60d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 60 days from the account that will be debited."""

    nsf_overdraft_transactions_count_90d: OptionalNullable[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 90 days from the account that will be debited."""

    days_since_first_plaid_connection: OptionalNullable[int] = UNSET
    """The number of days since the first time the Item was connected to an application via Plaid"""

    plaid_connections_count_7d: OptionalNullable[int] = UNSET
    """The number of times the Item has been connected to applications via Plaid over the past 7 days"""

    plaid_connections_count_30d: OptionalNullable[int] = UNSET
    """The number of times the Item has been connected to applications via Plaid over the past 30 days"""

    total_plaid_connections_count: OptionalNullable[int] = UNSET
    """The total number of times the Item has been connected to applications via Plaid"""

    is_savings_or_money_market_account: OptionalNullable[bool] = UNSET
    """Indicates if the ACH transaction funding account is a savings/money market account"""

    total_credit_transactions_amount_10d: OptionalNullable[float] = UNSET
    """The total credit (inflow) transaction amount over the past 10 days from the account that will be debited"""

    total_debit_transactions_amount_10d: OptionalNullable[float] = UNSET
    """The total debit (outflow) transaction amount over the past 10 days from the account that will be debited"""

    p50_credit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    p50_debit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    p95_credit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    p95_debit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    days_with_negative_balance_count_90d: OptionalNullable[int] = UNSET
    """The number of days within the past 90 days when the account that will be debited had a negative end-of-day
    available balance"""

    p90_eod_balance_30d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be
    debited"""

    p90_eod_balance_60d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be
    debited"""

    p90_eod_balance_90d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be
    debited"""

    p10_eod_balance_30d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be
    debited"""

    p10_eod_balance_60d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be
    debited"""

    p10_eod_balance_90d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be
    debited"""

    available_balance: OptionalNullable[float] = UNSET
    """Available balance, as of the ``balance_last_updated`` time. The available balance is the current balance less any
    outstanding holds or debits that have not yet posted to the account."""

    current_balance: OptionalNullable[float] = UNSET
    """Current balance, as of the ``balance_last_updated`` time. The current balance is the total amount of funds in the
    account."""

    balance_last_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDTHH:mm:ssZ) indicating the last
    time that the balance for the given account has been updated."""

    phone_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's phone numbers on file have changed over the past 28 days"""

    phone_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's phone numbers on file have changed over the past 90 days"""

    email_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's email addresses on file have changed over the past 28 days"""

    email_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's email addresses on file have changed over the past 90 days"""

    address_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's addresses on file have changed over the past 28 days"""

    address_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's addresses on file have changed over the past 90 days"""

    plaid_non_oauth_authentication_attempts_count_3d: OptionalNullable[int] = UNSET
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""

    plaid_non_oauth_authentication_attempts_count_7d: OptionalNullable[int] = UNSET
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""

    plaid_non_oauth_authentication_attempts_count_30d: OptionalNullable[int] = UNSET
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""

    failed_plaid_non_oauth_authentication_attempts_count_3d: OptionalNullable[int] = UNSET
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""

    failed_plaid_non_oauth_authentication_attempts_count_7d: OptionalNullable[int] = UNSET
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""

    failed_plaid_non_oauth_authentication_attempts_count_30d: OptionalNullable[int] = UNSET
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""

    debit_transactions_count_10d: OptionalNullable[int] = UNSET
    """The total number of debit (outflow) transactions over the past 10 days from the account that will be debited"""

    credit_transactions_count_10d: OptionalNullable[int] = UNSET
    """The total number of credit (inflow) transactions over the past 10 days from the account that will be debited"""

    debit_transactions_count_30d: OptionalNullable[int] = UNSET
    """The total number of debit (outflow) transactions over the past 30 days from the account that will be debited"""

    credit_transactions_count_30d: OptionalNullable[int] = UNSET
    """The total number of credit (inflow) transactions over the past 30 days from the account that will be debited"""

    debit_transactions_count_60d: OptionalNullable[int] = UNSET
    """The total number of debit (outflow) transactions over the past 60 days from the account that will be debited"""

    credit_transactions_count_60d: OptionalNullable[int] = UNSET
    """The total number of credit (inflow) transactions over the past 60 days from the account that will be debited"""

    debit_transactions_count_90d: OptionalNullable[int] = UNSET
    """The total number of debit (outflow) transactions over the past 90 days from the account that will be debited"""

    credit_transactions_count_90d: OptionalNullable[int] = UNSET
    """The total number of credit (inflow) transactions over the past 90 days from the account that will be debited"""

    total_debit_transactions_amount_30d: OptionalNullable[float] = UNSET
    """The total debit (outflow) transaction amount over the past 30 days from the account that will be debited"""

    total_credit_transactions_amount_30d: OptionalNullable[float] = UNSET
    """The total credit (inflow) transaction amount over the past 30 days from the account that will be debited"""

    total_debit_transactions_amount_60d: OptionalNullable[float] = UNSET
    """The total debit (outflow) transaction amount over the past 60 days from the account that will be debited"""

    total_credit_transactions_amount_60d: OptionalNullable[float] = UNSET
    """The total credit (inflow) transaction amount over the past 60 days from the account that will be debited"""

    total_debit_transactions_amount_90d: OptionalNullable[float] = UNSET
    """The total debit (outflow) transaction amount over the past 90 days from the account that will be debited"""

    total_credit_transactions_amount_90d: OptionalNullable[float] = UNSET
    """The total credit (inflow) transaction amount over the past 90 days from the account that will be debited"""

    p50_eod_balance_30d: OptionalNullable[float] = UNSET
    """The 50th percentile of the end-of-day available balance over the past 30 days of the account that will be
    debited"""

    p50_eod_balance_60d: OptionalNullable[float] = UNSET
    """The 50th percentile of the end-of-day available balance over the past 60 days of the account that will be
    debited"""

    p50_eod_balance_90d: OptionalNullable[float] = UNSET
    """The 50th percentile of the end-of-day available balance over the past 90 days of the account that will be
    debited"""

    p50_eod_balance_31d_to_60d: OptionalNullable[float] = UNSET
    """The 50th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the
    account that will be debited"""

    p50_eod_balance_61d_to_90d: OptionalNullable[float] = UNSET
    """The 50th percentile of the end-of-day available balance between day 61 and day 90 over the past 90 days of the
    account that will be debited"""

    p90_eod_balance_31d_to_60d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the
    account that will be debited"""

    p90_eod_balance_61d_to_90d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance between day 61 and day 90 over the past 90 days of the
    account that will be debited"""

    p10_eod_balance_31d_to_60d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance between day 31 and day 60 over the past 60 days of the
    account that will be debited"""

    p10_eod_balance_61d_to_90d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance between day 61 and day 90 over the past 90 days of the
    account that will be debited"""

    transactions_last_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDTHH:mm:ssZ) indicating the last
    time that the transactions for the given account have been updated."""

    is_account_closed: OptionalNullable[bool] = UNSET
    """Indicates if the account that will be debited is closed"""

    is_account_frozen_or_restricted: OptionalNullable[bool] = UNSET
    """Indicates if the account that will be debited is either frozen or restricted"""

    distinct_ip_addresses_count_3d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 3
    days"""

    distinct_ip_addresses_count_7d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 7
    days"""

    distinct_ip_addresses_count_30d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 30
    days (max 100)"""

    distinct_ip_addresses_count_90d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 90
    days (max 100)"""

    distinct_user_agents_count_3d: OptionalNullable[int] = UNSET
    """The number of distinct user agents linked to the same bank account during Plaid authentication in the last 3
    days"""

    distinct_user_agents_count_7d: OptionalNullable[int] = UNSET
    """The number of distinct user agents linked to the same bank account during Plaid authentication in the last 7
    days"""

    distinct_user_agents_count_30d: OptionalNullable[int] = UNSET
    """The number of distinct user agents linked to the same bank account during Plaid authentication in the last 30
    days"""

    distinct_user_agents_count_90d: OptionalNullable[int] = UNSET
    """The number of distinct user agents linked to the same bank account during Plaid authentication in the last 90
    days"""

    distinct_ssl_tls_connection_sessions_count_3d: OptionalNullable[int] = UNSET
    """The number of distinct SSL/TLS connection sessions linked to the same bank account during Plaid authentication in
    the last 3 days"""

    distinct_ssl_tls_connection_sessions_count_7d: OptionalNullable[int] = UNSET
    """The number of distinct SSL/TLS connection sessions linked to the same bank account during Plaid authentication in
    the last 7 days"""

    distinct_ssl_tls_connection_sessions_count_30d: OptionalNullable[int] = UNSET
    """The number of distinct SSL/TLS connection sessions linked to the same bank account during Plaid authentication in
    the last 30 days"""

    distinct_ssl_tls_connection_sessions_count_90d: OptionalNullable[int] = UNSET
    """The number of distinct SSL/TLS connection sessions linked to the same bank account during Plaid authentication in
    the last 90 days"""

    days_since_account_opening: OptionalNullable[int] = UNSET
    """The number of days since the bank account was opened, as reported by the financial institution"""

    balance_to_transaction_amount_ratio: OptionalNullable[float] = UNSET
    """Taking ``available_or_current_balance`` and dividing it by the transaction amount. Useful to say "10% buffer",
    for example. This is a convenience function to build Signal Rules upon."""


class SignalEvaluateCoreAttributesDict(TypedDict):
    unauthorized_transactions_count_7d: NotRequired[int | None]
    unauthorized_transactions_count_30d: NotRequired[int | None]
    unauthorized_transactions_count_60d: NotRequired[int | None]
    unauthorized_transactions_count_90d: NotRequired[int | None]
    nsf_overdraft_transactions_count_7d: NotRequired[int | None]
    nsf_overdraft_transactions_count_30d: NotRequired[int | None]
    nsf_overdraft_transactions_count_60d: NotRequired[int | None]
    nsf_overdraft_transactions_count_90d: NotRequired[int | None]
    days_since_first_plaid_connection: NotRequired[int | None]
    plaid_connections_count_7d: NotRequired[int | None]
    plaid_connections_count_30d: NotRequired[int | None]
    total_plaid_connections_count: NotRequired[int | None]
    is_savings_or_money_market_account: NotRequired[bool | None]
    total_credit_transactions_amount_10d: NotRequired[float | None]
    total_debit_transactions_amount_10d: NotRequired[float | None]
    p50_credit_transactions_amount_28d: NotRequired[float | None]
    p50_debit_transactions_amount_28d: NotRequired[float | None]
    p95_credit_transactions_amount_28d: NotRequired[float | None]
    p95_debit_transactions_amount_28d: NotRequired[float | None]
    days_with_negative_balance_count_90d: NotRequired[int | None]
    p90_eod_balance_30d: NotRequired[float | None]
    p90_eod_balance_60d: NotRequired[float | None]
    p90_eod_balance_90d: NotRequired[float | None]
    p10_eod_balance_30d: NotRequired[float | None]
    p10_eod_balance_60d: NotRequired[float | None]
    p10_eod_balance_90d: NotRequired[float | None]
    available_balance: NotRequired[float | None]
    current_balance: NotRequired[float | None]
    balance_last_updated: NotRequired[RFC3339DateTime | None]
    phone_change_count_28d: NotRequired[int | None]
    phone_change_count_90d: NotRequired[int | None]
    email_change_count_28d: NotRequired[int | None]
    email_change_count_90d: NotRequired[int | None]
    address_change_count_28d: NotRequired[int | None]
    address_change_count_90d: NotRequired[int | None]
    plaid_non_oauth_authentication_attempts_count_3d: NotRequired[int | None]
    plaid_non_oauth_authentication_attempts_count_7d: NotRequired[int | None]
    plaid_non_oauth_authentication_attempts_count_30d: NotRequired[int | None]
    failed_plaid_non_oauth_authentication_attempts_count_3d: NotRequired[int | None]
    failed_plaid_non_oauth_authentication_attempts_count_7d: NotRequired[int | None]
    failed_plaid_non_oauth_authentication_attempts_count_30d: NotRequired[int | None]
    debit_transactions_count_10d: NotRequired[int | None]
    credit_transactions_count_10d: NotRequired[int | None]
    debit_transactions_count_30d: NotRequired[int | None]
    credit_transactions_count_30d: NotRequired[int | None]
    debit_transactions_count_60d: NotRequired[int | None]
    credit_transactions_count_60d: NotRequired[int | None]
    debit_transactions_count_90d: NotRequired[int | None]
    credit_transactions_count_90d: NotRequired[int | None]
    total_debit_transactions_amount_30d: NotRequired[float | None]
    total_credit_transactions_amount_30d: NotRequired[float | None]
    total_debit_transactions_amount_60d: NotRequired[float | None]
    total_credit_transactions_amount_60d: NotRequired[float | None]
    total_debit_transactions_amount_90d: NotRequired[float | None]
    total_credit_transactions_amount_90d: NotRequired[float | None]
    p50_eod_balance_30d: NotRequired[float | None]
    p50_eod_balance_60d: NotRequired[float | None]
    p50_eod_balance_90d: NotRequired[float | None]
    p50_eod_balance_31d_to_60d: NotRequired[float | None]
    p50_eod_balance_61d_to_90d: NotRequired[float | None]
    p90_eod_balance_31d_to_60d: NotRequired[float | None]
    p90_eod_balance_61d_to_90d: NotRequired[float | None]
    p10_eod_balance_31d_to_60d: NotRequired[float | None]
    p10_eod_balance_61d_to_90d: NotRequired[float | None]
    transactions_last_updated: NotRequired[RFC3339DateTime | None]
    is_account_closed: NotRequired[bool | None]
    is_account_frozen_or_restricted: NotRequired[bool | None]
    distinct_ip_addresses_count_3d: NotRequired[int | None]
    distinct_ip_addresses_count_7d: NotRequired[int | None]
    distinct_ip_addresses_count_30d: NotRequired[int | None]
    distinct_ip_addresses_count_90d: NotRequired[int | None]
    distinct_user_agents_count_3d: NotRequired[int | None]
    distinct_user_agents_count_7d: NotRequired[int | None]
    distinct_user_agents_count_30d: NotRequired[int | None]
    distinct_user_agents_count_90d: NotRequired[int | None]
    distinct_ssl_tls_connection_sessions_count_3d: NotRequired[int | None]
    distinct_ssl_tls_connection_sessions_count_7d: NotRequired[int | None]
    distinct_ssl_tls_connection_sessions_count_30d: NotRequired[int | None]
    distinct_ssl_tls_connection_sessions_count_90d: NotRequired[int | None]
    days_since_account_opening: NotRequired[int | None]
    balance_to_transaction_amount_ratio: NotRequired[float | None]
