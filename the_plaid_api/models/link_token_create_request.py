from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.consumer_report_permissible_purpose import ConsumerReportPermissiblePurposeOrStr
from .enums.country_code import CountryCodeOrStr
from .enums.link_token_create_request_appearance_mode import LinkTokenCreateRequestAppearanceModeOrStr
from .enums.products import ProductsOrStr
from .link_token_account_filters import LinkTokenAccountFilters, LinkTokenAccountFiltersDict
from .link_token_cashflow_report import LinkTokenCashflowReport, LinkTokenCashflowReportDict
from .link_token_create_card_switch import LinkTokenCreateCardSwitch, LinkTokenCreateCardSwitchDict
from .link_token_create_hosted_link import LinkTokenCreateHostedLink, LinkTokenCreateHostedLinkDict
from .link_token_create_identity import LinkTokenCreateIdentity, LinkTokenCreateIdentityDict
from .link_token_create_institution_data import LinkTokenCreateInstitutionData, LinkTokenCreateInstitutionDataDict
from .link_token_create_request_auth import LinkTokenCreateRequestAuth, LinkTokenCreateRequestAuthDict
from .link_token_create_request_base_report import (
    LinkTokenCreateRequestBaseReport,
    LinkTokenCreateRequestBaseReportDict,
)
from .link_token_create_request_cra_options import (
    LinkTokenCreateRequestCraOptions,
    LinkTokenCreateRequestCraOptionsDict,
)
from .link_token_create_request_credit_partner_insights import (
    LinkTokenCreateRequestCreditPartnerInsights,
    LinkTokenCreateRequestCreditPartnerInsightsDict,
)
from .link_token_create_request_employment import LinkTokenCreateRequestEmployment, LinkTokenCreateRequestEmploymentDict
from .link_token_create_request_identity_verification import (
    LinkTokenCreateRequestIdentityVerification,
    LinkTokenCreateRequestIdentityVerificationDict,
)
from .link_token_create_request_income_verification import (
    LinkTokenCreateRequestIncomeVerification,
    LinkTokenCreateRequestIncomeVerificationDict,
)
from .link_token_create_request_payment_configuration import (
    LinkTokenCreateRequestPaymentConfiguration,
    LinkTokenCreateRequestPaymentConfigurationDict,
)
from .link_token_create_request_payment_initiation import (
    LinkTokenCreateRequestPaymentInitiation,
    LinkTokenCreateRequestPaymentInitiationDict,
)
from .link_token_create_request_statements import LinkTokenCreateRequestStatements, LinkTokenCreateRequestStatementsDict
from .link_token_create_request_transfer import LinkTokenCreateRequestTransfer, LinkTokenCreateRequestTransferDict
from .link_token_create_request_update import LinkTokenCreateRequestUpdate, LinkTokenCreateRequestUpdateDict
from .link_token_create_request_user import LinkTokenCreateRequestUser, LinkTokenCreateRequestUserDict
from .link_token_euconfig import LinkTokenEuconfig, LinkTokenEuconfigDict
from .link_token_investments import LinkTokenInvestments, LinkTokenInvestmentsDict
from .link_token_investments_auth import LinkTokenInvestmentsAuth, LinkTokenInvestmentsAuthDict
from .link_token_transactions import LinkTokenTransactions, LinkTokenTransactionsDict


