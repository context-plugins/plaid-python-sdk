from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.originator_expected_transfer_frequency import OriginatorExpectedTransferFrequencyOrStr


class TransferDebitUsageConfiguration(SdkBaseModel):
    """Specifies the originator's expected usage of debits. For all dollar amounts, use a decimal string with two digits
    of precision e.g. "10.00". This field is required if the originator is expected to process debit transfers."""

    expected_frequency: OriginatorExpectedTransferFrequencyOrStr
    """The originator's expected transfer frequency."""

    expected_highest_amount: str
    """The originator's expected highest amount for a single debit transfer."""

    expected_average_amount: str
    """The originator's expected average amount per debit."""

    expected_monthly_amount: str
    """The originator's monthly expected ACH debit processing amount for the next 6-12 months."""

    sec_codes: list[AchclassOrStr]
    """Specifies the expected use cases for the originator's debit transfers. This should be a list that contains one or
    more of the following codes:

    ``"ccd"`` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    ``"ppd"`` - Prearranged Payment or Deposit - The transfer is part of a pre-existing relationship with a consumer.
    Authorization was obtained in writing either in person or via an electronic document signing, e.g. Docusign, by the
    consumer. Can be used for credits or debits.

    ``"web"`` - Internet-Initiated Entry. The transfer debits a consumer's bank account. Authorization from the consumer
    is obtained over the Internet (e.g. a web or mobile application). Can be used for single debits or recurring debits.

    ``"tel"`` - Telephone-Initiated Entry. The transfer debits a consumer. Debit authorization has been received orally
    over the telephone via a recorded call."""


class TransferDebitUsageConfigurationDict(TypedDict):
    expected_frequency: OriginatorExpectedTransferFrequencyOrStr
    expected_highest_amount: str
    expected_average_amount: str
    expected_monthly_amount: str
    sec_codes: list[AchclassOrStr]
