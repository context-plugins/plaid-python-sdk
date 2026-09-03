from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersAcats(SdkBaseModel):
    """Identifying information for transferring holdings to an investment account via ACATS."""

    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The full account number for the account"""

    dtc_numbers: list[str]
    """Identifiers for the clearinghouses that are associated with the account in order of relevance. If this array is
    empty, call ``/institutions/get_by_id`` with the ``item.institution_id`` to get the DTC number."""


class NumbersAcatsDict(TypedDict):
    account_id: str
    account: str
    dtc_numbers: list[str]
