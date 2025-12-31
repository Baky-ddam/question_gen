"""
API Dependencies - Shared state and utilities
"""
from functools import lru_cache
from generator.question_generator import QuestionGenerator


@lru_cache()
def get_generator() -> QuestionGenerator:
    """
    Get singleton QuestionGenerator instance.
    Patterns are loaded once at startup and cached.
    """
    gen = QuestionGenerator(pattern_dir="pattern")
    gen.load_patterns()
    return gen
