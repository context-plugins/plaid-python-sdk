from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .income_verification_create_request_options import (
    IncomeVerificationCreateRequestOptions,
    IncomeVerificationCreateRequestOptionsDict,
)


class IncomeVerificationCreateRequest(SdkBaseModel):
    """IncomeVerificationCreateRequest defines the request schema for ``/income/verification/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    webhook: str
    """The URL endpoint to which Plaid should send webhooks related to the progress of the income verification
    process."""

    precheck_id: Optional[str] = UNSET
    """The ID of a precheck created with ``/income/verification/precheck``. Will be used to improve conversion of the
    income verification flow."""

    options: Optional[IncomeVerificationCreateRequestOptions] = UNSET
    """Optional arguments for ``/income/verification/create``"""


class IncomeVerificationCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    webhook: str
    precheck_id: NotRequired[str]
    options: NotRequired[IncomeVerificationCreateRequestOptionsDict]
