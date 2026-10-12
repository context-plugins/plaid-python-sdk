from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .error import Error, ErrorDict


class RefreshResult(SdkBaseModel):
    """RefreshResult represents the result status of a user refresh for a specific item."""

    item_id: Optional[str] = UNSET
    """A unique identifier for the Plaid Item."""

    product: Optional[str] = UNSET
    """The product for which the refresh was attempted."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""


class RefreshResultDict(TypedDict):
    item_id: NotRequired[str]
    product: NotRequired[str]
    error: NotRequired[ErrorDict | None]
