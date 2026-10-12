from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .enums.physical_document_category import PhysicalDocumentCategoryOrStr
from .identity_verification_document_address_response import (
    IdentityVerificationDocumentAddressResponse,
    IdentityVerificationDocumentAddressResponseDict,
)
from .identity_verification_document_name_response import (
    IdentityVerificationDocumentNameResponse,
    IdentityVerificationDocumentNameResponseDict,
)


class PhysicalDocumentExtractedData(SdkBaseModel):
    """Data extracted from a user-submitted document."""

    id_number: str | None
    """Alpha-numeric ID number extracted via OCR from the user's document image."""

    category: PhysicalDocumentCategoryOrStr
    """The type of identity document detected in the images provided. Will always be one of the following values:

      ``drivers_license`` - A driver's license issued by the associated country, establishing identity without any
        guarantee as to citizenship, and granting driving privileges

      ``id_card`` - A general national identification card, distinct from driver's licenses as it only establishes
        identity

      ``passport`` - A travel passport issued by the associated country for one of its citizens

      ``residence_permit_card`` - An identity document issued by the associated country permitting a foreign citizen to
        <em>temporarily</em> reside there

      ``resident_card`` - An identity document issued by the associated country permitting a foreign citizen to
        <em>permanently</em> reside there

      ``visa`` - An identity document issued by the associated country permitting a foreign citizen entry for a short
        duration and for a specific purpose, typically no longer than 6 months

    Note: This value may be different from the ID type that the user selects within Link. For example, if they select
    "Driver's License" but then submit a picture of a passport, this field will say ``passport``"""

    expiration_date: Date | None
    """The expiration date of the document in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    issue_date: Date | None
    """The issue date of the document in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    issuing_country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""

    issuing_region: str | None
    """A subdivision code. "Subdivision" is a generic term for "state", "province", "prefecture", "zone", etc. For the
    list of valid codes, see `country subdivision codes <https://plaid.com/documents/country_subdivision_codes.json>`__.
    Country prefixes are omitted, since they are inferred from the ``country`` field."""

    date_of_birth: Date | None
    """A date extracted from the document in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    address: IdentityVerificationDocumentAddressResponse | None
    """The address extracted from the document. The address must at least contain the following fields to be a valid
    address: ``street``, ``city``, ``country``. If any are missing or unable to be extracted, the address will be null.

    ``region``, and ``postal_code`` may be null based on the addressing system. For example:

    Addresses from the United Kingdom will not include a region

    Addresses from Hong Kong will not include postal code

    Note: Optical Character Recognition (OCR) technology may sometimes extract incorrect data from a document."""

    name: OptionalNullable[IdentityVerificationDocumentNameResponse] = UNSET
    """The individual's name extracted from the document."""


class PhysicalDocumentExtractedDataDict(TypedDict):
    id_number: str | None
    category: PhysicalDocumentCategoryOrStr
    expiration_date: Date | None
    issue_date: Date | None
    issuing_country: str
    issuing_region: str | None
    date_of_birth: Date | None
    address: IdentityVerificationDocumentAddressResponseDict | None
    name: NotRequired[IdentityVerificationDocumentNameResponseDict | None]
