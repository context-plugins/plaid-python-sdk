from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.income_verification_doc_parsing_config import IncomeVerificationDocParsingConfigOrStr
from .enums.income_verification_payroll_flow_type import IncomeVerificationPayrollFlowTypeOrStr


class LinkTokenCreateRequestIncomeVerificationPayrollIncome(SdkBaseModel):
    """Specifies options for initializing Link for use with Payroll Income (including Document Income). Further
    customization options for Document Income, such as customizing which document types may be uploaded, are also
    available via the `Link Customization pane <https://dashboard.plaid.com/link>`__ in the Dashboard. (Requires
    Production enablement.)"""

    flow_types: OptionalNullable[list[IncomeVerificationPayrollFlowTypeOrStr]] = UNSET
    """The types of payroll income verification to enable for the Link session. If none are specified, then users will
    see both document and digital payroll income."""

    is_update_mode: bool = False
    """An identifier to indicate whether the income verification Link token will be used for update mode. This field is
    only relevant for participants in the Payroll Income Refresh beta."""

    item_id_to_update: OptionalNullable[str] = UNSET
    """Uniquely identify a payroll income Item to update with. This field is only relevant for participants in the
    Payroll Income Refresh beta."""

    parsing_config: OptionalNullable[list[IncomeVerificationDocParsingConfigOrStr]] = UNSET
    """The types of analysis to enable for document uploads. If this field is not provided, then docs will undergo OCR
    parsing only."""


class LinkTokenCreateRequestIncomeVerificationPayrollIncomeDict(TypedDict):
    flow_types: NotRequired[list[IncomeVerificationPayrollFlowTypeOrStr] | None]
    is_update_mode: NotRequired[bool]
    item_id_to_update: NotRequired[str | None]
    parsing_config: NotRequired[list[IncomeVerificationDocParsingConfigOrStr] | None]
