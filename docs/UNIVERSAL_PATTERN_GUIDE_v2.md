# Universal Pattern Guide v2 (Concise)

> For full examples and detailed explanations, see `UNIVERSAL_PATTERN_GUIDE_FULL.md`
> For grammar rules, see `grammar_registry.json`

---

## 1. Core Principles

1. **Grammar-Focus:** Blank tests grammar, NOT vocabulary
2. **Context Markers:** Include markers that force ONE correct answer
3. **5 Options:** 1 correct + 3 wrong forms + 1 semantic distractor
4. **Uniqueness:** Meet level targets (A1: 30-50, A2: 80-120, B1: 150-250, B2: 300-500, C1: 500+)
5. **Subject Grouping:** Group by grammar rules (varies per tense)
6. **Level Scaling:** Complexity increases A1→C1

---

## 2. Template Types

| Type | Blank Contains | When to Use |
|------|---------------|-------------|
| Type 1 | Full form | Affirmatives, complete structure |
| Type 2 | Aux + Verb | Negatives, continuous, perfect |
| Type 3 | Aux only | Focus on auxiliary selection |

---

## 3. Subject Grouping (Quick Reference)

| Grammar | Group A | Group B | Notes |
|---------|---------|---------|-------|
| Present Simple | I/you/we/they (base) | he/she/it (verb-s) | |
| Past Simple | ALL (past form) | - | Single group |
| Present Continuous | I (am) | you/we/they (are), he/she/it (is) | 3 groups |
| Past Continuous | you/we/they (were) | I/he/she/it (was) | I goes with was! |
| Present Perfect | I/you/we/they (have) | he/she/it (has) | |
| Modals | ALL (same form) | - | No conjugation |

---

## 4. JSON Structure

```json
{
  "pattern_id": "GRAMMAR_DOMAIN_LEVEL_TYPE_GROUP",
  "focus": "grammar_type",
  "level": "A1|A2|B1|B2|C1",
  "domain": "domain_name",
  "category": "grammar",
  "template_type": "type_1|type_2|type_3",
  "subject_group": "group_a|group_b|all",
  "template": "{SUBJ} ____ {OBJ}.",
  "example": "I drink coffee.",
  "explanation": "Brief grammar explanation.",
  "chunks": {
    "SUBJ": ["I", "you", "they"],
    "VERB": {
      "drink": {
        "correct_forms": ["drink"],
        "wrong_forms": ["drinks", "drank", "am drinking"],
        "objects": ["coffee", "tea", "water"],
        "distractor": "waste"
      }
    }
  }
}
```

**Required Fields:**
- `pattern_id`, `focus`, `level`, `domain`, `category`
- `template_type`, `template`, `example`, `explanation`
- `chunks` with SUBJ and VERB (nested structure)

**VERB Structure (each verb):**
- `correct_forms`: Array of correct answers
- `wrong_forms`: EXACTLY 3 wrong grammar forms
- `objects`: Semantically paired objects
- `distractor`: Single semantic distractor word

---

## 5. Context Markers by Grammar

| Grammar | Markers |
|---------|---------|
| Present Simple | every day, usually, always, often |
| Past Simple | yesterday, last week, ago, in [year] |
| Present Continuous | right now, at the moment, currently |
| Past Continuous | at [time] yesterday, when [event], while |
| Present Perfect | already, yet, ever, never, since, for |
| Future | tomorrow, next week, soon, will |

---

## 6. Level Complexity

| Level | Chunks | Structure | Vocab |
|-------|--------|-----------|-------|
| A1 | 2-3 | Simple SVO | Top 500 |
| A2 | 3-4 | + TIME/PLACE | 500-1000 |
| B1 | 4-5 | + REASON | 1000-2000 |
| B2 | 5-6 | + Clauses | 2000-3000 |
| C1 | 6-7+ | Complex | 3000+ |

---

## 7. Distractor Rules by Level

| Level | Distractor Type | Example |
|-------|-----------------|---------|
| A1 | Simple opposites | waste, ignore, break |
| A2 | Clear contradictions | quit, skip, destroy |
| B1 | Action opposites | abandon, neglect, dismiss |
| B2 | Sophisticated | disregard, suppress, undermine |
| C1 | Advanced vocab | forsake, obliterate, renounce |

---

## 8. Pattern Creation Checklist

### Before Creating
- [ ] Check `grammar_registry.json` for rules
- [ ] Check `PATTERN_CONTEXT.md` for domain availability
- [ ] Identify correct subject grouping

### While Creating
- [ ] Correct naming: `GRAMMAR_DOMAIN_LEVEL_TYPE_GROUP`
- [ ] Context markers disambiguate answer
- [ ] Exactly 3 wrong_forms per verb
- [ ] Objects semantically paired with verbs
- [ ] Distractor is semantic (not grammar error)

### After Creating
- [ ] Valid JSON syntax
- [ ] Run validation: `python validate_patterns.py --pattern PATTERN_ID`
- [ ] Check uniqueness meets level target
- [ ] Update `PATTERN_CONTEXT.md`

---

## 9. Common Mistakes

| Mistake | Fix |
|---------|-----|
| Testing vocabulary not grammar | Put grammar in blank, vocab in template |
| Missing context markers | Add time/frequency markers |
| Wrong subject grouping | Check `grammar_registry.json` |
| Non-semantic distractor | Use different verb, not grammar variant |
| Unnatural verb-object combo | Use nested objects per verb |

---

## 10. File References

| File | Content |
|------|---------|
| `grammar_registry.json` | All grammar rules (single source of truth) |
| `docs/GRAMMAR_COVERAGE.md` | Coverage status |
| `docs/TODO.md` | Work queue |
| `docs/PATTERN_CONTEXT.md` | Existing patterns list |
| `UNIVERSAL_PATTERN_GUIDE_FULL.md` | Full examples and details |
