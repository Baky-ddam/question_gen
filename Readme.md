# EYESH English Exam Question Generator

An intelligent question generation system for the EYESH (Mongolian National University Exam) English section. Generates unlimited grammatically correct questions with automatic subject-verb agreement, intelligent distractor generation, and rule-based answer matching.

**NEW**: Now includes an automatic dashboard system for extracting tables from Excel files!

---

## 🎯 Project Overview

### What is EYESH?
EYESH is the Mongolian National University Entrance Exam. The English section has 5 core question types:
1. **Grammar** ✅ (Fully Supported)
2. **Vocabulary** ✅ (Supported)
3. **Communication** ⚠️ (Limited - requires context)
4. **Reading** ⚠️ (Limited - requires paragraphs)
5. **Part 2** ✅ (Multiple formats supported)

### What This Generator Does
- Creates **grammatically correct** English exam questions from JSON templates
- Automatically handles **subject-verb agreement** (he goes, they go)
- Generates **intelligent distractors** (wrong answers)
- Supports **multiple difficulty levels** (A2, B1, B2)
- Exports to **JSON and TXT** formats

## 📊 Dashboard System (NEW!)

Automatic table extraction from Excel files with support for:
- **Merged Headers**: Detects and handles merged cells
- **Hierarchical Columns**: Tags sub-headers with big headers (Sheet > Big Header > Sub-header)
- **Table Boundaries**: Automatically detects multiple tables in one sheet
- **Pattern Recognition**: Recognizes month sequences (Jan-Dec), percentages, etc.

See [`dashboard/README.md`](dashboard/README.md) for full documentation.