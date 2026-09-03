from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class WalletTransactionListRequestOptions(SdkBaseModel):
    """Additional wallet transaction options"""

    start_time: Optional[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDThh:mm:ssZ) for filtering
    transactions, inclusive of the provided date."""

    end_time: Optional[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDThh:mm:ssZ) for filtering
    transactions, inclusive of the provided date."""


class WalletTransactionListRequestOptionsDict(TypedDict):
    start_time: NotRequired[RFC3339DateTime]
    end_time: NotRequired[RFC3339DateTime]
