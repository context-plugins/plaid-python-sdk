from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EntityDocumentType(str, Enum):
    """The kind of official document represented by this object.

    ``bik`` - Russian bank code

    ``business_number`` - A number that uniquely identifies the business within a category of businesses

    ``imo`` - Number assigned to the entity by the International Maritime Organization

    ``other`` - Any document not covered by other categories

    ``swift`` - Number identifying a bank and branch.

    ``tax_id`` - Identification issued for the purpose of collecting taxes"""

    BIK = "bik"
    BUSINESS_NUMBER = "business_number"
    IMO = "imo"
    OTHER = "other"
    SWIFT = "swift"
    TAX_ID = "tax_id"

    __str__ = str.__str__


EntityDocumentTypeOrStr: TypeAlias = Annotated[EntityDocumentType | str, open_enum_validator(EntityDocumentType)]
