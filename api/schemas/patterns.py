"""
Pydantic models for pattern-related API endpoints
"""
from typing import List, Dict, Optional, Any
from pydantic import BaseModel


class PatternSummary(BaseModel):
    """Summary of a pattern for listing"""
    pattern_id: str
    focus: str
    level: str
    domain: str
    category: str


class PatternDetail(BaseModel):
    """Full pattern details"""
    pattern_id: str
    focus: str
    level: str
    domain: str
    category: str
    template: str
    template_type: Optional[str] = None
    subject_group: Optional[str] = None
    sub_grammar: Optional[List[str]] = []
    explanation: str
    example: Optional[str] = None
    chunks: Dict[str, Any]


class PatternListResponse(BaseModel):
    """Response for pattern listing"""
    patterns: List[PatternSummary]
    total: int
    page: int = 1
    pages: int = 1


class StatsResponse(BaseModel):
    """Response for stats endpoint"""
    total_patterns: int
    by_focus: Dict[str, int]
    by_level: Dict[str, int]
    by_domain: Dict[str, int]
