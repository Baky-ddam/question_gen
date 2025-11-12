# Vocabulary Patterns - Verb-Noun Collocations

This directory contains vocabulary-focused patterns that test students' knowledge of natural verb-noun collocations in English.

## Purpose

These patterns were previously mislabeled as "present_simple" grammar patterns but actually test **vocabulary selection** rather than grammatical structure. Students must choose the correct noun/noun phrase that naturally collocates with a given verb in context.

## What These Patterns Test

**Focus:** Verb-noun collocations
**Category:** Vocabulary
**Skill:** Lexical appropriacy and natural word combinations

Students see sentences like:
- "I manage ____ at the office."
- Options: projects / coffee breaks / parking spaces

The correct answer is "projects" because "manage projects" is a natural collocation in business English, while "manage coffee breaks" and "manage parking spaces" are grammatically correct but semantically awkward.

## Pattern Structure

### Template Format
```
{SUBJ} {VERB} ____ {CONTEXT}.
```

The blank is filled with noun phrases from the VERB dictionary's `phrases` array.

### Example Pattern Components

**SUBJ:** Subject pronouns or nouns (grouped by conjugation)
- Base form: I, you, we, they
- Third person: he, she, it, proper names

**VERB:** Dictionary mapping verbs to their natural collocations
```json
"manage": {
  "phrases": ["multiple projects", "small teams", "client relationships"],
  "bases": ["multiple projects", "small teams", "client relationships"],
  "context_distractors": ["company failures", "budget losses"],
  "wrong_collocations": ["office parties", "coffee breaks"],
  "explanation": "The verb 'manage' commonly collocates with..."
}
```

**CONTEXT:** Domain-appropriate phrases
- Business: "at the office", "during work hours", "regularly"
- Travel: "when traveling abroad", "on every trip", "during vacations"

## Distractor Methods

Unlike grammar patterns, vocabulary patterns use semantic distractor methods:

1. **related_words**: Words from the same domain that don't collocate naturally
2. **wrong_collocation**: Grammatically possible but unnatural combinations
3. **semantic_mismatch**: Words that don't fit the context meaningfully
4. **context_distractor**: Semantically incompatible phrases (existing field)

## Available Domains

This collection includes 60 patterns across 10 domains:

### 1. Business (6 patterns)
- Verbs: manage, attend, develop, negotiate, analyze
- Collocations: projects, meetings, strategies, deals, reports
- Files: `business_collocations_*.json`

### 2. Travel (6 patterns)
- Verbs: visit, explore, book, prefer, enjoy
- Collocations: countries, destinations, hotels, accommodations, experiences
- Files: `travel_collocations_*.json`

### 3. Food & Cooking (6 patterns)
- Verbs: prepare, cook, eat, prefer, try
- Collocations: meals, dishes, vegetables, ingredients, recipes
- Files: `food_cooking_collocations_*.json` / `food_collocations_*.json`

### 4. Technology (6 patterns)
- Verbs: install, update, backup, configure, troubleshoot
- Collocations: software, systems, data, settings, issues
- Files: `technology_collocations_*.json`

### 5. Leisure (6 patterns)
- Verbs: play, watch, practice, enjoy, attend
- Collocations: sports, movies, hobbies, activities, events
- Files: `leisure_collocations_*.json`

### 6. Film (6 patterns)
- Verbs: watch, direct, produce, review, recommend
- Collocations: movies, scenes, films, performances, titles
- Files: `film_collocations_*.json`

### 7. Gardening (6 patterns)
- Verbs: plant, water, prune, harvest, grow
- Collocations: seeds, flowers, trees, vegetables, plants
- Files: `gardening_collocations_*.json`

### 8. Pets (6 patterns)
- Verbs: feed, walk, train, groom, adopt
- Collocations: dogs, cats, animals, pets, companions
- Files: `pets_collocations_*.json`

### 9. Weather (6 patterns)
- Verbs: forecast, monitor, experience, expect, record
- Collocations: temperatures, conditions, storms, precipitation, patterns
- Files: `weather_collocations_*.json`

### 10. Psychology (6 patterns)
- Verbs: understand, analyze, develop, express, manage
- Collocations: behavior, emotions, skills, feelings, stress
- Files: `psychology_collocations_*.json`

## Sentence Structures

Each domain has patterns for three sentence types:

- **Affirmative**: `{SUBJ} {VERB} ____ {CONTEXT}.`
- **Negative**: `{SUBJ} don't/doesn't {VERB} ____ {CONTEXT}.`
- **Interrogative**: `Do/Does {SUBJ} {VERB} ____ {CONTEXT}?`

