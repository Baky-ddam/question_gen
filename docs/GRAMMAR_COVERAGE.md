# Grammar Coverage Status

> Last Updated: 2025-12-17

## Quick Status

| Grammar | Status | Patterns | Levels | Quality |
|---------|--------|----------|--------|---------|
| Present Simple | COMPLETE | 50 | A1-C1 | Validated |
| Past Simple | COMPLETE | 50 | A1-C1 | Created |
| Present Continuous | NOT STARTED | 0 | - | - |
| Past Continuous | NOT STARTED | 0 | - | - |
| Present Perfect | NOT STARTED | 0 | - | - |
| Past Perfect | NOT STARTED | 0 | - | - |
| Future Simple | NOT STARTED | 0 | - | - |
| Modals | NOT STARTED | 0 | - | - |
| Passive Voice | NOT STARTED | 0 | - | - |
| Gerund/Infinitive | PARTIAL | 6 | B1 | Needs review |
| Vocabulary | COMPLETE | 60 | B1 | Validated |

---

## Detailed Coverage

### Present Simple (COMPLETE)

**Status:** 50 patterns validated and deployed

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness Range |
|-------|----------|---------|------------------|
| A1 | 10 | food, sports, technology, entertainment, travel, leisure | 48-72 |
| A2 | 10 | business, education, healthcare, nature, social_media | 108-144 |
| B1 | 10 | art, environment, finance, music, science | 192-240 |
| B2 | 10 | architecture, economics, law, literature, politics | 360-480 |
| C1 | 10 | automotive, design, fashion, photography, realestate | 600+ |

**Template Types Used:**
- Type 1 (Full form): 24 patterns
- Type 2 (Aux+verb): 14 patterns
- Type 3 (Aux only): 12 patterns

**Location:** `pattern/present_simple/`

---

### Past Simple (COMPLETE)

**Status:** 50 patterns created

**Coverage by Level:**
| Level | Patterns | Domains | Template Types |
|-------|----------|---------|----------------|
| A1 | 10 | travel, food, sports, entertainment, technology, shopping, home, school, friends, weather | Type 1 |
| A2 | 10 | work, education, hobbies, family, daily_routine | Type 1, Type 2 |
| B1 | 10 | career, health, culture, events, science | Type 1, Type 2, Type 3 |
| B2 | 10 | business, journalism, law, research, politics | Type 1, Type 2, Type 3 |
| C1 | 10 | economics, diplomacy, academia, technology_advanced, literature | Type 1, Type 2 |

**Subject Grouping:** Single group "all" (all subjects use same past form)

**Context Markers:** yesterday, last week/month/year, ago expressions

**Location:** `pattern/past_simple/`

---

### Present Continuous (NOT STARTED)

**Priority:** 2

**Subject Grouping:**
- Group A: I → am + verb-ing
- Group B: you/we/they → are + verb-ing
- Group C: he/she/it → is + verb-ing

**Context Markers:** right now, at the moment, currently, today, this week

---

### Past Continuous (NOT STARTED)

**Priority:** 3

**Subject Grouping (CRITICAL - different from present simple):**
- Group A: you/we/they → were + verb-ing
- Group B: I/he/she/it → was + verb-ing

**Context Markers:** at [time] yesterday, when [event], while, during, all day

---

### Present Perfect (NOT STARTED)

**Priority:** 4

**Subject Grouping:**
- Group A: I/you/we/they → have + past participle
- Group B: he/she/it → has + past participle

**Context Markers:** already, yet, just, ever, never, since, for, recently

---

### Modals (NOT STARTED)

**Priority:** 5

**Types:** can, could, should, must, may, might, would, will

**Subject Grouping:** Single group (no conjugation)

**Context Markers:** Semantic (ability, obligation, advice, possibility)

---

### Gerund/Infinitive (PARTIAL)

**Status:** 6 patterns exist, need expansion

**Current Files:**
- `pattern/infinite_gerund/gerund_verbs_daily.json`
- `pattern/infinite_gerund/infinitive_verbs_daily.json`
- Additional files in directory

**Needs:** More domains, levels, validation

---

### Vocabulary Collocations (COMPLETE)

**Status:** 60 patterns validated

**Coverage:**
- 10 semantic domains
- 6 patterns per domain
- B1 level
- Verb-noun collocations

**Location:** `pattern/vocabulary/`

---

## Coverage Metrics

```
Total Grammars: 11
Completed: 3 (27%)
Partial: 1 (9%)
Not Started: 7 (64%)

Total Patterns: 166
Present Simple: 50 (30%)
Past Simple: 50 (30%)
Vocabulary: 60 (36%)
Gerund/Infinitive: 6 (4%)
```

---

## Next Actions

1. **Implement Present Continuous** (50 patterns across 5 levels)
2. Implement Past Continuous
3. Implement Present Perfect
4. Implement Modals
5. Expand Gerund/Infinitive patterns

---

## Quality Checklist Per Grammar

When marking a grammar as COMPLETE, verify:
- [ ] All 5 CEFR levels covered (A1-C1)
- [ ] Minimum 10 patterns per level
- [ ] Template types balanced (Type 1, 2, 3)
- [ ] Subject groups properly separated
- [ ] Context markers disambiguate answers
- [ ] Distractors level-appropriate
- [ ] JSON structure validated
- [ ] Sample questions generated and reviewed
