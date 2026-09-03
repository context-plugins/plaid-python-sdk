from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.flow_type import FlowTypeOrStr
from .enums.reroute_to_credentials import RerouteToCredentialsOrStr


class LinkTokenCreateRequestAuth(SdkBaseModel):
    """Specifies options for initializing Link for use with the Auth product. This field can be used to enable or
    disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be
    configured by your account manager. The default behavior described in the documentation is the default behavior that
    will apply if you have not requested your account manager to apply a different default. If you have enabled the
    `Dashboard Account Verification pane <https://dashboard.plaid.com/account-verification>`__, the settings enabled
    there will override any settings in this object."""

    auth_type_select_enabled: Optional[bool] = UNSET
    """Specifies whether Auth Type Select is enabled for the Link session, allowing the end user to choose between
    linking via a credentials-based flow (i.e. Instant Auth, Instant Match, Automated Micro-deposits) or a manual flow
    that does not require login (all other Auth flows) prior to selecting their financial institution. Default behavior
    is ``false``."""

    automated_microdeposits_enabled: Optional[bool] = UNSET
    """Specifies whether the Link session is enabled for the Automated Micro-deposits flow. Default behavior is
    ``false``."""

    instant_match_enabled: Optional[bool] = UNSET
    """Specifies whether the Link session is enabled for the Instant Match flow. Instant Match is enabled by default.
    Instant Match can be disabled by setting this field to ``false``."""

    same_day_microdeposits_enabled: Optional[bool] = UNSET
    """Specifies whether the Link session is enabled for the Same-Day Micro-deposits flow. Default behavior is
    ``false``."""

    instant_microdeposits_enabled: Optional[bool] = UNSET
    """Specifies whether the Link session is enabled for the Instant Micro-deposits flow. Default behavior for Plaid
    teams created after November 2023 is ``false``; default behavior for Plaid teams created before that date is
    ``true``."""

    reroute_to_credentials: Optional[RerouteToCredentialsOrStr] = UNSET
    """Specifies what type of `Reroute to Credentials
    <https://plaid.com/docs/auth/coverage/flow-options/#removing-manual-verification-entry-points-with-reroute-to-credentials>`__
    pane should be used in the Link session for the Same-Day Micro-deposits flow. Default behavior is ``OPTIONAL``."""

    database_match_enabled: Optional[bool] = UNSET
    """Database Match has been deprecated and replaced with Database Auth. Use the `Account Verification Dashboard
    <https://dashboard.plaid.com/account-verification>`__ to enable Database Auth."""

    database_insights_enabled: Optional[bool] = UNSET
    """Database Insights has been deprecated and replaced with Database Auth. Use the `Account Verification Dashboard
    <https://dashboard.plaid.com/account-verification>`__ to enable Database Auth. In Canada, Database Auth is in early
    availability and cannot yet be managed via the Dashboard; it must be enabled by passing ``database_insights_enabled:
    true`` in ``/link/token/create``."""

    flow_type: Optional[FlowTypeOrStr] = UNSET
    """This field has been deprecated in favor of ``auth_type_select_enabled``."""

    sms_microdeposits_verification_enabled: Optional[bool] = UNSET
    """Specifies whether the Link session is enabled for SMS micro-deposits verification. Default behavior is
    ``true``."""


class LinkTokenCreateRequestAuthDict(TypedDict):
    auth_type_select_enabled: NotRequired[bool]
    automated_microdeposits_enabled: NotRequired[bool]
    instant_match_enabled: NotRequired[bool]
    same_day_microdeposits_enabled: NotRequired[bool]
    instant_microdeposits_enabled: NotRequired[bool]
    reroute_to_credentials: NotRequired[RerouteToCredentialsOrStr]
    database_match_enabled: NotRequired[bool]
    database_insights_enabled: NotRequired[bool]
    flow_type: NotRequired[FlowTypeOrStr]
    sms_microdeposits_verification_enabled: NotRequired[bool]
