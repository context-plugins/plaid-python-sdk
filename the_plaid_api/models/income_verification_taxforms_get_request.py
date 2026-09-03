from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class IncomeVerificationTaxformsGetRequest(SdkBaseModel):
    """IncomeVerificationTaxformsGetRequest defines the request schema for ``/income/verification/taxforms/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    income_verification_id: OptionalNullable[str] = UNSET
    """The ID of the verification."""

    access_token: OptionalNullable[str] = UNSET
    """The access token associated with the Item for which data is being requested."""


class IncomeVerificationTaxformsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    income_verification_id: NotRequired[str | None]
    access_token: NotRequired[str | None]
