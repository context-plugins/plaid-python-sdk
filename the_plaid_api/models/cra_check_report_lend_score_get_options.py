from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.plaid_lend_score_version import PlaidLendScoreVersionOrStr


class CraCheckReportLendScoreGetOptions(SdkBaseModel):
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``options``."""

    lend_score_version: OptionalNullable[PlaidLendScoreVersionOrStr] = UNSET
    """The version of the LendScore to use. Required if using LendScore."""


class CraCheckReportLendScoreGetOptionsDict(TypedDict):
    lend_score_version: NotRequired[PlaidLendScoreVersionOrStr | None]
