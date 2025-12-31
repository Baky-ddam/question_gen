"""
Pattern listing and detail routes
"""
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from api.dependencies import get_generator
from api.schemas.patterns import PatternSummary, PatternDetail, PatternListResponse

router = APIRouter()


@router.get("", response_model=PatternListResponse)
async def list_patterns(
    level: Optional[str] = Query(None, description="Filter by CEFR level (A1, A2, B1, B2, C1, C2)"),
    focus: Optional[str] = Query(None, description="Filter by grammar focus"),
    domain: Optional[str] = Query(None, description="Filter by domain"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(50, ge=1, le=100, description="Items per page"),
    generator=Depends(get_generator)
):
    """List all patterns with optional filtering"""
    patterns = generator.patterns

    # Apply filters
    if level:
        patterns = [p for p in patterns if p.get("level", "").upper() == level.upper()]
    if focus:
        patterns = [p for p in patterns if p.get("focus", "").lower() == focus.lower()]
    if domain:
        patterns = [p for p in patterns if p.get("domain", "").lower() == domain.lower()]

    # Pagination
    total = len(patterns)
    pages = (total + limit - 1) // limit
    start = (page - 1) * limit
    end = start + limit
    paginated = patterns[start:end]

    # Convert to summaries
    summaries = [
        PatternSummary(
            pattern_id=p.get("pattern_id", ""),
            focus=p.get("focus", ""),
            level=p.get("level", ""),
            domain=p.get("domain", ""),
            category=p.get("category", "")
        )
        for p in paginated
    ]

    return PatternListResponse(
        patterns=summaries,
        total=total,
        page=page,
        pages=pages
    )


@router.get("/{pattern_id}", response_model=PatternDetail)
async def get_pattern(pattern_id: str, generator=Depends(get_generator)):
    """Get full details of a specific pattern"""
    pattern = generator.pattern_loader.get_pattern_by_id(pattern_id)

    if pattern is None:
        raise HTTPException(status_code=404, detail=f"Pattern not found: {pattern_id}")

    return PatternDetail(
        pattern_id=pattern.get("pattern_id", ""),
        focus=pattern.get("focus", ""),
        level=pattern.get("level", ""),
        domain=pattern.get("domain", ""),
        category=pattern.get("category", ""),
        template=pattern.get("template", ""),
        template_type=pattern.get("template_type"),
        subject_group=pattern.get("subject_group"),
        sub_grammar=pattern.get("sub_grammar", []),
        explanation=pattern.get("explanation", ""),
        example=pattern.get("example"),
        chunks=pattern.get("chunks", {})
    )


@router.get("/focus/list")
async def list_focuses(generator=Depends(get_generator)):
    """Get list of all unique grammar focuses"""
    focuses = set()
    for p in generator.patterns:
        if p.get("focus"):
            focuses.add(p["focus"])
    return {"focuses": sorted(focuses)}


@router.get("/level/list")
async def list_levels(generator=Depends(get_generator)):
    """Get list of all unique levels"""
    levels = set()
    for p in generator.patterns:
        if p.get("level"):
            levels.add(p["level"])
    return {"levels": sorted(levels)}


@router.get("/domain/list")
async def list_domains(generator=Depends(get_generator)):
    """Get list of all unique domains"""
    domains = set()
    for p in generator.patterns:
        if p.get("domain"):
            domains.add(p["domain"])
    return {"domains": sorted(domains)}
