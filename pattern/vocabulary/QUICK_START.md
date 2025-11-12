# Vocabulary Patterns - Quick Start Guide

## What Are These Patterns?

These are **vocabulary-focused patterns** that test students' knowledge of **verb-noun collocations** - which words naturally pair together in English.

**Example Question:**
"I manage ____ at work."
- A. multiple projects ✅ (natural collocation)
- B. office parties ❌ (grammatical but unnatural)
- C. company failures ❌ (negative context)
- D. parking spaces ❌ (unnatural collocation)

## Quick Facts

- **Total Patterns:** 60
- **Category:** Vocabulary
- **Focus:** Verb-noun collocations
- **CEFR Level:** B1 (Intermediate)
- **Domains:** 10 (Business, Travel, Food, Technology, Leisure, Film, Gardening, Pets, Weather, Psychology)
- **Structures:** 3 per domain (Affirmative, Negative, Interrogative)
- **Conjugations:** 2 per structure (Base form, Third person)

## Pattern Naming Convention

Format: `{domain}_collocations_{structure}_{conjugation}.json`

Examples:
- `business_collocations_affirmative_base.json`
- `travel_collocations_negative_third.json`
- `food_cooking_collocations_question_base.json`

## How to Use

### 1. Load a Pattern

```python
import json

# Load business collocations pattern
with open('pattern/vocabulary/business_collocations_affirmative_base.json') as f:
    pattern = json.load(f)

print(pattern['focus'])  # "verb_noun_collocations"
print(pattern['category'])  # "vocabulary"
print(pattern['domain'])  # "Business"
```

### 2. Generate a Question

```python
import random

# Get template
template = pattern['template']  # "{SUBJ} {VERB} ____ {CONTEXT}."

# Select random components
subj = random.choice(pattern['chunks']['SUBJ'])  # "I"
verb_name = random.choice(list(pattern['chunks']['VERB'].keys()))  # "manage"
verb_data = pattern['chunks']['VERB'][verb_name]

# Correct answer (random phrase from this verb)
correct = random.choice(verb_data['phrases'])  # "multiple projects"

# Distractors
distractors = [
    random.choice([p for v in pattern['chunks']['VERB'].values() for p in v['phrases'] if p != correct]),  # related_words
    random.choice(verb_data.get('wrong_collocations', [])),  # wrong_collocation
    random.choice(verb_data.get('context_distractors', []))  # context_distractor
]

# Context
context = random.choice(pattern['chunks']['CONTEXT'])  # "at the office"

# Generate question
question = template.replace('{SUBJ}', subj).replace('{VERB}', verb_name).replace('{CONTEXT}', context)
# Result: "I manage ____ at the office."

# Options
options = [correct] + distractors
random.shuffle(options)
```

### 3. Use Distractor Methods

The pattern specifies which distractor methods to use:

```python
methods = pattern['distractor_config']['methods']
# ['related_words', 'wrong_collocation', 'semantic_mismatch', 'context_distractor']
```

**Distractor Types:**

1. **related_words**: Other phrases from the same verb or domain
2. **wrong_collocation**: From `wrong_collocations` field - grammatical but unnatural
3. **semantic_mismatch**: Phrases from other verbs that don't fit semantically
4. **context_distractor**: From `context_distractors` field - negative/incompatible context

## Pattern Structure

```json
{
  "pattern_id": "BUSINESS_COLLOCATIONS_AFFIRMATIVE_BASE",
  "focus": "verb_noun_collocations",
  "level": "B1",
  "domain": "Business",
  "category": "vocabulary",
  "template": "{SUBJ} {VERB} ____ {CONTEXT}.",
  "explanation": "Pattern-level explanation...",

  "chunks": {
    "SUBJ": ["I", "you", "we", "they"],

    "VERB": {
      "manage": {
        "phrases": ["multiple projects", "small teams"],
        "bases": ["multiple projects", "small teams"],
        "context_distractors": ["company failures"],
        "wrong_collocations": ["office parties"],
        "explanation": "Verb-level explanation..."
      }
    },

    "CONTEXT": ["at the office", "every week"]
  },

  "distractor_config": {
    "methods": ["related_words", "wrong_collocation", "semantic_mismatch", "context_distractor"]
  }
}
```

## Available Domains

