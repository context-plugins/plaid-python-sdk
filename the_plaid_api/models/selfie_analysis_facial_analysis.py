from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.selfie_analysis_facial_analysis_outcome import SelfieAnalysisFacialAnalysisOutcomeOrStr


class SelfieAnalysisFacialAnalysis(SdkBaseModel):
    """Analysis of the facial features of the selfie when compared to the face in the uploaded document, if one is
    present."""

    left_eye: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    right_eye: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    left_brow: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    right_brow: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    forehead: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    middle_forehead: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    nose: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    philtrum: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    mouth: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    jaw: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    left_cheek: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""

    right_cheek: SelfieAnalysisFacialAnalysisOutcomeOrStr
    """Outcome of the facial analysis for a specific facial feature."""


class SelfieAnalysisFacialAnalysisDict(TypedDict):
    left_eye: SelfieAnalysisFacialAnalysisOutcomeOrStr
    right_eye: SelfieAnalysisFacialAnalysisOutcomeOrStr
    left_brow: SelfieAnalysisFacialAnalysisOutcomeOrStr
    right_brow: SelfieAnalysisFacialAnalysisOutcomeOrStr
    forehead: SelfieAnalysisFacialAnalysisOutcomeOrStr
    middle_forehead: SelfieAnalysisFacialAnalysisOutcomeOrStr
    nose: SelfieAnalysisFacialAnalysisOutcomeOrStr
    philtrum: SelfieAnalysisFacialAnalysisOutcomeOrStr
    mouth: SelfieAnalysisFacialAnalysisOutcomeOrStr
    jaw: SelfieAnalysisFacialAnalysisOutcomeOrStr
    left_cheek: SelfieAnalysisFacialAnalysisOutcomeOrStr
    right_cheek: SelfieAnalysisFacialAnalysisOutcomeOrStr
