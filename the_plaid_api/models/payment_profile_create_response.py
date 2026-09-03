from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaymentProfileCreateResponse(SdkBaseModel):
    """PaymentProfileCreateResponse defines the response schema for ``/payment_profile/create``"""

    payment_profile_token: str
    """A payment profile token associated with the Payment Profile data that is being requested."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentProfileCreateResponseDict(TypedDict):
    payment_profile_token: str
    request_id: str
