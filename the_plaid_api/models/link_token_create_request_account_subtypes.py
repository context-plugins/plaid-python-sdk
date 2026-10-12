from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_token_create_credit_filter import LinkTokenCreateCreditFilter, LinkTokenCreateCreditFilterDict
from .link_token_create_depository_filter import LinkTokenCreateDepositoryFilter, LinkTokenCreateDepositoryFilterDict
from .link_token_create_investment_filter import LinkTokenCreateInvestmentFilter, LinkTokenCreateInvestmentFilterDict
from .link_token_create_loan_filter import LinkTokenCreateLoanFilter, LinkTokenCreateLoanFilterDict


class LinkTokenCreateRequestAccountSubtypes(SdkBaseModel):
    """By default, Link will only display account types that are compatible with all products supplied in the
    ``products`` parameter of ``/link/token/create``. You can further limit the accounts shown in Link by using
    ``account_filters`` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown.
    This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions
    that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown,
    use the value ``"all"``. If the ``account_filters`` filter is used, any account type for which a filter is not
    specified will be entirely omitted from Link.

    For a full list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__.

    For institutions using OAuth, the filter will not affect the list of institutions or accounts shown by the bank in
    the OAuth window."""

    depository: Optional[LinkTokenCreateDepositoryFilter] = UNSET
    """A filter to apply to ``depository``-type accounts"""

    credit: Optional[LinkTokenCreateCreditFilter] = UNSET
    """A filter to apply to ``credit``-type accounts"""

    loan: Optional[LinkTokenCreateLoanFilter] = UNSET
    """A filter to apply to ``loan``-type accounts"""

    investment: Optional[LinkTokenCreateInvestmentFilter] = UNSET
    """A filter to apply to ``investment``-type accounts (or ``brokerage``-type accounts for API versions 2018-05-22 and
    earlier)."""


class LinkTokenCreateRequestAccountSubtypesDict(TypedDict):
    depository: NotRequired[LinkTokenCreateDepositoryFilterDict]
    credit: NotRequired[LinkTokenCreateCreditFilterDict]
    loan: NotRequired[LinkTokenCreateLoanFilterDict]
    investment: NotRequired[LinkTokenCreateInvestmentFilterDict]
