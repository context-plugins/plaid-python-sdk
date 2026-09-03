from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BeaconAccountRiskEvaluateEvaluationReason(str, Enum):
    """Description of the reason you want to evaluate risk. ``ONBOARDING``: user links a first bank account as part of
    the onboarding flow of your platform. ``NEW_ACCOUNT``: user links another bank account or replaces the currently
    linked bank account on your platform. ``INFORMATION_CHANGE``: user changes their information on your platform, e.g.,
    updating their phone number. ``DORMANT_USER``: you decide to re-evaluate a user that becomes active after a period
    of inactivity. ``OTHER``: any other reasons not listed here Possible values: ``ONBOARDING``, ``NEW_ACCOUNT``,
    ``INFORMATION_CHANGE``, ``DORMANT_USER``, ``OTHER``"""

    ONBOARDING = "ONBOARDING"
    NEW_ACCOUNT = "NEW_ACCOUNT"
    INFORMATION_CHANGE = "INFORMATION_CHANGE"
    DORMANT_USER = "DORMANT_USER"
    OTHER = "OTHER"

    __str__ = str.__str__


BeaconAccountRiskEvaluateEvaluationReasonOrStr: TypeAlias = Annotated[
    BeaconAccountRiskEvaluateEvaluationReason | str, open_enum_validator(BeaconAccountRiskEvaluateEvaluationReason)
]
