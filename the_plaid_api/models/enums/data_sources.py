from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DataSources(str, Enum):
    """A description of the source of data for a given product/data type.

    ``INSTITUTION``: The institution supports this product, and the data was provided by the institution.
    ``INSTITUTION_MASK``: The user manually provided the full account number, which was matched to the account mask
    provided by the institution. Only applicable to the ``numbers`` data type. ``USER``: The institution does not
    support this product, and the data was manually provided by the user."""

    INSTITUTION = "INSTITUTION"
    INSTITUTION_MASK = "INSTITUTION_MASK"
    USER = "USER"

    __str__ = str.__str__


DataSourcesOrStr: TypeAlias = Annotated[DataSources | str, open_enum_validator(DataSources)]
