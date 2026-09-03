from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PrismCashScoreMetadata(SdkBaseModel):
    """An object containing metadata about the provided transactions."""

    max_age: int | None
    """Number of days since the oldest transaction."""

    min_age: int | None
    """Number of days since the latest transaction."""

    min_age_credit: int | None
    """Number of days since the latest credit transaction."""

    min_age_debit: int | None
    """Number of days since the latest debit transaction."""

    max_age_debit: int | None
    """Number of days since the oldest debit transaction."""

    max_age_credit: int | None
    """Number of days since the oldest credit transaction."""

    num_trxn_credit: int | None
    """Number of credit transactions."""

    num_trxn_debit: int | None
    """Number of debit transactions."""

    l1m_credit_value_cnt: int | None
    """Number of credit transactions in the last 30 days."""

    l1m_debit_value_cnt: int | None
    """Number of debit transactions in the last 30 days."""


class PrismCashScoreMetadataDict(TypedDict):
    max_age: int | None
    min_age: int | None
    min_age_credit: int | None
    min_age_debit: int | None
    max_age_debit: int | None
    max_age_credit: int | None
    num_trxn_credit: int | None
    num_trxn_debit: int | None
    l1m_credit_value_cnt: int | None
    l1m_debit_value_cnt: int | None
