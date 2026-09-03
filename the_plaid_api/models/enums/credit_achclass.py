from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditAchclass(str, Enum):
    """Specifies the use case of the transfer. Required for transfers on an ACH network.

    ``"ccd"`` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    ``"ppd"`` - Prearranged Payment or Deposit - The transfer is part of a pre-existing relationship with a consumer.
    Authorization was obtained in writing either in person or via an electronic document signing, e.g. Docusign, by the
    consumer. Can be used for credits or debits.

    ``"web"`` - Internet-Initiated Entry. The transfer debits a consumer's bank account. Authorization from the consumer
    is obtained over the Internet (e.g. a web or mobile application). Can be used for single debits or recurring
    debits."""

    CCD = "ccd"
    PPD = "ppd"
    WEB = "web"

    __str__ = str.__str__


CreditAchclassOrStr: TypeAlias = Annotated[CreditAchclass | str, open_enum_validator(CreditAchclass)]
