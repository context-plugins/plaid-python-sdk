from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkEventMetadata(SdkBaseModel):
    """Metadata about an event that occurred while the user was going through Link"""

    error_code: Optional[str] = UNSET
    """The error code that the user encountered. Emitted by ``ERROR``, ``EXIT``."""

    error_message: Optional[str] = UNSET
    """The error message that the user encountered. Emitted by: ``ERROR``, ``EXIT``."""

    error_type: Optional[str] = UNSET
    """The error type that the user encountered. Emitted by: ``ERROR``, ``EXIT``."""

    exit_status: Optional[str] = UNSET
    """The status key indicates the point at which the user exited the Link flow. Emitted by: ``EXIT``."""

    institution_id: Optional[str] = UNSET
    """The ID of the selected institution. Emitted by: all events."""

    institution_name: Optional[str] = UNSET
    """The name of the selected institution. Emitted by: all events."""

    institution_search_query: Optional[str] = UNSET
    """The query used to search for institutions. Emitted by: ``SEARCH_INSTITUTION``."""

    request_id: Optional[str] = UNSET
    """The request ID for the last request made by Link. This can be shared with Plaid support to expedite
    investigation. Emitted by: all events."""

    mfa_type: Optional[str] = UNSET
    """If set, the user has encountered one of the following MFA types: code, device, questions, selections. Emitted by:
    ``SUBMIT_MFA`` and ``TRANSITION_VIEW`` when ``view_name`` is ``MFA``."""

    view_name: Optional[str] = UNSET
    """The name of the view that is being transitioned to. Emitted by: ``TRANSITION_VIEW``."""

    selection: Optional[str] = UNSET
    """Either the verification method for a matched institution selected by the user or the Auth Type Select flow type
    selected by the user. If selection is used to describe selected verification method, then possible values are
    ``phoneotp`` or ``password``; if selection is used to describe the selected Auth Type Select flow, then possible
    values are ``flow_type_manual`` or ``flow_type_instant``. Emitted by: ``MATCHED_SELECT_VERIFY_METHOD`` and
    ``SELECT_AUTH_TYPE``."""

    brand_name: Optional[str] = UNSET
    """The name of the selected brand."""

    match_reason: Optional[str] = UNSET
    """The reason this institution was matched. This will be either ``returning_user`` or ``routing_number`` if emitted
    by ``MATCHED_SELECT_INSTITUTION``. Otherwise, this will be ``SAVED_INSTITUTION`` or
    ``AUTO_SELECT_SAVED_INSTITUTION`` if emitted by ``SELECT_INSTITUTION``."""

    routing_number: Optional[str] = UNSET
    """The routing number submitted by the user at the micro-deposits routing number pane. Emitted by
    ``SUBMIT_ROUTING_NUMBER``."""

    account_number_mask: Optional[str] = UNSET
    """The account number mask extracted from the user-provided account number. If the user-inputted account number is
    four digits long, ``account_number_mask`` is empty. Emitted by ``SUBMIT_ACCOUNT_NUMBER``."""


class LinkEventMetadataDict(TypedDict):
    error_code: NotRequired[str]
    error_message: NotRequired[str]
    error_type: NotRequired[str]
    exit_status: NotRequired[str]
    institution_id: NotRequired[str]
    institution_name: NotRequired[str]
    institution_search_query: NotRequired[str]
    request_id: NotRequired[str]
    mfa_type: NotRequired[str]
    view_name: NotRequired[str]
    selection: NotRequired[str]
    brand_name: NotRequired[str]
    match_reason: NotRequired[str]
    routing_number: NotRequired[str]
    account_number_mask: NotRequired[str]
