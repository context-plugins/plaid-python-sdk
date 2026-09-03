from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.risk_check_behavior_bot_detected_label import RiskCheckBehaviorBotDetectedLabelOrStr
from .enums.risk_check_behavior_fraud_ring_detected_label import RiskCheckBehaviorFraudRingDetectedLabelOrStr
from .enums.risk_check_behavior_user_interactions_label import RiskCheckBehaviorUserInteractionsLabelOrStr
from .enums.risk_level_with_no_data import RiskLevelWithNoDataOrStr


class RiskCheckBehavior(SdkBaseModel):
    """Result summary object specifying values for ``behavior`` attributes of risk check, when available."""

    user_interactions: RiskCheckBehaviorUserInteractionsLabelOrStr
    """Field describing the overall user interaction signals of a behavior risk check. This value represents how
    familiar the user is with the personal data they provide, based on a number of signals that are collected during
    their session.

    ``genuine`` indicates the user has high familiarity with the data they are providing, and that fraud is unlikely.

    ``neutral`` indicates some signals are present in between ``risky`` and ``genuine``, but there are not enough clear
    signals to determine an outcome.

    ``risky`` indicates the user has low familiarity with the data they are providing, and that fraud is likely.

    ``no_data`` indicates there is not sufficient information to give an accurate signal."""

    fraud_ring_detected: RiskCheckBehaviorFraudRingDetectedLabelOrStr
    """Field describing the outcome of a fraud ring behavior risk check.

    ``yes`` indicates that fraud ring activity was detected.

    ``no`` indicates that fraud ring activity was not detected.

    ``no_data`` indicates there was not enough information available to give an accurate signal."""

    bot_detected: RiskCheckBehaviorBotDetectedLabelOrStr
    """Field describing the outcome of a bot detection behavior risk check.

    ``yes`` indicates that automated activity was detected.

    ``no`` indicates that automated activity was not detected.

    ``no_data`` indicates there was not enough information available to give an accurate signal."""

    risk_level: Optional[RiskLevelWithNoDataOrStr] = UNSET
    """Risk level for the given risk check type, when available."""


class RiskCheckBehaviorDict(TypedDict):
    user_interactions: RiskCheckBehaviorUserInteractionsLabelOrStr
    fraud_ring_detected: RiskCheckBehaviorFraudRingDetectedLabelOrStr
    bot_detected: RiskCheckBehaviorBotDetectedLabelOrStr
    risk_level: NotRequired[RiskLevelWithNoDataOrStr]
