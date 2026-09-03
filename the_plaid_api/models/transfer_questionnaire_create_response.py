from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransferQuestionnaireCreateResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/questionnaire/create``"""

    onboarding_url: str
    """Plaid-hosted onboarding URL that you will redirect the end customer to."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferQuestionnaireCreateResponseDict(TypedDict):
    onboarding_url: str
    request_id: str
