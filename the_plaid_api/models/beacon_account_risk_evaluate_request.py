from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .beacon_account_risk_evaluate_request_options import (
    BeaconAccountRiskEvaluateRequestOptions,
    BeaconAccountRiskEvaluateRequestOptionsDict,
)
from .enums.beacon_account_risk_evaluate_evaluation_reason import BeaconAccountRiskEvaluateEvaluationReasonOrStr
from .signal_evaluate_device import SignalEvaluateDevice, SignalEvaluateDeviceDict


class BeaconAccountRiskEvaluateRequest(SdkBaseModel):
    """BeaconAccountRiskEvaluateRequest defines the request schema for ``/beacon/account_risk/v1/evaluate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: Optional[str] = UNSET
    """The access token associated with the Item for which data is being requested."""

    options: Optional[BeaconAccountRiskEvaluateRequestOptions] = UNSET
    """An optional object to filter ``/beacon/account_risk/v1/evaluate`` results to a subset of the accounts on the
    linked Item."""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with
    multiple evaluations and/or multiple linked accounts. Personally identifiable information, such as an email address
    or phone number, should not be used in the ``client_user_id``."""

    client_evaluation_id: Optional[str] = UNSET
    """Unique identifier of what you are looking to evaluate (account add, information change, etc.) to allow us to tie
    the activity to the decisions and possible fraud outcome sent via our feedback endpoints. You can use your internal
    request ID or similar."""

    evaluation_reason: Optional[BeaconAccountRiskEvaluateEvaluationReasonOrStr] = UNSET
    """Description of the reason you want to evaluate risk. ``ONBOARDING``: user links a first bank account as part of
    the onboarding flow of your platform. ``NEW_ACCOUNT``: user links another bank account or replaces the currently
    linked bank account on your platform. ``INFORMATION_CHANGE``: user changes their information on your platform, e.g.,
    updating their phone number. ``DORMANT_USER``: you decide to re-evaluate a user that becomes active after a period
    of inactivity. ``OTHER``: any other reasons not listed here Possible values: ``ONBOARDING``, ``NEW_ACCOUNT``,
    ``INFORMATION_CHANGE``, ``DORMANT_USER``, ``OTHER``"""

    device: Optional[SignalEvaluateDevice] = UNSET
    """Details about the end user's device. These fields are optional, but strongly recommended to increase the accuracy
    of results when using Signal Transaction Scores. When using a Balance-only Ruleset, these fields are ignored if the
    Signal Addendum has been signed; if it has not been signed, using these fields will result in an error."""

    evaluate_time: Optional[str] = UNSET
    """The time the event for evaluation has occurred. Populate this field for backfilling data. If you don't populate
    this field, we'll use the timestamp at the time of receipt. Use ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ)."""


class BeaconAccountRiskEvaluateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: NotRequired[str]
    options: NotRequired[BeaconAccountRiskEvaluateRequestOptionsDict]
    client_user_id: NotRequired[str]
    client_evaluation_id: NotRequired[str]
    evaluation_reason: NotRequired[BeaconAccountRiskEvaluateEvaluationReasonOrStr]
    device: NotRequired[SignalEvaluateDeviceDict]
    evaluate_time: NotRequired[str]
