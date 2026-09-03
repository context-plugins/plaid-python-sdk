from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class LastDataAccessTimes(SdkBaseModel):
    """Describes the last time each datatype was accessed by an application."""

    application_id: str
    """ID of the application accessing data."""

    account_balance_info: RFC3339DateTime | None
    """The last time ``account_balance_info`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    account_routing_number: RFC3339DateTime | None
    """The last time ``account_routing_number`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    contact_details: RFC3339DateTime | None
    """The last time ``contact_details`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    transactions: RFC3339DateTime | None
    """The last time ``transactions`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    credit_and_loans: RFC3339DateTime | None
    """The last time ``credit_and_loans`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    investments: RFC3339DateTime | None
    """The last time ``investments`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    payroll_info: RFC3339DateTime | None
    """The last time ``payroll_info`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""

    transaction_risk_info: RFC3339DateTime | None
    """The last time ``transaction_risk_info`` was accessed by this application in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format in UTC. null if never accessed."""


class LastDataAccessTimesDict(TypedDict):
    application_id: str
    account_balance_info: RFC3339DateTime | None
    account_routing_number: RFC3339DateTime | None
    contact_details: RFC3339DateTime | None
    transactions: RFC3339DateTime | None
    credit_and_loans: RFC3339DateTime | None
    investments: RFC3339DateTime | None
    payroll_info: RFC3339DateTime | None
    transaction_risk_info: RFC3339DateTime | None
