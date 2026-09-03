from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PersonalFinanceCategoryVersion(str, Enum):
    """Indicates which version of the personal finance category taxonomy is being used. `View PFCv2 and PFCv1 taxonomies
    <https://plaid.com/documents/pfc-taxonomy-all.csv>`__.

    If you enabled Transactions or Enrich before December 3, 2025 you will receive the ``v1`` taxonomy by default and
    may request ``v2`` by explicitly setting this field to ``v2`` in the request.

    If you enabled Transactions or Enrich on or after December 3, 2025, you may only receive the ``v2`` taxonomy."""

    V1 = "v1"
    V2 = "v2"

    __str__ = str.__str__


PersonalFinanceCategoryVersionOrStr: TypeAlias = Annotated[
    PersonalFinanceCategoryVersion | str, open_enum_validator(PersonalFinanceCategoryVersion)
]
