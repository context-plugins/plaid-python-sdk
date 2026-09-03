from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.investment_account_subtype import InvestmentAccountSubtypeOrStr


class InvestmentFilter(SdkBaseModel):
    """A filter to apply to ``investment``-type accounts (or ``brokerage``-type accounts for API versions 2018-05-22 and
    earlier)."""

    account_subtypes: list[InvestmentAccountSubtypeOrStr]
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""


class InvestmentFilterDict(TypedDict):
    account_subtypes: list[InvestmentAccountSubtypeOrStr]
