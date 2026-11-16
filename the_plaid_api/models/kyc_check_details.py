from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .kyc_check_address_summary import KycCheckAddressSummary, KycCheckAddressSummaryDict
from .kyc_check_date_of_birth_summary import KycCheckDateOfBirthSummary, KycCheckDateOfBirthSummaryDict
from .kyc_check_id_number_summary import KycCheckIdNumberSummary, KycCheckIdNumberSummaryDict
from .kyc_check_name_summary import KycCheckNameSummary, KycCheckNameSummaryDict
from .kyc_check_phone_summary import KycCheckPhoneSummary, KycCheckPhoneSummaryDict


class KycCheckDetails(SdkBaseModel):
    """Additional information for the ``kyc_check`` (Data Source Verification) step. This field will be ``null`` unless
    ``steps.kyc_check`` has reached a terminal state of either ``success`` or ``failed``."""

    status: str
    """The outcome status for the associated Identity Verification attempt's ``kyc_check`` step. This field will always
    have the same value as ``steps.kyc_check``."""

    address: KycCheckAddressSummary
    """Result summary object specifying how the ``address`` field matched."""

    name: KycCheckNameSummary
    """Result summary object specifying how the ``name`` field matched."""

    date_of_birth: KycCheckDateOfBirthSummary
    """Result summary object specifying how the ``date_of_birth`` field matched."""

    id_number: KycCheckIdNumberSummary
    """Result summary object specifying how the ``id_number`` field matched."""

    phone_number: KycCheckPhoneSummary
    """Result summary object specifying how the ``phone`` field matched."""


class KycCheckDetailsDict(TypedDict):
    status: str
    address: KycCheckAddressSummaryDict
    name: KycCheckNameSummaryDict
    date_of_birth: KycCheckDateOfBirthSummaryDict
    id_number: KycCheckIdNumberSummaryDict
    phone_number: KycCheckPhoneSummaryDict
