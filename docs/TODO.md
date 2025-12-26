# Grammar Pattern TODO

> Active task tracking for pattern creation

---

## Current Work

### COMPLETE: Present Continuous (50 patterns)

**A1 Level - COMPLETE (10 patterns, 276 questions)**
- Domains: cooking, home, family, shopping, pets
- Subject Groups: group_a (I/am), group_b (you/we/they/are), group_c (he/she/it/is)
- Templates varied: "right now", "at the moment", "now", "Look!", "Currently"

**A2 Level - COMPLETE (10 patterns, 2544 questions)**
- Domains: hobbies, fitness, outdoor_activities, wellness, training
- Subject Groups: group_a (I/am), group_b (you/we/they/are), group_c (he/she/it/is)
- Templates varied: "{TIME}, {SUBJ} ____ {OBJ} {PLACE}.", "Look! {SUBJ} ____ {OBJ} {PLACE}.", "At the moment, {SUBJ} ____ {OBJ} {PLACE}.", etc.
- Uniqueness: 108-576 per pattern (exceeds A2 target of 80-120)

**B1 Level - COMPLETE (10 patterns, 4416 questions)**
- Domains: research, history, psychology, writing, theater
- Subject Groups: group_a (I/am), group_b (you/we/they/are), group_c (he/she/it/is)
- Templates varied with REASON/PURPOSE clauses:
  - `{SUBJ} ____ {OBJ} because {REASON}.`
  - `Currently, {SUBJ} ____ {OBJ} as part of {PROJECT}.`
  - `{SUBJ} ____ {OBJ} to {PURPOSE}.`
  - `{TIME}, {SUBJ} ____ {OBJ} for {PURPOSE}.`
  - `{SUBJ} ____ {OBJ} in order to {PURPOSE}.`
  - `Since {TRIGGER}, {SUBJ} ____ {OBJ}.`
  - `{SUBJ} ____ {OBJ} while {PARALLEL_ACTION}.`
  - `{SUBJ} ____ {OBJ} {PLACE} because {REASON}.`
  - `{SUBJ} ____ {OBJ} {PLACE} to {PURPOSE}.`
  - `{TIME}, {SUBJ} ____ {OBJ} because {REASON}.`
- Uniqueness: 64-1024 per pattern (exceeds B1 target of 150-250)

**B2 Level - COMPLETE (10 patterns)**
- Domains: journalism, engineering, marketing, software, data_science
- Subject Groups: group_a (I/am), group_b (you/we/they/are), group_c (he/she/it/is)
- Templates varied with COMPLEX CLAUSES and CONDITIONAL structures:
  - `Currently, {SUBJ} ____ {OBJ} {PLACE} to {PURPOSE}.`
  - `{SUBJ} ____ {OBJ} despite {CHALLENGE}.`
  - `While {CONTEXT}, {SUBJ} ____ {OBJ} to {PURPOSE}.`
  - `{SUBJ} ____ {OBJ}, which {RESULT}.`
  - `Given that {CONDITION}, {SUBJ} ____ {OBJ}.`
  - `{SUBJ} ____ {OBJ} {PLACE} as {TREND} continues.`
  - `In response to {TRIGGER}, {SUBJ} ____ {OBJ}.`
  - `{SUBJ} ____ {OBJ} in order to {PURPOSE}, which {IMPACT}.`
  - `{SUBJ} ____ {OBJ} {PLACE} to {PURPOSE}.`
  - `{SUBJ} ____ {OBJ} because {REASON}, which {IMPACT}.`
- B2-level distractors: disregard, overlook, suppress, undermine, circumvent, obstruct, impede, hinder

