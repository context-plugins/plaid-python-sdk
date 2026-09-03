from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .documentary_verification import DocumentaryVerification, DocumentaryVerificationDict
from .enums.identity_verification_status import IdentityVerificationStatusOrStr
from .identity_verification_step_summary import IdentityVerificationStepSummary, IdentityVerificationStepSummaryDict
from .identity_verification_template_reference import (
    IdentityVerificationTemplateReference,
    IdentityVerificationTemplateReferenceDict,
)
from .identity_verification_user_data import IdentityVerificationUserData, IdentityVerificationUserDataDict
from .idvprotect_event import IdvprotectEvent, IdvprotectEventDict
from .kyccheck_details import KyccheckDetails, KyccheckDetailsDict
from .risk_check_details import RiskCheckDetails, RiskCheckDetailsDict
from .selfie_check import SelfieCheck, SelfieCheckDict
from .verify_smsdetails import VerifySmsdetails, VerifySmsdetailsDict


class IdentityVerificationRetryResponse(SdkBaseModel):
    """An identity verification attempt represents a customer's attempt to verify their identity, reflecting the
    required steps for completing the session, the results for each step, and information collected in the process."""

    id: str
    """ID of the associated Identity Verification attempt."""

    client_user_id: str
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    completed_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    previous_attempt_id: str | None
    """The ID for the Identity Verification preceding this session. This field will only be filled if the current
    Identity Verification is a retry of a previous attempt."""

    shareable_url: str | None
    """A shareable URL that can be sent directly to the user to complete verification"""

    template: IdentityVerificationTemplateReference
    """The resource ID and version number of the template configuring the behavior of a given Identity Verification."""

    user: IdentityVerificationUserData
    """The identity data that was either collected from the user or provided via API in order to perform an Identity
    Verification."""

    status: IdentityVerificationStatusOrStr
    """The status of this Identity Verification attempt.


    ``active`` - The Identity Verification attempt is incomplete. The user may have completed part of the session, but
    has neither failed nor passed.

    ``success`` - The Identity Verification attempt has completed, passing all steps defined to the associated Identity
    Verification template.

    ``failed`` - The user failed one or more steps in the session and was told to contact support.

    ``expired`` - The Identity Verification attempt was active for a long period of time without being completed and was
    automatically marked as expired. Note that sessions currently do not expire. Automatic expiration is expected to be
    enabled in the future.

    ``canceled`` - The Identity Verification attempt was canceled, either via the dashboard by a user, or via API. The
    user may have completed part of the session, but has neither failed nor passed.

    ``pending_review`` - The Identity Verification attempt template was configured to perform a screening that had one
    or more hits needing review."""

    steps: IdentityVerificationStepSummary
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

    documentary_verification: DocumentaryVerification | None
    """Data, images, analysis, and results from the ``documentary_verification`` step. This field will be ``null``
    unless ``steps.documentary_verification`` has reached a terminal state of either ``success`` or ``failed``."""

    selfie_check: SelfieCheck | None
    """Additional information for the ``selfie_check`` step. This field will be ``null`` unless ``steps.selfie_check``
    has reached a terminal state of either ``success`` or ``failed``."""

    kyc_check: KyccheckDetails | None
    """Additional information for the ``kyc_check`` (Data Source Verification) step. This field will be ``null`` unless
    ``steps.kyc_check`` has reached a terminal state of either ``success`` or ``failed``."""

    risk_check: RiskCheckDetails | None
    """Additional information for the ``risk_check`` step."""

    verify_sms: VerifySmsdetails | None
    """Additional information for the ``verify_sms`` step."""

    watchlist_screening_id: str | None
    """ID of the associated screening."""

    beacon_user_id: str | None
    """Beacon is deprecated in favor of Plaid Protect. This field is only populated for users of the deprecated Beacon
    product."""

    user_id: str | None
    """Unique user identifier, created by calling ``/user/create``. Either a ``user_id`` or the ``client_user_id`` must
    be provided. The ``user_id`` may only be used instead of the ``client_user_id`` if you were not a pre-existing user
    of ``/user/create`` as of December 10, 2025, or if you have since `migrated to the new User APIs
    <https://plaid.com/docs/api/users/migrate-to-new-user-apis>`__; for more details, see `New User APIs
    <https://plaid.com/docs/api/users/user-apis>`__. If both this field and a ``client_user_id`` are present in a
    request, the ``user_id`` must have been created from the provided ``client_user_id``."""

    redacted_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    latest_scored_protect_event: OptionalNullable[IdvprotectEvent] = UNSET
    """Information about a Protect event including Trust Index score and fraud attributes."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IdentityVerificationRetryResponseDict(TypedDict):
    id: str
    client_user_id: str
    created_at: RFC3339DateTime
    completed_at: RFC3339DateTime | None
    previous_attempt_id: str | None
    shareable_url: str | None
    template: IdentityVerificationTemplateReference | IdentityVerificationTemplateReferenceDict
    user: IdentityVerificationUserData | IdentityVerificationUserDataDict
    status: IdentityVerificationStatusOrStr
    steps: IdentityVerificationStepSummary | IdentityVerificationStepSummaryDict
    documentary_verification: DocumentaryVerification | DocumentaryVerificationDict | None
    selfie_check: SelfieCheck | SelfieCheckDict | None
    kyc_check: KyccheckDetails | KyccheckDetailsDict | None
    risk_check: RiskCheckDetails | RiskCheckDetailsDict | None
    verify_sms: VerifySmsdetails | VerifySmsdetailsDict | None
    watchlist_screening_id: str | None
    beacon_user_id: str | None
    user_id: str | None
    redacted_at: RFC3339DateTime | None
    latest_scored_protect_event: NotRequired[IdvprotectEvent | IdvprotectEventDict | None]
    request_id: str
