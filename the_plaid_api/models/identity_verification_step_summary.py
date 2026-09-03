from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.identity_verification_step_status import IdentityVerificationStepStatusOrStr


class IdentityVerificationStepSummary(SdkBaseModel):
    """Each step will be one of the following values:


    ``active`` - This step is the user's current step. They are either in the process of completing this step, or they
    recently closed their Identity Verification attempt while in the middle of this step. Only one step will be marked
    as ``active`` at any given point.

    ``success`` - The Identity Verification attempt has completed this step.

    ``failed`` - The user failed this step. This can either cause the user to fail the session as a whole, or cause them
    to fall back to another step depending on how the Identity Verification template is configured. A failed step does
    not imply a failed session.

    ``waiting_for_prerequisite`` - The user needs to complete another step first, before they progress to this step.
    This step may never run, depending on if the user fails an earlier step or if the step is only run as a fallback.

    ``not_applicable`` - This step will not be run for this session.

    ``skipped`` - The retry instructions that created this Identity Verification attempt specified that this step should
    be skipped.

    ``expired`` - This step had not yet been completed when the Identity Verification attempt as a whole expired.

    ``canceled`` - The Identity Verification attempt was canceled before the user completed this step.

    ``pending_review`` - The Identity Verification attempt template was configured to perform a screening that had one
    or more hits needing review.

    ``manually_approved`` - The step was manually overridden to pass by a team member in the dashboard.

    ``manually_rejected`` - The step was manually overridden to fail by a team member in the dashboard."""

    accept_tos: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    verify_sms: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    kyc_check: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    documentary_verification: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    selfie_check: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    watchlist_screening: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    risk_check: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""


class IdentityVerificationStepSummaryDict(TypedDict):
    accept_tos: IdentityVerificationStepStatusOrStr
    verify_sms: IdentityVerificationStepStatusOrStr
    kyc_check: IdentityVerificationStepStatusOrStr
    documentary_verification: IdentityVerificationStepStatusOrStr
    selfie_check: IdentityVerificationStepStatusOrStr
    watchlist_screening: IdentityVerificationStepStatusOrStr
    risk_check: IdentityVerificationStepStatusOrStr
