from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferConfigurationGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/configuration/get``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    max_single_transfer_amount: str
    """The max limit of dollar amount of a single transfer (decimal string with two digits of precision e.g.
    "10.00")."""

    max_single_transfer_credit_amount: str
    """The max limit of dollar amount of a single credit transfer (decimal string with two digits of precision e.g.
    "10.00")."""

    max_single_transfer_debit_amount: str
    """The max limit of dollar amount of a single debit transfer (decimal string with two digits of precision e.g.
    "10.00")."""

    max_daily_credit_amount: str
    """The max limit of sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of
    precision e.g. "10.00")."""

    max_daily_debit_amount: str
    """The max limit of sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of
    precision e.g. "10.00")."""

    max_monthly_amount: str
    """The max limit of sum of dollar amount of credit and debit transfers in one calendar month (decimal string with
    two digits of precision e.g. "10.00")."""

    max_monthly_credit_amount: str
    """The max limit of sum of dollar amount of credit transfers in one calendar month (decimal string with two digits
    of precision e.g. "10.00")."""

    max_monthly_debit_amount: str
    """The max limit of sum of dollar amount of debit transfers in one calendar month (decimal string with two digits of
    precision e.g. "10.00")."""

    iso_currency_code: str
    """The currency of the dollar amount, e.g. "USD"."""


class TransferConfigurationGetResponseDict(TypedDict):
    request_id: str
    max_single_transfer_amount: str
    max_single_transfer_credit_amount: str
    max_single_transfer_debit_amount: str
    max_daily_credit_amount: str
    max_daily_debit_amount: str
    max_monthly_amount: str
    max_monthly_credit_amount: str
    max_monthly_debit_amount: str
    iso_currency_code: str
