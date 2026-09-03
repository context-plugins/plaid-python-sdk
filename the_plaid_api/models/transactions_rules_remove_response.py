from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionsRulesRemoveResponse(SdkBaseModel):
    """TransactionsRulesRemoveResponse defines the response schema for ``/beta/transactions/rules/v1/remove``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsRulesRemoveResponseDict(TypedDict):
    request_id: str
