from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationStatus5(str, Enum):
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

    AUTOMATICALLY_VERIFIED = "automatically_verified"
    PENDING_AUTOMATIC_VERIFICATION = "pending_automatic_verification"
    PENDING_MANUAL_VERIFICATION = "pending_manual_verification"
    UNSENT = "unsent"
    MANUALLY_VERIFIED = "manually_verified"
    VERIFICATION_EXPIRED = "verification_expired"
    VERIFICATION_FAILED = "verification_failed"
    DATABASE_MATCHED = "database_matched"
    DATABASE_INSIGHTS_PASS = "database_insights_pass"
    DATABASE_INSIGHTS_PASS_WITH_CAUTION = "database_insights_pass_with_caution"
    DATABASE_INSIGHTS_FAIL = "database_insights_fail"

    __str__ = str.__str__


VerificationStatus5OrStr: TypeAlias = Annotated[VerificationStatus5 | str, open_enum_validator(VerificationStatus5)]
