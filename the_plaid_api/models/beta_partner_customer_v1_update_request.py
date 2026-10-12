from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .partner_end_customer_bank_addendum_acceptance import (
    PartnerEndCustomerBankAddendumAcceptance,
    PartnerEndCustomerBankAddendumAcceptanceDict,
)
from .partner_end_customer_questionnaires import PartnerEndCustomerQuestionnaires, PartnerEndCustomerQuestionnairesDict


class BetaPartnerCustomerV1UpdateRequest(SdkBaseModel):
    """Request schema for ``/beta/partner/customer/v1/update``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    end_customer_client_id: str
    legal_entity_name: Optional[str] = UNSET
    redirect_uris: Optional[list[str]] = UNSET
    bank_addendum_acceptance: Optional[PartnerEndCustomerBankAddendumAcceptance] = UNSET
    """The bank addendum acceptance for the end customer."""

    questionnaires: Optional[PartnerEndCustomerQuestionnaires] = UNSET
    """The questionnaires for the end customer."""


class BetaPartnerCustomerV1UpdateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    end_customer_client_id: str
    legal_entity_name: NotRequired[str]
    redirect_uris: NotRequired[list[str]]
    bank_addendum_acceptance: NotRequired[PartnerEndCustomerBankAddendumAcceptanceDict]
    questionnaires: NotRequired[PartnerEndCustomerQuestionnairesDict]
