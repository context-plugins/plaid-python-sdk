from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .w2 import W2, W2Dict


class Taxform(SdkBaseModel):
    """Data about an official document used to report the user's income to the IRS."""

    doc_id: Optional[str] = UNSET
    """An identifier of the document referenced by the document metadata."""

    document_type: str
    """The type of tax document. Currently, the only supported value is ``w2``."""

    w2: Optional[W2] = UNSET
    """W2 is an object that represents income data taken from a W2 tax document."""


class TaxformDict(TypedDict):
    doc_id: NotRequired[str]
    document_type: str
    w2: NotRequired[W2 | W2Dict]
