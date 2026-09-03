from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.products import ProductsOrStr


class ProcessorTokenPermissionsSetRequest(SdkBaseModel):
    """ProcessorTokenPermissionsSetRequest defines the request schema for ``/processor/token/permissions/set``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format:
    ``processor-<environment>-<identifier>``"""

    products: list[ProductsOrStr]
    """A list of products the processor token should have access to. An empty list will grant access to all products."""


class ProcessorTokenPermissionsSetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    processor_token: str
    products: list[ProductsOrStr]
