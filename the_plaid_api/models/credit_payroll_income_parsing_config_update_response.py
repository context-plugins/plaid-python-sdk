from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditPayrollIncomeParsingConfigUpdateResponse(SdkBaseModel):
    """CreditPayrollIncomeParsingConfigUpdateResponse defines the response schema for
    ``/credit/payroll_income/parsing_config/update``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditPayrollIncomeParsingConfigUpdateResponseDict(TypedDict):
    request_id: str
