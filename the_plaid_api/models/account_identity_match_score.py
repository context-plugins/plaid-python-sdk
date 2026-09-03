from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .account_balance import AccountBalance, AccountBalanceDict
from .address_match_score import AddressMatchScore, AddressMatchScoreDict
from .email_address_match_score import EmailAddressMatchScore, EmailAddressMatchScoreDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr
from .enums.holder_category import HolderCategoryOrStr
from .enums.verification_status5 import VerificationStatus5OrStr
from .name_match_score import NameMatchScore, NameMatchScoreDict
from .phone_number_match_score import PhoneNumberMatchScore, PhoneNumberMatchScoreDict
from .verification_insights import VerificationInsights, VerificationInsightsDict


class AccountIdentityMatchScore(SdkBaseModel):
    """Identity match scores for an account"""

    account_id: str
    """Plaid's unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    The ``account_id`` can also change if the ``access_token`` is deleted and the same credentials that were used to
    generate that ``access_token`` are used to generate a new ``access_token`` on a later date. In that case, the new
    ``account_id`` will be different from the old ``account_id``.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    When using a CRA endpoint (an endpoint associated with Plaid Check Consumer Report, i.e. any endpoint beginning with
    ``/cra/``), the ``account_id`` returned will not match the ``account_id`` returned by a non-CRA endpoint.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    balances: AccountBalance
    """A set of fields describing the balance for an account. For real-time values, use ``/accounts/balance/get`` or
    ``/signal/evaluate`` (with a Balance-only ruleset), which are fetched live from the institution at request time.
    Values returned by other endpoints may be cached, or adjusted by Plaid to reflect transaction activity received
    since the last refresh."""

    mask: str | None
    """The last 2-4 alphanumeric characters of either the account's displayed mask or the account's official account
    number. Note that the mask may be non-unique between an Item's accounts."""

    name: str
    """The name of the account, either assigned by the user or by the financial institution itself"""

    official_name: str | None
    """The official name of the account as given by the financial institution"""

    type_: AccountTypeOrStr = Field(alias="type")
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    subtype: AccountSubtypeOrStr | None
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    verification_status: Optional[VerificationStatus5OrStr] = UNSET
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

    verification_name: Optional[str] = UNSET
    """The account holder name that was used for micro-deposit and/or database verification. Only returned for Auth
    Items created via micro-deposit or database verification. This name was manually-entered by the user during Link,
    unless it was otherwise provided via the ``user.legal_name`` request field in ``/link/token/create`` for the Link
    session that created the Item."""

    verification_insights: Optional[VerificationInsights] = UNSET
    """Insights from performing database verification for the account. Only returned for Auth Items using Database
    Auth."""

    persistent_account_id: Optional[str] = UNSET
    """A unique and persistent identifier for accounts that can be used to trace multiple instances of the same account
    across different Items for depository accounts. This field is currently supported only for Items at institutions
    that use Tokenized Account Numbers (i.e., Chase, PNC, and US Bank). Because these accounts have a different account
    number each time they are linked, this field may be used instead of the account number to uniquely identify an
    account across multiple Items for payments use cases, helping to reduce duplicate Items or attempted fraud. In
    Sandbox, this field is populated for TAN-based institutions (``ins_56``, ``ins_13``, ``ins_127990``) as well as the
    OAuth Sandbox institution (``ins_127287``); in Production, it will only be populated for accounts at applicable
    institutions."""

    holder_category: OptionalNullable[HolderCategoryOrStr] = UNSET
    """Indicates the account's categorization as either a personal or a business account. This field is currently in
    beta; to request access, contact your account manager."""

    legal_name: OptionalNullable[NameMatchScore] = UNSET
    """Score found by matching name provided by the API with the name on the account at the financial institution. If
    the account contains multiple owners, the maximum match score is filled."""

    phone_number: OptionalNullable[PhoneNumberMatchScore] = UNSET
    """Score found by matching phone number provided by the API with the phone number on the account at the financial
    institution. 100 is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match
    score is filled."""

    email_address: OptionalNullable[EmailAddressMatchScore] = UNSET
    """Score found by matching email provided by the API with the email on the account at the financial institution. 100
    is a perfect match and 0 is a no match. If the account contains multiple owners, the maximum match score is
    filled."""

    address: OptionalNullable[AddressMatchScore] = UNSET
    """Score found by matching address provided by the API with the address on the account at the financial institution.
    The score can range from 0 to 100 where 100 is a perfect match and 0 is a no match. If the account contains multiple
    owners, the maximum match score is filled."""


class AccountIdentityMatchScoreDict(TypedDict):
    account_id: str
    balances: AccountBalance | AccountBalanceDict
    mask: str | None
    name: str
    official_name: str | None
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr | None
    verification_status: NotRequired[VerificationStatus5OrStr]
    verification_name: NotRequired[str]
    verification_insights: NotRequired[VerificationInsights | VerificationInsightsDict]
    persistent_account_id: NotRequired[str]
    holder_category: NotRequired[HolderCategoryOrStr | None]
    legal_name: NotRequired[NameMatchScore | NameMatchScoreDict | None]
    phone_number: NotRequired[PhoneNumberMatchScore | PhoneNumberMatchScoreDict | None]
    email_address: NotRequired[EmailAddressMatchScore | EmailAddressMatchScoreDict | None]
    address: NotRequired[AddressMatchScore | AddressMatchScoreDict | None]
