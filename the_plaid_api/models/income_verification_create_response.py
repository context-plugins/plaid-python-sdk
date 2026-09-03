from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IncomeVerificationCreateResponse(SdkBaseModel):
    """IncomeVerificationCreateResponse defines the response schema for ``/income/verification/create``."""

    income_verification_id: str
    """ID of the verification. This ID is persisted throughout the lifetime of the verification."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IncomeVerificationCreateResponseDict(TypedDict):
    income_verification_id: str
    request_id: str
