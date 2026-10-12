from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .counterparty_numbers_bacs import CounterpartyNumbersBacs, CounterpartyNumbersBacsDict
from .counterparty_numbers_international import CounterpartyNumbersInternational, CounterpartyNumbersInternationalDict


class CounterpartyNumbers(SdkBaseModel):
    """Account numbers associated with the counterparty, when available. This field is currently only filled in for
    select financial institutions in Europe."""

    bacs: OptionalNullable[CounterpartyNumbersBacs] = UNSET
    """Identifying information for a UK bank account via Bacs."""

    international: OptionalNullable[CounterpartyNumbersInternational] = UNSET
    """Account numbers using the International Bank Account Number and BIC/SWIFT code format."""


class CounterpartyNumbersDict(TypedDict):
    bacs: NotRequired[CounterpartyNumbersBacsDict | None]
    international: NotRequired[CounterpartyNumbersInternationalDict | None]
