from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.products import ProductsOrStr
from .item_import_request_options import ItemImportRequestOptions, ItemImportRequestOptionsDict
from .item_import_request_user_auth import ItemImportRequestUserAuth, ItemImportRequestUserAuthDict


class ItemImportRequest(SdkBaseModel):
    """ItemImportRequest defines the request schema for ``/item/import``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    institution_id: Optional[str] = UNSET
    """The Plaid Institution ID associated with the Item."""

    products: list[ProductsOrStr]
    """Array of product strings"""

    user_auth: ItemImportRequestUserAuth
    """Object of user ID and auth token pair, permitting Plaid to aggregate a user's accounts"""

    options: Optional[ItemImportRequestOptions] = UNSET
    """An optional object to configure ``/item/import`` request."""


class ItemImportRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    institution_id: NotRequired[str]
    products: list[ProductsOrStr]
    user_auth: ItemImportRequestUserAuth | ItemImportRequestUserAuthDict
    options: NotRequired[ItemImportRequestOptions | ItemImportRequestOptionsDict]
