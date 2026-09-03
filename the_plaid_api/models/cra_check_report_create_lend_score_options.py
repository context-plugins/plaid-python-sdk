from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.plaid_lend_score_version import PlaidLendScoreVersionOrStr


class CraCheckReportCreateLendScoreOptions(SdkBaseModel):
    """Defines configuration options to generate the LendScore"""

    lend_score_version: OptionalNullable[PlaidLendScoreVersionOrStr] = UNSET
    """The version of the LendScore to use. Required if using LendScore."""


class CraCheckReportCreateLendScoreOptionsDict(TypedDict):
    lend_score_version: NotRequired[PlaidLendScoreVersionOrStr | None]
