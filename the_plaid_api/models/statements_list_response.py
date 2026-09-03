from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .statements_account import StatementsAccount, StatementsAccountDict


class StatementsListResponse(SdkBaseModel):
    """StatementsListResponse defines the response schema for ``/statements/list``"""

    accounts: list[StatementsAccount]
    institution_id: str
    """The Plaid Institution ID associated with the Item."""

    institution_name: str
    """The name of the institution associated with the Item."""

    item_id: str
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class StatementsListResponseDict(TypedDict):
    accounts: list[StatementsAccount | StatementsAccountDict]
    institution_id: str
    institution_name: str
    item_id: str
    request_id: str
