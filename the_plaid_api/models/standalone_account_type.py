from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.credit_account import CreditAccountOrStr
from .enums.depository_account import DepositoryAccountOrStr
from .enums.investment_account_subtype1 import InvestmentAccountSubtype1OrStr
from .enums.loan_account import LoanAccountOrStr
from .enums.payroll_account import PayrollAccountOrStr


class StandaloneAccountType(SdkBaseModel):
    """The schema below describes the various ``types`` and corresponding ``subtypes`` that Plaid recognizes and reports
    for financial institution accounts. For a mapping of supported types and subtypes to Plaid products, see the
    `Account type / product support matrix
    <https://plaid.com/docs/api/accounts/#account-type--product-support-matrix>`__."""

    depository: DepositoryAccountOrStr
    """An account type holding cash, in which funds are deposited."""

    credit: CreditAccountOrStr
    """A credit card type account."""

    loan: LoanAccountOrStr
    """A loan type account."""

    investment: InvestmentAccountSubtype1OrStr
    """An investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``."""

    payroll: Optional[PayrollAccountOrStr] = UNSET
    """A payroll account."""

    other: str
    """Other or unknown account type."""


class StandaloneAccountTypeDict(TypedDict):
    depository: DepositoryAccountOrStr
    credit: CreditAccountOrStr
    loan: LoanAccountOrStr
    investment: InvestmentAccountSubtype1OrStr
    payroll: NotRequired[PayrollAccountOrStr]
    other: str
