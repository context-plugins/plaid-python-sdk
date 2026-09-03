from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LinkSessionSuccessMetadataAccount(SdkBaseModel):
    """An account attached to the connected Item."""

    id: Optional[str] = UNSET
    """The Plaid ``account_id``"""

    name: Optional[str] = UNSET
    """The official account name"""

    mask: OptionalNullable[str] = UNSET
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts. It may also not match the mask that the bank displays to the user."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The account type. See the `Account schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full
    list of possible values"""

    subtype: Optional[str] = UNSET
    """The account subtype. See the `Account schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a
    full list of possible values"""

    verification_status: OptionalNullable[str] = UNSET
    """Indicates an Item's micro-deposit-based verification or database verification status. This field is only
    populated when using Auth and falling back to micro-deposit or database verification. Possible values are:

    ``pending_automatic_verification``: The Item is pending automatic verification.

    ``pending_manual_verification``: The Item is pending manual micro-deposit verification. Items remain in this state
    until the user successfully verifies the code.

    ``automatically_verified``: The Item has successfully been automatically verified.

    ``manually_verified``: The Item has successfully been manually verified.

    ``verification_expired``: Plaid was unable to automatically verify the deposit within 7 calendar days and will no
    longer attempt to validate the Item. Users may retry by submitting their information again through Link.

    ``verification_failed``: The Item failed manual micro-deposit verification because the user exhausted all 3
    verification attempts. Users may retry by submitting their information again through Link.

    ``unsent``: The Item is pending micro-deposit verification, but Plaid has not yet sent the micro-deposit.

    ``database_insights_pending``: The Database Auth result is pending and will be available upon Auth request.

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
    returned for Auth Items created via Database Auth.

    ``database_matched``: (deprecated) The Item has successfully been verified using Plaid's data sources. Only returned
    for Auth Items created via Database Match.

    ``null`` or empty string: Neither micro-deposit-based verification nor database verification are being used for the
    Item."""

    class_type: OptionalNullable[str] = UNSET
    """If micro-deposit verification was being used, indicates the user's selection when asked if the account being
    verified is a ``business`` or ``personal`` account. This field is deprecated as Plaid no longer collects this
    information during the micro-deposit flow. To see whether an account is business or personal, use the
    ``holder_category`` field instead."""


class LinkSessionSuccessMetadataAccountDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    mask: NotRequired[str | None]
    type_: NotRequired[str]
    subtype: NotRequired[str]
    verification_status: NotRequired[str | None]
    class_type: NotRequired[str | None]
