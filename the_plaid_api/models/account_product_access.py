from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AccountProductAccess(SdkBaseModel):
    """Allow the application to access specific products on this account"""

    account_data: bool | None = True
    """Allow the application to access account data. Only used by certain partners. If relevant to the partner and
    unset, defaults to ``true``."""

    statements: bool | None = True
    """Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and
    unset, defaults to ``true``."""

    tax_documents: bool | None = True
    """Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and
    unset, defaults to ``true``."""


class AccountProductAccessDict(TypedDict):
    account_data: NotRequired[bool | None]
    statements: NotRequired[bool | None]
    tax_documents: NotRequired[bool | None]
