"""
Exam generation and submission routes
"""
import uuid
from datetime import datetime
from typing import Dict
from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_generator
from api.schemas.exams import (
    ExamRequest, ExamResponse, Question,
    ExamSubmitRequest, ExamSubmitResponse, QuestionResult
)

router = APIRouter()

# In-memory exam storage for grading
# In production, use Redis or database
exam_storage: Dict[str, Dict] = {}


def generate_exam_id() -> str:
    """Generate unique exam identifier"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique = uuid.uuid4().hex[:8]
    return f"exam_{timestamp}_{unique}"


def normalize_level(level: str) -> str:
    """Convert CEFR level codes to named levels for the generator"""
    if not level:
        return None

    level_lower = level.lower()

    # Already a named level
    if level_lower in ['beginner', 'intermediate', 'advanced']:
        return level_lower

    # CEFR code to named level
    cefr_map = {
        'a1': 'beginner', 'a2': 'beginner',
        'b1': 'intermediate', 'b2': 'intermediate',
        'c1': 'advanced', 'c2': 'advanced'
    }
    return cefr_map.get(level_lower)


@router.post("/generate", response_model=ExamResponse)
async def generate_exam(request: ExamRequest, generator=Depends(get_generator)):
    """Generate an exam with questions"""

    # Normalize level
    level = normalize_level(request.level) if request.level else None

    # Generate questions
    try:
        questions = generator.generate_multiple(
            count=request.count,
            pattern_id=request.pattern_id,
            level=level
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating questions: {str(e)}")

    if not questions:
        raise HTTPException(status_code=404, detail="No questions could be generated with given filters")

    # Generate exam ID
    exam_id = generate_exam_id()

    # Process questions based on mode
    processed_questions = []
    for q in questions:
        if request.mode == "developer":
            # Developer mode: show all info
            processed_questions.append(Question(
                question_id=q["question_id"],
                pattern_id=q["pattern_id"],
                focus=q["focus"],
                level=q["level"],
                domain=q.get("domain", ""),
                sentence=q["sentence"],
                options=q["options"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"]
            ))
        else:
            # User mode: hide answers
            processed_questions.append(Question(
                question_id=q["question_id"],
                pattern_id=q["pattern_id"],
                focus=q["focus"],
                level=q["level"],
                domain=q.get("domain", ""),
                sentence=q["sentence"],
                options=q["options"],
                correct_answer=None,
                explanation=None
            ))

    # Store exam for later grading (user mode only)
    if request.mode == "user":
        exam_storage[exam_id] = {
            "questions": questions,
            "generated_at": datetime.now().isoformat()
        }

    return ExamResponse(
        exam_id=exam_id,
        questions=processed_questions,
        generated_at=datetime.now().isoformat(),
        mode=request.mode,
        total_questions=len(processed_questions)
    )


@router.post("/submit", response_model=ExamSubmitResponse)
async def submit_exam(request: ExamSubmitRequest):
    """Submit exam answers and get results"""

    # Get stored exam
    exam_data = exam_storage.get(request.exam_id)
    if not exam_data:
        raise HTTPException(status_code=404, detail=f"Exam not found: {request.exam_id}")

    questions = exam_data["questions"]

    # Grade the exam
    results = []
    correct_count = 0

    for q in questions:
        question_id = q["question_id"]
        user_answer = request.answers.get(question_id, "")
        correct_answer = q["correct_answer"]
        is_correct = user_answer.upper() == correct_answer.upper() if user_answer else False

        if is_correct:
            correct_count += 1

        results.append(QuestionResult(
            question_id=question_id,
            user_answer=user_answer,
            correct_answer=correct_answer,
            is_correct=is_correct,
            explanation=q["explanation"]
        ))

    total = len(questions)
    score = (correct_count / total * 100) if total > 0 else 0

    # Clean up stored exam
    del exam_storage[request.exam_id]

    return ExamSubmitResponse(
        exam_id=request.exam_id,
        total_questions=total,
        correct=correct_count,
        incorrect=total - correct_count,
        score_percentage=round(score, 1),
        results=results
    )
