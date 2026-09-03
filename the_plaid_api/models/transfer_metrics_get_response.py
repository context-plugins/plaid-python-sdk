from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .transfer_metrics_get_authorization_usage import (
    TransferMetricsGetAuthorizationUsage,
    TransferMetricsGetAuthorizationUsageDict,
)
from .transfer_metrics_get_return_rates import TransferMetricsGetReturnRates, TransferMetricsGetReturnRatesDict


class TransferMetricsGetResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/metrics/get``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    daily_debit_transfer_volume: str
    """Sum of dollar amount of debit transfers in last 24 hours (decimal string with two digits of precision e.g.
    "10.00")."""

    daily_credit_transfer_volume: str
    """Sum of dollar amount of credit transfers in last 24 hours (decimal string with two digits of precision e.g.
    "10.00")."""

    monthly_transfer_volume: str
    """Sum of dollar amount of credit and debit transfers in current calendar month (decimal string with two digits of
    precision e.g. "10.00")."""

    monthly_debit_transfer_volume: str
    """Sum of dollar amount of debit transfers in current calendar month (decimal string with two digits of precision
    e.g. "10.00")."""

    monthly_credit_transfer_volume: str
    """Sum of dollar amount of credit transfers in current calendar month (decimal string with two digits of precision
    e.g. "10.00")."""

    iso_currency_code: str
    """The currency of the dollar amount, e.g. "USD"."""

    return_rates: OptionalNullable[TransferMetricsGetReturnRates] = UNSET
    """Details regarding return rates."""

    authorization_usage: OptionalNullable[TransferMetricsGetAuthorizationUsage] = UNSET
    """Details regarding authorization usage."""


class TransferMetricsGetResponseDict(TypedDict):
    request_id: str
    daily_debit_transfer_volume: str
    daily_credit_transfer_volume: str
    monthly_transfer_volume: str
    monthly_debit_transfer_volume: str
    monthly_credit_transfer_volume: str
    iso_currency_code: str
    return_rates: NotRequired[TransferMetricsGetReturnRates | TransferMetricsGetReturnRatesDict | None]
    authorization_usage: NotRequired[
        TransferMetricsGetAuthorizationUsage | TransferMetricsGetAuthorizationUsageDict | None
    ]
