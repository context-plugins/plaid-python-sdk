from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .verification_insights import VerificationInsights, VerificationInsightsDict


class AuthVerifyResponse(SdkBaseModel):
    """AuthVerifyResponse defines the response schema for ``/auth/verify``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    item_id: OptionalNullable[str] = UNSET
    """The ``item_id`` value of the Item created for verification. If numbers data provided is invalid, an Item may not
    be created."""

    verification_status: str
    """Indicates the Item's database verification status. Possible values are:

    ``database_insights_fail``: The Item's numbers have been verified using Plaid's data sources and have signal for
    being invalid and/or have no signal for being valid. Typically this indicates that the routing number is invalid,
    the account number does not match the account number format associated with the routing number, or the account has
    been reported as closed or frozen. Only returned for Auth Items created via Database Auth.

    ``database_insights_pass``: The Item's numbers have been verified using Plaid's data sources: the routing and
    account number match a routing and account number of an account recognized on the Plaid network, and the account is
    not known by Plaid to be frozen or closed. Only returned for Auth Items created via Database Auth.

    ``database_insights_pass_with_caution``: The Item's numbers have been verified using Plaid's data sources and have
    some signal for being valid: the routing and account number were not recognized on the Plaid network, but the
    routing number is valid and the account number is a potential valid account number for that routing number. Only
    returned for Auth Items created via Database Auth."""

    verification_insights: VerificationInsights
    """Insights from performing database verification for the account. Only returned for Auth Items using Database
    Auth."""


class AuthVerifyResponseDict(TypedDict):
    request_id: str
    item_id: NotRequired[str | None]
    verification_status: str
    verification_insights: VerificationInsightsDict
