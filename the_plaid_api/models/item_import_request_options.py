from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemImportRequestOptions(SdkBaseModel):
    """An optional object to configure ``/item/import`` request."""

    webhook: Optional[str] = UNSET
    """Specifies a webhook URL to associate with an Item. Plaid fires a webhook if credentials fail."""


class ItemImportRequestOptionsDict(TypedDict):
    webhook: NotRequired[str]
