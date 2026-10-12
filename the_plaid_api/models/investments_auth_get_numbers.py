from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .numbers_acats import NumbersAcats, NumbersAcatsDict
from .numbers_aton import NumbersAton, NumbersAtonDict
from .numbers_retirement401_k import NumbersRetirement401K, NumbersRetirement401KDict


class InvestmentsAuthGetNumbers(SdkBaseModel):
    """Identifying information for transferring holdings to an investment account."""

    acats: Optional[list[NumbersAcats]] = UNSET
    aton: Optional[list[NumbersAton]] = UNSET
    retirement_401k: Optional[list[NumbersRetirement401K]] = UNSET


class InvestmentsAuthGetNumbersDict(TypedDict):
    acats: NotRequired[list[NumbersAcatsDict]]
    aton: NotRequired[list[NumbersAtonDict]]
    retirement_401k: NotRequired[list[NumbersRetirement401KDict]]
