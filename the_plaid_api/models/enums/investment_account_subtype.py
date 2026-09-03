from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvestmentAccountSubtype(str, Enum):
    """Valid account subtypes for investment accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-investment>`__."""

    _529 = "529"
    """The ``529`` investment account subtype."""

    _401A = "401a"
    """The ``401a`` investment account subtype."""

    _401K = "401k"
    """The ``401k`` investment account subtype."""

    _403_B = "403B"
    """The ``403B`` investment account subtype."""

    _457B = "457b"
    """The ``457b`` investment account subtype."""

    BROKERAGE = "brokerage"
    """The ``brokerage`` investment account subtype."""

    CASH_ISA = "cash isa"
    """The ``cash isa`` investment account subtype."""

    CRYPTO_EXCHANGE = "crypto exchange"
    """The ``crypto exchange`` investment account subtype."""

    EDUCATION_SAVINGS_ACCOUNT = "education savings account"
    """The ``education savings account`` investment account subtype."""

    FHSA = "fhsa"
    """The ``fhsa`` investment account subtype."""

    FIXED_ANNUITY = "fixed annuity"
    """The ``fixed annuity`` investment account subtype."""

    GIC = "gic"
    """The ``gic`` investment account subtype."""

    HEALTH_REIMBURSEMENT_ARRANGEMENT = "health reimbursement arrangement"
    """The ``health reimbursement arrangement`` investment account subtype."""

    HSA = "hsa"
    """The ``hsa`` investment account subtype."""

    IRA = "ira"
    """The ``ira`` investment account subtype."""

    ISA = "isa"
    """The ``isa`` investment account subtype."""

    KEOGH = "keogh"
    """The ``keogh`` investment account subtype."""

    LIF = "lif"
    """The ``lif`` investment account subtype."""

    LIFE_INSURANCE = "life insurance"
    """The ``life insurance`` investment account subtype."""

    LINE_OF_CREDIT = "line of credit"
    """The ``line of credit`` investment account subtype."""

    LIRA = "lira"
    """The ``lira`` investment account subtype."""

    LRIF = "lrif"
    """The ``lrif`` investment account subtype."""

    LRSP = "lrsp"
    """The ``lrsp`` investment account subtype."""

    MUTUAL_FUND = "mutual fund"
    """The ``mutual fund`` investment account subtype."""

    NON_CUSTODIAL_WALLET = "non-custodial wallet"
    """The ``non-custodial wallet`` investment account subtype."""

    NON_TAXABLE_BROKERAGE_ACCOUNT = "non-taxable brokerage account"
    """The ``non-taxable brokerage account`` investment account subtype."""

    OTHER = "other"
    """The ``other`` investment account subtype."""

    OTHER_ANNUITY = "other annuity"
    """The ``other annuity`` investment account subtype."""

    OTHER_INSURANCE = "other insurance"
    """The ``other insurance`` investment account subtype."""

    PENSION = "pension"
    """The ``pension`` investment account subtype."""

    PRIF = "prif"
    """The ``prif`` investment account subtype."""

    PROFIT_SHARING_PLAN = "profit sharing plan"
    """The ``profit sharing plan`` investment account subtype."""

    QSHR = "qshr"
    """The ``qshr`` investment account subtype."""

    RDSP = "rdsp"
    """The ``rdsp`` investment account subtype."""

    RESP = "resp"
    """The ``resp`` investment account subtype."""

    RETIREMENT = "retirement"
    """The ``retirement`` investment account subtype."""

    RLIF = "rlif"
    """The ``rlif`` investment account subtype."""

    ROTH = "roth"
    """The ``roth`` investment account subtype."""

    ROTH_401K = "roth 401k"
    """The ``roth 401k`` investment account subtype."""

    ROTH_403_B = "roth 403B"
    """The ``roth 403B`` investment account subtype."""

    ROTH_457B = "roth 457b"
    """The ``roth 457b`` investment account subtype."""

    ROTH_PENSION = "roth pension"
    """The ``roth pension`` investment account subtype."""

    ROTH_PROFIT_SHARING_PLAN = "roth profit sharing plan"
    """The ``roth profit sharing plan`` investment account subtype."""

    ROTH_THRIFT_SAVINGS_PLAN = "roth thrift savings plan"
    """The ``roth thrift savings plan`` investment account subtype."""

    RRIF = "rrif"
    """The ``rrif`` investment account subtype."""

    RRSP = "rrsp"
    """The ``rrsp`` investment account subtype."""

    SARSEP = "sarsep"
    """The ``sarsep`` investment account subtype."""

    SEP_IRA = "sep ira"
    """The ``sep ira`` investment account subtype."""

    SIMPLE_IRA = "simple ira"
    """The ``simple ira`` investment account subtype."""

    SIPP = "sipp"
    """The ``sipp`` investment account subtype."""

    STOCK_PLAN = "stock plan"
    """The ``stock plan`` investment account subtype."""

    THRIFT_SAVINGS_PLAN = "thrift savings plan"
    """The ``thrift savings plan`` investment account subtype."""

    TFSA = "tfsa"
    """The ``tfsa`` investment account subtype."""

    TRUST = "trust"
    """The ``trust`` investment account subtype."""

    UGMA = "ugma"
    """The ``ugma`` investment account subtype."""

    UTMA = "utma"
    """The ``utma`` investment account subtype."""

    VARIABLE_ANNUITY = "variable annuity"
    """The ``variable annuity`` investment account subtype."""

    ALL = "all"
    """The ``all`` investment account subtype."""

    __str__ = str.__str__


InvestmentAccountSubtypeOrStr: TypeAlias = Annotated[
    InvestmentAccountSubtype | str, open_enum_validator(InvestmentAccountSubtype)
]
