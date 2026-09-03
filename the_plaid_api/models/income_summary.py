from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .employee_income_summary_field_string import EmployeeIncomeSummaryFieldString, EmployeeIncomeSummaryFieldStringDict
from .employer_income_summary_field_string import EmployerIncomeSummaryFieldString, EmployerIncomeSummaryFieldStringDict
from .pay_frequency import PayFrequency, PayFrequencyDict
from .projected_income_summary_field_number import (
    ProjectedIncomeSummaryFieldNumber,
    ProjectedIncomeSummaryFieldNumberDict,
)
from .transaction_data import TransactionData, TransactionDataDict
from .ytdgross_income_summary_field_number import YtdgrossIncomeSummaryFieldNumber, YtdgrossIncomeSummaryFieldNumberDict
from .ytdnet_income_summary_field_number import YtdnetIncomeSummaryFieldNumber, YtdnetIncomeSummaryFieldNumberDict


class IncomeSummary(SdkBaseModel):
    """The verified fields from a paystub verification. All fields are provided as reported on the paystub."""

    employer_name: EmployerIncomeSummaryFieldString | None
    """The name of the employer, as reported on the paystub."""

    employee_name: EmployeeIncomeSummaryFieldString | None
    """The name of the employee, as reported on the paystub."""

    ytd_gross_income: YtdgrossIncomeSummaryFieldNumber | None
    """Year-to-date pre-tax earnings, as reported on the paystub."""

    ytd_net_income: YtdnetIncomeSummaryFieldNumber | None
    """Year-to-date earnings after any tax withholdings, benefit payments or deductions, as reported on the paystub."""

    pay_frequency: PayFrequency | None
    """The frequency of the pay period."""

    projected_wage: ProjectedIncomeSummaryFieldNumber | None
    """The employee's estimated annual salary, as derived from information reported on the paystub."""

    verified_transaction: TransactionData | None
    """Information about the matched direct deposit transaction used to verify a user's payroll information."""


class IncomeSummaryDict(TypedDict):
    employer_name: EmployerIncomeSummaryFieldString | EmployerIncomeSummaryFieldStringDict | None
    employee_name: EmployeeIncomeSummaryFieldString | EmployeeIncomeSummaryFieldStringDict | None
    ytd_gross_income: YtdgrossIncomeSummaryFieldNumber | YtdgrossIncomeSummaryFieldNumberDict | None
    ytd_net_income: YtdnetIncomeSummaryFieldNumber | YtdnetIncomeSummaryFieldNumberDict | None
    pay_frequency: PayFrequency | PayFrequencyDict | None
    projected_wage: ProjectedIncomeSummaryFieldNumber | ProjectedIncomeSummaryFieldNumberDict | None
    verified_transaction: TransactionData | TransactionDataDict | None
