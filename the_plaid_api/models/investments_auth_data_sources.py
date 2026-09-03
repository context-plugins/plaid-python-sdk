from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.data_sources import DataSourcesOrStr


class InvestmentsAuthDataSources(SdkBaseModel):
    """Object with metadata pertaining to the source of data for the account numbers, owners, and holdings that are
    returned."""

    numbers: Optional[DataSourcesOrStr] = UNSET
    """A description of the source of data for a given product/data type.

    ``INSTITUTION``: The institution supports this product, and the data was provided by the institution.
    ``INSTITUTION_MASK``: The user manually provided the full account number, which was matched to the account mask
    provided by the institution. Only applicable to the ``numbers`` data type. ``USER``: The institution does not
    support this product, and the data was manually provided by the user."""

    owners: Optional[DataSourcesOrStr] = UNSET
    """A description of the source of data for a given product/data type.

    ``INSTITUTION``: The institution supports this product, and the data was provided by the institution.
    ``INSTITUTION_MASK``: The user manually provided the full account number, which was matched to the account mask
    provided by the institution. Only applicable to the ``numbers`` data type. ``USER``: The institution does not
    support this product, and the data was manually provided by the user."""

    holdings: Optional[DataSourcesOrStr] = UNSET
    """A description of the source of data for a given product/data type.

    ``INSTITUTION``: The institution supports this product, and the data was provided by the institution.
    ``INSTITUTION_MASK``: The user manually provided the full account number, which was matched to the account mask
    provided by the institution. Only applicable to the ``numbers`` data type. ``USER``: The institution does not
    support this product, and the data was manually provided by the user."""


class InvestmentsAuthDataSourcesDict(TypedDict):
    numbers: NotRequired[DataSourcesOrStr]
    owners: NotRequired[DataSourcesOrStr]
    holdings: NotRequired[DataSourcesOrStr]
