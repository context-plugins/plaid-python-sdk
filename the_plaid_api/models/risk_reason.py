from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RiskReason(SdkBaseModel):
    """This object includes a code and description to describe medium risk transactions and above on
    ``/accounts/balance/get``."""

    code: str
    """A code that represents the type of risk associated with the proposed transaction.

    The codes are from PL01 to PL08 and from BK01 to BK07. For a full listing of risk reason codes, see `Risk codes
    <https://plaid.com/docs/balance/balance-plus/#risk-codes>`__."""

    description: str
    """A human-readable description explaining the risk code associated with the proposed transaction and some
    recommended actions. This field is subject to change; any programmatic logic should be based on the ``code`` field
    instead."""


class RiskReasonDict(TypedDict):
    code: str
    description: str
