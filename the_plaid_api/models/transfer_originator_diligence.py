from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .transfer_credit_usage_configuration import TransferCreditUsageConfiguration, TransferCreditUsageConfigurationDict
from .transfer_debit_usage_configuration import TransferDebitUsageConfiguration, TransferDebitUsageConfigurationDict
from .transfer_funding_account import TransferFundingAccount, TransferFundingAccountDict
from .transfer_originator_address import TransferOriginatorAddress, TransferOriginatorAddressDict


class TransferOriginatorDiligence(SdkBaseModel):
    """The diligence information for the originator."""

    dba: str
    """The business name of the originator."""

    tax_id: str
    """The tax ID of the originator."""

    credit_usage_configuration: OptionalNullable[TransferCreditUsageConfiguration] = UNSET
    """Specifies the originator's expected usage of credits. For all dollar amounts, use a decimal string with two
    digits of precision e.g. "10.00". This field is required if the originator is expected to process credit
    transfers."""

    debit_usage_configuration: OptionalNullable[TransferDebitUsageConfiguration] = UNSET
    """Specifies the originator's expected usage of debits. For all dollar amounts, use a decimal string with two digits
    of precision e.g. "10.00". This field is required if the originator is expected to process debit transfers."""

    address: TransferOriginatorAddress
    """The originator's address."""

    website: str
    """The website of the originator."""

    naics_code: str
    """The NAICS code of the originator."""

    funding_account: TransferFundingAccount
    """The originator's funding account, linked with Plaid Link or ``/transfer/migrate_account``."""


class TransferOriginatorDiligenceDict(TypedDict):
    dba: str
    tax_id: str
    credit_usage_configuration: NotRequired[
        TransferCreditUsageConfiguration | TransferCreditUsageConfigurationDict | None
    ]
    debit_usage_configuration: NotRequired[TransferDebitUsageConfiguration | TransferDebitUsageConfigurationDict | None]
    address: TransferOriginatorAddress | TransferOriginatorAddressDict
    website: str
    naics_code: str
    funding_account: TransferFundingAccount | TransferFundingAccountDict
