from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.selfie_analysis_document_comparison import SelfieAnalysisDocumentComparisonOrStr
from .enums.selfie_analysis_liveness_check import SelfieAnalysisLivenessCheckOrStr
from .selfie_age_check import SelfieAgeCheck, SelfieAgeCheckDict
from .selfie_analysis_facial_analysis import SelfieAnalysisFacialAnalysis, SelfieAnalysisFacialAnalysisDict


class SelfieAnalysis(SdkBaseModel):
    """High level descriptions of how the associated selfie was processed. If a selfie fails verification, the details
    in the ``analysis`` object should help clarify why the selfie was rejected."""

    document_comparison: SelfieAnalysisDocumentComparisonOrStr
    """Information about the comparison between the selfie and the document (if documentary verification also ran)."""

    liveness_check: SelfieAnalysisLivenessCheckOrStr
    """Assessment of whether the selfie capture is of a real human being, as opposed to a picture of a human on a
    screen, a picture of a paper cut out, someone wearing a mask, or a deepfake."""

    age_check: OptionalNullable[SelfieAgeCheck] = UNSET
    """Age-estimation results from the selfie capture. This field is ``null`` when an age range could not be estimated
    from the selfie capture."""

    facial_analysis: OptionalNullable[SelfieAnalysisFacialAnalysis] = UNSET
    """Analysis of the facial features of the selfie when compared to the face in the uploaded document, if one is
    present."""


class SelfieAnalysisDict(TypedDict):
    document_comparison: SelfieAnalysisDocumentComparisonOrStr
    liveness_check: SelfieAnalysisLivenessCheckOrStr
    age_check: NotRequired[SelfieAgeCheckDict | None]
    facial_analysis: NotRequired[SelfieAnalysisFacialAnalysisDict | None]
