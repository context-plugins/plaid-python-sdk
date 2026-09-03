from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.apr_type import AprTypeOrStr


class Apr(SdkBaseModel):
    """Information about the APR on the account."""

    apr_percentage: float
    """Annual Percentage Rate applied."""

    apr_type: AprTypeOrStr
    """The type of balance to which the APR applies."""

    balance_subject_to_apr: float | None
    """Amount of money that is subjected to the APR if a balance was carried beyond payment due date. How it is
    calculated can vary by card issuer. It is often calculated as an average daily balance."""

    interest_charge_amount: float | None
    """Amount of money charged due to interest from last statement."""


class AprDict(TypedDict):
    apr_percentage: float
    apr_type: AprTypeOrStr
    balance_subject_to_apr: float | None
    interest_charge_amount: float | None
