from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvestmentsTransactionsGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/investments/transactions/get`` results. If provided, must be non-``null``."""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_ids`` to retrieve for the Item."""

    count: Optional[int] = UNSET
    """The number of transactions to fetch."""

    offset: Optional[int] = UNSET
    """The number of transactions to skip when fetching transaction history"""

    async_update: Optional[bool] = UNSET
    """If the Item was not initialized with the investments product via the ``products``,
    ``required_if_supported_products``, or ``optional_products`` array when calling ``/link/token/create``, and
    ``async_update`` is set to true, the initial Investments extraction will happen asynchronously. Plaid will
    subsequently fire a ``HISTORICAL_UPDATE`` webhook when the extraction completes. When ``false``, Plaid will wait to
    return a response until extraction completion and no ``HISTORICAL_UPDATE`` webhook will fire. Note that while the
    extraction is happening asynchronously, calls to ``/investments/transactions/get`` and ``/investments/refresh`` will
    return ``PRODUCT_NOT_READY`` errors until the extraction completes."""


class InvestmentsTransactionsGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
    count: NotRequired[int]
    offset: NotRequired[int]
    async_update: NotRequired[bool]
