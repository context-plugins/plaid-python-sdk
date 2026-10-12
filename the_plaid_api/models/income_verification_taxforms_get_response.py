from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .document_metadata import DocumentMetadata, DocumentMetadataDict
from .error import Error, ErrorDict
from .taxform import Taxform, TaxformDict


class IncomeVerificationTaxformsGetResponse(SdkBaseModel):
    """IncomeVerificationTaxformsGetResponse defines the response schema for ``/income/verification/taxforms/get``"""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    document_metadata: list[DocumentMetadata]
    taxforms: list[Taxform]
    """A list of forms."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""


class IncomeVerificationTaxformsGetResponseDict(TypedDict):
    request_id: NotRequired[str]
    document_metadata: list[DocumentMetadataDict]
    taxforms: list[TaxformDict]
    error: NotRequired[ErrorDict | None]
