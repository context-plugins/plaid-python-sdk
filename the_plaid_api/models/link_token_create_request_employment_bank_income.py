from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateRequestEmploymentBankIncome(SdkBaseModel):
    """Specifies options for initializing Link for use with Bank Employment. This field is required if ``employment`` is
    included in the ``products`` array and ``bank`` is specified in ``employment_source_types``."""

    days_requested: int
    """The number of days of data to request for the Bank Employment product."""


class LinkTokenCreateRequestEmploymentBankIncomeDict(TypedDict):
    days_requested: int
