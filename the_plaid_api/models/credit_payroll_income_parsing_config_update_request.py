from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.income_verification_doc_parsing_config import IncomeVerificationDocParsingConfigOrStr


class CreditPayrollIncomeParsingConfigUpdateRequest(SdkBaseModel):
    """CreditPayrollIncomeParsingConfigUpdateRequest defines the request schema for
    ``/credit/payroll_income/parsing_config/update``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_token: str
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    user_id: Optional[str] = UNSET
    item_id: Optional[str] = UNSET
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    parsing_config: list[IncomeVerificationDocParsingConfigOrStr]
    """The types of analysis to enable for the document income verification session"""


class CreditPayrollIncomeParsingConfigUpdateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_token: str
    user_id: NotRequired[str]
    item_id: NotRequired[str]
    parsing_config: list[IncomeVerificationDocParsingConfigOrStr]
