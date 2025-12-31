"""
Pydantic models for exam-related API endpoints
"""
from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime


class Question(BaseModel):
    """A single exam question"""
    question_id: str
    pattern_id: str
    focus: str
    level: str
    domain: str
    sentence: str
    options: Dict[str, str]
    correct_answer: Optional[str] = None  # Hidden in user mode
    explanation: Optional[str] = None  # Hidden in user mode


class ExamRequest(BaseModel):
    """Request to generate an exam"""
    count: int = Field(default=10, ge=1, le=50, description="Number of questions")
    level: Optional[str] = Field(default=None, description="Level filter: beginner, intermediate, advanced, or A1-C2")
    pattern_id: Optional[str] = Field(default=None, description="Specific pattern ID")
    mode: Literal["developer", "user"] = Field(default="user", description="Exam mode")


class ExamResponse(BaseModel):
    """Response with generated exam"""
    exam_id: str
    questions: List[Question]
    generated_at: str
    mode: str
    total_questions: int


class ExamSubmitRequest(BaseModel):
    """Request to submit exam answers"""
    exam_id: str
    answers: Dict[str, str]  # question_id -> selected option (A, B, C, D, E)


class QuestionResult(BaseModel):
    """Result for a single question"""
    question_id: str
    user_answer: str
    correct_answer: str
    is_correct: bool
    explanation: str


class ExamSubmitResponse(BaseModel):
    """Response after exam submission"""
    exam_id: str
    total_questions: int
    correct: int
    incorrect: int
    score_percentage: float
    results: List[QuestionResult]
