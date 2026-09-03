from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerCrauseCase(str, Enum):
    """A CRA use case under a permissible purpose."""

    CREDIT_UNDERWRITING = "CREDIT_UNDERWRITING"
    TENANT_SCREENING = "TENANT_SCREENING"
    INVESTOR_OR_SERVICER_OF_CREDIT = "INVESTOR_OR_SERVICER_OF_CREDIT"
    UTILITIES = "UTILITIES"
    BANK_ACCOUNT_OPENING = "BANK_ACCOUNT_OPENING"
    IDENTITY_VERIFICATION_FRAUD_PREVENTION = "IDENTITY_VERIFICATION_FRAUD_PREVENTION"
    COLLECTIONS_DEBT_RECOVERY = "COLLECTIONS_DEBT_RECOVERY"

    __str__ = str.__str__


PartnerEndCustomerCrauseCaseOrStr: TypeAlias = Annotated[
    PartnerEndCustomerCrauseCase | str, open_enum_validator(PartnerEndCustomerCrauseCase)
]
