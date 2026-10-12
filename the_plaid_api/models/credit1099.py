from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .credit1099_filer import Credit1099Filer, Credit1099FilerDict
from .credit1099_payer import Credit1099Payer, Credit1099PayerDict
from .credit1099_recipient import Credit1099Recipient, Credit1099RecipientDict
from .credit_document_metadata import CreditDocumentMetadata, CreditDocumentMetadataDict
from .enums.form1099_type import Form1099TypeOrStr


class Credit1099(SdkBaseModel):
    """An object representing an end user's 1099 tax form"""

    document_id: str | None
    """An identifier of the document referenced by the document metadata."""

    document_metadata: Optional[CreditDocumentMetadata] = UNSET
    """Object representing metadata pertaining to the document."""

    form_1099_type: Optional[Form1099TypeOrStr] = UNSET
    """Form 1099 Type"""

    recipient: Optional[Credit1099Recipient] = UNSET
    """An object representing a recipient used in both 1099-K and 1099-MISC tax documents."""

    payer: Optional[Credit1099Payer] = UNSET
    """An object representing a payer used by 1099-MISC tax documents."""

    filer: Optional[Credit1099Filer] = UNSET
    """An object representing a filer used by 1099-K tax documents."""

    tax_year: OptionalNullable[str] = UNSET
    """Tax year of the tax form."""

    rents: OptionalNullable[float] = UNSET
    """Amount in rent by payer."""

    royalties: OptionalNullable[float] = UNSET
    """Amount in royalties by payer."""

    other_income: OptionalNullable[float] = UNSET
    """Amount in other income by payer."""

    federal_income_tax_withheld: OptionalNullable[float] = UNSET
    """Amount of federal income tax withheld from payer."""

    fishing_boat_proceeds: OptionalNullable[float] = UNSET
    """Amount of fishing boat proceeds from payer."""

    medical_and_healthcare_payments: OptionalNullable[float] = UNSET
    """Amount of medical and healthcare payments from payer."""

    nonemployee_compensation: OptionalNullable[float] = UNSET
    """Amount of nonemployee compensation from payer."""

    substitute_payments_in_lieu_of_dividends_or_interest: OptionalNullable[float] = UNSET
    """Amount of substitute payments made by payer."""

    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: OptionalNullable[str] = UNSET
    """Whether or not payer made direct sales over $5000 of consumer products."""

    crop_insurance_proceeds: OptionalNullable[float] = UNSET
    """Amount of crop insurance proceeds."""

    excess_golden_parachute_payments: OptionalNullable[float] = UNSET
    """Amount of golden parachute payments made by payer."""

    gross_proceeds_paid_to_an_attorney: OptionalNullable[float] = UNSET
    """Amount of gross proceeds paid to an attorney by payer."""

    section_409a_deferrals: OptionalNullable[float] = UNSET
    """Amount of 409A deferrals earned by payer."""

    section_409a_income: OptionalNullable[float] = UNSET
    """Amount of 409A income earned by payer."""

    state_tax_withheld: OptionalNullable[float] = UNSET
    """Amount of state tax withheld of payer for primary state."""

    state_tax_withheld_lower: OptionalNullable[float] = UNSET
    """Amount of state tax withheld of payer for secondary state."""

    payer_state_number: OptionalNullable[str] = UNSET
    """Primary state ID."""

    payer_state_number_lower: OptionalNullable[str] = UNSET
    """Secondary state ID."""

    state_income: OptionalNullable[float] = UNSET
    """State income reported for primary state."""

    state_income_lower: OptionalNullable[float] = UNSET
    """State income reported for secondary state."""

    transactions_reported: OptionalNullable[str] = UNSET
    """One of the values will be provided Payment card Third party network"""

    pse_name: OptionalNullable[str] = UNSET
    """Name of the PSE (Payment Settlement Entity)."""

    pse_telephone_number: OptionalNullable[str] = UNSET
    """Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity)."""

    gross_amount: OptionalNullable[float] = UNSET
    """Gross amount reported."""

    card_not_present_transaction: OptionalNullable[float] = UNSET
    """Amount in card not present transactions."""

    merchant_category_code: OptionalNullable[str] = UNSET
    """Merchant category of filer."""

    number_of_payment_transactions: OptionalNullable[str] = UNSET
    """Number of payment transactions made."""

    january_amount: OptionalNullable[float] = UNSET
    """Amount reported for January."""

    february_amount: OptionalNullable[float] = UNSET
    """Amount reported for February."""

    march_amount: OptionalNullable[float] = UNSET
    """Amount reported for March."""

    april_amount: OptionalNullable[float] = UNSET
    """Amount reported for April."""

    may_amount: OptionalNullable[float] = UNSET
    """Amount reported for May."""

    june_amount: OptionalNullable[float] = UNSET
    """Amount reported for June."""

    july_amount: OptionalNullable[float] = UNSET
    """Amount reported for July."""

    august_amount: OptionalNullable[float] = UNSET
    """Amount reported for August."""

    september_amount: OptionalNullable[float] = UNSET
    """Amount reported for September."""

    october_amount: OptionalNullable[float] = UNSET
    """Amount reported for October."""

    november_amount: OptionalNullable[float] = UNSET
    """Amount reported for November."""

    december_amount: OptionalNullable[float] = UNSET
    """Amount reported for December."""

    primary_state: OptionalNullable[str] = UNSET
    """Primary state of business."""

    secondary_state: OptionalNullable[str] = UNSET
    """Secondary state of business."""

    primary_state_id: OptionalNullable[str] = UNSET
    """Primary state ID."""

    secondary_state_id: OptionalNullable[str] = UNSET
    """Secondary state ID."""

    primary_state_income_tax: OptionalNullable[float] = UNSET
    """State income tax reported for primary state."""

    secondary_state_income_tax: OptionalNullable[float] = UNSET
    """State income tax reported for secondary state."""


