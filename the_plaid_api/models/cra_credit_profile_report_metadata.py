from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, RFC3339DateTime, SdkBaseModel


class CraCreditProfileReportMetadata(SdkBaseModel):
    """Metadata about the CRA Credit Profile Report."""

    item_count: int
    """The number of items used to calculate the report."""

    institution_ids: list[str]
    """The institution IDs associated with the report."""

    account_count: int
    """The total number of accounts in the report."""

    primary_account_count: int
    """The number of primary accounts in the report."""

    depository_account_type_count: int
    """The number of depository accounts in the report."""

    credit_account_type_count: int
    """The number of credit accounts in the report."""

    other_account_type_count: int
    """The number of other accounts in the report."""

    multiple_owner_account_count: int
    """The number of accounts with multiple owners in the report."""

    generated_at: RFC3339DateTime
    """The time when the report was generated."""

    oldest_transaction_date: Date
    """The date of the oldest transaction in the report."""

    most_recent_transaction_date: Date
    """The date of the most recent transaction in the report."""


class CraCreditProfileReportMetadataDict(TypedDict):
    item_count: int
    institution_ids: list[str]
    account_count: int
    primary_account_count: int
    depository_account_type_count: int
    credit_account_type_count: int
    other_account_type_count: int
    multiple_owner_account_count: int
    generated_at: RFC3339DateTime
    oldest_transaction_date: Date
    most_recent_transaction_date: Date