| Domain | Pattern Count | Example Verbs | Example Collocations |
|--------|---------------|---------------|---------------------|
| Business | 6 | manage, attend, develop | projects, meetings, strategies |
| Travel | 6 | visit, explore, book | countries, destinations, hotels |
| Food/Cooking | 6 | prepare, cook, eat | meals, dishes, vegetables |
| Technology | 6 | install, update, backup | software, systems, data |
| Leisure | 6 | play, watch, practice | sports, movies, hobbies |
| Film | 6 | watch, direct, produce | movies, scenes, films |
| Gardening | 6 | plant, water, prune | seeds, flowers, trees |
| Pets | 6 | feed, walk, train | dogs, cats, animals |
| Weather | 6 | forecast, monitor, expect | temperatures, conditions, storms |
| Psychology | 6 | understand, analyze, express | behavior, emotions, feelings |

## Sentence Structures

Each domain has 3 sentence structures:

### 1. Affirmative
- **Base:** `{SUBJ} {VERB} ____ {CONTEXT}.`
  - "I manage ____ at the office."
- **Third:** `{SUBJ} {VERB} ____ {CONTEXT}.`
  - "She manages ____ at the office."

### 2. Negative
- **Base:** `{SUBJ} don't {VERB} ____ {CONTEXT}.`
  - "We don't prepare ____ at home."
- **Third:** `{SUBJ} doesn't {VERB} ____ {CONTEXT}.`
  - "He doesn't prepare ____ at home."

### 3. Interrogative (Questions)
- **Base:** `Do {SUBJ} {VERB} ____ {CONTEXT}?`
  - "Do you visit ____ during vacations?"
- **Third:** `Does {SUBJ} {VERB} ____ {CONTEXT}?`
  - "Does she visit ____ during vacations?"

## Filtering Patterns

```python
# Get all business patterns
business = [p for p in patterns if 'business' in p['pattern_id'].lower()]

# Get all affirmative patterns
affirmative = [p for p in patterns if 'affirmative' in p['pattern_id'].lower()]

# Get all base form patterns
base_forms = [p for p in patterns if 'base' in p['pattern_id'].lower()]

# Get all third person patterns
third_person = [p for p in patterns if 'third' in p['pattern_id'].lower()]

# Combine filters
business_affirmative_base = [p for p in patterns
                             if 'business' in p['pattern_id'].lower()
                             and 'affirmative' in p['pattern_id'].lower()
                             and 'base' in p['pattern_id'].lower()]
```

## Common Mistakes to Avoid

### ❌ DON'T Use These for Grammar Practice
These patterns test vocabulary, not grammar:
```python
# WRONG
if student_needs_grammar_practice:
    load_vocabulary_patterns()  # ❌ Wrong category!
```

### ❌ DON'T Use Grammar Distractor Methods
```python
# WRONG
distractors = generate_wrong_tense(verb)  # ❌ Not for vocabulary!
```

### ❌ DON'T Mix Conjugation Groups
```python
# WRONG - mixing I/you/we/they with he/she/it
subjects = ["I", "you", "he", "she"]  # ❌ Requires different verb forms!

# CORRECT - use base patterns for I/you/we/they
subjects = ["I", "you", "we", "they"]  # ✅

# CORRECT - use third patterns for he/she/it
subjects = ["he", "she", "it", "Maria"]  # ✅
```

### ✅ DO Track as Vocabulary Practice
```python
# CORRECT
analytics.track_practice(
    category='vocabulary',
    focus='verb_noun_collocations',
    domain='business',
    score=score
)
```

## Integration Checklist

- [ ] Load patterns from `pattern/vocabulary/` directory
- [ ] Filter by `category: "vocabulary"` not `focus: "present_simple"`
- [ ] Use vocabulary-appropriate distractor methods
- [ ] Track analytics under "vocabulary/collocations"
- [ ] Display as "Vocabulary Practice" in UI
- [ ] Use `wrong_collocations` field for distractor generation
- [ ] Respect conjugation grouping (base vs third)
- [ ] Provide collocation-focused feedback

## Where to Find More Information

- **README.md** - Comprehensive documentation
- **CONVERSION_SUMMARY.md** - Why these patterns were created
- **BEFORE_AFTER_EXAMPLES.md** - Detailed conversion examples
- **conversion_log.json** - Complete conversion audit trail

## Questions?

These patterns were converted from mislabeled "present_simple" grammar patterns. They always tested vocabulary but had incorrect metadata. Now they're properly categorized and ready to use!

For technical details about the conversion, see `/CONVERSION_SUMMARY.md`.

---

**Quick Start Version:** 1.0
**Last Updated:** 2025-10-26
**Total Patterns:** 60
**Status:** ✅ Ready for Production
