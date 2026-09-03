from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.income_verification_doc_parsing_config import IncomeVerificationDocParsingConfigOrStr


class LinkTokenCreateIdentity(SdkBaseModel):
    """Identity object used to specify document upload"""

    is_document_upload: Optional[bool] = UNSET
    """Used to specify whether the Link session is Identity Document Upload"""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_ids``. Currently can only contain one ``account_id``. Must be populated if using Document
    Upload."""

    parsing_configs: Optional[list[IncomeVerificationDocParsingConfigOrStr]] = UNSET
    """An array of parsing configurations. Valid parsing configurations are ``ocr`` and ``risk_signals``. If parsing
    configurations are omitted, defaults to ``ocr``"""


class LinkTokenCreateIdentityDict(TypedDict):
    is_document_upload: NotRequired[bool]
    account_ids: NotRequired[list[str]]
    parsing_configs: NotRequired[list[IncomeVerificationDocParsingConfigOrStr]]
