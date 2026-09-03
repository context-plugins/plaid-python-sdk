from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProtectLinkModelInputs(SdkBaseModel):
    """Inputs for link session Trust Index models."""

    link_session_id: str
    """A unique identifier for the Link session, used to compute a Trust Index score and fraud attributes."""

    require_extracted_data: Optional[bool] = UNSET
    """Controls whether transaction extraction must be complete before scoring. If ``false`` (default), returns a score
    whether or not transaction extraction is complete, as long as the link session is finished; if data has been
    extracted it will still be included in the score computation. If ``true``, returns HTTP 400 with ``error_type`` =
    ``INVALID_REQUEST`` and ``error_code`` = ``FAILED_PRECONDITION`` if extraction is still in progress; once data is
    ready a score will be returned normally."""


class ProtectLinkModelInputsDict(TypedDict):
    link_session_id: str
    require_extracted_data: NotRequired[bool]
