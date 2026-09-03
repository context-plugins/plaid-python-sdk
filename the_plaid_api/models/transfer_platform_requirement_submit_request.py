from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .requirement_submission import RequirementSubmission, RequirementSubmissionDict


class TransferPlatformRequirementSubmitRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/platform/requirement/submit``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: str
    """The client ID of the originator"""

    requirement_submissions: list[RequirementSubmission]
    """Use the ``/transfer/platform/requirement/submit`` endpoint to submit a list of requirement submissions that all
    relate to the originator. Must contain between 1 and 50 requirement submissions. See `Requirement type schema
    documentation <https://docs.google.com/document/d/1NEQkTD0sVK50iAQi6xHigrexDUxZ4QxXqSEfV_FFTiU/>`__ for a list of
    requirements and possible values."""


class TransferPlatformRequirementSubmitRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: str
    requirement_submissions: list[RequirementSubmission | RequirementSubmissionDict]
