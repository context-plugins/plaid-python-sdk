from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_filter import CreditFilter, CreditFilterDict
from .depository_filter import DepositoryFilter, DepositoryFilterDict
from .investment_filter import InvestmentFilter, InvestmentFilterDict
from .loan_filter import LoanFilter, LoanFilterDict
from .other_filter import OtherFilter, OtherFilterDict


class LinkTokenAccountFilters(SdkBaseModel):
    """By default, Link will provide limited account filtering: it will only display Institutions that are compatible
    with all products supplied in the ``products`` parameter of ``/link/token/create``, and, if ``auth`` is specified in
    the ``products`` array, will also filter out accounts other than ``checking``, ``savings``, and ``cash management``
    accounts on the Account Select pane. You can further limit the accounts shown in Link by using ``account_filters``
    to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering
    applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not
    support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the
    value ``"all"``. If the ``account_filters`` filter is used, any account type for which a filter is not specified
    will be entirely omitted from Link. For a full list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__.

    The filter may or may not impact the list of accounts shown by the institution in the OAuth account selection flow,
    depending on the specific institution. If the user selects excluded account subtypes in the OAuth flow, these
    accounts will not be added to the Item. If the user selects only excluded account subtypes, the link attempt will
    fail and the user will be prompted to try again."""

    depository: Optional[DepositoryFilter] = UNSET
    """A filter to apply to ``depository``-type accounts"""

    credit: Optional[CreditFilter] = UNSET
    """A filter to apply to ``credit``-type accounts"""

    loan: Optional[LoanFilter] = UNSET
    """A filter to apply to ``loan``-type accounts"""

    investment: Optional[InvestmentFilter] = UNSET
    """A filter to apply to ``investment``-type accounts (or ``brokerage``-type accounts for API versions 2018-05-22 and
    earlier)."""

    other: Optional[OtherFilter] = UNSET
    """A filter to apply to ``other``-type accounts"""


class LinkTokenAccountFiltersDict(TypedDict):
    depository: NotRequired[DepositoryFilter | DepositoryFilterDict]
    credit: NotRequired[CreditFilter | CreditFilterDict]
    loan: NotRequired[LoanFilter | LoanFilterDict]
    investment: NotRequired[InvestmentFilter | InvestmentFilterDict]
    other: NotRequired[OtherFilter | OtherFilterDict]
