# EYESH Exam Dataset Analysis

> Comprehensive analysis of 5 years of EYESH (English Exam for Secondary and Higher Education) exam data
> Last Updated: 2025-12-27

---

## Dataset Overview

**Location:** `/Users/baky/Documents/edu_mining/question_generator/dataset/`

**Total Files:** 135 exam images

| Year | File Type | Variants | Files | Description |
|------|-----------|----------|-------|-------------|
| 2024 | JPEG | A, B, C, D | 24 | 4 variants with 6 pages each |
| English Series | PNG | A, B, C, D | 32 | 4 variants with 8 pages each |
| Mongolian Series | PNG | A, B, C, D | 48 | 4 variants with 9 pages each |
| 2021 | PNG | All | 16 | All variants combined |
| 2025 | PNG | B, D visible | 15+ | Multiple variant pages |

**Years Covered:** 2021, 2024, 2025 (5+ year span)

**Variants per Year:** 4 (A, B, C, D)

---

## Exam Structure

Each EYESH exam contains **TWO MAIN SECTIONS:**

### Section 1: Grammar (Tasks 1-4)

| Task | Description | Questions | Format |
|------|-------------|-----------|--------|
| Task 1 | Choose the most suitable word to complete sentences | 6 | Multiple choice (A, B, C, D) |
| Task 2 | Choose word/phrase that best completes sentences | 7 | Multiple choice |
| Task 3 | Read conversations and choose appropriate responses | 3 | Multiple choice with 2 extra options |
| Task 4 | Read sentences and transform using KEY WORDS IN BOLD | 2-3 | Word transformation |

### Section 2: Vocabulary (Tasks 1-4)

| Task | Description | Questions | Format |
|------|-------------|-----------|--------|
| Task 1 | Choose correct word to complete sentences | 4 | Multiple choice |
| Task 2 | Choose word with different meanings that fits all gaps | 3 | Gap-fill |
| Task 3 | Find suitable phrases for situations | 2 | Situational matching |
| Task 4 | Choose correct prefix/suffix for collocations | 2 | Word formation |

---

## Grammar Topics Tested in EYESH Exams

### Currently Implemented (11 categories, 530 patterns)

| Grammar | Frequency | Patterns | Coverage |
|---------|-----------|----------|----------|
| Present Simple | High | 50 | A1-C1 |
| Past Simple | High | 50 | A1-C1 |
| Present Continuous | Medium | 50 | A1-C1 |
| Past Continuous | Medium | 50 | A2-C1 |
| Present Perfect | High | 50 | A2-C1 |
| Past Perfect | Medium | 30 | B1-C1 |
| Future Simple | Medium | 50 | A1-C1 |
| Modals | Very High | 50 | A1-C1 |
| Passive Voice | High | 50 | A2-C1 |
| Gerund/Infinitive | High | 40 | A2-C1 |
| Vocabulary Collocations | High | 60 | B1 |

### NOT Implemented (12 categories, 0 patterns)

#### Tier 1: High Frequency in EYESH

| Grammar | Exam Frequency | Recommended | Levels | Example |
|---------|----------------|-------------|--------|---------|
| **Relative Clauses** | Very High | 40 patterns | A2-C1 | "The person ___ helped me was kind." (who) |
| **Reported Speech** | Very High | 40 patterns | B1-C1 | "She said that she ___ to the store." (had gone) |
| **Phrasal Verbs** | Very High | 50 patterns | A2-C1 | "Please turn ___ the light." (off) |
| **Conditional Structures** | High | 40 patterns | B2-C1 | "If I ___ rich, I would travel." (were) |
| **Adjective Order** | High | 30 patterns | B1-B2 | "A ___ ___ jacket" (beautiful leather) |

#### Tier 2: Medium Frequency in EYESH

