from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountSubtype(str, Enum):
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    _401A = "401a"
    """The ``401a`` account subtype."""

    _401K = "401k"
    """The ``401k`` account subtype."""

    _403_B = "403B"
    """The ``403B`` account subtype."""

    _457B = "457b"
    """The ``457b`` account subtype."""

    _529 = "529"
    """The ``529`` account subtype."""

    AUTO = "auto"
    """The ``auto`` account subtype."""

    BROKERAGE = "brokerage"
    """The ``brokerage`` account subtype."""

    BUSINESS = "business"
    """The ``business`` account subtype."""

    CASH_ISA = "cash isa"
    """The ``cash isa`` account subtype."""

    CASH_MANAGEMENT = "cash management"
    """The ``cash management`` account subtype."""

    CD = "cd"
    """The ``cd`` account subtype."""

    CHECKING = "checking"
    """The ``checking`` account subtype."""

    COMMERCIAL = "commercial"
    """The ``commercial`` account subtype."""

    CONSTRUCTION = "construction"
    """The ``construction`` account subtype."""

    CONSUMER = "consumer"
    """The ``consumer`` account subtype."""

    CREDIT_CARD = "credit card"
    """The ``credit card`` account subtype."""

    CRYPTO_EXCHANGE = "crypto exchange"
    """The ``crypto exchange`` account subtype."""

    EBT = "ebt"
    """The ``ebt`` account subtype."""

    EDUCATION_SAVINGS_ACCOUNT = "education savings account"
    """The ``education savings account`` account subtype."""

    FHSA = "fhsa"
    """The ``fhsa`` account subtype."""

    FIXED_ANNUITY = "fixed annuity"
    """The ``fixed annuity`` account subtype."""

    GIC = "gic"
    """The ``gic`` account subtype."""

    HEALTH_REIMBURSEMENT_ARRANGEMENT = "health reimbursement arrangement"
    """The ``health reimbursement arrangement`` account subtype."""

    HOME_EQUITY = "home equity"
    """The ``home equity`` account subtype."""

    HSA = "hsa"
    """The ``hsa`` account subtype."""

    ISA = "isa"
    """The ``isa`` account subtype."""

    IRA = "ira"
    """The ``ira`` account subtype."""

    KEOGH = "keogh"
    """The ``keogh`` account subtype."""

    LIF = "lif"
    """The ``lif`` account subtype."""

    LIFE_INSURANCE = "life insurance"
    """The ``life insurance`` account subtype."""

    LIMITED_PURPOSE_CHECKING = "limited purpose checking"
    """The ``limited purpose checking`` account subtype."""

    LINE_OF_CREDIT = "line of credit"
    """The ``line of credit`` account subtype."""

    LIRA = "lira"
    """The ``lira`` account subtype."""

    LOAN = "loan"
    """The ``loan`` account subtype."""

    LRIF = "lrif"
    """The ``lrif`` account subtype."""

    LRSP = "lrsp"
    """The ``lrsp`` account subtype."""

    MONEY_MARKET = "money market"
    """The ``money market`` account subtype."""

    MORTGAGE = "mortgage"
    """The ``mortgage`` account subtype."""

    MUTUAL_FUND = "mutual fund"
    """The ``mutual fund`` account subtype."""

    NON_CUSTODIAL_WALLET = "non-custodial wallet"
    """The ``non-custodial wallet`` account subtype."""

    NON_TAXABLE_BROKERAGE_ACCOUNT = "non-taxable brokerage account"
    """The ``non-taxable brokerage account`` account subtype."""

    OTHER = "other"
    """The ``other`` account subtype."""

    OTHER_INSURANCE = "other insurance"
    """The ``other insurance`` account subtype."""

    OTHER_ANNUITY = "other annuity"
    """The ``other annuity`` account subtype."""

    OVERDRAFT = "overdraft"
    """The ``overdraft`` account subtype."""

    PAYPAL = "paypal"
    """The ``paypal`` account subtype."""

    PAYROLL = "payroll"
    """The ``payroll`` account subtype."""

    PENSION = "pension"
    """The ``pension`` account subtype."""

    PREPAID = "prepaid"
    """The ``prepaid`` account subtype."""

    PRIF = "prif"
    """The ``prif`` account subtype."""

    PROFIT_SHARING_PLAN = "profit sharing plan"
    """The ``profit sharing plan`` account subtype."""

    QSHR = "qshr"
    """The ``qshr`` account subtype."""

    RDSP = "rdsp"
    """The ``rdsp`` account subtype."""

    RESP = "resp"
    """The ``resp`` account subtype."""

    RETIREMENT = "retirement"
    """The ``retirement`` account subtype."""

    RLIF = "rlif"
    """The ``rlif`` account subtype."""

    ROTH = "roth"
    """The ``roth`` account subtype."""

    ROTH_401K = "roth 401k"
    """The ``roth 401k`` account subtype."""

    ROTH_403_B = "roth 403B"
    """The ``roth 403B`` account subtype."""

    ROTH_457B = "roth 457b"
    """The ``roth 457b`` account subtype."""

    ROTH_PENSION = "roth pension"
    """The ``roth pension`` account subtype."""

    ROTH_PROFIT_SHARING_PLAN = "roth profit sharing plan"
    """The ``roth profit sharing plan`` account subtype."""

    ROTH_THRIFT_SAVINGS_PLAN = "roth thrift savings plan"
    """The ``roth thrift savings plan`` account subtype."""

    RRIF = "rrif"
    """The ``rrif`` account subtype."""

    RRSP = "rrsp"
    """The ``rrsp`` account subtype."""

    SARSEP = "sarsep"
    """The ``sarsep`` account subtype."""

    SAVINGS = "savings"
    """The ``savings`` account subtype."""

    SEP_IRA = "sep ira"
    """The ``sep ira`` account subtype."""

    SIMPLE_IRA = "simple ira"
    """The ``simple ira`` account subtype."""

    SIPP = "sipp"
    """The ``sipp`` account subtype."""

    STOCK_PLAN = "stock plan"
    """The ``stock plan`` account subtype."""

    STUDENT = "student"
    """The ``student`` account subtype."""

    THRIFT_SAVINGS_PLAN = "thrift savings plan"
    """The ``thrift savings plan`` account subtype."""

    TFSA = "tfsa"
    """The ``tfsa`` account subtype."""

    TRUST = "trust"
    """The ``trust`` account subtype."""

    UGMA = "ugma"
    """The ``ugma`` account subtype."""

    UTMA = "utma"
    """The ``utma`` account subtype."""

    VARIABLE_ANNUITY = "variable annuity"
    """The ``variable annuity`` account subtype."""

    __str__ = str.__str__


AccountSubtypeOrStr: TypeAlias = Annotated[AccountSubtype | str, open_enum_validator(AccountSubtype)]
