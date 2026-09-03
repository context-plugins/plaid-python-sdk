from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProtectReportType(str, Enum):
    """The type of incident being reported.

    ``USER_ACCOUNT_TAKEOVER`` - Indicates that a legitimate user's account was accessed or controlled by an unauthorized
    party.

    ``FALSE_IDENTITY`` - Indicates that a user created an account using stolen or fabricated identity information.

    ``STOLEN_IDENTITY`` - Indicates that a user created an account using identity information belonging to a real
    individual without their consent.

    ``SYNTHETIC_IDENTITY`` - Indicates that a user created an account using a fake or partially fabricated identity
    (e.g., combining real and fake information to form a new persona).

    ``MULTIPLE_USER_ACCOUNTS`` - Indicates that the same individual is operating multiple accounts in violation of
    policy.

    ``SCAM_VICTIM`` - Indicates that the user was tricked into authorizing or sending funds as part of a scam.

    ``BANK_ACCOUNT_TAKEOVER`` - Indicates that a user's linked bank account was accessed or misused by an unauthorized
    party.

    ``BANK_CONNECTION_REVOKED`` - Indicates that a linked bank account connection was revoked by the financial
    institution, often due to suspected misuse, fraud, or security concerns.

    ``CARD_TESTING`` - Indicates that a card was used in small or repeated transactions to test its validity.

    ``UNAUTHORIZED_TRANSACTION`` - Indicates that a transaction was made without the user's consent or authorization.

    ``CARD_CHARGEBACK`` - Indicates that a card transaction was reversed via a chargeback claim.

    ``ACH_RETURN`` - Indicates that an ACH transaction was returned or reversed by the bank.

    ``DISPUTE`` - Indicates that a user filed a dispute regarding a transaction or account activity.

    ``FIRST_PARTY_FRAUD`` - Indicates that a user intentionally misrepresented themselves or their actions for financial
    gain.

    ``MISSED_PAYMENT`` - Indicates that a user failed to make a required payment on time.

    ``LOAN_STACKING`` - Indicates that a user applied for or took out multiple loans simultaneously beyond their ability
    to repay.

    ``MONEY_LAUNDERING`` - Indicates that funds are being moved through accounts to obscure their illicit origin.

    ``NO_FRAUD`` - Indicates that an investigation determined no fraudulent activity occurred on user/event (positive
    label).

    ``OTHER`` - Indicates that the case involves fraud or financial risk not covered by other report types. Requires
    notes describing the report."""

    USER_ACCOUNT_TAKEOVER = "USER_ACCOUNT_TAKEOVER"
    FALSE_IDENTITY = "FALSE_IDENTITY"
    STOLEN_IDENTITY = "STOLEN_IDENTITY"
    SYNTHETIC_IDENTITY = "SYNTHETIC_IDENTITY"
    MULTIPLE_USER_ACCOUNTS = "MULTIPLE_USER_ACCOUNTS"
    SCAM_VICTIM = "SCAM_VICTIM"
    BANK_ACCOUNT_TAKEOVER = "BANK_ACCOUNT_TAKEOVER"
    BANK_CONNECTION_REVOKED = "BANK_CONNECTION_REVOKED"
    CARD_TESTING = "CARD_TESTING"
    UNAUTHORIZED_TRANSACTION = "UNAUTHORIZED_TRANSACTION"
    CARD_CHARGEBACK = "CARD_CHARGEBACK"
    ACH_RETURN = "ACH_RETURN"
    DISPUTE = "DISPUTE"
    FIRST_PARTY_FRAUD = "FIRST_PARTY_FRAUD"
    MISSED_PAYMENT = "MISSED_PAYMENT"
    LOAN_STACKING = "LOAN_STACKING"
    MONEY_LAUNDERING = "MONEY_LAUNDERING"
    NO_FRAUD = "NO_FRAUD"
    OTHER = "OTHER"

    __str__ = str.__str__


ProtectReportTypeOrStr: TypeAlias = Annotated[ProtectReportType | str, open_enum_validator(ProtectReportType)]
