from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class BeaconAccountRiskEvaluateAccountAttributes(SdkBaseModel):
    """The attributes object contains data that can be used to assess account risk. Examples of data include:
    ``days_since_first_plaid_connection``: The number of days since the first time the Item was connected to an
    application via Plaid ``plaid_connections_count_7d``: The number of times the Item has been connected to
    applications via Plaid over the past 7 days ``plaid_connections_count_30d``: The number of times the Item has been
    connected to applications via Plaid over the past 30 days ``total_plaid_connections_count``: The number of times the
    Item has been connected to applications via Plaid For the full list and detailed documentation of core attributes
    available, or to request that core attributes not be returned, contact sales or your Plaid account manager"""

    days_since_first_plaid_connection: OptionalNullable[int] = UNSET
    """The number of days since the first time the Item was connected to an application via Plaid"""

    is_account_closed: OptionalNullable[bool] = UNSET
    """Indicates if the account has been closed by the financial institution or the consumer, or is at risk of being
    closed"""

    is_account_frozen_or_restricted: OptionalNullable[bool] = UNSET
    """Indicates whether the account has withdrawals and transfers disabled or if access to the account is restricted.
    This could be due to a freeze by the credit issuer, legal restrictions (e.g., sanctions), or regulatory requirements
    limiting monthly withdrawals, among other reasons"""

    total_plaid_connections_count: OptionalNullable[int] = UNSET
    """The total number of times the item has been connected to applications via Plaid"""

    plaid_connections_count_7d: OptionalNullable[int] = UNSET
    """The number of times the Item has been connected to applications via Plaid over the past 7 days"""

    plaid_connections_count_30d: OptionalNullable[int] = UNSET
    """The number of times the Item has been connected to applications via Plaid over the past 30 days"""

    failed_plaid_non_oauth_authentication_attempts_count_3d: OptionalNullable[int] = UNSET
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""

    plaid_non_oauth_authentication_attempts_count_3d: OptionalNullable[int] = UNSET
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days"""

    failed_plaid_non_oauth_authentication_attempts_count_7d: OptionalNullable[int] = UNSET
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""

    plaid_non_oauth_authentication_attempts_count_7d: OptionalNullable[int] = UNSET
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days"""

    failed_plaid_non_oauth_authentication_attempts_count_30d: OptionalNullable[int] = UNSET
    """The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""

    plaid_non_oauth_authentication_attempts_count_30d: OptionalNullable[int] = UNSET
    """The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days"""

    distinct_ip_addresses_count_3d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 3
    days"""

    distinct_ip_addresses_count_7d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 7
    days"""

    distinct_ip_addresses_count_30d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 30
    days"""

    distinct_ip_addresses_count_90d: OptionalNullable[int] = UNSET
    """The number of distinct IP addresses linked to the same bank account during Plaid authentication in the last 90
    days"""

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

    address_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's addresses on file have changed over the past 28 days"""

    email_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's email addresses on file have changed over the past 28 days"""

    phone_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's phone numbers on file have changed over the past 28 days"""

    address_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's addresses on file have changed over the past 90 days"""

    email_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's email addresses on file have changed over the past 90 days"""

    phone_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's phone numbers on file have changed over the past 90 days"""

    days_since_account_opening: OptionalNullable[int] = UNSET
    """The number of days since the bank account was opened, as reported by the financial institution"""

    days_since_first_observed_transaction: OptionalNullable[int] = UNSET
    """The number of days since the oldest transaction available to Plaid for this account. This measure, combined with
    Plaid connection history, can be used to infer the age of the account"""


class BeaconAccountRiskEvaluateAccountAttributesDict(TypedDict):
    days_since_first_plaid_connection: NotRequired[int | None]
    is_account_closed: NotRequired[bool | None]
    is_account_frozen_or_restricted: NotRequired[bool | None]
    total_plaid_connections_count: NotRequired[int | None]
    plaid_connections_count_7d: NotRequired[int | None]
    plaid_connections_count_30d: NotRequired[int | None]
    failed_plaid_non_oauth_authentication_attempts_count_3d: NotRequired[int | None]
    plaid_non_oauth_authentication_attempts_count_3d: NotRequired[int | None]
    failed_plaid_non_oauth_authentication_attempts_count_7d: NotRequired[int | None]
    plaid_non_oauth_authentication_attempts_count_7d: NotRequired[int | None]
    failed_plaid_non_oauth_authentication_attempts_count_30d: NotRequired[int | None]
    plaid_non_oauth_authentication_attempts_count_30d: NotRequired[int | None]
    distinct_ip_addresses_count_3d: NotRequired[int | None]
    distinct_ip_addresses_count_7d: NotRequired[int | None]
    distinct_ip_addresses_count_30d: NotRequired[int | None]
    distinct_ip_addresses_count_90d: NotRequired[int | None]
    distinct_user_agents_count_3d: NotRequired[int | None]
    distinct_user_agents_count_7d: NotRequired[int | None]
    distinct_user_agents_count_30d: NotRequired[int | None]
    distinct_user_agents_count_90d: NotRequired[int | None]
    address_change_count_28d: NotRequired[int | None]
    email_change_count_28d: NotRequired[int | None]
    phone_change_count_28d: NotRequired[int | None]
    address_change_count_90d: NotRequired[int | None]
    email_change_count_90d: NotRequired[int | None]
    phone_change_count_90d: NotRequired[int | None]
    days_since_account_opening: NotRequired[int | None]
    days_since_first_observed_transaction: NotRequired[int | None]
