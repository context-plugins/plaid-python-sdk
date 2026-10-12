from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.products import ProductsOrStr
from .partner_end_customer_address import PartnerEndCustomerAddress, PartnerEndCustomerAddressDict
from .partner_end_customer_assets_under_management import (
    PartnerEndCustomerAssetsUnderManagement,
    PartnerEndCustomerAssetsUnderManagementDict,
)
from .partner_end_customer_billing_contact import PartnerEndCustomerBillingContact, PartnerEndCustomerBillingContactDict
from .partner_end_customer_customer_support_info import (
    PartnerEndCustomerCustomerSupportInfo,
    PartnerEndCustomerCustomerSupportInfoDict,
)
from .partner_end_customer_technical_contact import (
    PartnerEndCustomerTechnicalContact,
    PartnerEndCustomerTechnicalContactDict,
)


class PartnerCustomerCreateRequest(SdkBaseModel):
    """Request schema for ``/partner/customer/create``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    company_name: str
    """The company name of the end customer being created. This will be used to display the end customer in the Plaid
    Dashboard. It will not be shown to end users."""

    is_diligence_attested: bool
    """Denotes whether or not the partner has completed attestation of diligence for the end customer to be created."""

    products: Optional[list[ProductsOrStr]] = UNSET
    """The products to be enabled for the end customer. If empty or ``null``, this field will default to the products
    enabled for the reseller at the time this endpoint is called."""

    create_link_customization: Optional[bool] = UNSET
    """If ``true``, the end customer's default Link customization will be set to match the partner's. You can always
    change the end customer's Link customization in the Plaid Dashboard. See the `Link Customization docs
    <https://plaid.com/docs/link/customization/>`__ for more information. If you require the ability to programmatically
    create end customers using multiple different Link customization profiles, contact your Plaid account manager for
    assistance.

    Important: Data Transparency Messaging (DTM) use cases will not be copied to the end customer's Link customization
    unless the **Publish changes** button is clicked after the use cases are applied. Link will not work in Production
    unless the end customer's DTM use cases are configured. For more details, see `Data Transparency Messaging
    <https://plaid.com/docs/link/data-transparency-messaging-migration-guide/>`__."""

    logo: Optional[str] = UNSET
    """Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. The logo
    will be shared with financial institutions and shown to the end user during Link flows. A logo is required if
    ``create_link_customization`` is ``true``. If ``create_link_customization`` is ``false`` and the logo is omitted,
    the partner's logo will be used if one exists, otherwise a stock logo will be used."""

    legal_entity_name: str
    """The end customer's legal name. This will be shared with financial institutions as part of the OAuth registration
    process. It will not be shown to end users."""

    website: str
    """The end customer's website."""

    application_name: str
    """The name of the end customer's application. This will be shown to end users when they go through the Plaid Link
    flow. The application name must be unique and cannot match the name of another application already registered with
    Plaid."""

    technical_contact: Optional[PartnerEndCustomerTechnicalContact] = UNSET
    """The technical contact for the end customer. Defaults to partner's technical contact if omitted."""

    billing_contact: Optional[PartnerEndCustomerBillingContact] = UNSET
    """The billing contact for the end customer. Defaults to partner's billing contact if omitted."""

    customer_support_info: Optional[PartnerEndCustomerCustomerSupportInfo] = UNSET
    """This information is public. Users of your app will see this information when managing connections between your
    app and their bank accounts in Plaid Portal. Defaults to partner's customer support info if omitted. This field is
    mandatory for partners whose Plaid accounts were created after November 26, 2024 and will be mandatory for all
    partners by the 1033 compliance deadline."""

    address: PartnerEndCustomerAddress
    """The end customer's address."""

    is_bank_addendum_completed: bool
    """Denotes whether the partner has forwarded the Plaid bank addendum to the end customer."""

    assets_under_management: Optional[PartnerEndCustomerAssetsUnderManagement] = UNSET
    """Assets under management for the given end customer. Required for end customers with monthly service
    commitments."""

    redirect_uris: Optional[list[str]] = UNSET
    """A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used
    to support OAuth authentication flows when launching Link in the browser or another app. URIs should not contain any
    query parameters. When used in Production, URIs must use https. To modify redirect URIs for an end customer after
    creating them, go to the end customer's `API page <https://dashboard.plaid.com/team/api>`__ in the Dashboard."""

    registration_number: Optional[str] = UNSET
    """The unique identifier assigned to a financial institution by regulatory authorities, if applicable. For banks,
    this is the FDIC Certificate Number. For credit unions, this is the Credit Union Charter Number."""


class PartnerCustomerCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    company_name: str
    is_diligence_attested: bool
    products: NotRequired[list[ProductsOrStr]]
    create_link_customization: NotRequired[bool]
    logo: NotRequired[str]
    legal_entity_name: str
    website: str
    application_name: str
    technical_contact: NotRequired[PartnerEndCustomerTechnicalContactDict]
    billing_contact: NotRequired[PartnerEndCustomerBillingContactDict]
    customer_support_info: NotRequired[PartnerEndCustomerCustomerSupportInfoDict]
    address: PartnerEndCustomerAddressDict
    is_bank_addendum_completed: bool
    assets_under_management: NotRequired[PartnerEndCustomerAssetsUnderManagementDict]
    redirect_uris: NotRequired[list[str]]
    registration_number: NotRequired[str]