**C1 Level - COMPLETE (10 patterns)**
- Domains: climate, conservation, cybersecurity, urban_life, logistics
- Subject Groups: group_a (I/am), group_b (you/we/they/are), group_c (he/she/it/is)
- Templates varied with HIGHLY SOPHISTICATED multi-clause structures:
  - `{SUBJ} ____ increasingly {OBJ} as {TREND}, which {CONSEQUENCE}.`
  - `While {GLOBAL_CONTEXT}, {SUBJ} ____ {OBJ} to {PURPOSE}.`
  - `In light of {SITUATION}, {SUBJ} ____ {OBJ}, thereby {OUTCOME}.`
  - `{SUBJ} ____ {OBJ} {PLACE}, a development that {IMPLICATION}.`
  - `Given the {COMPLEXITY}, {SUBJ} ____ {OBJ} in order to {PURPOSE}.`
  - `{SUBJ} ____ {OBJ} amid {CHALLENGE}, which {IMPACT}.`
  - `As {TREND} accelerates, {SUBJ} ____ {OBJ} to {STRATEGIC_GOAL}.`
  - `{SUBJ} ____ {OBJ}, a process that {SIGNIFICANCE} in the context of {BROADER_ISSUE}.`
  - `Given that {CONDITION}, {SUBJ} ____ {OBJ} to {OPERATIONAL_GOAL}.`
  - `In response to {MARKET_FORCE}, {SUBJ} ____ {OBJ}, thereby {BUSINESS_OUTCOME}.`
- C1-level distractors: forsake, obliterate, renounce, repudiate, nullify, abrogate, rescind, countermand, exacerbate, eradicate
- Uniqueness: 500+ per pattern (exceeds C1 target)

---

## Grammar Queue

| Priority | Grammar | Status | Notes |
|----------|---------|--------|-------|
| 1 | Past Simple | COMPLETE | 50 patterns, all levels |
| 2 | Present Continuous | COMPLETE | 50 patterns, 3 subject groups (am/are/is) |
| 3 | Past Continuous | QUEUED | Builds on past simple |
| 4 | Present Perfect | QUEUED | Common in EYESH exams |
| 5 | Modals | QUEUED | High variety, no conjugation |
| 6 | Future Simple | QUEUED | All subjects same form |
| 7 | Past Perfect | QUEUED | Advanced |
| 8 | Passive Voice | QUEUED | Multiple tense variations |
| 9 | Gerund/Infinitive | QUEUED | Expand existing 6 patterns |

---

## Pattern Creation Checklist

When starting a new grammar:

### 1. Pre-Creation
- [ ] Read grammar rules from `grammar_registry.json`
- [ ] Check `PATTERN_CONTEXT.md` for domain availability
- [ ] Review existing patterns for reference
- [ ] Identify subject groupings needed

### 2. Level A1 (10 patterns)
- [ ] Select 5 unique domains (food, sports, etc.)
- [ ] Create 2 patterns per domain (Group A, Group B if applicable)
- [ ] Validate uniqueness: 30-50 questions minimum
- [ ] Run validation cycle

### 3. Level A2 (10 patterns)
- [ ] Select 5 unique domains (different from A1)
- [ ] Create patterns with TIME/PLACE chunks
- [ ] Validate uniqueness: 80-120 questions minimum
- [ ] Run validation cycle

### 4. Level B1 (10 patterns)
- [ ] Select 5 unique domains
- [ ] Add sub-grammars (articles, prepositions)
- [ ] Validate uniqueness: 150-250 questions minimum
- [ ] Run validation cycle

### 5. Level B2 (10 patterns)
- [ ] Select 5 unique domains (academic/professional)
- [ ] Complex structures, relative clauses
- [ ] Validate uniqueness: 300-500 questions minimum
- [ ] Run validation cycle

### 6. Level C1 (10 patterns)
- [ ] Select 5 unique domains (advanced)
- [ ] Sophisticated structures, multiple clauses
- [ ] Validate uniqueness: 500+ questions minimum
- [ ] Run validation cycle

### 7. Post-Creation
- [ ] Update `GRAMMAR_COVERAGE.md`
- [ ] Update `PATTERN_CONTEXT.md`
- [ ] Mark grammar as COMPLETE

---

## Completed Grammars

| Grammar | Completion Date | Patterns | Notes |
|---------|-----------------|----------|-------|
| Present Simple | 2025-10-26 | 50 | Full validation complete |
| Past Simple | 2025-12-17 | 50 | All levels, single group |
| Present Continuous | 2025-12-26 | 50 | 3 subject groups (am/are/is), all levels A1-C1 |
| Vocabulary | 2025-11 | 60 | Collocations B1 level |

---

## Issues / Blockers

_None currently_

---

## Notes

- Each pattern takes ~5-10 minutes to create and validate
- Full grammar (50 patterns) takes ~2-4 hours
- Always run validation before marking complete
- Reference dataset images for vocabulary inspiration
