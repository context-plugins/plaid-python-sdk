from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditBankStatementsUploadsGetRequestOptions(SdkBaseModel):
    """An optional object for ``/credit/bank_statements/uploads/get`` request options."""

    item_ids: Optional[list[str]] = UNSET
    """An array of ``item_id``s whose bank statements information is returned. Each ``item_id`` should uniquely identify
    a bank statements uploaded item. If this field is not provided, all ``item_id``s associated with the ``user_token``
    will be returned in the response."""


class CreditBankStatementsUploadsGetRequestOptionsDict(TypedDict):
    item_ids: NotRequired[list[str]]
