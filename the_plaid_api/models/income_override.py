from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paystub_override import PaystubOverride, PaystubOverrideDict
from .w2_override import W2Override, W2OverrideDict


class IncomeOverride(SdkBaseModel):
    """Specify payroll data on the account."""

    paystubs: Optional[list[PaystubOverride]] = UNSET
    """A list of paystubs associated with the account."""

    w2s: Optional[list[W2Override]] = UNSET
    """A list of w2s associated with the account."""


class IncomeOverrideDict(TypedDict):
    paystubs: NotRequired[list[PaystubOverride | PaystubOverrideDict]]
    w2s: NotRequired[list[W2Override | W2OverrideDict]]
