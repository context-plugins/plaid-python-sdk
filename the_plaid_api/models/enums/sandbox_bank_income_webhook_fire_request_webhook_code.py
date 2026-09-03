from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SandboxBankIncomeWebhookFireRequestWebhookCode(str, Enum):
    """The webhook codes this endpoint can be used to test"""

    BANK_INCOME_REFRESH_UPDATE = "BANK_INCOME_REFRESH_UPDATE"
    BANK_INCOME_REFRESH_COMPLETE = "BANK_INCOME_REFRESH_COMPLETE"

    __str__ = str.__str__


SandboxBankIncomeWebhookFireRequestWebhookCodeOrStr: TypeAlias = Annotated[
    SandboxBankIncomeWebhookFireRequestWebhookCode | str,
    open_enum_validator(SandboxBankIncomeWebhookFireRequestWebhookCode),
]
