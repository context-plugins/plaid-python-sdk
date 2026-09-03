from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CounterpartyType(str, Enum):
    """The counterparty type.

    ``merchant``: a provider of goods or services for purchase ``financial_institution``: a financial entity (bank,
    credit union, BNPL, fintech) ``payment_app``: a transfer or P2P app (e.g. Zelle) ``marketplace``: a marketplace
    (e.g. DoorDash, Google Play Store) ``payment_terminal``: a point-of-sale payment terminal (e.g. Square, Toast)
    ``income_source``: the payer in an income transaction (e.g., an employer, client, or government agency)"""

    MERCHANT = "merchant"
    FINANCIAL_INSTITUTION = "financial_institution"
    PAYMENT_APP = "payment_app"
    MARKETPLACE = "marketplace"
    PAYMENT_TERMINAL = "payment_terminal"
    INCOME_SOURCE = "income_source"

    __str__ = str.__str__


CounterpartyTypeOrStr: TypeAlias = Annotated[CounterpartyType | str, open_enum_validator(CounterpartyType)]
