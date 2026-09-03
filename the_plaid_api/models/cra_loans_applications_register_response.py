from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraLoansApplicationsRegisterResponse(SdkBaseModel):
    """CraLoansApplicationsRegisterResponse defines the response schema for ``/cra/loans/applications/register``."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CraLoansApplicationsRegisterResponseDict(TypedDict):
    request_id: str
