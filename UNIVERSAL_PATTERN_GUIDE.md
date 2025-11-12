# Universal Pattern Generation Guide

## Table of Contents
1. [Overview & Philosophy](#overview--philosophy)
2. [The Universal Principles](#the-universal-principles)
3. [Template Type System (Works for ALL Grammars)](#template-type-system-works-for-all-grammars)
4. [Subject-Auxiliary Grouping by Grammar](#subject-auxiliary-grouping-by-grammar)
5. [Context Markers & Disambiguation](#context-markers--disambiguation)
6. [Level-Based Complexity](#level-based-complexity)
7. [Domain-Based Pattern Creation](#domain-based-pattern-creation)
8. [Uniqueness Targets & Calculation](#uniqueness-targets--calculation)
9. [Grammar-Specific Guidelines](#grammar-specific-guidelines)
10. [Complete Pattern Structure](#complete-pattern-structure)
11. [Examples Across Grammars](#examples-across-grammars)
12. [Pattern Creation Workflow](#pattern-creation-workflow)
13. [Best Practices & Checklist](#best-practices--checklist)
14. [Common Mistakes & Troubleshooting](#common-mistakes--troubleshooting)

---

## Overview & Philosophy

### Core Philosophy

> **"One template, one domain, one JSON file. Maximum variety through 100 domains × multiple grammars."**

This guide provides a **universal framework** for creating English grammar question patterns that work for:
- ✅ ALL grammar types (present simple, past continuous, modals, perfect tenses, etc.)
- ✅ ALL CEFR levels (A1 to C1)
- ✅ ALL domains (100 different semantic domains)
- ✅ ALL template types (full form, aux+verb, auxiliary only)

### Design Principles

1. **Grammar-Agnostic Templates** - Same template type system works for any grammar
2. **Domain-Specific Vocabulary** - Each JSON focuses on one domain (travel, journalism, technology, etc.)
3. **Level-Scaled Complexity** - Template complexity increases with CEFR level
4. **Context-Based Disambiguation** - Markers ensure only one correct answer
5. **Uniqueness Through Variety** - Enough variable chunks to generate 30-500+ unique questions

---

## The Universal Principles

### Principle 1: Grammar-Focus Principle
**Rule:** The blank MUST test the grammar point, NOT vocabulary.

```
WRONG (Tests vocabulary):
Focus: present_simple
Template: "He doesn't collect ____ during leisure time."
Options: stamps | coins | memorabilia ✓ | books
Problem: All are nouns - tests word choice, not grammar!

CORRECT (Tests grammar):
Focus: present_simple
Template: "He ____ memorabilia during leisure time."
Options: doesn't collect ✓ | don't collect | didn't collect | isn't collecting
Success: Tests present simple negative form!
```

### Principle 2: Context Marker Principle
**Rule:** Include context markers that make only ONE auxiliary/tense grammatically appropriate.

```
WRONG (Multiple answers work):
Template: "She ____ like coffee."
Options: doesn't ✓ | didn't ✓ | won't ✓ | isn't ✓
Problem: All are grammatically correct!

CORRECT (Only one answer works):
Template: "She ____ like coffee right now."
Options: doesn't ✓ | didn't ✗ | won't ✗ | isn't ✗
Success: "right now" requires present simple!
```

### Principle 3: Answer Option Structure
**Rule:** Every question has 5 options (A-E): 1 correct + 3 wrong forms + 1 distractor.

```
Option Structure for EYESH:
- 1 Correct Answer: The grammatically correct form
- 3 Wrong Forms: Grammatical transformations (wrong tense, conjugation, etc.)
- 1 Distractor: Semantically inappropriate but could be grammatically valid

Example - Present Simple:
Correct: "drink" (base form)
Wrong Forms: "drinks" (wrong conjugation), "drank" (past), "am drinking" (continuous)
Distractor: A word/phrase that doesn't fit the context semantically

Total: 5 options
```

### Principle 4: Uniqueness Principle
**Rule:** Patterns must generate enough unique questions for their CEFR level.

```
Uniqueness = Product of all variable chunks

Example:
SUBJ: 3 items × VERB: 4 items × OBJ: 5 items × TIME: 4 items = 240 unique questions

Targets by level:
A1: 30-50 questions minimum
A2: 80-120 questions minimum
B1: 150-250 questions minimum
B2: 300-500 questions minimum
C1: 500+ questions minimum
```

### Principle 5: Subject Grouping Principle
**Rule:** Group subjects based on which form they take in the TARGET grammar (not always the same!).

```
Present Simple:
- Group A: I/you/we/they → base form (drink)
- Group B: he/she/it → -s form (drinks)

Past Continuous:
- Group A: you/we/they → were + verb-ing
- Group B: I/he/she/it → was + verb-ing

Present Perfect:
- Group A: I/you/we/they → have + past participle
- Group B: he/she/it → has + past participle

Modals:
- Single Group: ALL subjects → same form (can speak)
```

### Principle 6: Grammar-Specific Context Principle
**Rule:** Use semantic contexts that naturally require the target grammar.

```
Present Simple → Facts, routines, universal truths
- "Water boils at 100 degrees Celsius"
- "I drink coffee every morning"
- "The sun rises in the east"

Past Continuous → Specific past time, interrupted actions
- "She was reading at 8pm yesterday"
- "They were studying when I called"

Present Perfect → Past actions with present relevance
- "I have visited Paris before"
- "She has already finished her work"
```

### Principle 7: Level Complexity Principle
**Rule:** Template complexity and vocabulary sophistication scale with CEFR level.

```
A1: 2-3 chunks, simple structure, high-frequency words
    "{SUBJ} ____ {OBJ}."

A2: 3-4 chunks, time/place markers, common words
    "{SUBJ} ____ {OBJ} {TIME}."

B1: 4-5 chunks, 1-2 sub-grammars, broader domains
    "{SUBJ} ____ {ARTICLE}{OBJ} {PREP}{TIME}."

B2: 5-6 chunks, 2-3 sub-grammars, academic vocabulary
    "{SUBJ} ____ {MODAL}{VERB} {ARTICLE}{OBJ} {PREP}{PLACE} {TIME}."

C1: 6-7 chunks, 3+ sub-grammars, complex structures
    "{SUBJ} ____ {MODAL}{VERB} {ARTICLE}{OBJ} {RELATIVE_CLAUSE} {PREP}{PLACE}."
```

---

## Template Type System (Works for ALL Grammars)

### The Three Universal Template Types

**Every grammar can be tested using one of these three template types:**

| Type | Blank Contains | Best For | Example |
|------|---------------|----------|---------|
| **Type 1** | Full target form | Complete structure testing, affirmatives | "I ____ daily" → drink/drinks/drank |
| **Type 2** | Auxiliary + Main Verb | Testing aux+verb coordination | "He ____ daily" → doesn't drink/don't drink |
| **Type 3** | Auxiliary/Modal Only | Laser-focus on auxiliary selection | "He ____ drink daily" → doesn't/don't/didn't |

### Type 1: Full Target Form

**Definition:** The blank contains the COMPLETE grammatical structure being tested.

**When to Use:**
- Affirmative sentences
- Testing tense/aspect recognition
- Testing subject-verb agreement
- Complete structure forms (gerund vs infinitive, modal+verb, etc.)

**Examples Across Grammars:**

```markdown
Present Simple:
Template: "{SUBJ} ____ {OBJ} {FREQUENCY}."
Blank: drink/drinks/drank/am drinking/will drink
Grammar Test: Present simple base form vs -s form vs other tenses

Past Continuous:
Template: "{SUBJ} ____ {SPECIFIC_PAST_TIME}."
Blank: was reading/were reading/read/reads/is reading
Grammar Test: Past continuous vs other tenses + subject-auxiliary agreement

Modals:
Template: "{SUBJ} ____ {ACTIVITY} {ADVERB}."
Blank: can speak/could speak/will speak/must speak
Grammar Test: Modal selection + base verb form

Present Perfect:
Template: "{SUBJ} ____ {PLACE} {PRESENT_PERFECT_MARKER}."
Blank: have visited/has visited/had visited/visited
Grammar Test: Present perfect vs other tenses

Gerund/Infinitive:
Template: "{SUBJ} {VERB} ____ {TIME}."
Blank: reading books/to read books/read books
Grammar Test: Gerund vs infinitive vs bare infinitive
```

### Type 2: Auxiliary + Main Verb

**Definition:** The blank contains auxiliary AND main verb together.

**When to Use:**
- Negative sentences
- Continuous tenses
- Perfect tenses
- Passive voice
- Testing auxiliary + verb coordination

**Examples Across Grammars:**

```markdown
Present Simple Negative:
Template: "{SUBJ} ____ {OBJ} {PRESENT_MARKER}."
Blank: doesn't drink/don't drink/didn't drink/isn't drinking
Grammar Test: Present negative auxiliary + base verb
Subject Grouping: he/she/it → doesn't

Past Continuous:
Template: "{SUBJ} ____ {SPECIFIC_PAST_TIME}."
Blank: were studying/was studying/are studying/studied
Grammar Test: Past continuous auxiliary + -ing form
Subject Grouping: you/we/they → were

Present Perfect:
Template: "{SUBJ} ____ {OBJ} {PRESENT_PERFECT_MARKER}."
Blank: have seen/has seen/had seen/saw
Grammar Test: Perfect auxiliary + past participle
Subject Grouping: I/you/we/they → have

Passive Voice:
Template: "{SUBJ} ____ {TIME}."
Blank: was built/were built/is built/has been built
Grammar Test: Passive auxiliary + past participle
```

### Type 3: Auxiliary/Modal Only

**Definition:** Main verb already in template; blank tests ONLY auxiliary/modal choice.

**When to Use:**
- Laser-focus on auxiliary selection
- Testing do/does/did distinction
- Testing was/were distinction
- Testing has/have distinction
- Modal selection based on meaning

**Examples Across Grammars:**

```markdown
Present Simple Negative:
Template: "{SUBJ} ____ like {OBJ} {PRESENT_MARKER}."
Blank: doesn't/don't/didn't/isn't/won't
Grammar Test: ONLY present negative auxiliary selection
Main Verb: "like" (already in base form)
Context: "right now" → requires "doesn't"

Past Continuous:
Template: "{SUBJ} ____ reading {SPECIFIC_PAST_TIME}."
Blank: were/was/are/have been
Grammar Test: ONLY past continuous auxiliary
Main Verb: "reading" (already in -ing form)
Context: "at 8pm yesterday" → requires "were" or "was"

Present Perfect:
Template: "{SUBJ} ____ visited {PLACE} {PRESENT_PERFECT_MARKER}."
Blank: have/has/had/were
Grammar Test: ONLY present perfect auxiliary
Main Verb: "visited" (already in past participle)
Context: "before" → requires "have" or "has"

Modals:
Template: "{SUBJ} ____ exercise {FREQUENCY}."
Blank: should/must/can/could/will
Grammar Test: ONLY modal selection based on meaning (advice/obligation/ability)
Main Verb: "exercise" (already in base form)
```

### Decision Tree: Choosing Template Type

```
What aspect of the grammar do you want to test?

├─ The complete structure (form + tense recognition)?
│  └─> Type 1: Full Target Form
│     Examples:
│     - "I ____ coffee daily" → drink/drinks/drank/am drinking
│     - "She ____ at 8pm" → was reading/were reading/read
│
├─ Both auxiliary AND verb form coordination?
│  └─> Type 2: Auxiliary + Main Verb
│     Examples:
│     - "He ____ coffee" → doesn't drink/don't drink/didn't drink
│     - "They ____ now" → are working/is working/were working
│
└─ ONLY the auxiliary/modal choice?
   └─> Type 3: Auxiliary/Modal Only
      Examples:
      - "He ____ drink coffee" → doesn't/don't/didn't
      - "You ____ study harder" → should/must/can/could
```

---

## Subject-Auxiliary Grouping by Grammar

### Why Subject Grouping Matters

**Different grammars require different subject groupings!**

For example:
- Present Simple: "he drinks" vs "they drink" → group by -s form
- Past Continuous: "he was" vs "they were" → group by was/were
- Modals: "he can" vs "they can" → NO grouping needed (same form)

### Grouping Rules by Grammar Type

#### 1. Present Simple

**Affirmative:**
- **Group A:** I, you, we, they → base form (drink, eat, work)
- **Group B:** he, she, it, [proper nouns] → -s form (drinks, eats, works)

**Negative (Type 2: aux+verb):**
- **Group A:** I, you, we, they → don't + base verb (don't drink)
- **Group B:** he, she, it → doesn't + base verb (doesn't drink)

**Negative (Type 3: auxiliary only):**
- **Group A:** I, you, we, they → don't
- **Group B:** he, she, it → doesn't

#### 2. Past Simple

**All subjects use same form!**
- **Single Group:** I, you, he, she, it, we, they → past form (drank, ate, worked)

**Negative:**
- **Single Group:** All subjects → didn't + base verb

#### 3. Past Continuous

**Critical: Different grouping than present simple!**

- **Group A:** you, we, they → were + verb-ing (were reading)
- **Group B:** I, he, she, it → was + verb-ing (was reading)

**Note:** "I" goes with "he/she/it" for past continuous!

#### 4. Present Continuous

**Three groups needed:**
- **Group A:** I → am + verb-ing (am reading)
- **Group B:** you, we, they → are + verb-ing (are reading)
- **Group C:** he, she, it → is + verb-ing (is reading)

#### 5. Present Perfect

- **Group A:** I, you, we, they → have + past participle (have visited)
- **Group B:** he, she, it → has + past participle (has visited)

#### 6. Past Perfect

**All subjects use same form!**
- **Single Group:** All subjects → had + past participle (had visited)

#### 7. Future Simple (will)

**All subjects use same form!**
- **Single Group:** All subjects → will + base verb (will drink)

#### 8. Modals (can, could, should, must, may, might, would)

**All subjects use same form!**
- **Single Group:** All subjects → modal + base verb (can speak, should study)

#### 9. Passive Voice

**Group by tense:**

Present Simple Passive:
- **Group A:** I, you, we, they → are + past participle (are invited)
- **Group B:** he, she, it → is + past participle (is invited)

Past Simple Passive:
- **Group A:** you, we, they → were + past participle (were invited)
- **Group B:** I, he, she, it → was + past participle (was invited)

### Quick Reference Table

| Grammar | Group A Subjects | Group A Form | Group B Subjects | Group B Form |
|---------|-----------------|--------------|------------------|--------------|
| Present Simple | I/you/we/they | base verb | he/she/it | verb-s |
| Past Simple | ALL | past form | - | - |
| Past Continuous | you/we/they | were + -ing | I/he/she/it | was + -ing |
| Present Continuous | I | am + -ing | you/we/they (are), he/she/it (is) | - |
| Present Perfect | I/you/we/they | have + p.p. | he/she/it | has + p.p. |
| Past Perfect | ALL | had + p.p. | - | - |
| Future (will) | ALL | will + base | - | - |
| Modals | ALL | modal + base | - | - |

---

## Context Markers & Disambiguation

### The Problem

**Without context markers, multiple tenses can be grammatically correct:**

```
Template: "She ____ coffee."

All correct:
- doesn't drink (present simple negative)
- didn't drink (past simple negative)
- won't drink (future simple negative)
- isn't drinking (present continuous negative)
```

### The Solution: Context Markers

**Add temporal or contextual markers that make only ONE tense appropriate:**

```
Template: "She ____ coffee right now."
Context: "right now" → requires present (doesn't/isn't)

Template: "She ____ coffee yesterday."
Context: "yesterday" → requires past (didn't/wasn't)

Template: "She ____ coffee tomorrow."
Context: "tomorrow" → requires future (won't)
```

### Context Markers by Grammar

#### Present Simple Context Markers

**Routines/Habits:**
- every day, every morning, every week
- usually, always, often, sometimes, rarely, never
- on weekends, on Mondays, on weekdays

**Facts:**
- (scientific facts need no marker: "Water boils at 100°C")
- generally, typically, normally

**Present state:**
- right now, currently, these days, nowadays, at the moment (for negatives/questions)

#### Past Simple Context Markers

**Specific past time:**
- yesterday, last week, last month, last year
- in 2020, in January, in the summer
- ago (two days ago, three weeks ago)
- when I was young, when he lived in Paris

#### Past Continuous Context Markers

**Specific past moment:**
- at 8pm yesterday, at this time last week
- when you called, when he arrived
- while I was cooking, during the meeting
- all day yesterday, all evening

#### Present Continuous Context Markers

**Current ongoing:**
- right now, at the moment, currently
- today, this week, this month
- these days (for temporary situations)
- Look! Listen! (imperative starters)

#### Present Perfect Context Markers

**Past to present relevance:**
- before, already, yet, just, recently
- ever, never
- since (since 2020, since Monday)
- for (for three years, for a long time)
- so far, up to now, until now

#### Future Simple Context Markers

**Future time:**
- tomorrow, next week, next month, next year
- soon, later, in the future
- in 2030, in five years

#### Modals Context Markers

**Modals rely on semantic context, not temporal:**
- Ability: naturally, well, easily, fluently
- Obligation: (no specific marker needed - meaning is clear)
- Advice: (no specific marker needed)
- Possibility: perhaps, maybe, possibly

### Context Marker Implementation

**In your JSON, create specific marker lists for each grammar:**

```json
// Present Simple Pattern
{
  "chunks": {
    "PRESENT_MARKER": [
      "every day",
      "usually",
      "often",
      "right now",
      "these days"
    ]
  }
}

// Past Simple Pattern
{
  "chunks": {
    "PAST_MARKER": [
      "yesterday",
      "last week",
      "in 2020",
      "two days ago"
    ]
  }
}

// Present Perfect Pattern
{
  "chunks": {
    "PRESENT_PERFECT_MARKER": [
      "before",
      "already",
    
      "for three years"
    ]
  }
}
```

---

## Level-Based Complexity

### Overview

**Template complexity, chunk count, and vocabulary sophistication scale with CEFR level.**

### A1 (Beginner)

**Goal:** Basic form recognition, simple sentences
**Template Complexity:** 2-3 chunks maximum
**Sub-grammars:** None
**Vocabulary:** High-frequency (100-500 most common words)
**Uniqueness Target:** 30-50 unique questions

**Template Examples:**
```
"{SUBJ} ____ {OBJ}."
"{SUBJ} ____ {FREQUENCY}."
"I ____ {ACTIVITY}."
```

**Chunk Example:**
```json
{
  "SUBJ": ["I", "you", "we"],
  "VERB": {"drink": {...}, "eat": {...}},
  "OBJ": ["coffee", "water", "tea"]
}
```

**Uniqueness:** 3 × 2 × 3 = 18 questions
**Need:** Add TIME chunk with 2 items → 3 × 2 × 3 × 2 = 36 ✓

### A2 (Elementary)

**Goal:** Basic sentence variety with context
**Template Complexity:** 3-4 chunks
**Sub-grammars:** 0-1 (usually just prepositions)
**Vocabulary:** Common words (500-1000 most frequent)
**Uniqueness Target:** 80-120 unique questions

**Template Examples:**
```
"{SUBJ} ____ {OBJ} {TIME}."
"{SUBJ} ____ {PREP}{PLACE} {TIME}."
"{SUBJ} ____ {OBJ} {FREQUENCY}."
```

**Chunk Example:**
```json
{
  "SUBJ": ["he", "she"],
  "VERB": {"drink": {...}, "eat": {...}, "watch": {...}},
  "OBJ": ["coffee", "breakfast", "TV"],
  "TIME": ["in the morning", "at night", "every day", "usually"]
}
```

**Uniqueness:** 2 × 3 × 3 × 4 = 72 questions
**Need:** Add one more verb → 2 × 4 × 3 × 4 = 96 ✓

### B1 (Intermediate)

**Goal:** Varied sentence patterns with multiple contexts
**Template Complexity:** 4-5 chunks
**Sub-grammars:** 1-2 (articles, prepositions)
**Vocabulary:** Broader domains (1000-2000 words)
**Uniqueness Target:** 150-250 unique questions

**Template Examples:**
```
"{SUBJ} ____ {ARTICLE}{OBJ} {PREP}{TIME}."
"{SUBJ} ____ {VERB} {OBJ} because {REASON}."
"{PREP}{TIME}, {SUBJ} ____ {VERB} {OBJ}."
```

**Chunk Example:**
```json
{
  "SUBJ": ["journalists", "reporters", "editors"],
  "VERB": {"write": {...}, "publish": {...}, "investigate": {...}},
  "ARTICLE_OBJ": ["an article", "a report", "the news", "the story"],
  "PREP_TIME": ["in the morning", "every day", "on deadline"],
  "REASON": ["it's important", "it's newsworthy", "readers need to know"]
}
```

**Uniqueness:** 3 × 3 × 4 × 3 × 3 = 324 questions ✓

### B2 (Upper-Intermediate)

**Goal:** Sophisticated, complex sentences
**Template Complexity:** 5-6 chunks
**Sub-grammars:** 2-3 (articles, prepositions, relative clauses)
**Vocabulary:** Academic, professional (2000-3000 words)
**Uniqueness Target:** 300-500 unique questions

**Template Examples:**
```
"{SUBJ} ____ {MODAL}{VERB} {ARTICLE}{OBJ} {PREP}{PLACE} {TIME}."
"{SUBJ} ____ {VERB} {ARTICLE}{OBJ} that {RELATIVE_CLAUSE}."
"{PREP}{TIME}, {SUBJ} ____ {VERB} {ARTICLE}{OBJ} {PREP}{PLACE}."
```

**Chunk Example:**
```json
{
  "SUBJ": ["the correspondent", "the investigative journalist", "the editor-in-chief"],
  "MODAL_VERB": ["should verify", "must confirm", "could investigate"],
  "ARTICLE_OBJ": ["the allegations", "the evidence", "the sources"],
  "PREP_PLACE": ["at the scene", "in the field", "during the investigation"],
  "TIME": ["before publication", "immediately", "as soon as possible"]
}
```

### C1 (Advanced)

**Goal:** Near-native complexity and nuance
**Template Complexity:** 6-7+ chunks
**Sub-grammars:** 3+ (articles, prepositions, relative clauses, conditionals)
**Vocabulary:** Sophisticated, field-specific (3000+ words)
**Uniqueness Target:** 500+ unique questions

**Template Examples:**
```
"{SUBJ} ____ {MODAL}{VERB} {ARTICLE}{OBJ} {RELATIVE_CLAUSE} {PREP}{PLACE} {CONDITIONAL}."
"{GERUND}{ARTICLE}{OBJ}, {SUBJ} ____ {VERB} {PREP}{PLACE} {TIME}."
```

### Complexity Scaling Table

| Level | Chunks | Sub-grammars | Vocab Range | Uniqueness | Template Structure |
|-------|--------|--------------|-------------|------------|-------------------|
| A1 | 2-3 | 0 | Top 500 words | 30-50 | Simple, direct |
| A2 | 3-4 | 0-1 | 500-1000 words | 80-120 | Basic context |
| B1 | 4-5 | 1-2 | 1000-2000 words | 150-250 | Multiple contexts |
| B2 | 5-6 | 2-3 | 2000-3000 words | 300-500 | Complex structures |
| C1 | 6-7+ | 3+ | 3000+ words | 500+ | Sophisticated |

---

## Domain-Based Pattern Creation

### The Domain Strategy

**You have 100 domains prepared. Each pattern JSON file focuses on ONE domain.**

**Benefits:**
- Each domain gets focused, relevant vocabulary
- Easy to manage (one template per file)
- Maximum variety (100 domains × 10 grammars = 1000+ patterns)
- Modular and scalable
- Domain experts can contribute vocabulary

### Naming Convention

**Pattern ID Format:** `{GRAMMAR}_{DOMAIN}_{LEVEL}_{TYPE}`

**Examples:**
```
PRESENT_SIMPLE_JOURNALISM_B1_TYPE1.json
PAST_CONTINUOUS_TRAVEL_A2_TYPE2.json
PRESENT_PERFECT_TECHNOLOGY_B2_TYPE2.json
MODALS_HEALTHCARE_B1_TYPE3.json
GERUND_VERBS_EDUCATION_B1_TYPE1.json
```

### Domain Examples

**Daily Life:** coffee, breakfast, morning routine, hobbies
**Journalism:** articles, reporters, investigation, publication
**Travel:** destinations, booking, flights, accommodation
**Technology:** software, programming, devices, internet
**Healthcare:** doctors, treatment, patients, medicine
**Education:** students, teachers, curriculum, exams
**Business:** meetings, clients, projects, deadlines
**Environment:** pollution, climate, conservation, recycling
**Sports:** training, competition, athletes, teams
**Food:** ingredients, cooking, recipes, restaurants

### Domain-Specific Template Example

**Domain: Journalism**
**Grammar: Present Simple Negative**
**Level: B1**
**Type: 2 (Aux + Verb)**

```json
{
  "pattern_id": "PRESENT_SIMPLE_NEG_JOURNALISM_B1_TYPE2",
  "focus": "present_simple_negative",
  "level": "B1",
  "domain": "journalism",
  "category": "grammar",
  "template_type": "type_2",
  "sub_grammar": ["present_simple"],

  "template": "{SUBJ} ____ {OBJ} {PREP}{TIME}.",

  "example": "The journalist doesn't publish false information before publication.",

  "explanation": "Present simple negative is formed with don't/doesn't + base verb. Use 'doesn't' with he/she/it and 'don't' with I/you/we/they.",

  "chunks": {
    "SUBJ": ["the journalist", "the reporter", "the editor"],

    "VERB": {
      "publish": {
        "correct_forms": ["doesn't publish"],
        "wrong_forms": ["don't publish", "didn't publish", "isn't publishing"],
        "objects": ["false information", "unverified claims", "anonymous sources"],
        "distractor": "doesn't hide"
      },
      "write": {
        "correct_forms": ["doesn't write"],
        "wrong_forms": ["don't write", "didn't write", "isn't writing"],
        "objects": ["biased articles", "opinion pieces", "sensational headlines"],
        "distractor": "doesn't ignore"
      },
      "verify": {
        "correct_forms": ["doesn't verify"],
        "wrong_forms": ["don't verify", "didn't verify", "isn't verifying"],
        "objects": ["the facts", "the sources", "the allegations"],
        "distractor": "doesn't fabricate"
      }
    },

    "OBJ": [
      "false information",
      "unverified claims",
      "biased articles",
      "the facts",
      "the sources"
    ],

    "PREP_TIME": [
      "before publication",
      "without checking",
      "in daily news",
      "during breaking news",
      "on deadline"
    ]
  }
}
```

**Generated Questions:**
```
1. "The journalist ____ false information before publication."
   A. doesn't publish ✓ (correct - present simple negative 3rd person)
   B. don't publish (wrong auxiliary - should be 'doesn't')
   C. didn't publish (past simple negative)
   D. isn't publishing (present continuous negative)
   E. doesn't hide (distractor - semantically inappropriate)

2. "The editor ____ the facts without checking."
   A. doesn't verify ✓ (correct - present simple negative 3rd person)
   B. don't verify (wrong auxiliary - should be 'doesn't')
   C. didn't verify (past simple negative)
   D. isn't verifying (present continuous negative)
   E. doesn't fabricate (distractor - opposite of verify in journalism context)
```

---

## Uniqueness Targets & Calculation

### Uniqueness Formula

```
Total Unique Questions = Product of all variable chunks

Example:
SUBJ: 3 items
VERB: 4 items
OBJ: 5 items
TIME: 4 items

Uniqueness = 3 × 4 × 5 × 4 = 240 questions
```

### Targets by Level

| Level | Minimum Questions | Recommended Strategy |
|-------|------------------|---------------------|
| A1 | 30-50 | 2-3 chunks with 3-5 items each |
| A2 | 80-120 | 3-4 chunks with 3-5 items each |
| B1 | 150-250 | 4-5 chunks with 3-5 items each |
| B2 | 300-500 | 5-6 chunks with 4-6 items each |
| C1 | 500+ | 6-7 chunks with 5+ items each |

### Achieving Uniqueness

#### Strategy 1: Add Variable Chunks

```
LOW (18 questions):
SUBJ: 3 × VERB: 2 × OBJ: 3 = 18 ❌

MEDIUM (72 questions):
SUBJ: 3 × VERB: 2 × OBJ: 3 × TIME: 4 = 72 ✓

HIGH (288 questions):
SUBJ: 3 × VERB: 4 × OBJ: 4 × TIME: 3 × PLACE: 2 = 288 ✓
```

#### Strategy 2: Increase Items Per Chunk

```
SMALL:
VERB: 2 verbs × OBJ: 3 objects = 6 combinations

LARGE:
VERB: 5 verbs × OBJ: 6 objects = 30 combinations
```

#### Strategy 3: Domain-Specific Expansion

**Create multiple patterns for same grammar + different domains:**

```
Pattern 1: PRESENT_SIMPLE_DAILY_A2.json
- Domain: daily_life
- Vocab: coffee, breakfast, TV, books

Pattern 2: PRESENT_SIMPLE_TRAVEL_A2.json
- Domain: travel
- Vocab: destinations, flights, hotels, tours

Pattern 3: PRESENT_SIMPLE_WORK_A2.json
- Domain: work
- Vocab: meetings, projects, clients, deadlines

Result: 3 patterns × 80 questions each = 240 total questions for present simple A2
```

### Uniqueness Checklist

Before finalizing a pattern:

- [ ] Calculate total uniqueness: Product of all chunk sizes
- [ ] Verify meets minimum target for level
- [ ] Check each chunk has enough variety (3+ items)
- [ ] Ensure chunks are semantically diverse (not all synonyms)
- [ ] Confirm structural variety (not just word swaps)

---

## Grammar-Specific Guidelines

### Present Simple

**Subject Grouping:**
- Group A: I/you/we/they → base verb
- Group B: he/she/it → verb-s

**Template Types:**
- Type 1: Affirmative (I ____ coffee → drink/drinks/drank)
- Type 2: Negative (He ____ coffee → doesn't drink/don't drink)
- Type 3: Negative (He ____ drink → doesn't/don't)

**Context Markers:** every day, usually, often, always, sometimes, right now (for negatives)

**Distractor Methods:** wrong_conjugation, past_simple, present_continuous, future_simple

**Example Chunk Structure:**
```json
{
  "SUBJ": ["I", "you", "we", "they"],
  "VERB": {
    "drink": {
      "correct_forms": ["drink"],
      "wrong_forms": ["drinks", "drank", "am drinking", "will drink"]
    }
  },
  "OBJ": ["coffee", "tea", "water"],
  "FREQUENCY": ["every day", "usually", "often"]
}
```

---

### Past Simple

**Subject Grouping:**
- Single Group: ALL subjects → past form

**Template Types:**
- Type 1: Affirmative (I ____ Paris → visited/visit/have visited)
- Type 2: Negative (He ____ Paris → didn't visit/doesn't visit)
- Type 3: Negative (He ____ visit → didn't/doesn't)

**Context Markers:** yesterday, last week, ago, in 2020, when I was young

**Distractor Methods:** present_simple, present_perfect, past_continuous

**Example Chunk Structure:**
```json
{
  "SUBJ": ["I", "you", "he", "she", "we", "they"],
  "VERB": {
    "visit": {
      "correct_forms": ["visited"],
      "wrong_forms": ["visit", "visits", "have visited", "was visiting"]
    }
  },
  "OBJ": ["Paris", "London", "Tokyo"],
  "PAST_MARKER": ["yesterday", "last week", "in 2020"]
}
```

---

### Past Continuous

**Subject Grouping (CRITICAL - different from present simple!):**
- Group A: you/we/they → were + verb-ing
- Group B: I/he/she/it → was + verb-ing

**Template Types:**
- Type 1: Full form (He ____ at 8pm → was reading/were reading/read)
- Type 2: Aux + verb-ing (They ____ at 8pm → were studying/was studying)
- Type 3: Auxiliary only (They ____ studying → were/was/are)

**Context Markers:** at 8pm yesterday, when you called, while I was cooking, all evening

**Distractor Methods:** wrong_auxiliary (was/were), past_simple, present_continuous, present_perfect_continuous

**Example Chunk Structure:**
```json
{
  "SUBJ": ["you", "we", "they"],
  "VERB": {
    "study": {
      "correct_forms": ["were studying"],
      "wrong_forms": ["was studying", "studied", "are studying", "have been studying"]
    }
  },
  "SPECIFIC_PAST_TIME": ["at 8pm yesterday", "when you called", "all evening"]
}
```

---

### Present Continuous

**Subject Grouping (THREE groups!):**
- Group A: I → am + verb-ing
- Group B: you/we/they → are + verb-ing
- Group C: he/she/it → is + verb-ing

**Template Types:**
- Type 1: Full form (She ____ now → is working/are working/works)
- Type 2: Aux + verb-ing (He ____ now → is studying/are studying)
- Type 3: Auxiliary only (He ____ studying now → is/are/was)

**Context Markers:** right now, at the moment, currently, today, this week, Look!, Listen!

**Distractor Methods:** wrong_auxiliary (is/are/am), present_simple, past_continuous

**Example Chunk Structure:**
```json
{
  "SUBJ": ["he", "she", "it"],
  "VERB": {
    "work": {
      "correct_forms": ["is working"],
      "wrong_forms": ["are working", "am working", "works", "was working"]
    }
  },
  "PRESENT_CONTINUOUS_MARKER": ["right now", "at the moment", "currently"]
}
```

---

### Present Perfect

**Subject Grouping:**
- Group A: I/you/we/they → have + past participle
- Group B: he/she/it → has + past participle

**Template Types:**
- Type 1: Full form (I ____ Paris → have visited/has visited/visited)
- Type 2: Aux + past participle (She ____ Paris → has visited/have visited)
- Type 3: Auxiliary only (She ____ visited → has/have/had)

**Context Markers:** before, already, yet, just, recently, ever, never, since, for, so far

**Distractor Methods:** wrong_auxiliary (has/have), past_simple, past_perfect

**Example Chunk Structure:**
```json
{
  "SUBJ": ["I", "you", "we", "they"],
  "VERB": {
    "visit": {
      "correct_forms": ["have visited"],
      "wrong_forms": ["has visited", "had visited", "visited", "are visiting"]
    }
  },
  "OBJ": ["Paris", "the museum", "that restaurant"],
  "PRESENT_PERFECT_MARKER": ["before", "already", "recently", "many times"]
}
```

---

### Modals (can, could, should, must, will, would, may, might)

**Subject Grouping:**
- Single Group: ALL subjects → same form (no conjugation!)

**Template Types:**
- Type 1: Modal + verb (She ____ well → can swim/could swim/must swim)
- Type 3: Modal only (She ____ swim well → can/could/should/must)

**Context Markers:** Semantic context (not temporal)
- Ability: well, fluently, easily, naturally
- Obligation: (context makes it clear)
- Advice: (context makes it clear)
- Possibility: perhaps, maybe, possibly

**Distractor Methods:** different modals based on meaning

**Example Chunk Structure:**
```json
{
  "SUBJ": ["I", "you", "he", "she", "we", "they"],
  "MODAL": {
    "can": {
      "correct": "can",
      "wrong": ["could", "should", "must", "will"],
      "context": "ability"
    }
  },
  "BASE_VERB": ["speak", "write", "understand"],
  "ADVERB": ["fluently", "well", "easily"]
}
```

---

### Gerund vs Infinitive

**Subject Grouping:**
- Group by verb form (base form subjects vs -s form subjects)

**Template Types:**
- Type 1: Full phrase (I enjoy ____ → reading books/to read books/read books)

**Context Markers:** Not time-based; verb itself determines form

**Distractor Methods:** to_infinitive, bare_infinitive, gerund, wrong_conjugation

**Example Chunk Structure:**
```json
{
  "SUBJ": ["I", "you", "we", "they"],
  "VERB": {
    "enjoy": {
      "correct_forms": ["reading books", "watching TV"],
      "wrong_forms": ["to read books", "read books"],
      "bases": ["read books", "watch TV"],
      "form_type": "gerund"
    },
    "want": {
      "correct_forms": ["to learn Spanish", "to travel abroad"],
      "wrong_forms": ["learning Spanish", "learn Spanish"],
      "bases": ["learn Spanish", "travel abroad"],
      "form_type": "infinitive"
    }
  },
  "TIME": ["on weekends", "every day", "in my free time"]
}
```

---

### Passive Voice

**Subject Grouping (by tense):**

Present Simple Passive:
- Group A: I/you/we/they → are + past participle
- Group B: he/she/it → is + past participle

Past Simple Passive:
- Group A: you/we/they → were + past participle
- Group B: I/he/she/it → was + past participle

**Template Types:**
- Type 2: Be + past participle (It ____ in 1990 → was built/were built/is built)

**Context Markers:** Time markers matching the tense

**Distractor Methods:** wrong_auxiliary (was/were/is/are), active_voice, wrong_tense

**Example Chunk Structure:**
```json
{
  "SUBJ": ["the building", "the bridge", "the monument"],
  "VERB": {
    "build": {
      "correct_forms": ["was built"],
      "wrong_forms": ["were built", "is built", "has been built", "built"]
    }
  },
  "TIME": ["in 1990", "last year", "in 2010"]
}
```

---

## Complete Pattern Structure

### Critical Standardization Rules

**🔴 MANDATORY STANDARDS - DO NOT DEVIATE:**

1. **Blank Chunk Structure:** ANY chunk that goes in the blank (`____`) MUST have the nested structure with:
   - `correct_forms` (array)
   - `wrong_forms` (array with exactly 3 items)
   - `objects` or `article_objects` or `prep_objects` (array, can be empty)
   - `distractor` (string)

2. **Object Field Names:** Use semantic field names:
   - `objects` → maps to `{OBJ}` placeholder
   - `article_objects` → maps to `{ARTICLE_OBJ}` placeholder
   - `prep_objects` → maps to `{PREP_OBJ}` placeholder
   - `items` → maps to `{OBJ}` placeholder (generic)

3. **No Redundant Chunks:** If your blank chunk has nested objects, do NOT create a separate chunk with the same placeholder name

4. **Exactly 3 wrong_forms:** Always provide exactly 3 items in the `wrong_forms` array

5. **Grammar-Agnostic Design:** The generator automatically detects which chunk is the "blank chunk" by looking for the nested structure - it works with VERB, AUX, MODAL, ARTICLE, PREP, or any future chunk type!

**Why this matters:** The generator is now **fully grammar-agnostic**. It automatically detects and processes any chunk with the correct nested structure, regardless of its name.

### Full JSON Template

**IMPORTANT: The BLANK (`____`) can test ANY grammar element!**

The generator **automatically detects** which chunk is the "blank chunk" by looking for the nested structure. You can test:
- **VERB** → Verb forms/tenses (Type 1, 2)
- **AUX** → Auxiliary selection (Type 3: don't/doesn't/didn't)
- **MODAL** → Modal selection (Type 3: can/should/must)
- **ARTICLE** → Article choice (a/an/the)
- **PREP** → Preposition selection (in/on/at)
- **Any future grammar element!**

```json
{
  "pattern_id": "{GRAMMAR}_{DOMAIN}_{LEVEL}_{TYPE}_{GROUP}",
  "focus": "grammar_point_being_tested",
  "level": "A1|A2|B1|B2|C1",
  "domain": "domain_name",
  "category": "grammar",
  "template_type": "type_1|type_2|type_3",
  "subject_group": "group_a|group_b",
  "sub_grammar": ["optional_sub_grammar_rules"],

  "template": "{PLACEHOLDER1} ____ {PLACEHOLDER2} {PLACEHOLDER3}.",

  "example": "I drink coffee every day.",

  "explanation": "General explanation of the grammar rule.",

  "chunks": {
    "PLACEHOLDER1": ["item1", "item2", "item3"],

    "BLANK_CHUNK_NAME": {
      "item_name_1": {
        "correct_forms": ["correct answer"],
        "wrong_forms": ["wrong1", "wrong2", "wrong3"],
        "objects": ["obj1", "obj2"],              // or article_objects, prep_objects
        "distractor": "semantically wrong option"
      },
      "item_name_2": {
        "correct_forms": ["..."],
        "wrong_forms": ["...", "...", "..."],
        "article_objects": ["..."],               // Example: different object type
        "distractor": "..."
      }
    },

    "PLACEHOLDER2": ["context1", "context2", "context3"]
  }
}
```

**How the Auto-Detection Works:**
1. Generator scans all chunks in your pattern
2. Finds the chunk with nested structure containing `correct_forms`, `wrong_forms`, `distractor`
3. Automatically extracts answer options from that chunk
4. Maps object fields to appropriate placeholders:
   - `objects` → `{OBJ}`
   - `article_objects` → `{ARTICLE_OBJ}`
   - `prep_objects` → `{PREP_OBJ}`
5. **No hardcoding!** Works with any chunk name (VERB, AUX, MODAL, etc.)

**Notes:**
- Template placeholders must match chunk names exactly
- Only ONE chunk should have the nested structure (the blank chunk)
- Objects from the blank chunk override any redundant separate chunks

### Concrete Examples for Different Grammar Types

#### Example 1: Testing VERB (Present Simple)
```json
{
  "template": "{SUBJ} ____ {FREQUENCY}.",
  "chunks": {
    "SUBJ": ["I", "you", "we"],
    "VERB": {  // ← BLANK tests VERB
      "drink": {
        "correct_forms": ["drink"],
        "wrong_forms": ["drinks", "drank", "am drinking"],
        "objects": ["coffee", "tea", "water"],
        "distractor": "sleep"
      }
    },
    "FREQUENCY": ["every day", "usually"]
  }
}
```
Question: "I ____ every day." → Options: drink/drinks/drank/am drinking/sleep

---

#### Example 2: Testing ARTICLE
```json
{
  "template": "{SUBJ} {VERB} ____ {NOUN}.",
  "chunks": {
    "SUBJ": ["I", "you", "we"],
    "VERB": ["eat", "drink", "want"],
    "ARTICLE": {  // ← BLANK tests ARTICLE
      "an": {
        "correct_forms": ["an"],
        "wrong_forms": ["a", "the", "some"],
        "objects": ["apple", "orange", "egg"],
        "distractor": "many"
      }
    },
    "NOUN": ["apple", "orange", "egg"]
  }
}
```
Question: "I eat ____ apple." → Options: an/a/the/some/many

---

#### Example 3: Testing PREPOSITION (Time)
```json
{
  "template": "{SUBJ} {VERB} {ACTIVITY} ____ {TIME}.",
  "chunks": {
    "SUBJ": ["I", "you", "we"],
    "VERB": ["work", "study", "sleep"],
    "ACTIVITY": ["hard", "well"],
    "PREP": {  // ← BLANK tests PREP
      "in": {
        "correct_forms": ["in"],
        "wrong_forms": ["on", "at", "during"],
        "objects": ["the morning", "the evening", "winter"],
        "distractor": "between"
      }
    },
    "TIME": ["the morning", "the evening", "winter"]
  }
}
```
Question: "I work hard ____ the morning." → Options: in/on/at/during/between

---

#### Example 4: Testing MODAL (Type 3)
```json
{
  "template": "{SUBJ} ____ {VERB} {OBJ}.",
  "chunks": {
    "SUBJ": ["you", "he", "they"],
    "MODAL": {  // ← BLANK tests MODAL
      "should": {
        "correct_forms": ["should"],
        "wrong_forms": ["must", "can", "could"],
        "objects": [],  // Empty - modals don't need objects
        "distractor": "might"
      }
    },
    "VERB": ["study", "exercise", "practice"],
    "OBJ": ["harder", "regularly", "daily"]
  }
}
```
Question: "You ____ study harder." → Options: should/must/can/could/might

### Answer Options Structure

**Each question generates 5 options (A-E):**
1. **Correct form** - From `correct_forms`
2. **Wrong form 1** - From `wrong_forms[0]` (different tense/conjugation)
3. **Wrong form 2** - From `wrong_forms[1]` (different tense/conjugation)
4. **Wrong form 3** - From `wrong_forms[2]` (different tense/conjugation)
5. **Distractor** - From `distractor` (semantically wrong but grammatically possible)

**Example:**
```json
"drink": {
  "correct_forms": ["drink"],
  "wrong_forms": ["drinks", "drank", "am drinking"],
  "distractor": "sleep"
}
```

**Generated Options:**
- A. drink ✓ (correct)
- B. drinks (wrong conjugation)
- C. drank (wrong tense)
- D. am drinking (wrong aspect)
- E. sleep (distractor - doesn't fit context "I ___ coffee")

### Field Descriptions

| Field | Required | Type | Description | Example |
|-------|----------|------|-------------|---------|
| `pattern_id` | Yes | String | Unique identifier | `"PRESENT_SIMPLE_JOURNALISM_B1_TYPE2"` |
| `focus` | Yes | String | Grammar point tested | `"present_simple_negative"` |
| `level` | Yes | String | CEFR level | `"B1"` |
| `domain` | Yes | String | Semantic domain | `"journalism"` |
| `category` | Yes | String | Question category | `"grammar"` |
| `template_type` | Yes | String | Type 1, 2, or 3 | `"type_2"` |
| `sub_grammar` | No | Array | Supporting grammar rules | `["articles", "prepositions"]` |
| `template` | Yes | String | Sentence structure with placeholders | `"{SUBJ} ____ {OBJ} {TIME}."` |
| `example` | Yes | String | Sample question from this pattern | `"I drink coffee every day."` |
| `explanation` | Yes | String | Grammar rule explanation (why this grammar works) | `"Present simple with I/you/we/they uses base form..."` |
| `chunks` | Yes | Object | Variable parts of sentence | See structure above |

### Blank Item Structure Fields

**This structure applies to whatever goes in the BLANK (VERB, AUX, MODAL, ARTICLE, PREP, etc.):**

| Field | Required | Type | Description | Example |
|-------|----------|------|-------------|---------|
| `correct_forms` | Yes | Array | The correct answer(s) | `["drink"]` or `["an"]` or `["don't"]` |
| `wrong_forms` | Yes | Array (3 items) | Exactly 3 grammatical transformations | `["drinks", "drank", "am drinking"]` |
| `objects` | Conditional | Array | Items that work with this option (for general objects) | `["coffee", "tea"]` |
| `article_objects` | Conditional | Array | Items with articles (for ARTICLE or VERB that needs articles) | `["clients", "cases"]` |
| `prep_objects` | Conditional | Array | Items with prepositions (for PREP testing) | `["the morning", "Monday"]` |
| `items` | Conditional | Array | Generic items (alternative to objects) | `["football", "tennis"]` |
| `distractor` | Yes | String | Semantically wrong option | `"sleep"` or `"many"` or `"won't"` |

**Note on object fields:**
- **Use when:** The blank item needs specific compatible objects
- **Choose the right type:**
  - `objects` → General objects, maps to `{OBJ}`
  - `article_objects` → Objects with articles, maps to `{ARTICLE_OBJ}`
  - `prep_objects` → Objects with prepositions, maps to `{PREP_OBJ}`
  - `items` → Generic items, maps to `{OBJ}`
- **Skip when:** Not needed (AUX, MODAL often don't need objects - use empty array `[]`)
- **Never create:** A separate chunk if objects are in the blank item!

**How objects work in templates:**

**Option 1: Objects NOT in template** (Recommended)
```json
{
  "template": "{SUBJ} ____ {FREQUENCY}.",
  "chunks": {
    "VERB": {
      "drink": {"objects": ["coffee", "tea"]}
    }
  }
}
```
→ System inserts object after blank: "I ____ coffee every day."

**Option 2: Objects AS template placeholder**
```json
{
  "template": "{SUBJ} ____ {OBJ} {FREQUENCY}.",
  "chunks": {
    "VERB": {
      "drink": {"objects": ["coffee", "tea"]}
    }
    // NO separate OBJ array!
  }
}
```
→ System picks object from selected VERB's objects and uses for {OBJ} placeholder

**❌ WRONG - Redundant:**
```json
{
  "template": "{SUBJ} ____ {OBJ} {FREQUENCY}.",
  "chunks": {
    "VERB": {"drink": {"objects": ["coffee", "tea"]}},
    "OBJ": ["coffee", "tea", "breakfast"]  // ❌ Duplicate!
  }
}
```

### Chunk Naming Conventions

**Chunks that go IN the BLANK (test grammar) - Grammar-Agnostic!**

The generator **automatically detects** any chunk with the nested structure. Common examples:

| Chunk Name | Tests | Object Field | Example Structure |
|------------|-------|--------------|-------------------|
| `VERB` | Verb forms/tenses | `objects` or `article_objects` | `{"drink": {"correct_forms": ["drink"], "wrong_forms": ["drinks", "drank", "am drinking"], "objects": ["coffee"], "distractor": "sleep"}}` |
| `AUX` | Auxiliaries (Type 3) | Usually empty `[]` | `{"don't": {"correct_forms": ["don't"], "wrong_forms": ["doesn't", "didn't", "aren't"], "objects": [], "distractor": "won't"}}` |
| `MODAL` | Modal verbs | Usually empty `[]` | `{"should": {"correct_forms": ["should"], "wrong_forms": ["must", "can", "could"], "objects": [], "distractor": "might"}}` |
| `ARTICLE` | Articles (a/an/the) | `objects` (nouns) | `{"an": {"correct_forms": ["an"], "wrong_forms": ["a", "the", "some"], "objects": ["apple", "egg"], "distractor": "many"}}` |
| `PREP` | Prepositions | `prep_objects` | `{"in": {"correct_forms": ["in"], "wrong_forms": ["on", "at", "during"], "prep_objects": ["the morning"], "distractor": "between"}}` |

**Key Point:** The generator doesn't care what you name the chunk! It automatically finds and processes any chunk with:
- `correct_forms` (array)
- `wrong_forms` (array with 3 items)
- Object field (can be empty)
- `distractor` (string)

**Chunks that go OUTSIDE the BLANK (context/structure):**
| Chunk Name | Contains | Example |
|------------|----------|---------|
| `SUBJ` | Subject pronouns or nouns | `["I", "you", "he", "the journalist"]` |
| `TIME` / `PRESENT_MARKER` / `PAST_MARKER` | Time expressions | `["yesterday", "every day"]` |
| `FREQUENCY` | Frequency adverbs | `["always", "usually", "often"]` |
| `PLACE` | Places | `["at home", "in the office", "at school"]` |
| `REASON` | Reason clauses | `["because it's important"]` |
| `RELATIVE_CLAUSE` | Relative clauses | `["which was written yesterday"]` |

**Combined Chunks (when sub-grammars interact):**
| Chunk Name | Contains | Why Combined? | Example |
|------------|----------|---------------|---------|
| `ARTICLE_OBJ` | Article + object together | Article must agree with noun | `["a book", "an apple", "the report"]` |
| `PREP_TIME` | Preposition + time | Specific time expressions | `["in the morning", "on Monday"]` |
| `PREP_PLACE` | Preposition + place | Specific place expressions | `["at home", "in the office"]` |

**IMPORTANT:** Don't create redundant chunks! If VERB already has `objects: ["coffee", "tea"]`, don't create a separate `OBJ` array!

---

## Grammar-Agnostic Architecture

### How the Generator Works

**The generator is now fully grammar-agnostic!** It doesn't have hardcoded logic for specific chunk names.

**Auto-Detection Process:**
1. Scans all chunks in your pattern JSON
2. Looks for ANY chunk with nested structure containing:
   - `correct_forms`
   - `wrong_forms`
   - An object field (`objects`, `article_objects`, `prep_objects`, or `items`)
   - `distractor`
3. Treats that chunk as the "blank chunk" (regardless of its name!)
4. Extracts answer options from that chunk
5. Maps object fields to template placeholders automatically

**This means you can:**
- Test VERB with `VERB` chunk
- Test auxiliaries with `AUX` chunk
- Test modals with `MODAL` chunk
- Test articles with `ARTICLE` chunk
- Test prepositions with `PREP` chunk
- **Or create your own chunk types for future grammar points!**

**Example - Type 3 with AUX:**
```json
{
  "template": "{SUBJ} ____ {BASE_VERB} {OBJ} {TIME}.",
  "chunks": {
    "SUBJ": ["people", "we", "they"],
    "AUX": {
      "don't": {
        "correct_forms": ["don't"],
        "wrong_forms": ["doesn't", "didn't", "aren't"],
        "objects": [],
        "distractor": "won't"
      }
    },
    "BASE_VERB": ["recycle", "conserve"],
    "OBJ": ["plastic", "water"],
    "TIME": ["enough", "often"]
  }
}
```

**What happens:**
1. Generator detects `AUX` has the nested structure → **This is the blank chunk!**
2. Extracts: correct = "don't", wrong = ["doesn't", "didn't", "aren't"], distractor = "won't"
3. Generates: "People ____ recycle plastic enough."
4. Options: don't ✓ | doesn't | didn't | aren't | won't

**No hardcoding needed!** The same generator code works for VERB, AUX, MODAL, ARTICLE, or any future grammar type.

---

## Examples Across Grammars

### Example 1: Present Simple Type 1 - Daily Life Domain

```json
{
  "pattern_id": "PRESENT_SIMPLE_DAILY_A2_TYPE1",
  "focus": "present_simple",
  "level": "A2",
  "domain": "daily_life",
  "category": "grammar",
  "template_type": "type_1",
  "sub_grammar": [],

  "template": "{SUBJ} ____ {FREQUENCY}.",

  "example": "I drink coffee every day.",

  "explanation": "Present simple is used for habits and routines. With I/you/we/they, use the base form of the verb. The verb does not change.",

  "chunks": {
    "SUBJ": ["I", "you", "we", "they"],

    "VERB": {
      "drink": {
        "correct_forms": ["drink"],
        "wrong_forms": ["drinks", "drank", "am drinking"],
        "objects": ["coffee", "tea", "water", "juice"],
        "distractor": "sleep"
      },
      "eat": {
        "correct_forms": ["eat"],
        "wrong_forms": ["eats", "ate", "am eating"],
        "objects": ["breakfast", "lunch", "dinner", "snacks"],
        "distractor": "cook"
      },
      "watch": {
        "correct_forms": ["watch"],
        "wrong_forms": ["watches", "watched", "am watching"],
        "objects": ["TV", "movies", "videos", "the news"],
        "distractor": "listen"
      },
      "play": {
        "correct_forms": ["play"],
        "wrong_forms": ["plays", "played", "am playing"],
        "objects": ["football", "tennis", "games", "music"],
        "distractor": "study"
      }
    },

    "FREQUENCY": ["every day", "usually", "often", "sometimes", "always"]
  }
}
```

**Generated Question:**
```
I ____ coffee every day.

A. drink ✓ (correct - present simple base form)
B. drinks (wrong conjugation - third person)
C. drank (past simple)
D. am drinking (present continuous)
E. sleep (distractor - semantically wrong: doesn't fit "coffee")
```

**How it works:**
1. System selects verb: "drink"
2. System selects object from that verb's objects: "coffee"
3. Inserts object after blank: "I ____ coffee every day."
4. Object is NOT a template placeholder - it comes from the selected VERB!

**Uniqueness:** 4 subjects × 4 verbs × (avg 4 objects/verb) × 5 frequencies = 320 questions ✓

---

### Example 2: Past Continuous Type 2 - Travel Domain

```json
{
  "pattern_id": "PAST_CONTINUOUS_TRAVEL_B1_TYPE2",
  "focus": "past_continuous",
  "level": "B1",
  "domain": "travel",
  "category": "grammar",
  "template_type": "type_2",
  "sub_grammar": ["past_continuous"],

  "template": "{SUBJ} ____ {PREP}{PLACE} {SPECIFIC_PAST_TIME}.",

  "example": "We were traveling to Paris at this time last year.",

  "explanation": "Past continuous shows an action in progress at a specific time in the past. Use 'was' with I/he/she/it and 'were' with you/we/they.",

  "chunks": {
    "SUBJ": ["you", "we", "they"],

    "VERB": {
      "travel": {
        "correct_forms": ["were traveling"],
        "wrong_forms": ["was traveling", "traveled", "are traveling"],
        "objects": ["to Paris", "to London", "to Tokyo"],
        "distractor": "were sleeping"
      },
      "explore": {
        "correct_forms": ["were exploring"],
        "wrong_forms": ["was exploring", "explored", "are exploring"],
        "objects": ["the city", "the museum", "the ruins"],
        "distractor": "were working"
      },
      "stay": {
        "correct_forms": ["were staying"],
        "wrong_forms": ["was staying", "stayed", "are staying"],
        "objects": ["at a hotel", "at a hostel", "with friends"],
        "distractor": "were leaving"
      }
    },

    "PREP_PLACE": [
      "to Paris",
      "to London",
      "at a hotel",
      "in the city",
      "at the museum"
    ],

    "SPECIFIC_PAST_TIME": [
      "at this time last year",
      "when you called",
      "all day yesterday",
      "during the summer"
    ]
  }
}
```

**Generated Question:**
```
We ____ to Paris at this time last year.

A. were traveling ✓ (correct - past continuous with 'were')
B. was traveling (wrong auxiliary - should be 'were')
C. traveled (past simple)
D. are traveling (present continuous)
E. were sleeping (distractor - doesn't fit "to Paris")
```

**Uniqueness:** 3 subjects × 3 verbs × 5 places × 4 times = 180 questions ✓

---

### Example 3: Present Perfect Type 2 - Technology Domain

```json
{
  "pattern_id": "PRESENT_PERFECT_TECHNOLOGY_B2_TYPE2",
  "focus": "present_perfect",
  "level": "B2",
  "domain": "technology",
  "category": "grammar",
  "template_type": "type_2",
  "sub_grammar": ["present_perfect"],

  "template": "{SUBJ} ____ {ARTICLE}{OBJ} {PRESENT_PERFECT_MARKER}.",

  "example": "Developers have developed the software recently.",

  "explanation": "Present perfect connects past actions to the present. Use 'have' with I/you/we/they and 'has' with he/she/it, followed by the past participle.",

  "chunks": {
    "SUBJ": ["developers", "engineers", "programmers", "the team"],

    "VERB": {
      "develop": {
        "correct_forms": ["have developed"],
        "wrong_forms": ["has developed", "had developed", "developed"],
        "objects": ["the software", "the application", "the platform"],
        "distractor": "have deleted"
      },
      "implement": {
        "correct_forms": ["have implemented"],
        "wrong_forms": ["has implemented", "had implemented", "implemented"],
        "objects": ["the feature", "the solution", "the algorithm"],
        "distractor": "have removed"
      },
      "optimize": {
        "correct_forms": ["have optimized"],
        "wrong_forms": ["has optimized", "had optimized", "optimized"],
        "objects": ["the code", "the database", "the performance"],
        "distractor": "have broken"
      }
    },

    "ARTICLE_OBJ": [
      "the software",
      "the application",
      "the feature",
      "the code",
      "the database"
    ],

    "PRESENT_PERFECT_MARKER": [
      "recently",
      "already",
      "since last month",
      "for several weeks",
      "so far"
    ]
  }
}
```

**Generated Question:**
```
Developers ____ the software recently.

A. have developed ✓ (correct - present perfect with 'have')
B. has developed (wrong auxiliary - should be 'have')
C. had developed (past perfect)
D. developed (past simple)
E. have deleted (distractor - semantically wrong: developers don't "delete" newly)
```

**Uniqueness:** 4 subjects × 3 verbs × 5 objects × 5 markers = 300 questions ✓

---

### Example 4: Modals Type 3 - Healthcare Domain

```json
{
  "pattern_id": "MODALS_HEALTHCARE_B1_TYPE3",
  "focus": "modals_obligation",
  "level": "B1",
  "domain": "healthcare",
  "category": "grammar",
  "template_type": "type_3",
  "sub_grammar": [],

  "template": "{SUBJ} ____ {BASE_VERB} {OBJ} {FREQUENCY}.",

  "example": "Patients should take the medication regularly.",

  "explanation": "Modal verbs express obligation, ability, or advice. 'Should' gives advice, 'must' shows strong obligation, 'can' shows ability. Modals do not change form with different subjects.",

  "chunks": {
    "SUBJ": ["patients", "doctors", "nurses", "you", "people"],

    "MODAL": {
      "should": {
        "correct_forms": ["should"],
        "wrong_forms": ["must", "can", "could"],
        "context": "advice",
        "distractor": "might"
      },
      "must": {
        "correct_forms": ["must"],
        "wrong_forms": ["should", "can", "may"],
        "context": "strong_obligation",
        "distractor": "could"
      }
    },

    "BASE_VERB": [
      "take",
      "follow",
      "consult",
      "avoid",
      "exercise"
    ],

    "OBJ": [
      "the medication",
      "the doctor's advice",
      "a specialist",
      "smoking",
      "regularly"
    ],

    "FREQUENCY": [
      "regularly",
      "daily",
      "immediately",
      "as prescribed"
    ]
  }
}
```

**Generated Question:**
```
Patients ____ take the medication regularly.

A. should ✓ (correct - modal for advice)
B. must (strong obligation, not advice)
C. can (ability, not advice)
D. could (possibility/past ability)
E. might (distractor - too weak for health advice)
```

**Uniqueness:** 5 subjects × 2 modals × 5 verbs × 4 objects × 4 frequencies = 800 questions ✓

---

### Example 5: Gerund Verbs Type 1 - Education Domain

```json
{
  "pattern_id": "GERUND_VERBS_EDUCATION_B1_TYPE1",
  "focus": "gerund_verbs",
  "level": "B1",
  "domain": "education",
  "category": "grammar",
  "template_type": "type_1",
  "sub_grammar": ["gerunds"],

  "template": "{SUBJ} {VERB} ____ {TIME}.",

  "example": "Students enjoy learning new concepts during class.",

  "explanation": "Some verbs are followed by gerunds (verb + -ing). Common examples: enjoy, avoid, finish, keep, suggest, practice. The gerund acts as the object of these verbs.",

  "chunks": {
    "SUBJ": ["students", "teachers", "I", "we"],

    "VERB": {
      "enjoy": {
        "correct_forms": ["learning new concepts", "studying mathematics", "reading literature"],
        "wrong_forms": ["to learn new concepts", "learn new concepts", "learns new concepts"],
        "objects": ["new concepts", "mathematics", "literature"],
        "distractor": "sleeping late"
      },
      "avoid": {
        "correct_forms": ["procrastinating", "making mistakes", "missing deadlines"],
        "wrong_forms": ["to procrastinate", "procrastinate", "procrastinates"],
        "objects": ["procrastinating", "mistakes", "deadlines"],
        "distractor": "studying hard"
      },
      "finish": {
        "correct_forms": ["writing the essay", "completing homework", "grading papers"],
        "wrong_forms": ["to write the essay", "write the essay", "writes the essay"],
        "objects": ["the essay", "homework", "papers"],
        "distractor": "starting projects"
      }
    },

    "TIME": [
      "during class",
      "every day",
      "before exams",
      "in the evening"
    ]
  }
}
```

**Generated Question:**
```
Students enjoy ____ during class.

A. learning new concepts ✓ (correct - gerund form)
B. to learn new concepts (infinitive - wrong form)
C. learn new concepts (bare infinitive - wrong form)
D. learns new concepts (conjugated verb - wrong form)
E. sleeping late (distractor - students don't "enjoy" this in class context)
```

**Uniqueness:** 4 subjects × 3 verbs × 3 phrases × 4 times = 144 questions ✓

---

## Pattern Creation Workflow

### Step-by-Step Process

#### Step 1: Choose Grammar + Domain + Level

```
Grammar: Present Simple Negative
Domain: Journalism (from your 100 domains)
Level: B1
```

#### Step 2: Determine Subject Grouping for This Grammar

```
Present Simple Negative:
- Group A: I/you/we/they → don't + base verb
- Group B: he/she/it → doesn't + base verb

Choose Group B for this pattern (he/she/it)
```

#### Step 3: Choose Template Type

```
Decision:
- Testing auxiliary + verb coordination
- Negative sentence
→ Type 2: Auxiliary + Main Verb

Template: "{SUBJ} ____ {OBJ} {PREP}{TIME}."
Blank will contain: doesn't + verb
```

#### Step 4: Add Context Markers

```
Need PRESENT context to disambiguate from past/future:
PREP_TIME: ["right now", "these days", "currently", "usually"]
```

#### Step 5: Gather Domain-Specific Vocabulary

```
Domain: Journalism

Subjects: journalists, reporters, editors, correspondents
Verbs: publish, write, verify, investigate, report
Objects: false information, biased articles, the facts, sources
```

#### Step 6: Calculate Uniqueness

```
SUBJ: 3 items (journalists, reporters, editors)
VERB: 3 items (publish, write, verify)
OBJ: 5 items (false information, biased articles, etc.)
PREP_TIME: 4 items (right now, these days, etc.)

Uniqueness: 3 × 3 × 5 × 4 = 180 questions
Target for B1: 150-250 ✓
```

#### Step 7: Define Distractor Methods

```
For present simple negative Type 2:
- wrong_auxiliary (don't instead of doesn't)
- past_simple (didn't + verb)
- present_continuous (isn't + verb-ing)
- present_perfect (hasn't + past participle)
```

#### Step 8: Create JSON File

```
File name: present_simple_neg_journalism_b1_type2.json
Location: patterns/present_simple_neg_journalism_b1_type2.json
```

#### Step 9: Validate

```
Check:
✓ Pattern ID unique
✓ Subject grouping correct for grammar
✓ Context markers disambiguate
✓ Uniqueness target met
✓ All verb-object combinations make sense
✓ Distractor methods appropriate
```

#### Step 10: Test Generate

```bash
python main.py --pattern present_simple_neg_journalism_b1_type2 --count 10
```

Review generated questions for:
- Grammatical correctness
- Semantic naturalness
- Distractor quality

---

## Best Practices & Checklist

### Before Creating a Pattern

- [ ] **Grammar chosen** - Know exact grammar point to test
- [ ] **Domain selected** - From your 100 domains
- [ ] **Level determined** - A1, A2, B1, B2, or C1
- [ ] **Subject grouping researched** - Which subjects take which forms in THIS grammar?
- [ ] **Template type decided** - Type 1, 2, or 3 based on what aspect to test

### During Pattern Creation

- [ ] **Template includes context markers** - Ensures only one correct answer
- [ ] **Example field added** - Shows sample question from pattern
- [ ] **Uniqueness calculated** - Meets minimum target for level
- [ ] **3+ variable chunks** - For adequate variety
- [ ] **Domain vocabulary gathered** - Relevant, natural vocabulary
- [ ] **All verb-object combinations tested mentally** - Do they sound natural?
- [ ] **Exactly 3 wrong_forms provided** - Grammatical transformations
- [ ] **Distractor added for each verb** - Semantically inappropriate option

### After Pattern Creation

- [ ] **JSON structure valid** - No syntax errors
- [ ] **Pattern ID follows convention** - {GRAMMAR}_{DOMAIN}_{LEVEL}_{TYPE}
- [ ] **All fields filled** - No empty strings or missing fields
- [ ] **Explanation clear** - Student-friendly language
- [ ] **Test generation run** - At least 10 sample questions reviewed
- [ ] **Questions make sense** - Grammatically and semantically correct

### Common Mistakes to Avoid

❌ **Wrong subject grouping for grammar**
```
Present Simple: ✓ I/you/we/they vs he/she/it
Past Continuous: ✗ I/you/we/they vs he/she/it (WRONG!)
Past Continuous: ✓ you/we/they vs I/he/she/it (CORRECT!)
```

❌ **No context markers - multiple answers possible**
```
Bad: "She ____ coffee." (doesn't/didn't/won't all work)
Good: "She ____ coffee right now." (only doesn't works)
```

❌ **Testing vocabulary instead of grammar**
```
Bad: Focus is present_simple, but blank tests noun choice
Good: Focus is present_simple, blank tests verb form
```

❌ **Insufficient uniqueness**
```
Bad: 2 subjects × 2 verbs × 3 objects = 12 questions for B1 (target: 150)
Good: Add TIME chunk → 2 × 2 × 3 × 13 = 156 questions ✓
```

❌ **Unnatural verb-object combinations**
```
Bad: "enjoy having problems" (semantically wrong)
Good: "enjoy reading books" (natural)
```

❌ **Wrong number of wrong_forms**
```
Bad: "wrong_forms": ["drinks", "drank"] (only 2)
Bad: "wrong_forms": ["drinks", "drank", "drinking", "drunk"] (4)
Good: "wrong_forms": ["drinks", "drank", "am drinking"] (exactly 3) ✓
```

❌ **Missing or inappropriate distractor**
```
Bad: No distractor field provided
Bad: "distractor": "drinks" (grammatical transformation, should be in wrong_forms)
Good: "distractor": "sleep" (semantically wrong for "I ___ coffee") ✓
```

---

## Common Mistakes & Troubleshooting

### Critical Rule: Field Name Standardization

**⚠️ ALWAYS use `objects` and `{OBJ}` - NEVER use custom names!**

The system is designed to work with standardized field names. Using custom names causes semantic mismatches.

**❌ WRONG - Custom field names:**
```json
{
  "template": "{SUBJ} ____ {ACTIVITY} {FREQUENCY}.",
  "chunks": {
    "VERB": {
      "play": {
        "activities": ["football", "tennis", "basketball"]  // ❌ Wrong field name
      }
    },
    "ACTIVITY": ["football", "tennis", "yoga"]  // ❌ Redundant chunk
  }
}
```
**Result:** Generates "He does football" instead of "He plays football" ❌

**✅ CORRECT - Standardized names:**
```json
{
  "template": "{SUBJ} ____ {OBJ} {FREQUENCY}.",
  "chunks": {
    "VERB": {
      "play": {
        "objects": ["football", "tennis", "basketball"]  // ✅ Standardized
      }
    }
    // ✅ No separate chunk needed
  }
}
```
**Result:** Generates "He plays football" ✅

### Common Mistake #1: Redundant Chunks

**Problem:** Creating both verb-specific objects AND a separate chunk

```json
// ❌ WRONG
{
  "chunks": {
    "VERB": {
      "learn": {"objects": ["languages", "skills"]},
      "review": {"objects": ["notes", "materials"]}
    },
    "OBJ": ["languages", "skills", "notes"]  // ❌ Redundant!
  }
}
```

**What happens:** Separate chunk overwrites verb-specific objects → wrong pairings
- "review languages" ❌ (should be "review notes")
- "learn notes" ❌ (should be "learn languages")

**✅ FIX:** Remove the redundant chunk
```json
{
  "chunks": {
    "VERB": {
      "learn": {"objects": ["languages", "skills"]},
      "review": {"objects": ["notes", "materials"]}
    }
    // ✅ No separate OBJ chunk
  }
}
```

### Common Mistake #2: Old Structure Format

**Problem:** Using deprecated field names from old system

```json
// ❌ WRONG - Old structure
{
  "VERB": {
    "want": {
      "phrases": ["to learn Spanish", "to buy a car"],  // ❌ Old name
      "bases": ["learn Spanish", "buy a car"],          // ❌ Deprecated
      "context_distractors": ["to fail", "to waste"]   // ❌ Old format
    }
  }
}
```

**Error:** `Verb 'want' missing 'correct_forms'`

**✅ FIX:** Use new standardized structure
```json
{
  "VERB": {
    "want": {
      "correct_forms": ["to learn Spanish", "to buy a car"],  // ✅ New name
      "wrong_forms": ["learning Spanish", "learn Spanish", "learns Spanish"],  // ✅ Exactly 3
      "objects": [],  // ✅ Required (can be empty)
      "distractor": "to waste time"  // ✅ Single string
    }
  }
}
```

### Common Mistake #3: Wrong Number of wrong_forms

**Problem:** Not providing exactly 3 wrong_forms

```json
// ❌ WRONG
{
  "wrong_forms": ["drinks", "drank"]  // Only 2
}

// ❌ WRONG
{
  "wrong_forms": ["drinks", "drank", "drinking", "drunk"]  // 4 items
}
```

**Error:** `wrong_forms must have exactly 3 items`

**✅ FIX:** Always provide exactly 3
```json
{
  "wrong_forms": ["drinks", "drank", "am drinking"]  // ✅ Exactly 3
}
```

### Common Mistake #4: Custom Placeholder Names

**Problem:** Using custom placeholder names in templates

```json
// ❌ WRONG
{
  "template": "{SUBJ} ____ {ACTIVITY} {FREQUENCY}.",  // ❌ {ACTIVITY}
  "template": "{SUBJ} ____ {PHRASE} {TIME}.",         // ❌ {PHRASE}
  "template": "{SUBJ} ____ {ITEM} {CONTEXT}."         // ❌ {ITEM}
}
```

**✅ FIX:** Always use {OBJ}
```json
{
  "template": "{SUBJ} ____ {OBJ} {FREQUENCY}.",  // ✅ {OBJ}
  "template": "{SUBJ} ____ {OBJ} {TIME}.",       // ✅ {OBJ}
  "template": "{SUBJ} ____ {OBJ} {CONTEXT}."     // ✅ {OBJ}
}
```

### Troubleshooting Guide

#### Error: "Verb 'X' missing 'correct_forms'"

**Cause:** Using old structure (phrases/bases) instead of new structure

**Solution:**
1. Rename `phrases` → `correct_forms`
2. Create `wrong_forms` array with exactly 3 items
3. Pick one `distractor` from context_distractors
4. Add `objects` field (can be empty array)

#### Error: Semantic mismatch (e.g., "review languages")

**Cause:** Redundant separate chunk overwriting verb-specific objects

**Solution:**
1. Check if VERB has `objects` field
2. If yes, remove any separate OBJ/ACTIVITY/PHRASE chunks
3. Keep only verb-specific objects

#### Error: Wrong verb used (e.g., "does football" instead of "plays football")

**Cause:** Using custom field names (activities/phrases/items) instead of `objects`

**Solution:**
1. Rename all custom fields → `objects`
2. Update template placeholders → `{OBJ}`
3. Remove redundant separate chunks

### Validation Checklist

Before finalizing a pattern file, verify:

**Structure Requirements:**
- [ ] All required fields present: pattern_id, focus, level, category, template, explanation, chunks
- [ ] Template uses standardized placeholders: {SUBJ}, {OBJ}, {FREQUENCY}, etc.
- [ ] No custom placeholder names ({ACTIVITY}, {PHRASE}, {ITEM}, etc.)

**VERB Structure (if present):**
- [ ] Each verb has `correct_forms` (array)
- [ ] Each verb has `wrong_forms` (array with EXACTLY 3 items)
- [ ] Each verb has `distractor` (single string)
- [ ] Each verb has `objects` field (array, can be empty)
- [ ] NO old fields: phrases, bases, context_distractors, wrong_collocations

**Chunk Structure:**
- [ ] If VERB has `objects`, NO separate OBJ chunk exists
- [ ] If template uses {OBJ}, either VERB has objects OR separate OBJ chunk exists (but not both)
- [ ] All chunks referenced in template exist in chunks object
- [ ] No redundant chunks

**Semantic Correctness:**
- [ ] All verb-object combinations make sense
- [ ] Distractors are semantically inappropriate (not just grammatically wrong)
- [ ] Context markers disambiguate to single correct answer

### Automated Fixes

If you encounter these errors, use the provided scripts:

1. **Old structure → New structure:**
   ```bash
   python convert_patterns.py
   ```

2. **Redundant chunks:**
   ```bash
   python fix_redundant_obj.py
   ```

3. **Custom field names:**
   ```bash
   python standardize_patterns.py
   ```

All scripts create backups (.json.backup) before making changes.

---

## Final Summary

### The Universal Framework

This guide provides a **grammar-agnostic, level-scalable, domain-based framework** for creating English grammar question patterns.

**Core Principles:**
1. ✅ Grammar-Focus: Blank tests grammar, not vocabulary
2. ✅ Context Markers: Disambiguate to ensure one correct answer
3. ✅ Subject Grouping: Group subjects based on target grammar's rules
4. ✅ Template Types: Type 1 (full form), Type 2 (aux+verb), Type 3 (aux only)
5. ✅ Level Scaling: Complexity increases with CEFR level
6. ✅ Domain Strategy: One template, one domain, one JSON file
7. ✅ Uniqueness: Meet minimum targets through chunk variety
8. ✅ **Grammar-Agnostic Design:** Auto-detects any blank chunk type (VERB, AUX, MODAL, etc.)

**The Architecture:**
- **Fully grammar-agnostic** - No hardcoded chunk names
- **Auto-detection** - Automatically finds and processes any chunk with the nested structure
- **Flexible object mapping** - Supports `objects`, `article_objects`, `prep_objects`, `items`
- **Future-proof** - Works with any grammar type you create

**The Strategy:**
- 100 domains × 10+ grammars × 3-5 levels = **3000+ unique patterns**
- Each pattern generates 30-500+ unique questions
- Total question bank: **100,000+ questions possible**

**Key Takeaway:**
> **"Same universal principles, different grammars. One template per file, maximum variety through domains. The generator automatically handles VERB, AUX, MODAL, ARTICLE, PREP, or any future grammar type!"**

---

**Version:** 2.0 Grammar-Agnostic
**Date:** 2025-11-09
**Author:** EYESH Question Generator Team
**Major Update:** Fully grammar-agnostic architecture with auto-detection of blank chunks

---

## Quick Reference Tables

### Grammar Subject Grouping Summary

| Grammar | Group A | Group A Form | Group B | Group B Form |
|---------|---------|--------------|---------|--------------|
| Present Simple | I/you/we/they | base | he/she/it | verb-s |
| Past Simple | ALL | past | - | - |
| **Past Continuous** | **you/we/they** | **were + -ing** | **I/he/she/it** | **was + -ing** |
| Present Continuous | I (am), you/we/they (are) | am/are + -ing | he/she/it | is + -ing |
| Present Perfect | I/you/we/they | have + p.p. | he/she/it | has + p.p. |
| Modals | ALL | modal + base | - | - |

### Uniqueness Targets

| Level | Target | Chunks | Items/Chunk |
|-------|--------|--------|-------------|
| A1 | 30-50 | 2-3 | 3-5 |
| A2 | 80-120 | 3-4 | 3-5 |
| B1 | 150-250 | 4-5 | 3-5 |
| B2 | 300-500 | 5-6 | 4-6 |
| C1 | 500+ | 6-7+ | 5+ |

### Pattern Naming

```
{GRAMMAR}_{DOMAIN}_{LEVEL}_{TYPE}

Examples:
PRESENT_SIMPLE_JOURNALISM_B1_TYPE2
PAST_CONTINUOUS_TRAVEL_A2_TYPE2
MODALS_HEALTHCARE_B1_TYPE3
```
