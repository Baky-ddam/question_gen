"""
EYESH Question Generator - Web API
==================================
FastAPI application for generating English exam questions.
"""
import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

from api.routes import health, patterns, exams

# Initialize FastAPI app
app = FastAPI(
    title="EYESH Question Generator API",
    description="Generate English exam questions from pattern templates",
    version="1.0.0"
)

# Get base directory
BASE_DIR = Path(__file__).resolve().parent

# Check if running on Vercel (serverless) or locally
IS_VERCEL = os.environ.get("VERCEL", False)

# Mount static files only when not on Vercel (Vercel serves from public/)
if not IS_VERCEL:
    app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Include API routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(patterns.router, prefix="/api/patterns", tags=["Patterns"])
app.include_router(exams.router, prefix="/api/exams", tags=["Exams"])


# HTML Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/patterns", response_class=HTMLResponse)
async def patterns_page(request: Request):
    """Pattern browser page"""
    return templates.TemplateResponse("patterns.html", {"request": request})


@app.get("/test", response_class=HTMLResponse)
async def test_page(request: Request):
    """Developer test page"""
    return templates.TemplateResponse("test.html", {"request": request})


@app.get("/exam", response_class=HTMLResponse)
async def exam_page(request: Request):
    """User exam page"""
    return templates.TemplateResponse("exam.html", {"request": request})


# Run with: uvicorn app:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
