from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .employment_verification import EmploymentVerification, EmploymentVerificationDict


class EmploymentVerificationGetResponse(SdkBaseModel):
    """EmploymentVerificationGetResponse defines the response schema for ``/employment/verification/get``."""

    employments: list[EmploymentVerification]
    """A list of employment verification summaries."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class EmploymentVerificationGetResponseDict(TypedDict):
    employments: list[EmploymentVerificationDict]
    request_id: str
