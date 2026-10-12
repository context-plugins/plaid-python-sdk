from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateRequestIdentityVerification(SdkBaseModel):
    """Specifies option for initializing Link for use with the Identity Verification product."""

    template_id: str
    consent: Optional[bool] = UNSET
    gave_consent: bool = False
    """A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be
    shared with Plaid for verification purposes.

    If ``gave_consent`` is set to ``true``, the ``accept_tos`` step will be marked as ``skipped`` and the end user's
    session will start at the next step requirement."""


class LinkTokenCreateRequestIdentityVerificationDict(TypedDict):
    template_id: str
    consent: NotRequired[bool]
    gave_consent: NotRequired[bool]
