from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .beacon_account_risk_evaluate_account_attributes import (
    BeaconAccountRiskEvaluateAccountAttributes,
    BeaconAccountRiskEvaluateAccountAttributesDict,
)
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr


class BeaconAccountRiskEvaluateAccount(SdkBaseModel):
    """An account in the ``/beacon/account_risk/v1/evaluate`` response."""

    account_id: Optional[str] = UNSET
    """The account ID."""

    type_: Optional[AccountTypeOrStr] = Field(default=UNSET, alias="type")
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    subtype: OptionalNullable[AccountSubtypeOrStr] = UNSET
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    attributes: Optional[BeaconAccountRiskEvaluateAccountAttributes] = UNSET
    """The attributes object contains data that can be used to assess account risk. Examples of data include:
    ``days_since_first_plaid_connection``: The number of days since the first time the Item was connected to an
    application via Plaid ``plaid_connections_count_7d``: The number of times the Item has been connected to
    applications via Plaid over the past 7 days ``plaid_connections_count_30d``: The number of times the Item has been
    connected to applications via Plaid over the past 30 days ``total_plaid_connections_count``: The number of times the
    Item has been connected to applications via Plaid For the full list and detailed documentation of core attributes
    available, or to request that core attributes not be returned, contact sales or your Plaid account manager"""


class BeaconAccountRiskEvaluateAccountDict(TypedDict):
    account_id: NotRequired[str]
    type_: NotRequired[AccountTypeOrStr]
    subtype: NotRequired[AccountSubtypeOrStr | None]
    attributes: NotRequired[BeaconAccountRiskEvaluateAccountAttributes | BeaconAccountRiskEvaluateAccountAttributesDict]
