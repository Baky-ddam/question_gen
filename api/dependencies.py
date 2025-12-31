"""
API Dependencies - Shared state and utilities
"""
from functools import lru_cache
from pathlib import Path
from generator.question_generator import QuestionGenerator

# Get the base directory (project root)
BASE_DIR = Path(__file__).resolve().parent.parent
PATTERN_DIR = BASE_DIR / "pattern"


@lru_cache()
def get_generator() -> QuestionGenerator:
    """
    Get singleton QuestionGenerator instance.
    Patterns are loaded once at startup and cached.
    """
    gen = QuestionGenerator(pattern_dir=str(PATTERN_DIR))
    gen.load_patterns()
    return gen
