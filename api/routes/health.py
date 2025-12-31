"""
Health check and stats routes
"""
from fastapi import APIRouter, Depends
from api.dependencies import get_generator
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
