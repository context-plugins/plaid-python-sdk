from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxIncomeWebhookFireRequestWebhookCode(str, Enum):
    """The webhook codes that can be fired by this test endpoint."""

    INCOME_VERIFICATION = "INCOME_VERIFICATION"
    INCOME_VERIFICATION_RISK_SIGNALS = "INCOME_VERIFICATION_RISK_SIGNALS"

    __str__ = str.__str__


SandboxIncomeWebhookFireRequestWebhookCodeOrStr: TypeAlias = Annotated[
    SandboxIncomeWebhookFireRequestWebhookCode | str, open_enum_validator(SandboxIncomeWebhookFireRequestWebhookCode)
]