## Conjugation Groups

Patterns are split by subject type to ensure proper verb conjugation:

- **_base**: For I, you, we, they (base verb form)
- **_third**: For he, she, it, proper names (third-person singular)

## CEFR Level

All patterns are **B1 (Intermediate)** level, appropriate for students who:
- Understand basic grammar structures
- Are building domain-specific vocabulary
- Need practice with natural word combinations

## Verb Dictionary Fields

Each verb entry contains:

- **phrases**: Array of natural collocations (correct answers)
- **bases**: Array matching phrases (used for distractor generation)
- **context_distractors**: Semantically negative or incompatible phrases
- **wrong_collocations**: Grammatically valid but unnatural combinations
- **explanation**: Why these words naturally pair together

## Usage in Question Generation

The question generator should:

1. Select a random subject from SUBJ
2. Select a random verb from VERB dictionary
3. Select a random phrase from that verb's phrases array (correct answer)
4. Generate distractors using:
   - Other phrases from the same verb (related_words)
   - wrong_collocations from the verb entry
   - context_distractors from the verb entry
   - Semantically mismatched phrases from other verbs
5. Select a random CONTEXT phrase
6. Construct the sentence and present options

## Conversion History

These patterns were converted from `pattern/present_simple/` on 2025-10-26.

### What Changed

**Before (Incorrect):**
- pattern_id: `PRESENT_SIMPLE_BUSINESS_AFFIRMATIVE_BASE`
- focus: `present_simple`
- category: `grammar`
- explanation: "Present simple is used to describe work routines..."
- distractor methods: `wrong_tense, wrong_conjugation, wrong_form`

**After (Correct):**
- pattern_id: `BUSINESS_COLLOCATIONS_AFFIRMATIVE_BASE`
- focus: `verb_noun_collocations`
- category: `vocabulary`
- explanation: "This pattern tests common verb-noun collocations..."
- distractor methods: `related_words, wrong_collocation, semantic_mismatch, context_distractor`

### Why This Matters

Grammar patterns test structural knowledge (verb forms, tenses, conjugations).
Vocabulary patterns test lexical knowledge (word choice, collocations, appropriacy).

The old patterns had grammar-focused metadata but vocabulary-focused content. This mislabeling could confuse:
- Students about what they're practicing
- Teachers about learning objectives
- Analytics about student strengths/weaknesses

The corrected patterns now accurately reflect what they test: the ability to select words that naturally collocate in specific contexts.

## Example Questions Generated

### Business Domain
**Question:** "We analyze ____ every week."

**Options:**
A. market trends (correct - natural collocation)
B. coffee breaks (wrong_collocation - grammatical but unnatural)
C. business failures (context_distractor - negative context)
D. office parties (wrong_collocation - grammatical but unnatural)

### Travel Domain
**Question:** "She visits ____ when traveling abroad."

**Options:**
A. historical sites (correct - natural collocation)
B. ticket stubs (wrong_collocation - grammatical but unnatural)
C. dangerous areas (context_distractor - negative context)
D. boarding passes (wrong_collocation - grammatical but unnatural)

## Pattern Quality Standards

All patterns meet these vocabulary-focused criteria:

- Correct answers are natural, frequently-used collocations
- All options are grammatically valid (tests vocabulary, not grammar)
- Distractors are believable but less natural
- context_distractors provide semantic contrast
- wrong_collocations test collocation strength
- Explanations focus on why words pair together, not grammar rules

## Integration with Question Generator

To use these patterns in the EYESH system:

1. Load patterns from `pattern/vocabulary/`
2. Filter by domain, level, or sentence structure as needed
3. Use vocabulary-appropriate distractor generation methods
4. Present as vocabulary exercises, not grammar drills
5. Track as vocabulary/collocation practice in student progress

## Files

Total patterns: **60 files**
Conversion log: `conversion_log.json`
Conversion script: `/convert_to_vocabulary_patterns.py`

## Notes for Developers

- These patterns should NOT be used for present simple grammar practice
- The true present simple grammar patterns have `_fullverb`, `_auxverb`, or `_auxonly` suffixes
- When filtering patterns, use `category: "vocabulary"` not `focus: "present_simple"`
- Distractor generation should use semantic similarity, not grammatical transformation
- Analytics should track these under "vocabulary/collocations", not "grammar/present_simple"

---

**Pattern Architecture:** EYESH English Question Generator
**Conversion Date:** 2025-10-26
**Total Patterns:** 60
**Domains:** 10
**CEFR Level:** B1
**Category:** Vocabulary
**Focus:** Verb-Noun Collocations