| Grammar | Exam Frequency | Recommended | Levels | Example |
|---------|----------------|-------------|--------|---------|
| **Prefix/Suffix** | Medium | 40 patterns | B1-C1 | "The ___ of the project" (completion) |
| **Quantifiers** | Medium | 30 patterns | A2-B1 | "There isn't ___ time." (much) |
| **Question Tags** | Medium | 25 patterns | B1-B2 | "You're coming, ___ you?" (aren't) |
| **Emphatic Structures** | Medium | 25 patterns | B2-C1 | "Never ___ I seen this." (have) |

#### Tier 3: Lower Frequency in EYESH

| Grammar | Exam Frequency | Recommended | Levels | Example |
|---------|----------------|-------------|--------|---------|
| **Causatives** | Low | 20 patterns | B2-C1 | "She had her car ___." (repaired) |
| **Participle Clauses** | Low | 20 patterns | B2-C1 | "Running late, she ___." |
| **Cleft Sentences** | Low | 20 patterns | B2-C1 | "What I want ___ a vacation." (is) |

---

## Detailed Grammar Patterns Found in Exams

### 1. Relative Clauses

**Frequency:** Appears in nearly every exam variant

**Types Tested:**
- who (for people): "The teacher who taught us..."
- whom (formal, for people as object): "The person whom I called..."
- which (for things): "The book which I read..."
- that (restrictive, people or things): "The car that we bought..."
- where (for places): "The restaurant where we ate..."
- whose (possession): "The student whose work..."

**Common Errors Tested:**
- who vs. which confusion
- that vs. which usage
- whom vs. who distinction
- Missing or incorrect relative pronoun

### 2. Reported Speech

**Frequency:** Very common, especially in Task 2

**Structures Tested:**
- Statements: "She said (that) she was tired."
- Questions: "He asked if/whether I had finished."
- Commands: "She told him to wait."

**Tense Backshift Rules:**
- Present Simple → Past Simple
- Present Continuous → Past Continuous
- Past Simple → Past Perfect
- Will → Would
- Can → Could
- Must → Had to

### 3. Conditional Structures

**Frequency:** High, especially Types 2 and 3

**Types Tested:**

| Type | Structure | Example |
|------|-----------|---------|
| Type 0 | If + present, present | "If you heat water, it boils." |
| Type 1 | If + present, will + base | "If it rains, I will stay home." |
| Type 2 | If + past, would + base | "If I had money, I would buy a car." |
| Type 3 | If + past perfect, would have + pp | "If I had studied, I would have passed." |
| Mixed | Various combinations | "If I had studied, I would be successful now." |

**Common Errors Tested:**
- would in if-clause
- Incorrect tense in result clause
- Type mixing without context

### 4. Phrasal Verbs

**Frequency:** Very high, appears in multiple tasks

**Categories:**

| Type | Example | Meaning |
|------|---------|---------|
| Separable | turn off, pick up, put on | Object can go between verb and particle |
| Inseparable | look after, get over, run into | Object must follow the whole phrase |
| Three-word | look forward to, put up with | Combination of verb + adverb + preposition |

**Common Phrasal Verbs Tested:**
- look after, look for, look up, look into
- turn on/off, turn up/down, turn out
- give up, give in, give away
- take off, take over, take up
- put off, put on, put up with
- get up, get over, get along with
- break down, break up, break into
- come across, come up with

### 5. Adjective Order

**Frequency:** Medium, often in descriptive contexts

**OSASCOMP Order:**
1. Opinion (beautiful, ugly, nice)
2. Size (big, small, tall)
3. Age (old, new, young)
4. Shape (round, square, flat)
5. Color (red, blue, green)
6. Origin (French, Japanese, American)
7. Material (wooden, plastic, leather)
8. Purpose (sleeping bag, running shoes)

**Example Tested:**
"She wore a beautiful new leather jacket." (Opinion-Age-Material)

### 6. Prefix/Suffix Transformations

**Frequency:** Medium, especially in Task 4 of Vocabulary section

**Common Prefixes:**
- un- (unhappy, uncomfortable, unusual)
- in-/im-/il-/ir- (impossible, illegal, irregular)
- dis- (disagree, disappear, disconnect)
- re- (rewrite, rebuild, reconsider)
- pre- (preview, predict, prevent)
- mis- (misunderstand, misplace, mislead)
- over- (overwork, overcook, overpay)

**Common Suffixes:**
- -tion/-sion (completion, decision)
- -ment (development, improvement)
- -ness (happiness, awareness)
- -ity (possibility, creativity)
- -able/-ible (readable, visible)
- -ful/-less (helpful, hopeless)
- -er/-or (teacher, actor)
- -ly (quickly, carefully)

### 7. Quantifiers & Determiners

**Frequency:** Medium

**Countable vs. Uncountable:**

| Countable | Uncountable |
|-----------|-------------|
| many, few, a few | much, little, a little |
| several, a number of | a great deal of, an amount of |

**Universal:**
- some (positive), any (negative/questions)
- no, none, all, most, half
- both, either, neither (for two)
- every, each (singular)

### 8. Question Tags

**Frequency:** Medium, often in conversational contexts

**Rules:**
- Positive statement → Negative tag: "You are coming, aren't you?"
- Negative statement → Positive tag: "She doesn't like coffee, does she?"
- Imperatives: "Open the door, will you?"
- Let's: "Let's go, shall we?"

**Special Cases:**
- I am → aren't I?
- There is → isn't there?
- This/That is → isn't it?
- Everyone/Someone → they tag

---

## Gap Analysis

### Current Coverage: ~70%

| Category | Status | Gap |
|----------|--------|-----|
| Verb Tenses | Excellent | None |
| Modals | Excellent | None |
| Voice (Active/Passive) | Good | None |
| Non-finite (Gerund/Inf) | Good | None |
| Relative Clauses | Missing | Critical gap |
| Reported Speech | Missing | Critical gap |
| Conditionals (2 & 3) | Missing | Important gap |
| Phrasal Verbs | Missing | Critical gap |
| Word Formation | Missing | Important gap |
| Quantifiers | Missing | Moderate gap |
| Question Tags | Missing | Moderate gap |
| Emphatic Structures | Missing | Minor gap |

### Recommended Implementation Priority

| Priority | Grammar | Impact | Effort |
|----------|---------|--------|--------|
| 1 | Phrasal Verbs | Very High | Medium |
| 2 | Relative Clauses | Very High | Medium |
| 3 | Reported Speech | Very High | High |
| 4 | Conditional Structures | High | Medium |
| 5 | Adjective Order | High | Low |
| 6 | Prefix/Suffix | Medium | Medium |
| 7 | Quantifiers | Medium | Low |
| 8 | Question Tags | Medium | Low |
| 9 | Emphatic Structures | Low | Medium |
| 10 | Causatives | Low | Medium |
| 11 | Participle Clauses | Low | Medium |
| 12 | Cleft Sentences | Low | Medium |

---

## Dataset File Inventory

### 2024 Exam Files (24 files)
```
2024_A_1.jpg - 2024_A_6.jpg (Variant A)
2024_B_1.jpg - 2024_B_6.jpg (Variant B)
2024_C_1.jpg - 2024_C_6.jpg (Variant C)
2024_D_1.jpg - 2024_D_6.jpg (Variant D)
```

### English Series (32 files)
```
English-A (1).png - English-A (8).png (Variant A)
English-B (1).png - English-B (8).png (Variant B)
English-C (1).png - English-C (8).png (Variant C)
English-D (1).png - English-D (8).png (Variant D)
```

### Mongolian Series (48 files)
```
Монгол-A (1).png - Монгол-A (9).png (Variant A, extra page)
Монгол-B (1).png - Монгол-B (9).png (Variant B)
Монгол-C (1).png - Монгол-C (9).png (Variant C)
Монгол-D (1).png - Монгол-D (9).png (Variant D)
```

### 2021 EYESH (16 files)
```
2021 оны ЭЕШ бүх хувилбарууд (1).png - (16).png
```

### 2025 Preview (15+ files)
```
2025 ЭЕШ-B (1).png - 2025 ЭЕШ-B (8).png
2025 ЭЕШ-D (1).png - 2025 ЭЕШ-D (8).png
```

---

## Recommendations

### For Pattern Creation

1. **Prioritize Tier 1 grammars** - These appear in every exam
2. **Use exam examples** - Extract actual question formats from images
3. **Match difficulty levels** - EYESH targets B1-B2 primarily
4. **Include wrong options** - Study the distractor patterns in actual exams
5. **Consider word formation** - Task 4 in Vocabulary section is unique

### For Future Updates

1. Scan new exams as they become available
2. Track grammar frequency changes across years
3. Update pattern priorities based on exam trends
4. Consider adding Reading Comprehension patterns

---

## Notes

- EYESH is a standardized national exam in Mongolia
- Primary target level: B1-B2 (Intermediate to Upper-Intermediate)
- Exam format has remained consistent 2021-2025
- Both English and Mongolian language exams follow same structure
- Grammar section is worth approximately 40% of total score
