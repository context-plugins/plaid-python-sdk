from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.income_verification_source_type import IncomeVerificationSourceTypeOrStr
from .link_token_create_request_income_verification_bank_income import (
    LinkTokenCreateRequestIncomeVerificationBankIncome,
    LinkTokenCreateRequestIncomeVerificationBankIncomeDict,
)
from .link_token_create_request_income_verification_payroll_income import (
    LinkTokenCreateRequestIncomeVerificationPayrollIncome,
    LinkTokenCreateRequestIncomeVerificationPayrollIncomeDict,
)
from .link_token_create_request_user_stated_income_source import (
    LinkTokenCreateRequestUserStatedIncomeSource,
    LinkTokenCreateRequestUserStatedIncomeSourceDict,
)


class LinkTokenCreateRequestIncomeVerification(SdkBaseModel):
    """Specifies options for initializing Link for use with the Income product. This field is required if
    ``income_verification`` is included in the ``products`` array."""

    income_verification_id: Optional[str] = UNSET
    """The ``income_verification_id`` of the verification instance, as provided by ``/income/verification/create``.
    Replaced by the user token."""

    asset_report_id: Optional[str] = UNSET
    """The ``asset_report_id`` of an asset report associated with the user, as provided by ``/asset_report/create``.
    Providing an ``asset_report_id`` is optional and can be used to verify the user through a streamlined flow. If
    provided, the bank linking flow will be skipped."""

    access_tokens: Optional[list[str | None]] = UNSET
    """An array of access tokens corresponding to Items that a user has previously connected with. Data from these
    institutions will be cross-referenced with document data received during the Document Income flow to help verify
    that the uploaded documents are accurate. If the ``transactions`` product was not initialized for these Items during
    Link, it will be initialized after this Link session.

    This field should only be used with the ``payroll`` income source type."""

    income_source_types: Optional[list[IncomeVerificationSourceTypeOrStr]] = UNSET
    """The types of source income data that users will be permitted to share. Options include ``bank`` and ``payroll``.
    Currently you can only specify one of these options."""

    bank_income: Optional[LinkTokenCreateRequestIncomeVerificationBankIncome] = UNSET
    """Specifies options for initializing Link for use with Bank Income. This field is required if
    ``income_verification`` is included in the ``products`` array and ``bank`` is specified in
    ``income_source_types``."""

    payroll_income: Optional[LinkTokenCreateRequestIncomeVerificationPayrollIncome] = UNSET
    """Specifies options for initializing Link for use with Payroll Income (including Document Income). Further
    customization options for Document Income, such as customizing which document types may be uploaded, are also
    available via the `Link Customization pane <https://dashboard.plaid.com/link>`__ in the Dashboard. (Requires
    Production enablement.)"""

    stated_income_sources: Optional[list[LinkTokenCreateRequestUserStatedIncomeSource]] = UNSET
    """A list of user stated income sources"""


class LinkTokenCreateRequestIncomeVerificationDict(TypedDict):
    income_verification_id: NotRequired[str]
    asset_report_id: NotRequired[str]
    access_tokens: NotRequired[list[str | None]]
    income_source_types: NotRequired[list[IncomeVerificationSourceTypeOrStr]]
    bank_income: NotRequired[
        LinkTokenCreateRequestIncomeVerificationBankIncome | LinkTokenCreateRequestIncomeVerificationBankIncomeDict
    ]
    payroll_income: NotRequired[
        (
            LinkTokenCreateRequestIncomeVerificationPayrollIncome
            | LinkTokenCreateRequestIncomeVerificationPayrollIncomeDict
        )
    ]
    stated_income_sources: NotRequired[
        list[LinkTokenCreateRequestUserStatedIncomeSource | LinkTokenCreateRequestUserStatedIncomeSourceDict]
    ]