class LinkTokenCreateRequest(SdkBaseModel):
    """LinkTokenCreateRequest defines the request schema for ``/link/token/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_name: str
    """The name of your application, as it should be displayed in Link. Maximum length of 30 characters. If a value
    longer than 30 characters is provided, Link will display "This Application" instead."""

    language: str
    """The language that Link should be displayed in. When initializing with Identity Verification, this field is not
    used; for more details, see `Identity Verification supported languages
    <https://plaid.com/docs/identity-verification/#supported-languages>`__.

    Supported languages are:
    - Danish (``'da'``)
    - Dutch (``'nl'``)
    - English (``'en'``)
    - Estonian (``'et'``)
    - French (``'fr'``)
    - German (``'de'``)
    - Hindi (``'hi'``)
    - Italian (``'it'``)
    - Latvian (``'lv'``)
    - Lithuanian (``'lt'``)
    - Norwegian (``'no'``)
    - Polish (``'pl'``)
    - Portuguese (``'pt'``)
    - Romanian (``'ro'``)
    - Spanish (``'es'``)
    - Swedish (``'sv'``)
    - Vietnamese (``'vi'``)

    When using a Link customization, the language configured here must match the setting in the customization, or the
    customization will not be applied."""

    country_codes: list[CountryCodeOrStr]
    """Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard.
    Institutions from all listed countries will be shown. For a complete mapping of supported products by country, see
    https://support.plaid.com/hc/en-us/articles/27895826947735-What-Plaid-products-are-supported-in-each-country-and-region.
    For access to additional countries beyond what you have been approved for, `contact sales
    <https://plaid.com/contact/>`__, your account manager, or support.

    If using Identity Verification, ``country_codes`` should be set to the country where your company is based, not the
    country where your user is located. For all other products, ``country_codes`` represents the location of your user's
    financial institution.

    If Link is launched with multiple country codes, only products that you are enabled for in all countries will be
    used by Link. While all countries are enabled by default in Sandbox, in Production only the countries you have
    requested access for are shown. To request access to additional countries, `file a product access Support ticket
    <https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access>`__
    via the Plaid dashboard.

    If using a Link customization, make sure the country codes in the customization match those specified in
    ``country_codes``, or the customization may not be applied.

    If using the Auth features Instant Match, Instant Micro-deposits, Same-Day Micro-deposits, Automated Micro-deposits,
    or Database Auth, ``country_codes`` must be set to ``['US']``."""

    user: Optional[LinkTokenCreateRequestUser] = UNSET
    """An object specifying information about the end user who will be linking their account. **Required** if
    ``user_id`` isn't included."""

    user_id: Optional[str] = UNSET
    """A ``user_id`` generated using ``/user/create``. Required for integrations that began using Plaid Protect,
    Multi-Item Link, or Plaid Check Consumer Report after December 10, 2025. For more details, see `New User APIs
    <https://plaid.com/docs/api/users/user-apis>`__. One of either the ``user_id`` or the ``user`` field is required."""

    products: OptionalNullable[list[ProductsOrStr]] = UNSET
    """List of Plaid product(s) that the linked Item must support. If launching Link in update mode, should be omitted
    (unless you are using update mode to add a credit product, such as Assets, Statements, Income, or Plaid Check
    Consumer Report, to an existing Item); at least one ``product`` is required otherwise.

    To maximize the number of institutions and accounts available, initialize Link with the minimal product set required
    for your use case, as the products specified will limit which institutions and account types will be available to
    your users in Link. Only institutions that support *all* requested products can be selected; if a user attempts to
    select an institution that does not support a listed product, a "Connectivity not supported" error message will
    appear in Link. For each specified product, the Item connected by the user must contain at least one compatible
    account. For details on compatible product / account type combinations, see `the account type/product support matrix
    <https://plaid.com/docs/api/accounts/#account-type--product-support-matrix>`__.

    To add products without limiting the institution list or account types, use the
    https://plaid.com/docs/api/link/#link-token-create-request-optional-products or
    https://plaid.com/docs/api/link/#link-token-create-request-required-if-supported-products fields. Products can also
    be added to an Item by calling the product endpoint after obtaining an access token; this may require the product to
    be listed in the https://plaid.com/docs/api/link/#link-token-create-request-additional-consented-products array. For
    details, see `Choosing when to initialize products <https://plaid.com/docs/link/initializing-products/>`__.

    ``balance`` is *not* a valid value, the Balance product does not require explicit initialization and will
    automatically be initialized when any other product is initialized.

    If launching Link with CRA products, ``cra_base_report`` is required and must be included in the ``products`` array.

    Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also
    be shown in Link if ``auth`` is specified as a product, even though these institutions do not contain ``auth`` in
    their product array.

    In Production, you will be billed for each product that you specify when initializing Link. Note that a product
    cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for
    subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via
    ``/item/remove``."""

    required_if_supported_products: OptionalNullable[list[ProductsOrStr]] = UNSET
    """List of Plaid product(s) you wish to use only if the institution and account(s) selected by the user support the
    product. Institutions that do not support these products will still be shown in Link. The products will only be
    extracted and billed if the user selects an institution and account type that supports them.

    There should be no overlap between this array and the ``products``, ``optional_products``, or
    ``additional_consented_products`` arrays. The ``products`` array must have at least one product.

    For more details on using this feature, see `Required if Supported Products
    <https://plaid.com/docs/link/initializing-products/#required-if-supported-products>`__."""

    optional_products: OptionalNullable[list[ProductsOrStr]] = UNSET
    """List of Plaid product(s) that will enhance the consumer's use case, but that your app can function without. Plaid
    will attempt to fetch data for these products on a best-effort basis, and failure to support these products will not
    affect Item creation.

    There should be no overlap between this array and the ``products``, ``required_if_supported_products``, or
    ``additional_consented_products`` arrays. The ``products`` array must have at least one product.

    For more details on using this feature, see `Optional Products
    <https://plaid.com/docs/link/initializing-products/#optional-products>`__."""

    additional_consented_products: OptionalNullable[list[ProductsOrStr]] = UNSET
    """List of additional Plaid product(s) you wish to collect consent for to support your use case. These products will
    not be billed until you start using them by calling the relevant endpoints.

    ``balance`` is *not* a valid value, the Balance product does not require explicit initialization and will
    automatically have consent collected.

    Institutions that do not support these products will still be shown in Link.

    There should be no overlap between this array and the ``products`` or ``required_if_supported_products`` arrays.

    If you include ``signal`` in ``additional_consented_products``, you will need to call
    https://plaid.com/docs/api/products/signal/#signalprepare before calling ``/signal/evaluate`` for the first time on
    an Item in order to get the most accurate results. For more details, see
    https://plaid.com/docs/api/products/signal/#signalprepare."""

    webhook: Optional[str] = UNSET
    """The destination URL to which any webhooks should be sent. Note that webhooks for Payment Initiation (e-wallet
    transactions only), Transfer, Bank Transfer (including Auth micro-deposit notification webhooks), Monitor, and
    Identity Verification are configured via the Dashboard instead. In update mode, this field will not have an effect;
    to update the webhook receiver endpoint for an existing Item, use ``/item/webhook/update`` instead."""

    access_token: OptionalNullable[str] = UNSET
    """The ``access_token`` associated with the Item to update or reference, used when updating, modifying, or accessing
    an existing ``access_token``. Used when launching Link in update mode, when completing the Same-Day Micro-deposit
    (manual) flow, or (optionally) when initializing Link for a returning user as part of the Transfer UI flow."""

    access_tokens: Optional[list[str]] = UNSET
    """A list of access tokens associated with the items to update in Link update mode for the Assets product. Using
    this instead of the ``access_token`` field allows the updating of multiple items at once. This feature is in closed
    beta, please contact your account manager for more info."""

    link_customization_name: Optional[str] = UNSET
    """The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the
    ``default`` customization will be used. When using a Link customization, the language in the customization must
    match the language selected via the ``language`` parameter, and the countries in the customization should match the
    country codes selected via ``country_codes``."""

    appearance_mode: OptionalNullable[LinkTokenCreateRequestAppearanceModeOrStr] = UNSET
    """Enum representing the desired appearance mode for Link, used to force light or dark modes or set Link to change
    depending on user system settings. Currently in closed beta."""

    redirect_uri: Optional[str] = UNSET
    """A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support
    OAuth authentication flows when launching Link in the browser or another app. The ``redirect_uri`` should not
    contain any query parameters. When used in Production, must be an https URI. Note that any redirect URI must also be
    added to the Allowed redirect URIs list in the `developer dashboard <https://dashboard.plaid.com/team/api>`__. If
    initializing on Android, ``android_package_name`` must be specified instead and ``redirect_uri`` should be left
    blank."""

    android_package_name: Optional[str] = UNSET
    """The name of your app's Android package. Required if using the ``link_token`` to initialize Link on Android. Any
    package name specified here must also be added to the Allowed Android package names setting on the `developer
    dashboard <https://dashboard.plaid.com/team/api>`__. When creating a ``link_token`` for initializing Link on other
    platforms, ``android_package_name`` must be left blank and ``redirect_uri`` should be used instead."""

    institution_data: Optional[LinkTokenCreateInstitutionData] = UNSET
    """A map containing data used to highlight institutions in Link."""

    card_switch: Optional[LinkTokenCreateCardSwitch] = UNSET
    """A map containing data to pass in for the Card Switch flow."""

    account_filters: Optional[LinkTokenAccountFilters] = UNSET
    """By default, Link will provide limited account filtering: it will only display Institutions that are compatible
    with all products supplied in the ``products`` parameter of ``/link/token/create``, and, if ``auth`` is specified in
    the ``products`` array, will also filter out accounts other than ``checking``, ``savings``, and ``cash management``
    accounts on the Account Select pane. You can further limit the accounts shown in Link by using ``account_filters``
    to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering
    applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not
    support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the
    value ``"all"``. If the ``account_filters`` filter is used, any account type for which a filter is not specified
    will be entirely omitted from Link. For a full list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#account-type-schema>`__.

    The filter may or may not impact the list of accounts shown by the institution in the OAuth account selection flow,
    depending on the specific institution. If the user selects excluded account subtypes in the OAuth flow, these
    accounts will not be added to the Item. If the user selects only excluded account subtypes, the link attempt will
    fail and the user will be prompted to try again."""

    eu_config: Optional[LinkTokenEuconfig] = UNSET
    """Configuration parameters for EU flows"""

    institution_id: Optional[str] = UNSET
    """Used for certain legacy use cases"""

    payment_configuration: Optional[LinkTokenCreateRequestPaymentConfiguration] = UNSET
    """Specifies options for initializing Link for use with the Pay By Bank flow. This is an optional field to configure
    the user experience, and currently requires the amount field to be set."""

    payment_initiation: Optional[LinkTokenCreateRequestPaymentInitiation] = UNSET
    """Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is
    required if ``payment_initiation`` is included in the ``products`` array. Either ``payment_id`` or ``consent_id``
    must be provided."""

    employment: Optional[LinkTokenCreateRequestEmployment] = UNSET
    """Specifies options for initializing Link for use with the Employment product. This field is required if
    ``employment`` is included in the ``products`` array."""

    income_verification: Optional[LinkTokenCreateRequestIncomeVerification] = UNSET
    """Specifies options for initializing Link for use with the Income product. This field is required if
    ``income_verification`` is included in the ``products`` array."""

    base_report: Optional[LinkTokenCreateRequestBaseReport] = UNSET
    """Specifies options for initializing Link for use with the Base Report product. This field is required if
    ``assets`` is included in the ``products`` array and the client is CRA-enabled."""

    credit_partner_insights: Optional[LinkTokenCreateRequestCreditPartnerInsights] = UNSET
    """Specifies options for initializing Link for use with the Credit Partner Insights product."""

    cra_options: Optional[LinkTokenCreateRequestCraOptions] = UNSET
    """Specifies options for initializing Link for use with Plaid Check products"""

    consumer_report_permissible_purpose: Optional[ConsumerReportPermissiblePurposeOrStr] = UNSET
    """Describes the reason you are generating a Consumer Report for this user. When calling ``/link/token/create``,
    this field is required when using Plaid Check (CRA) products; invalid if not using Plaid Check (CRA) products.

    ``ACCOUNT_REVIEW_CREDIT``: In connection with a consumer credit transaction for the review or collection of an
    account pursuant to FCRA Section 604(a)(3)(A).

    ``ACCOUNT_REVIEW_NON_CREDIT``: For a legitimate business need of the information to review a non-credit account
    provided primarily for personal, family, or household purposes to determine whether the consumer continues to meet
    the terms of the account pursuant to FCRA Section 604(a)(3)(F)(2).

    ``EXTENSION_OF_CREDIT``: In connection with a credit transaction initiated by and involving the consumer pursuant to
    FCRA Section 604(a)(3)(A).

    ``LEGITIMATE_BUSINESS_NEED_TENANT_SCREENING``: For a legitimate business need in connection with a business
    transaction initiated by the consumer primarily for personal, family, or household purposes in connection with a
    property rental assessment pursuant to FCRA Section 604(a)(3)(F)(i).

    ``LEGITIMATE_BUSINESS_NEED_OTHER``: For a legitimate business need in connection with a business transaction made
    primarily for personal, family, or household initiated by the consumer pursuant to FCRA Section 604(a)(3)(F)(i).

    ``WRITTEN_INSTRUCTION_PREQUALIFICATION``: In accordance with the written instructions of the consumer pursuant to
    FCRA Section 604(a)(2), to evaluate an application's profile to make an offer to the consumer.

    ``WRITTEN_INSTRUCTION_OTHER``: In accordance with the written instructions of the consumer pursuant to FCRA Section
    604(a)(2), such as when an individual agrees to act as a guarantor or assumes personal liability for a consumer,
    business, or commercial loan.

    ``ELIGIBILITY_FOR_GOVT_BENEFITS``: In connection with an eligibility determination for a government benefit where
    the entity is required to consider an applicant's financial status pursuant to FCRA Section 604(a)(3)(D)."""

    auth: Optional[LinkTokenCreateRequestAuth] = UNSET
    """Specifies options for initializing Link for use with the Auth product. This field can be used to enable or
    disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be
    configured by your account manager. The default behavior described in the documentation is the default behavior that
    will apply if you have not requested your account manager to apply a different default. If you have enabled the
    `Dashboard Account Verification pane <https://dashboard.plaid.com/account-verification>`__, the settings enabled
    there will override any settings in this object."""

    transfer: Optional[LinkTokenCreateRequestTransfer] = UNSET
    """Specifies options for initializing Link for use with the Transfer product."""

    update: Optional[LinkTokenCreateRequestUpdate] = UNSET
    """Specifies options for initializing Link for `update mode <https://plaid.com/docs/link/update-mode>`__."""

    identity_verification: Optional[LinkTokenCreateRequestIdentityVerification] = UNSET
    """Specifies option for initializing Link for use with the Identity Verification product."""

    statements: Optional[LinkTokenCreateRequestStatements] = UNSET
    """Specifies options for initializing Link for use with the Statements product. This field is required for the
    statements product."""

    third_party_user_token: Optional[str] = UNSET
    """A third party user token associated with the current user."""

    investments: Optional[LinkTokenInvestments] = UNSET
    """Configuration parameters for the Investments product"""

    investments_auth: Optional[LinkTokenInvestmentsAuth] = UNSET
    """Configuration parameters for the Investments Move product"""

    hosted_link: Optional[LinkTokenCreateHostedLink] = UNSET
    """Configuration parameters for Hosted Link. To enable the session for Hosted Link, send this object in the request.
    It can be empty."""

    transactions: Optional[LinkTokenTransactions] = UNSET
    """Configuration parameters for the Transactions product"""

    cashflow_report: Optional[LinkTokenCashflowReport] = UNSET
    """Configuration parameters for the Cashflow Report product. Currently in closed beta."""

    cra_enabled: Optional[bool] = UNSET
    """If ``true``, request a CRA connection. Defaults to ``false``."""

    identity: Optional[LinkTokenCreateIdentity] = UNSET
    """Identity object used to specify document upload"""

    financekit_supported: Optional[bool] = UNSET
    """If ``true``, indicates that client supports linking FinanceKit / AppleCard items. Defaults to ``false``."""

    enable_multi_item_link: Optional[bool] = UNSET
    """If ``true``, enable linking multiple items in the same Link session. Defaults to ``false``."""

    user_token: Optional[str] = UNSET
    """A user token generated using ``/user/create``. Any Item created during the Link session will be associated with
    the user. Integrations that began using Plaid Protect, Multi-Item Link, or Plaid Check Consumer Report before
    December 10, 2025 use this field instead of the ``user_id``."""


class LinkTokenCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_name: str
    language: str
    country_codes: list[CountryCodeOrStr]
    user: NotRequired[LinkTokenCreateRequestUserDict]
    user_id: NotRequired[str]
    products: NotRequired[list[ProductsOrStr] | None]
    required_if_supported_products: NotRequired[list[ProductsOrStr] | None]
    optional_products: NotRequired[list[ProductsOrStr] | None]
    additional_consented_products: NotRequired[list[ProductsOrStr] | None]
    webhook: NotRequired[str]
    access_token: NotRequired[str | None]
    access_tokens: NotRequired[list[str]]
    link_customization_name: NotRequired[str]
    appearance_mode: NotRequired[LinkTokenCreateRequestAppearanceModeOrStr | None]
    redirect_uri: NotRequired[str]
    android_package_name: NotRequired[str]
    institution_data: NotRequired[LinkTokenCreateInstitutionDataDict]
    card_switch: NotRequired[LinkTokenCreateCardSwitchDict]
    account_filters: NotRequired[LinkTokenAccountFiltersDict]
    eu_config: NotRequired[LinkTokenEuconfigDict]
    institution_id: NotRequired[str]
    payment_configuration: NotRequired[LinkTokenCreateRequestPaymentConfigurationDict]
    payment_initiation: NotRequired[LinkTokenCreateRequestPaymentInitiationDict]
    employment: NotRequired[LinkTokenCreateRequestEmploymentDict]
    income_verification: NotRequired[LinkTokenCreateRequestIncomeVerificationDict]
    base_report: NotRequired[LinkTokenCreateRequestBaseReportDict]
    credit_partner_insights: NotRequired[LinkTokenCreateRequestCreditPartnerInsightsDict]
    cra_options: NotRequired[LinkTokenCreateRequestCraOptionsDict]
    consumer_report_permissible_purpose: NotRequired[ConsumerReportPermissiblePurposeOrStr]
    auth: NotRequired[LinkTokenCreateRequestAuthDict]
    transfer: NotRequired[LinkTokenCreateRequestTransferDict]
    update: NotRequired[LinkTokenCreateRequestUpdateDict]
    identity_verification: NotRequired[LinkTokenCreateRequestIdentityVerificationDict]
    statements: NotRequired[LinkTokenCreateRequestStatementsDict]
    third_party_user_token: NotRequired[str]
    investments: NotRequired[LinkTokenInvestmentsDict]
    investments_auth: NotRequired[LinkTokenInvestmentsAuthDict]
    hosted_link: NotRequired[LinkTokenCreateHostedLinkDict]
    transactions: NotRequired[LinkTokenTransactionsDict]
    cashflow_report: NotRequired[LinkTokenCashflowReportDict]
    cra_enabled: NotRequired[bool]
    identity: NotRequired[LinkTokenCreateIdentityDict]
    financekit_supported: NotRequired[bool]
    enable_multi_item_link: NotRequired[bool]
    user_token: NotRequired[str]
