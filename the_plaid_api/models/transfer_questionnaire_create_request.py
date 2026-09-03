from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferQuestionnaireCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/questionnaire/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    originator_client_id: str
    """Client ID of the end customer."""

    redirect_uri: str
    """URL the end customer will be redirected to after completing questions in Plaid-hosted onboarding flow."""


class TransferQuestionnaireCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    originator_client_id: str
    redirect_uri: str
