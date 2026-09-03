from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaxpayerIdentifierType(str, Enum):
    """A value from a MISMO prescribed list that classifies identification numbers used by the Internal Revenue Service
    (IRS) in the administration of tax laws. A Social Security number (SSN) is issued by the SSA; all other taxpayer
    identification numbers are issued by the IRS."""

    INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER = "IndividualTaxpayerIdentificationNumber"
    SOCIAL_SECURITY_NUMBER = "SocialSecurityNumber"

    __str__ = str.__str__


TaxpayerIdentifierTypeOrStr: TypeAlias = Annotated[
    TaxpayerIdentifierType | str, open_enum_validator(TaxpayerIdentifierType)
]
