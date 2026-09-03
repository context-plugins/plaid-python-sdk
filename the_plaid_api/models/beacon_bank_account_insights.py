from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_account_risk_attributes import BeaconAccountRiskAttributes, BeaconAccountRiskAttributesDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr


class BeaconBankAccountInsights(SdkBaseModel):
    """Bank Account Insights encapsulate the risk insights for a single Bank Account linked to an Item that is
    associated with a Beacon User."""

    account_id: str
    """The Plaid ``account_id``"""

    type_: AccountTypeOrStr = Field(alias="type")
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    subtype: AccountSubtypeOrStr | None
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    attributes: BeaconAccountRiskAttributes
    """The attributes object contains data that can be used to assess account risk. Examples of data include:
    ``days_since_first_plaid_connection``: The number of days since the first time the Item was connected to an
    application via Plaid ``plaid_connections_count_7d``: The number of times the Item has been connected to
    applications via Plaid over the past 7 days ``plaid_connections_count_30d``: The number of times the Item has been
    connected to applications via Plaid over the past 30 days ``total_plaid_connections_count``: The number of times the
    Item has been connected to applications via Plaid For the full list and detailed documentation of core attributes
    available, or to request that core attributes not be returned, contact sales or your Plaid account manager"""


class BeaconBankAccountInsightsDict(TypedDict):
    account_id: str
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr | None
    attributes: BeaconAccountRiskAttributes | BeaconAccountRiskAttributesDict
