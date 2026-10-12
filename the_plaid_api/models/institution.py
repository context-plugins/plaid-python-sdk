from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .auth_metadata import AuthMetadata, AuthMetadataDict
from .enums.country_code import CountryCodeOrStr
from .enums.products import ProductsOrStr
from .institution_status import InstitutionStatus, InstitutionStatusDict
from .payment_initiation_metadata import PaymentInitiationMetadata, PaymentInitiationMetadataDict


class Institution(SdkBaseModel):
    """Details relating to a specific financial institution"""

    institution_id: str
    """Unique identifier for the institution. Note that the same institution may have multiple records, each with
    different institution IDs; for example, if the institution has migrated to OAuth, there may be separate
    ``institution_id``s for the OAuth and non-OAuth versions of the institution. Institutions that operate in different
    countries or with multiple login portals may also have separate ``institution_id``s for each country or portal."""

    name: str
    """The official name of the institution."""

    products: list[ProductsOrStr]
    """A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth
    will return ``auth`` in the product array; institutions that do not list ``auth`` may still support other Auth
    methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those
    methods, use the ``auth_metadata`` object. For more details, see `Full Auth coverage
    <https://plaid.com/docs/auth/coverage/>`__. The ``income_verification`` product here indicates support for Bank
    Income. Note: For Signal Transaction Scores and Transfer, listed institutions may be incomplete or incorrect.
    Instead, use the following: ``balance`` support also indicates coverage of Signal Transaction Scores; ``auth``
    support also indicates coverage of Transfer."""

    country_codes: list[CountryCodeOrStr]
    """A list of the country codes supported by the institution."""

    url: OptionalNullable[str] = UNSET
    """The URL for the institution's website"""

    primary_color: OptionalNullable[str] = UNSET
    """Hexadecimal representation of the primary color used by the institution. If Plaid does not have primary color
    data for the institution, this field will be a deterministically generated fallback color."""

    logo: OptionalNullable[str] = UNSET
    """Base64 encoded representation of the institution's logo, returned as a base64 encoded 152x152 PNG. Not all
    institutions' logos are available."""

    routing_numbers: list[str]
    """A list of routing numbers known to be associated with the institution. This list is provided for the purpose of
    looking up institutions by routing number. It is generally comprehensive but is not guaranteed to be a complete list
    of routing numbers for an institution."""

    dtc_numbers: Optional[list[str]] = UNSET
    """A partial list of DTC numbers associated with the institution."""

    oauth: bool
    """Indicates that the institution has an OAuth login flow. This will be ``true`` if OAuth is supported for any Items
    associated with the institution, even if the institution also supports non-OAuth connections."""

    status: OptionalNullable[InstitutionStatus] = UNSET
    """The status of an institution is determined by the health of its Item logins, Transactions updates, Investments
    updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and
    Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough
    traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate
    data.

    Institution status is accessible in the Dashboard and via the API using the ``/institutions/get_by_id`` endpoint
    with the ``options.include_status`` option set to true. Note that institution status is not available in the Sandbox
    environment."""

    payment_initiation_metadata: OptionalNullable[PaymentInitiationMetadata] = UNSET
    """Metadata that captures what specific payment configurations an institution supports when making Payment
    Initiation requests."""

    auth_metadata: OptionalNullable[AuthMetadata] = UNSET
    """Metadata that captures information about the Auth features of an institution."""


class InstitutionDict(TypedDict):
    institution_id: str
    name: str
    products: list[ProductsOrStr]
    country_codes: list[CountryCodeOrStr]
    url: NotRequired[str | None]
    primary_color: NotRequired[str | None]
    logo: NotRequired[str | None]
    routing_numbers: list[str]
    dtc_numbers: NotRequired[list[str]]
    oauth: bool
    status: NotRequired[InstitutionStatusDict | None]
    payment_initiation_metadata: NotRequired[PaymentInitiationMetadataDict | None]
    auth_metadata: NotRequired[AuthMetadataDict | None]
