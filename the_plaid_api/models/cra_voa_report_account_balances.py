from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_voa_report_account_historical_balance import (
    CraVoaReportAccountHistoricalBalance,
    CraVoaReportAccountHistoricalBalanceDict,
)


class CraVoaReportAccountBalances(SdkBaseModel):
    """VOA Report information about an account's balances."""

    available: float | None
    """The amount of funds available to be withdrawn from the account, as determined by the financial institution.

    For ``credit``-type accounts, the ``available`` balance typically equals the ``limit`` less the ``current`` balance,
    less any pending outflows plus any pending inflows.

    For ``depository``-type accounts, the ``available`` balance typically equals the ``current`` balance less any
    pending outflows plus any pending inflows. For ``depository``-type accounts, the ``available`` balance does not
    include the overdraft limit.

    For ``investment``-type accounts (or ``brokerage``-type accounts for API versions 2018-05-22 and earlier), the
    ``available`` balance is the total cash available to withdraw as presented by the institution.

    Note that not all institutions calculate the ``available`` balance. In the event that ``available`` balance is
    unavailable, Plaid will return an ``available`` balance value of ``null``.

    Available balance may be cached and is not guaranteed to be up-to-date in real-time unless the value was returned by
    ``/accounts/balance/get``.

    If ``current`` is ``null`` this field is guaranteed not to be ``null``."""

    current: float | None
    """The total amount of funds in or owed by the account.

    For ``credit``-type accounts, a positive balance indicates the amount owed; a negative amount indicates the lender
    owing the account holder.

    For ``loan``-type accounts, the current balance is the principal remaining on the loan, except in the case of
    student loan accounts at Sallie Mae (``ins_116944``). For Sallie Mae student loans, the account's balance includes
    both principal and any outstanding interest.

    For ``investment``-type accounts (or ``brokerage``-type accounts for API versions 2018-05-22 and earlier), the
    current balance is the total value of assets as presented by the institution.

    Note that balance information may be cached unless the value was returned by ``/accounts/balance/get``; if the Item
    is enabled for Transactions, the balance will be at least as recent as the most recent Transaction update. If you
    require real-time balance information, use the ``available`` balance as provided by ``/accounts/balance/get``.

    When returned by ``/accounts/balance/get``, this field may be ``null``. When this happens, ``available`` is
    guaranteed not to be ``null``."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the balance. Always null if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the balance. Always null if ``iso_currency_code`` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    historical_balances: list[CraVoaReportAccountHistoricalBalance]
    """Calculated data about the historical balances on the account.

    Available for ``credit`` and ``depository`` type accounts."""

    average_balance_30_days: float | None
    """The average balance in the account over the last 30 days. Calculated using the derived historical balances."""

    average_balance_60_days: float | None
    """The average balance in the account over the last 60 days. Calculated using the derived historical balances."""

    nsf_overdraft_transactions_count: float
    """The number of net NSF fee transactions in the time range for the report in the given account (not counting any
    fees that were reversed within the time range)."""


class CraVoaReportAccountBalancesDict(TypedDict):
    available: float | None
    current: float | None
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    historical_balances: list[CraVoaReportAccountHistoricalBalanceDict]
    average_balance_30_days: float | None
    average_balance_60_days: float | None
    nsf_overdraft_transactions_count: float
