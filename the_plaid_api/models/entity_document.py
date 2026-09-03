from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.entity_document_type import EntityDocumentTypeOrStr


class EntityDocument(SdkBaseModel):
    """An official document, usually issued by a governing body or institution, with an associated identifier."""

    type_: EntityDocumentTypeOrStr = Field(alias="type")
    """The kind of official document represented by this object.

    ``bik`` - Russian bank code

    ``business_number`` - A number that uniquely identifies the business within a category of businesses

    ``imo`` - Number assigned to the entity by the International Maritime Organization

    ``other`` - Any document not covered by other categories

    ``swift`` - Number identifying a bank and branch.

    ``tax_id`` - Identification issued for the purpose of collecting taxes"""

    number: str
    """The numeric or alphanumeric identifier associated with this document. Must be between 4 and 32 characters long,
    and cannot have leading or trailing spaces."""


class EntityDocumentDict(TypedDict):
    type_: EntityDocumentTypeOrStr
    number: str
