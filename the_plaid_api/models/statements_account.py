from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .statements_statement import StatementsStatement, StatementsStatementDict


class StatementsAccount(SdkBaseModel):
    """Account associated with the Item."""

    account_id: str
    """Plaid's unique identifier for the account."""

    account_mask: str
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    account_name: str
    """The name of the account, either assigned by the user or by the financial institution itself."""

    account_official_name: str
    """The official name of the account as given by the financial institution."""

    account_subtype: str
    """The subtype of the account. For a full list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""

    account_type: str
    """The type of account. For a full list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__."""

    statements: list[StatementsStatement]
    """The list of statements' metadata associated with this account."""


class StatementsAccountDict(TypedDict):
    account_id: str
    account_mask: str
    account_name: str
    account_official_name: str
    account_subtype: str
    account_type: str
    statements: list[StatementsStatement | StatementsStatementDict]
