from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.document_date_of_birth_match_code import DocumentDateOfBirthMatchCodeOrStr
from .enums.document_name_match_code import DocumentNameMatchCodeOrStr
from .enums.expiration_date import ExpirationDateOrStr
from .enums.issuing_country import IssuingCountryOrStr


class PhysicalDocumentExtractedDataAnalysis(SdkBaseModel):
    """Analysis of the data extracted from the submitted document."""

    name: DocumentNameMatchCodeOrStr
    """A match summary describing the cross comparison between the subject's name, extracted from the document image,
    and the name they separately provided to the identity verification attempt."""

    date_of_birth: DocumentDateOfBirthMatchCodeOrStr
    """A match summary describing the cross comparison between the subject's date of birth, extracted from the document
    image, and the date of birth they separately provided to the identity verification attempt."""

    expiration_date: ExpirationDateOrStr
    """A description of whether the associated document was expired when the verification was performed.

    Note: In the case where an expiration date is not present on the document or failed to be extracted, this value will
    be ``no_data``."""

    issuing_country: IssuingCountryOrStr
    """A binary match indicator specifying whether the country that issued the provided document matches the country
    that the user separately provided to Plaid.

    Note: You can configure whether a ``no_match`` on ``issuing_country`` fails the ``documentary_verification`` by
    editing your Plaid Template."""


class PhysicalDocumentExtractedDataAnalysisDict(TypedDict):
    name: DocumentNameMatchCodeOrStr
    date_of_birth: DocumentDateOfBirthMatchCodeOrStr
    expiration_date: ExpirationDateOrStr
    issuing_country: IssuingCountryOrStr
