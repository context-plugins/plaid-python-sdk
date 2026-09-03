from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ProcessorTransactionsGetRequestOptions(SdkBaseModel):
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""

    count: Optional[int] = UNSET
    """The number of transactions to fetch."""

    offset: Optional[int] = UNSET
    """The number of transactions to skip. The default value is 0."""

    include_original_description: OptionalNullable[bool] = UNSET
    """Include the raw unparsed transaction description from the financial institution."""

    include_personal_finance_category_beta: Optional[bool] = UNSET
    """Personal finance categories are now returned by default."""

    include_personal_finance_category: Optional[bool] = UNSET
    """Personal finance categories are now returned by default."""

    include_logo_and_counterparty_beta: Optional[bool] = UNSET
    """Counterparties and extra merchant fields are now returned by default."""


class ProcessorTransactionsGetRequestOptionsDict(TypedDict):
    count: NotRequired[int]
    offset: NotRequired[int]
    include_original_description: NotRequired[bool | None]
    include_personal_finance_category_beta: NotRequired[bool]
    include_personal_finance_category: NotRequired[bool]
    include_logo_and_counterparty_beta: NotRequired[bool]
