from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.rule_result import RuleResultOrStr
from .rule_details import RuleDetails, RuleDetailsDict


class SignalEvaluateRuleset(SdkBaseModel):
    """Details about the transaction result after evaluation by the requested Ruleset. If a ``ruleset_key`` is not
    provided, for customers who began using Signal Transaction Scores before October 15, 2025, by default, this field
    will be omitted. To learn more, see `Signal Rules <https://plaid.com/docs/signal/signal-rules/>`__."""

    ruleset_key: Optional[str] = UNSET
    """The key of the Ruleset used for this transaction."""

    result: RuleResultOrStr
    """The result of the rule that was triggered for this transaction.

    ``ACCEPT``: Accept the transaction for processing. ``REROUTE``: Reroute the transaction to a different payment
    method, as this transaction is too risky. ``REVIEW``: Review the transaction before proceeding."""

    triggered_rule_details: OptionalNullable[RuleDetails] = UNSET
    """Rules are run in numerical order. The first rule with a logic match is triggered. These are the details of that
    rule."""

    outcome: Optional[str] = UNSET
    """The evaluated outcome for this transaction. This field is deprecated, use ``result`` or
    ``triggered_rule_details.custom_action_key`` instead."""


class SignalEvaluateRulesetDict(TypedDict):
    ruleset_key: NotRequired[str]
    result: RuleResultOrStr
    triggered_rule_details: NotRequired[RuleDetailsDict | None]
    outcome: NotRequired[str]
