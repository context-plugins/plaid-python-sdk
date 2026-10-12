from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ProcessorTransactionsGetRequestOptions(SdkBaseModel):
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""

    count: int = 100
    """The number of transactions to fetch."""

    offset: int = 0
    """The number of transactions to skip. The default value is 0."""

    include_original_description: bool | None = False
    """Include the raw unparsed transaction description from the financial institution."""

    include_personal_finance_category_beta: bool = False
    """Personal finance categories are now returned by default."""

    include_personal_finance_category: bool = False
    """Personal finance categories are now returned by default."""

    include_logo_and_counterparty_beta: bool = False
    """Counterparties and extra merchant fields are now returned by default."""


class ProcessorTransactionsGetRequestOptionsDict(TypedDict):
    count: NotRequired[int]
    offset: NotRequired[int]
    include_original_description: NotRequired[bool | None]
    include_personal_finance_category_beta: NotRequired[bool]
    include_personal_finance_category: NotRequired[bool]
    include_logo_and_counterparty_beta: NotRequired[bool]
