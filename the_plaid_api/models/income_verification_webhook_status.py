from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IncomeVerificationWebhookStatus(SdkBaseModel):
    """Status of the income verification webhook"""

    id: str


class IncomeVerificationWebhookStatusDict(TypedDict):
    id: str
