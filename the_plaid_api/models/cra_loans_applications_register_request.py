from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_loan_application import CraLoanApplication, CraLoanApplicationDict


class CraLoansApplicationsRegisterRequest(SdkBaseModel):
    """CraLoansApplicationsRegisterRequest defines the request schema for ``/cra/loans/applications/register``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    applications: list[CraLoanApplication]
    """A list of loan applications to register."""


class CraLoansApplicationsRegisterRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    applications: list[CraLoanApplication | CraLoanApplicationDict]
