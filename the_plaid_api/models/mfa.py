from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Mfa(SdkBaseModel):
    """Specifies the multi-factor authentication settings to use with this test account"""

    type_: str = Field(alias="type")
    """Possible values are ``device``, ``selections``, or ``questions``.

    If value is ``device``, the MFA answer is ``1234``.

    If value is ``selections``, the MFA answer is always the first option.

    If value is ``questions``, the MFA answer is ``answer_<i>_<j>`` for the j-th question in the i-th round, starting
    from 0. For example, the answer to the first question in the second round is ``answer_1_0``."""

    question_rounds: float
    """Number of rounds of questions. Required if value of ``type`` is ``questions``."""

    questions_per_round: float
    """Number of questions per round. Required if value of ``type`` is ``questions``. If value of type is
    ``selections``, default value is 2."""

    selection_rounds: float
    """Number of rounds of selections, used if ``type`` is ``selections``. Defaults to 1."""

    selections_per_question: float
    """Number of available answers per question, used if ``type`` is ``selections``. Defaults to 2."""


class MfaDict(TypedDict):
    type_: str
    question_rounds: float
    questions_per_round: float
    selection_rounds: float
    selections_per_question: float
