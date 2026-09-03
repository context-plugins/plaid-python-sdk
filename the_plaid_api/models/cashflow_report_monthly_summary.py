from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .cashflow_report_monthly_summary_average_daily_ending_balance import (
    CashflowReportMonthlySummaryAverageDailyEndingBalance,
    CashflowReportMonthlySummaryAverageDailyEndingBalanceDict,
)
from .cashflow_report_monthly_summary_average_daily_inflow_amount import (
    CashflowReportMonthlySummaryAverageDailyInflowAmount,
    CashflowReportMonthlySummaryAverageDailyInflowAmountDict,
)
from .cashflow_report_monthly_summary_average_daily_net_cashflow_amount import (
    CashflowReportMonthlySummaryAverageDailyNetCashflowAmount,
    CashflowReportMonthlySummaryAverageDailyNetCashflowAmountDict,
)
from .cashflow_report_monthly_summary_average_daily_outflow_amount import (
    CashflowReportMonthlySummaryAverageDailyOutflowAmount,
    CashflowReportMonthlySummaryAverageDailyOutflowAmountDict,
)
from .cashflow_report_monthly_summary_ending_balance import (
    CashflowReportMonthlySummaryEndingBalance,
    CashflowReportMonthlySummaryEndingBalanceDict,
)
from .cashflow_report_monthly_summary_starting_balance import (
    CashflowReportMonthlySummaryStartingBalance,
    CashflowReportMonthlySummaryStartingBalanceDict,
)
from .cashflow_report_monthly_summary_total_loan_payment import (
    CashflowReportMonthlySummaryTotalLoanPayment,
    CashflowReportMonthlySummaryTotalLoanPaymentDict,
)
from .cashflow_report_monthly_summary_total_payroll import (
    CashflowReportMonthlySummaryTotalPayroll,
    CashflowReportMonthlySummaryTotalPayrollDict,
)
from .cashflow_report_monthly_summary_total_revenue import (
    CashflowReportMonthlySummaryTotalRevenue,
    CashflowReportMonthlySummaryTotalRevenueDict,
)
from .cashflow_report_monthly_summary_total_variable_expense import (
    CashflowReportMonthlySummaryTotalVariableExpense,
    CashflowReportMonthlySummaryTotalVariableExpenseDict,
)


class CashflowReportMonthlySummary(SdkBaseModel):
    """Monthly summary statistics derived from transaction-level data."""

    start_date: Date
    """The start date of the period covered in this monthly summary.

    This date will be the first day of the month, unless the month being covered is a partial month because it is the
    first month included in the summary and the date range being requested does not begin with the first day of the
    month.

    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    end_date: Date
    """The end date of the period included in this monthly summary.

    This date will be the last day of the month, unless the month being covered is a partial month because it is the
    last month included in the summary and the date range being requested does not end with the last day of the month.

    The date will be returned in an ISO 8601 format (YYYY-MM-DD)."""

    starting_balance: CashflowReportMonthlySummaryStartingBalance | None
    """The starting balance of the month. This will be the same as the ending balance of the previous month. This field
    will not be available for the first monthly summary."""

    ending_balance: CashflowReportMonthlySummaryEndingBalance | None
    """The ending balance of the month. This will be the same as the starting balance of the next month. This field will
    not be available for the last monthly summary."""

    average_daily_ending_balance: CashflowReportMonthlySummaryAverageDailyEndingBalance
    """Calendar-day average of the ending balance."""

    average_daily_inflow_amount: CashflowReportMonthlySummaryAverageDailyInflowAmount
    """The average daily sum of inflow transactions, calculated over the month. Always represented as a positive
    monetary amount."""

    average_daily_outflow_amount: CashflowReportMonthlySummaryAverageDailyOutflowAmount
    """The average daily sum of outflow transactions, calculated over the month. Always represented as a positive
    monetary amount."""

    average_daily_net_cashflow_amount: CashflowReportMonthlySummaryAverageDailyNetCashflowAmount
    """The average daily net cash flow amount, calculated as total daily inflows less total daily outflows."""

    average_daily_inflow_transaction_count: float
    """The average count of the number of daily inflow transactions. Rounded to 2 decimal places."""

    average_daily_outflow_transaction_count: float
    """The average count of the number of daily outflow transactions. Rounded to 2 decimal places."""

    total_revenue: CashflowReportMonthlySummaryTotalRevenue
    """The total amount of all revenue transactions during this month."""

    total_loan_payment: CashflowReportMonthlySummaryTotalLoanPayment
    """The total amount of all loan payment transactions during this month."""

    total_variable_expense: CashflowReportMonthlySummaryTotalVariableExpense
    """The total amount of all variable expense transactions during this month."""

    total_payroll: CashflowReportMonthlySummaryTotalPayroll
    """The total amount of all payroll transactions during this month."""

    nsf_transaction_count: int
    """The total number of all NSF transactions during this month."""

    overdraft_transaction_count: int
    """The total number of all overdraft transactions during this month."""

    negative_ending_balance_day_count: int
    """The number of days with a negative daily average ending balance. The daily average is calculated across all valid
    accounts. Values will be in the range [0, 31]."""


class CashflowReportMonthlySummaryDict(TypedDict):
    start_date: Date
    end_date: Date
    starting_balance: (
        CashflowReportMonthlySummaryStartingBalance | CashflowReportMonthlySummaryStartingBalanceDict | None
    )
    ending_balance: CashflowReportMonthlySummaryEndingBalance | CashflowReportMonthlySummaryEndingBalanceDict | None
    average_daily_ending_balance: (
        CashflowReportMonthlySummaryAverageDailyEndingBalance
        | CashflowReportMonthlySummaryAverageDailyEndingBalanceDict
    )
    average_daily_inflow_amount: (
        CashflowReportMonthlySummaryAverageDailyInflowAmount | CashflowReportMonthlySummaryAverageDailyInflowAmountDict
    )
    average_daily_outflow_amount: (
        CashflowReportMonthlySummaryAverageDailyOutflowAmount
        | CashflowReportMonthlySummaryAverageDailyOutflowAmountDict
    )
    average_daily_net_cashflow_amount: (
        CashflowReportMonthlySummaryAverageDailyNetCashflowAmount
        | CashflowReportMonthlySummaryAverageDailyNetCashflowAmountDict
    )
    average_daily_inflow_transaction_count: float
    average_daily_outflow_transaction_count: float
    total_revenue: CashflowReportMonthlySummaryTotalRevenue | CashflowReportMonthlySummaryTotalRevenueDict
    total_loan_payment: CashflowReportMonthlySummaryTotalLoanPayment | CashflowReportMonthlySummaryTotalLoanPaymentDict
    total_variable_expense: (
        CashflowReportMonthlySummaryTotalVariableExpense | CashflowReportMonthlySummaryTotalVariableExpenseDict
    )
    total_payroll: CashflowReportMonthlySummaryTotalPayroll | CashflowReportMonthlySummaryTotalPayrollDict
    nsf_transaction_count: int
    overdraft_transaction_count: int
    negative_ending_balance_day_count: int
