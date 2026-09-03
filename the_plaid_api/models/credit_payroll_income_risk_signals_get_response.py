from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .error import Error, ErrorDict
from .payroll_risk_signals_item import PayrollRiskSignalsItem, PayrollRiskSignalsItemDict


class CreditPayrollIncomeRiskSignalsGetResponse(SdkBaseModel):
    """CreditPayrollIncomeRiskSignalsGetResponse defines the response schema for
    ``/credit/payroll_income/risk_signals/get``"""

    items: list[PayrollRiskSignalsItem]
    """Array of payroll items."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditPayrollIncomeRiskSignalsGetResponseDict(TypedDict):
    items: list[PayrollRiskSignalsItem | PayrollRiskSignalsItemDict]
    error: NotRequired[Error | ErrorDict | None]
    request_id: str
