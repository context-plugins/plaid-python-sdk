from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditSessionDocumentIncomeResult(SdkBaseModel):
    """The details of a document income verification in Link"""

    num_paystubs_uploaded: int
    """The number of paystubs uploaded by the user."""

    num_w2s_uploaded: int
    """The number of w2s uploaded by the user."""

    num_bank_statements_uploaded: int
    """The number of bank statements uploaded by the user."""

    num_1099s_uploaded: int
    """The number of 1099s uploaded by the user"""

    num_i20s_uploaded: int
    """The number of I-20s uploaded by the user"""


class CreditSessionDocumentIncomeResultDict(TypedDict):
    num_paystubs_uploaded: int
    num_w2s_uploaded: int
    num_bank_statements_uploaded: int
    num_1099s_uploaded: int
    num_i20s_uploaded: int
