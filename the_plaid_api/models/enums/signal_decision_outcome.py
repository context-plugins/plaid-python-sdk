from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SignalDecisionOutcome(str, Enum):
    """The payment decision from the risk assessment.

    ``APPROVE``: approve the transaction without requiring further actions from your customers. For example, use this
    field if you are placing a standard hold for all the approved transactions before making funds available to your
    customers. You should also use this field if you decide to accelerate the fund availability for your customers.

    ``REVIEW``: the transaction requires manual review

    ``REJECT``: reject the transaction

    ``TAKE_OTHER_RISK_MEASURES``: for example, placing a longer hold on funds than those approved transactions or
    introducing customer frictions such as step-up verification/authentication

    ``NOT_EVALUATED``: if only logging the results without using them"""

    APPROVE = "APPROVE"
    REVIEW = "REVIEW"
    REJECT = "REJECT"
    TAKE_OTHER_RISK_MEASURES = "TAKE_OTHER_RISK_MEASURES"
    NOT_EVALUATED = "NOT_EVALUATED"

    __str__ = str.__str__


SignalDecisionOutcomeOrStr: TypeAlias = Annotated[
    SignalDecisionOutcome | str, open_enum_validator(SignalDecisionOutcome)
]
