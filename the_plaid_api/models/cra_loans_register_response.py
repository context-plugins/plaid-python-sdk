from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraLoansRegisterResponse(SdkBaseModel):
    """CraLoansRegisterResponse defines the response schema for ``/cra/loans/register``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CraLoansRegisterResponseDict(TypedDict):
    request_id: str
