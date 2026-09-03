from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionCode(str, Enum):
    """An identifier classifying the transaction type.

    This field is populated for European institutions, as well as certain institutions in the United States. For
    institutions where this classification is not available, this field is set to ``null``.

    ``adjustment:`` Bank adjustment

    ``atm:`` Cash deposit or withdrawal via an automated teller machine

    ``bank charge:`` Charge or fee levied by the institution

    ``bill payment``: Payment of a bill

    ``cash:`` Cash deposit or withdrawal

    ``cash advance:`` Cash advance drawn against a credit card or line of credit

    ``cashback:`` Cash withdrawal while making a debit card purchase

    ``cheque:`` Document ordering the payment of money to another person or organization

    ``direct debit:`` Automatic withdrawal of funds initiated by a third party at a regular interval

    ``interest:`` Interest earned or incurred

    ``late fee:`` Fee associated with a late or past-due payment

    ``membership fee:`` Annual or recurring membership fee

    ``payment:`` One-off outbound payment not classified as a bill payment, direct debit, or standing order

    ``purchase:`` Purchase made with a debit or credit card

    ``refund:`` Merchant credit or return, such as a refund of a prior purchase

    ``returned item fee:`` Fee for a returned item, such as a returned check or stop payment

    ``standing order:`` Payment instructed by the account holder to a third party at a regular interval

    ``transfer:`` Transfer of money between accounts"""

    ADJUSTMENT = "adjustment"
    ATM = "atm"
    BANK_CHARGE = "bank charge"
    BILL_PAYMENT = "bill payment"
    CASH = "cash"
    CASH_ADVANCE = "cash advance"
    CASHBACK = "cashback"
    CHEQUE = "cheque"
    DIRECT_DEBIT = "direct debit"
    INTEREST = "interest"
    LATE_FEE = "late fee"
    MEMBERSHIP_FEE = "membership fee"
    PAYMENT = "payment"
    PURCHASE = "purchase"
    REFUND = "refund"
    RETURNED_ITEM_FEE = "returned item fee"
    STANDING_ORDER = "standing order"
    TRANSFER = "transfer"

    __str__ = str.__str__


TransactionCodeOrStr: TypeAlias = Annotated[TransactionCode | str, open_enum_validator(TransactionCode)]
