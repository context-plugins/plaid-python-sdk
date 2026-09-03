from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProcessorStripeBankAccountTokenCreateResponse(SdkBaseModel):
    """ProcessorStripeBankAccountTokenCreateResponse defines the response schema for
    ``/processor/stripe/bank_account_token/create``"""

    stripe_bank_account_token: str
    """A token that can be sent to Stripe for use in making API calls to Plaid"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorStripeBankAccountTokenCreateResponseDict(TypedDict):
    stripe_bank_account_token: str
    request_id: str
