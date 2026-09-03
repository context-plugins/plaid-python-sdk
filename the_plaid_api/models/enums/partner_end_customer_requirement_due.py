from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartnerEndCustomerRequirementDue(str, Enum):
    """A field that may be required to be submitted for enablement."""

    LEGAL_ENTITY_NAME = "legal_entity_name"
    WEBSITE = "website"
    APPLICATION_NAME = "application_name"
    IS_DILIGENCE_ATTESTED = "is_diligence_attested"
    TECHNICAL_CONTACT = "technical_contact"
    BILLING_CONTACT = "billing_contact"
    ADDRESS = "address"
    BANK_ADDENDUM_ACCEPTANCE = "bank_addendum_acceptance"
    QUESTIONNAIRES_CRA = "questionnaires.cra"

    __str__ = str.__str__


PartnerEndCustomerRequirementDueOrStr: TypeAlias = Annotated[
    PartnerEndCustomerRequirementDue | str, open_enum_validator(PartnerEndCustomerRequirementDue)
]
