from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateRequestIncomeVerificationBankIncome(SdkBaseModel):
    """Specifies options for initializing Link for use with Bank Income. This field is required if
    ``income_verification`` is included in the ``products`` array and ``bank`` is specified in
    ``income_source_types``."""

    days_requested: int
    """The number of days of data to request for the Bank Income product"""

    enable_multiple_items: bool | None = False
    """Whether to enable multiple Items to be added in the Link session. This setting is deprecated and has been
    replaced by the more general ``enable_multi_item_link`` setting, which supports all products."""


class LinkTokenCreateRequestIncomeVerificationBankIncomeDict(TypedDict):
    days_requested: int
    enable_multiple_items: NotRequired[bool | None]
