from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .kyccheck_address_summary import KyccheckAddressSummary, KyccheckAddressSummaryDict
from .kyccheck_date_of_birth_summary import KyccheckDateOfBirthSummary, KyccheckDateOfBirthSummaryDict
from .kyccheck_idnumber_summary import KyccheckIdnumberSummary, KyccheckIdnumberSummaryDict
from .kyccheck_name_summary import KyccheckNameSummary, KyccheckNameSummaryDict
from .kyccheck_phone_summary import KyccheckPhoneSummary, KyccheckPhoneSummaryDict


class KyccheckDetails(SdkBaseModel):
    """Additional information for the ``kyc_check`` (Data Source Verification) step. This field will be ``null`` unless
    ``steps.kyc_check`` has reached a terminal state of either ``success`` or ``failed``."""

    status: str
    """The outcome status for the associated Identity Verification attempt's ``kyc_check`` step. This field will always
    have the same value as ``steps.kyc_check``."""

    address: KyccheckAddressSummary
    """Result summary object specifying how the ``address`` field matched."""

    name: KyccheckNameSummary
    """Result summary object specifying how the ``name`` field matched."""

    date_of_birth: KyccheckDateOfBirthSummary
    """Result summary object specifying how the ``date_of_birth`` field matched."""

    id_number: KyccheckIdnumberSummary
    """Result summary object specifying how the ``id_number`` field matched."""

    phone_number: KyccheckPhoneSummary
    """Result summary object specifying how the ``phone`` field matched."""


class KyccheckDetailsDict(TypedDict):
    status: str
    address: KyccheckAddressSummary | KyccheckAddressSummaryDict
    name: KyccheckNameSummary | KyccheckNameSummaryDict
    date_of_birth: KyccheckDateOfBirthSummary | KyccheckDateOfBirthSummaryDict
    id_number: KyccheckIdnumberSummary | KyccheckIdnumberSummaryDict
    phone_number: KyccheckPhoneSummary | KyccheckPhoneSummaryDict