class Credit1099Dict(TypedDict):
    document_id: str | None
    document_metadata: NotRequired[CreditDocumentMetadataDict]
    form_1099_type: NotRequired[Form1099TypeOrStr]
    recipient: NotRequired[Credit1099RecipientDict]
    payer: NotRequired[Credit1099PayerDict]
    filer: NotRequired[Credit1099FilerDict]
    tax_year: NotRequired[str | None]
    rents: NotRequired[float | None]
    royalties: NotRequired[float | None]
    other_income: NotRequired[float | None]
    federal_income_tax_withheld: NotRequired[float | None]
    fishing_boat_proceeds: NotRequired[float | None]
    medical_and_healthcare_payments: NotRequired[float | None]
    nonemployee_compensation: NotRequired[float | None]
    substitute_payments_in_lieu_of_dividends_or_interest: NotRequired[float | None]
    payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer: NotRequired[str | None]
    crop_insurance_proceeds: NotRequired[float | None]
    excess_golden_parachute_payments: NotRequired[float | None]
    gross_proceeds_paid_to_an_attorney: NotRequired[float | None]
    section_409a_deferrals: NotRequired[float | None]
    section_409a_income: NotRequired[float | None]
    state_tax_withheld: NotRequired[float | None]
    state_tax_withheld_lower: NotRequired[float | None]
    payer_state_number: NotRequired[str | None]
    payer_state_number_lower: NotRequired[str | None]
    state_income: NotRequired[float | None]
    state_income_lower: NotRequired[float | None]
    transactions_reported: NotRequired[str | None]
    pse_name: NotRequired[str | None]
    pse_telephone_number: NotRequired[str | None]
    gross_amount: NotRequired[float | None]
    card_not_present_transaction: NotRequired[float | None]
    merchant_category_code: NotRequired[str | None]
    number_of_payment_transactions: NotRequired[str | None]
    january_amount: NotRequired[float | None]
    february_amount: NotRequired[float | None]
    march_amount: NotRequired[float | None]
    april_amount: NotRequired[float | None]
    may_amount: NotRequired[float | None]
    june_amount: NotRequired[float | None]
    july_amount: NotRequired[float | None]
    august_amount: NotRequired[float | None]
    september_amount: NotRequired[float | None]
    october_amount: NotRequired[float | None]
    november_amount: NotRequired[float | None]
    december_amount: NotRequired[float | None]
    primary_state: NotRequired[str | None]
    secondary_state: NotRequired[str | None]
    primary_state_id: NotRequired[str | None]
    secondary_state_id: NotRequired[str | None]
    primary_state_income_tax: NotRequired[float | None]
    secondary_state_income_tax: NotRequired[float | None]
