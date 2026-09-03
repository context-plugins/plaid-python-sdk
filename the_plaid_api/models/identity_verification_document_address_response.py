from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IdentityVerificationDocumentAddressResponse(SdkBaseModel):
    """The address extracted from the document. The address must at least contain the following fields to be a valid
    address: ``street``, ``city``, ``country``. If any are missing or unable to be extracted, the address will be null.

    ``region``, and ``postal_code`` may be null based on the addressing system. For example:

    Addresses from the United Kingdom will not include a region

    Addresses from Hong Kong will not include postal code

    Note: Optical Character Recognition (OCR) technology may sometimes extract incorrect data from a document."""

    street: str
    """The full street address extracted from the document."""

    city: str
    """City extracted from the document."""

    region: str | None
    """A subdivision code extracted from the document. Related terms would be "state", "province", "prefecture", "zone",
    "subdivision", etc. For a full list of valid codes, see `country subdivision codes
    <https://plaid.com/documents/country_subdivision_codes.json>`__. Country prefixes are omitted, since they can be
    inferred from the ``country`` field."""

    postal_code: str | None
    """The postal code extracted from the document. Between 2 and 10 alphanumeric characters. For US-based addresses
    this must be 5 numeric digits."""

    country: str
    """Valid, capitalized, two-letter ISO code representing the country extracted from the document. Must be in ISO
    3166-1 alpha-2 form."""


class IdentityVerificationDocumentAddressResponseDict(TypedDict):
    street: str
    city: str
    region: str | None
    postal_code: str | None
    country: str
