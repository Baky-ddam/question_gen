"""
EYESH English Question Generator
---------------------------------
A system for generating grammatically correct English exam questions
from JSON pattern templates.
"""

__version__ = "1.0.0"
__author__ = "EYESH Question Generator Team"

from .pattern_loader import PatternLoader
from .question_generator import QuestionGenerator
from .distractor_generator import DistractorGenerator
from .grammar_engine import GrammarEngine

__all__ = [
    "PatternLoader",
    "QuestionGenerator",
    "DistractorGenerator",
    "GrammarEngine"
]
