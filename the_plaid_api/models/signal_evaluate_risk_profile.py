from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignalEvaluateRiskProfile(SdkBaseModel):
    """RiskProfile is deprecated, use ``ruleset`` instead."""

    key: Optional[str] = UNSET
    """The key of the risk profile used for this transaction."""

    outcome: Optional[str] = UNSET
    """Legacy method of inspecting the result of the ruleset. New integrations should simply use the "result" property
    instead. This value will be omitted if you do not have a live existing integration with rules using this field."""


class SignalEvaluateRiskProfileDict(TypedDict):
    key: NotRequired[str]
    outcome: NotRequired[str]
