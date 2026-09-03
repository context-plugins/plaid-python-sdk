from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_loan_update import CraLoanUpdate, CraLoanUpdateDict


class CraLoansUpdateRequest(SdkBaseModel):
    """CraLoansUpdateRequest defines the request schema for ``/cra/loans/update``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    loans: list[CraLoanUpdate]
    """A list of loans to update."""


class CraLoansUpdateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    loans: list[CraLoanUpdate | CraLoanUpdateDict]
