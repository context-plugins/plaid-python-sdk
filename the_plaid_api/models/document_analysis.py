from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .aamvaanalysis import Aamvaanalysis, AamvaanalysisDict
from .enums.document_authenticity_match_code import DocumentAuthenticityMatchCodeOrStr
from .enums.image_quality import ImageQualityOrStr
from .fraud_analysis_details import FraudAnalysisDetails, FraudAnalysisDetailsDict
from .human_review import HumanReview, HumanReviewDict
from .image_quality_details import ImageQualityDetails, ImageQualityDetailsDict
from .physical_document_extracted_data_analysis import (
    PhysicalDocumentExtractedDataAnalysis,
    PhysicalDocumentExtractedDataAnalysisDict,
)


class DocumentAnalysis(SdkBaseModel):
    """High level descriptions of how the associated document was processed. If a document fails verification, the
    details in the ``analysis`` object should help clarify why the document was rejected."""

    authenticity: DocumentAuthenticityMatchCodeOrStr
    """High level summary of whether the document in the provided image matches the formatting rules and security checks
    for the associated jurisdiction.

    For example, most identity documents have formatting rules like the following:


    The image of the person's face must have a certain contrast in order to highlight skin tone


    The subject in the document's image must remove eye glasses and pose in a certain way


    The informational fields (name, date of birth, ID number, etc.) must be colored and aligned according to specific
    rules


    Security features like watermarks and background patterns must be present

    So a ``match`` status for this field indicates that the document in the provided image seems to conform to the
    various formatting and security rules associated with the detected document."""

    image_quality: ImageQualityOrStr
    """A high level description of the quality of the image the user submitted.

    For example, an image that is blurry, distorted by glare from a nearby light source, or improperly framed might be
    marked as low or medium quality. Poor quality images are more likely to fail OCR and/or template conformity checks.

    Note: By default, Plaid will let a user recapture document images twice before failing the entire session if we
    attribute the failure to low image quality."""

    extracted_data: PhysicalDocumentExtractedDataAnalysis | None
    """Analysis of the data extracted from the submitted document."""

    fraud_analysis_details: FraudAnalysisDetails | None
    """Details about the fraud analysis performed on the document."""

    image_quality_details: ImageQualityDetails | None
    """Details about the image quality of the document."""

    human_review: OptionalNullable[HumanReview] = UNSET
    """Details about the human review check, which refers to a check that is performed by a document specialist."""

    aamva_verification: Aamvaanalysis | None
    """Analyzed AAMVA data for the associated hit.

    Note: This field is only available for U.S. driver's licenses issued by participating states."""


class DocumentAnalysisDict(TypedDict):
    authenticity: DocumentAuthenticityMatchCodeOrStr
    image_quality: ImageQualityOrStr
    extracted_data: PhysicalDocumentExtractedDataAnalysis | PhysicalDocumentExtractedDataAnalysisDict | None
    fraud_analysis_details: FraudAnalysisDetails | FraudAnalysisDetailsDict | None
    image_quality_details: ImageQualityDetails | ImageQualityDetailsDict | None
    human_review: NotRequired[HumanReview | HumanReviewDict | None]
    aamva_verification: Aamvaanalysis | AamvaanalysisDict | None
