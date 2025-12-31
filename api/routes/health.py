"""
Health check and stats routes
"""
import os
from pathlib import Path
from fastapi import APIRouter, Depends
from api.dependencies import get_generator, BASE_DIR, PATTERN_DIR
from api.schemas.patterns import StatsResponse

router = APIRouter()


@router.get("/health")
async def health_check(generator=Depends(get_generator)):
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "patterns_loaded": len(generator.patterns)
    }


@router.get("/debug")
async def debug_info():
    """Debug endpoint to check paths"""
    pattern_exists = PATTERN_DIR.exists()
    pattern_files = []
    if pattern_exists:
        pattern_files = [f.name for f in PATTERN_DIR.iterdir()][:10]

    return {
        "base_dir": str(BASE_DIR),
        "pattern_dir": str(PATTERN_DIR),
        "pattern_dir_exists": pattern_exists,
        "cwd": os.getcwd(),
        "pattern_sample_files": pattern_files
    }


@router.get("/stats", response_model=StatsResponse)
async def get_stats(generator=Depends(get_generator)):
    """Get pattern statistics"""
    stats = generator.get_stats()
    return StatsResponse(
        total_patterns=stats.get("total_patterns", 0),
        by_focus=stats.get("by_focus", {}),
        by_level=stats.get("by_level", {}),
        by_domain=stats.get("by_domain", {})
    )
