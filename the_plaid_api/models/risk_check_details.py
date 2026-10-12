from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.identity_verification_step_status import IdentityVerificationStepStatusOrStr
from .risk_check_behavior import RiskCheckBehavior, RiskCheckBehaviorDict
from .risk_check_device import RiskCheckDevice, RiskCheckDeviceDict
from .risk_check_email import RiskCheckEmail, RiskCheckEmailDict
from .risk_check_facial_duplicate import RiskCheckFacialDuplicate, RiskCheckFacialDuplicateDict
from .risk_check_identity_abuse_signals import RiskCheckIdentityAbuseSignals, RiskCheckIdentityAbuseSignalsDict
from .risk_check_network import RiskCheckNetwork, RiskCheckNetworkDict
from .risk_check_phone import RiskCheckPhone, RiskCheckPhoneDict


class RiskCheckDetails(SdkBaseModel):
    """Additional information for the ``risk_check`` step."""

    status: IdentityVerificationStepStatusOrStr
    """The status of a step in the Identity Verification process."""

    behavior: RiskCheckBehavior | None
    """Result summary object specifying values for ``behavior`` attributes of risk check, when available."""

    email: RiskCheckEmail | None
    """Result summary object specifying values for ``email`` attributes of risk check."""

    phone: RiskCheckPhone | None
    """Result summary object specifying values for ``phone`` attributes of risk check."""

    devices: list[RiskCheckDevice]
    """Array of result summary objects specifying values for ``device`` attributes of risk check."""

    identity_abuse_signals: RiskCheckIdentityAbuseSignals | None
    """Result summary object capturing abuse signals related to ``identity abuse``, e.g. stolen and synthetic identity
    fraud. These attributes are only available for US identities and some signals may not be available depending on what
    information was collected."""

    network: OptionalNullable[RiskCheckNetwork] = UNSET
    """Result summary object specifying values for network attributes of risk check."""

    facial_duplicates: list[RiskCheckFacialDuplicate]
    """The attributes related to the facial duplicates captured in risk check."""

    trust_index_score: int | None
    """The trust index score for the ``risk_check`` step."""


class RiskCheckDetailsDict(TypedDict):
    status: IdentityVerificationStepStatusOrStr
    behavior: RiskCheckBehaviorDict | None
    email: RiskCheckEmailDict | None
    phone: RiskCheckPhoneDict | None
    devices: list[RiskCheckDeviceDict]
    identity_abuse_signals: RiskCheckIdentityAbuseSignalsDict | None
    network: NotRequired[RiskCheckNetworkDict | None]
    facial_duplicates: list[RiskCheckFacialDuplicateDict]
    trust_index_score: int | None
