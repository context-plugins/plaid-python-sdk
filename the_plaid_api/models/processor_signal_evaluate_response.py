from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .signal_evaluate_core_attributes import SignalEvaluateCoreAttributes, SignalEvaluateCoreAttributesDict
from .signal_evaluate_ruleset import SignalEvaluateRuleset, SignalEvaluateRulesetDict
from .signal_evaluate_scores import SignalEvaluateScores, SignalEvaluateScoresDict
from .signal_warning import SignalWarning, SignalWarningDict


class ProcessorSignalEvaluateResponse(SdkBaseModel):
    """ProcessorSignalEvaluateResponse defines the response schema for ``/processor/signal/evaluate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    scores: SignalEvaluateScores | None
    """Risk scoring details broken down by risk category. When using a Balance-only ruleset, this object will not be
    returned."""

    core_attributes: Optional[SignalEvaluateCoreAttributes] = UNSET
    """The core attributes object contains additional data that can be used to assess the ACH return risk.

    If using a Balance-only ruleset, only ``available_balance`` and ``current_balance`` will be returned as core
    attributes. If using a Signal Transaction Scores ruleset, over 80 core attributes will be returned. Examples of
    attributes include:

    ``available_balance`` and ``current_balance``: The balance in the ACH transaction funding account
    ``days_since_first_plaid_connection``: The number of days since the first time the Item was connected to an
    application via Plaid ``plaid_connections_count_7d``: The number of times the Item has been connected to
    applications via Plaid over the past 7 days ``plaid_connections_count_30d``: The number of times the Item has been
    connected to applications via Plaid over the past 30 days ``total_plaid_connections_count``: The number of times the
    Item has been connected to applications via Plaid ``is_savings_or_money_market_account``: Indicates whether the ACH
    transaction funding account is a savings/money market account

    For the full list and detailed documentation of core attributes available, or to request that core attributes not be
    returned, contact sales or your Plaid account manager."""

    ruleset: OptionalNullable[SignalEvaluateRuleset] = UNSET
    """Details about the transaction result after evaluation by the requested Ruleset. If a ``ruleset_key`` is not
    provided, for customers who began using Signal Transaction Scores before October 15, 2025, by default, this field
    will be omitted. To learn more, see `Signal Rules <https://plaid.com/docs/signal/signal-rules/>`__."""

    warnings: Optional[list[SignalWarning]] = UNSET
    """If bank information was not available to be used in the Signal Transaction Scores model, this array contains
    warnings describing why bank data is missing. If you want to receive an API error instead of scores in the case of
    missing bank data, file a support ticket or contact your Plaid account manager."""


class ProcessorSignalEvaluateResponseDict(TypedDict):
    request_id: str
    scores: SignalEvaluateScores | SignalEvaluateScoresDict | None
    core_attributes: NotRequired[SignalEvaluateCoreAttributes | SignalEvaluateCoreAttributesDict]
    ruleset: NotRequired[SignalEvaluateRuleset | SignalEvaluateRulesetDict | None]
    warnings: NotRequired[list[SignalWarning | SignalWarningDict]]
