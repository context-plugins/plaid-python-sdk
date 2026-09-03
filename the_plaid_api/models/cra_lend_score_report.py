from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .lend_score import LendScore, LendScoreDict


class CraLendScoreReport(SdkBaseModel):
    """Contains data for the CRA LendScore Report."""

    report_id: str
    """The unique identifier associated with the report object."""

    generated_time: RFC3339DateTime
    """The time when the report was generated."""

    lend_score: OptionalNullable[LendScore] = UNSET
    """The results of the LendScore"""


class CraLendScoreReportDict(TypedDict):
    report_id: str
    generated_time: RFC3339DateTime
    lend_score: NotRequired[LendScore | LendScoreDict | None]
