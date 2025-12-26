## 1. Overall Design

- Goal: A universal, grammar‑agnostic system that generates English grammar questions across:
  - All main grammar types (tenses, aspects, modals, passive, gerund/infinitive, etc.)
  - All CEFR levels (A1–C1)
  - Many semantic domains (100+)
  - Three template types (full form, aux+verb, aux only)

- Core strategy:
  - One template per file, one domain per file, many variable chunks per template.
  - Generator is grammar‑agnostic: it detects the tested grammar element by structure, not by chunk name.

---

## 2. Core Principles

1. **Grammar‑Focus Principle**
   - The blank (`____`) must test the target grammar point, not vocabulary or collocation choice.
   - Wrong and distractor options must differ grammatically or semantically, not just by lexical choice among equivalent content words.

2. **Context Marker Principle**
   - Every question must contain context markers (time/semantic cues) that make exactly one grammar choice clearly correct.
   - Without such markers, multiple tenses/aspects can be valid; these patterns are invalid.

3. **Answer Option Structure**
   - Each question always has 5 options:
     - 1 correct option: grammatically correct target form
     - 3 wrong forms: grammatically related transformations (wrong tense/aspect/agreement/etc.)
     - 1 distractor: grammatically possible but semantically inappropriate in context
   - Wrong forms must be grammar errors, not nonsense strings.
   - The distractor must not be just another grammatical variant of the same form; it must be a different lexical choice that clashes with the context.

4. **Uniqueness Principle**

   - Uniqueness is the product of the sizes of all variable chunks:
     - `total = |CHUNK1| × |CHUNK2| × ...`
   - Achieve targets by:
     - Adding more chunks (e.g., TIME, PLACE, REASON).
     - Increasing item counts in key chunks (especially SUBJ, VERB, OBJ, TIME).
     - Creating multiple domain‑specific patterns for the same grammar+level.

5. **Subject Grouping Principle**
   - Group subjects by how they behave in the target grammar, not by general intuition.
   - Different grammars require different groupings (see Section 4).

6. **Grammar‑Specific Context Principle**
   - Choose semantic contexts that naturally require the target grammar:
     - Present simple: habits, routines, general truths.
     - Past simple: completed actions at specific past times.
     - Past continuous: actions in progress at a specific past moment or interrupted actions.
     - Present continuous: actions happening now or temporary current situations.
     - Present perfect: past actions with present relevance; “since/for” durations; “ever/never,” “already/yet,” etc.
     - Future (will): future events or decisions, with future time references.
     - Modals: contexts of ability, obligation, advice, or possibility.
     - Gerund/infinitive: verbs that require specific complement types.
     - Passive: when focus is on action/result, not on the agent.

7. **Level Complexity Principle**
   - Increase structural complexity, sub‑grammars, and vocabulary sophistication with CEFR level.

8. **Sentence Structure Diversity Principle**
   - True uniqueness comes from **varied sentence structures**, not just word substitutions.
   - Swapping subjects (I/you/he) or objects creates *combinatorial* variety but not *cognitive* variety.
   - Each grammar + domain should have multiple sentence structure variants:
     - Basic: `{SUBJ} ____ {OBJ} {TIME}.`
     - Fronted time: `{TIME}, {SUBJ} ____ {OBJ}.`
     - With reason: `{SUBJ} ____ {OBJ} because {REASON}.`
     - Conditional: `When {CONDITION}, {SUBJ} ____ {OBJ}.`
     - Relative clause: `{SUBJ} who {RELATIVE} ____ {OBJ}.`
   - A pattern with 4 structure variants × 50 combinations each feels more "unlimited" than 1 structure × 200 word swaps.

9. **Quality Over Quantity Principle**
   - Grammatical correctness and semantic naturalness take priority over hitting uniqueness numbers.
   - A pattern generating 50 truly distinct, natural sentences is better than 500 mechanical variations.
   - For B2/C1 levels, focus on sophisticated structures rather than high combination counts.
   - Every generated sentence should pass the "would a native speaker say this?" test.

---

## 3. Template Types (Work for All Grammars)

Three template types determine what goes in the blank:

1. **Type 1 – Full Target Form**
   - Blank contains the entire structure being tested.
   - Use for:
     - Affirmative sentences.
     - Recognizing tense/aspect.
     - Testing full verb phrase forms (including gerunds/infinitives, modal+verb forms).
   - Example:  
     `{SUBJ} ____ {OBJ} {TIME}.` → `drink/drinks/drank/am drinking/...`

2. **Type 2 – Auxiliary + Main Verb**
   - Blank contains auxiliary + main verb together.
   - Use for:
     - Negatives.
     - Continuous tenses.
     - Perfect tenses.
     - Passive voice.
     - Cases where aux and verb form must be coordinated.
   - Example:  
     `{SUBJ} ____ {OBJ} {MARKER}.` → `doesn't drink/don't drink/didn't drink/isn't drinking`

3. **Type 3 – Auxiliary / Modal Only**
   - Blank contains only the auxiliary or modal; main verb is in the template.
   - Use for:
     - do/does/did; was/were; have/has; modal choice.
     - “Laser‑focus” on auxiliary selection.
   - Example:  
     `{SUBJ} ____ drink coffee {MARKER}.` → `doesn't/don't/didn't`

**Choosing a type:**

- Test complete verb phrase form recognition → Type 1.
- Test aux+verb coordination → Type 2.
- Test only aux/modal choice → Type 3.

---

## 4. Subject & Auxiliary Grouping by Grammar

Use these groupings when defining patterns.

### 4.1 Core Tenses

**Present Simple**

- Affirmative:
  - Group A: I / you / we / they → base verb (eat, drink)
  - Group B: he / she / it / singular nouns → verb‑s (eats, drinks)
- Negative:
  - Group A: I / you / we / they → don’t + base
  - Group B: he / she / it → doesn’t + base

**Past Simple**

- All subjects: past form (visited, worked).
- Negative: all → didn’t + base.

**Present Continuous**

- Group A: I → am + verb‑ing
- Group B: you / we / they → are + verb‑ing
- Group C: he / she / it → is + verb‑ing

**Past Continuous (critical difference from present simple)**

- Group A: you / we / they → were + verb‑ing
- Group B: I / he / she / it → was + verb‑ing

**Present Perfect**

- Group A: I / you / we / they → have + past participle
- Group B: he / she / it → has + past participle

**Past Perfect**

- All subjects: had + past participle.

**Future Simple (will)**

- All subjects: will + base verb.

### 4.2 Modals & Passive

**Modals (can, could, should, must, may, might, would, will as modal)**

- All subjects: modal + base verb (no change by subject).

**Passive Voice**

- Present simple passive:
  - Group A: I / you / we / they → are + past participle
  - Group B: he / she / it → is + past participle
- Past simple passive:
  - Group A: you / we / they → were + past participle
  - Group B: I / he / she / it → was + past participle

---

## 5. Context Markers (Disambiguation)

Always include markers that force a single correct tense/aspect/modal.

### 5.1 Example Marker Types per Grammar

- **Present Simple (habits/facts):**
  - Routines/frequency: every day, every morning, on Mondays, usually, often, always, sometimes, rarely, never.
  - General truths: generally, typically, normally (or no marker for universal facts).
  - Negative state contexts may include “these days,” “nowadays,” etc., when contrasting habits.

- **Past Simple:**
  - Specific past times: yesterday, last week/month/year, two days ago, in 2020, in January, when I was young.

- **Past Continuous:**
  - Specific past moments / interruptions:
    - at 8pm yesterday, at this time last week
    - when you called, when he arrived
    - while I was cooking, during the meeting
    - all day yesterday, all evening

- **Present Continuous:**
  - Ongoing present or temporary:
    - right now, at the moment, currently, today, this week, this month, these days
    - imperative cues: Look!, Listen!

- **Present Perfect:**
  - Past → present relevance / unspecified time:
    - already, yet, just, recently
    - ever, never
    - since + point in time (since 2020)
    - for + duration (for three years)
    - so far, up to now, until now, before

- **Future Simple:**
  - Future time: tomorrow, next week/month/year, soon, later, in five years, in 2030.

- **Modals:**
  - Ability: naturally, well, easily, fluently.
  - Possibility: perhaps, maybe, possibly.
  - Obligation/advice: usually clear from situation; no specific time marker required but semantic context must signal function.

### 5.2 Implementation in Patterns

- Store context markers in dedicated chunks (e.g., `PRESENT_MARKER`, `PAST_MARKER`, `PRESENT_PERFECT_MARKER`) and reference them in templates.
- Ensure the chosen marker makes only one of the answer options (tense/aspect/modal) appropriate.

---

## 6. Level‑Based Complexity & Uniqueness Targets

### 6.1 Complexity by CEFR Level

- **A1**
  - Chunks: 2–3.
  - Sub‑grammars: none.
  - Vocabulary: top ~500 words.
  - Structure: very simple (e.g., `{SUBJ} ____ {OBJ}.`).
  - Uniqueness: 30–50 questions.

- **A2**
  - Chunks: 3–4.
  - Sub‑grammars: 0–1 (often simple prepositions).
  - Vocabulary: ~500–1000.
  - Structures commonly add time/place/frequency: `{SUBJ} ____ {OBJ} {TIME}.`
  - Uniqueness: 80–120.

- **B1**
  - Chunks: 4–5.
  - Sub‑grammars: 1–2 (articles, prepositions, basic clauses).
  - Vocabulary: ~1000–2000.
  - More varied structures (e.g., reasons, ordering of chunks).
  - Uniqueness: 150–250.

- **B2**
  - Chunks: 5–6.
  - Sub‑grammars: 2–3 (e.g., articles, prepositions, relative clauses).
  - Vocabulary: ~2000–3000, more academic/professional.
  - Uniqueness: 300–500.

- **C1**
  - Chunks: 6–7+.
  - Sub‑grammars: 3+ (e.g., conditionals, multiple clauses).
  - Vocabulary: 3000+, advanced domain‑specific.
  - Uniqueness: 500+.

### 6.2 Achieving Targets

- Prefer 3+ items per chunk; more for higher levels.
- Add new chunks as needed (e.g., REASON, RELATIVE_CLAUSE, PREP_PLACE, PREP_TIME).
- Ensure items are semantically diverse, not just synonyms.

### 6.3 Quality-First Approach

> **Important:** These uniqueness numbers are *guidelines*, not hard requirements.

- **Priority order:** Grammatical correctness > Semantic naturalness > Uniqueness count
- For B2/C1: If you can only create 100 truly excellent sentences, that's better than 500 awkward ones.
- Focus on **sentence structure diversity** (multiple template variants) rather than maximizing chunk sizes.
- A single domain with 3-4 different sentence structures provides more learning value than one structure with hundreds of word combinations.

---

## 7. Domain‑Based Pattern Strategy

- Each JSON pattern file targets exactly:
  - one grammar focus,
  - one domain,
  - one CEFR level,
  - one template type,
  - (optionally) one subject group.

- Use domain‑specific vocabulary (subjects, verbs, objects, places, reasons) to:
  - keep content coherent,
  - support semantic pairing of verbs and objects.

- **Pattern ID Convention:**
  - `{GRAMMAR}_{DOMAIN}_{LEVEL}_{TYPE}`  
    Optional subject group suffix if used: `{...}_{GROUP}`.
  - Examples:
    - `PRESENT_SIMPLE_JOURNALISM_B1_TYPE2`
    - `PAST_CONTINUOUS_TRAVEL_A2_TYPE2`
    - `MODALS_HEALTHCARE_B1_TYPE3`

---

## 8. JSON Pattern Specification

### 8.1 Top‑Level Fields (Required Unless Marked Otherwise)

- `pattern_id` (string): Unique ID following naming convention.
- `focus` (string): Grammar point tested (e.g., `present_simple_negative`).
- `level` (string): `A1`–`C1`.
- `domain` (string): Semantic domain (e.g., `journalism`).
- `category` (string): `"grammar"`.
- `template_type` (string): `"type_1" | "type_2" | "type_3"`.
- `subject_group` (string, optional): e.g., `"group_a"` or `"group_b"` if you split patterns by subject grouping.
- `sub_grammar` (array, optional): Any additional grammar aspects (e.g., `["articles", "prepositions"]`).
- `template` (string): Text with placeholders and a single `____` blank.
- `example` (string): Example question generated by this pattern.
- `explanation` (string): Brief learner‑friendly explanation of the grammar rule and its use in the pattern.
- `chunks` (object): Definitions of variable components (see below).

### 8.2 Template & Placeholders

- Exactly one blank (`____`) per template; it corresponds to one “blank chunk” in `chunks`.
- Placeholders in curly braces must match chunk names or mapped object placeholders:
  - Common placeholders:
    - `{SUBJ}`, `{OBJ}`, `{ARTICLE_OBJ}`, `{PREP_OBJ}`, `{TIME}`, `{FREQUENCY}`, `{PLACE}`, `{REASON}`, `{RELATIVE_CLAUSE}`, `{PREP_TIME}`, `{PREP_PLACE}`, etc.
- **Standardization requirement:**
  - Use `{OBJ}` for generic objects; do not introduce custom placeholders like `{ACTIVITY}`, `{PHRASE}`, `{ITEM}`.
  - Objects that need an article+object bundle should use `{ARTICLE_OBJ}`.
  - Objects that include a preposition+object combination should use `{PREP_OBJ}`, `{PREP_TIME}`, or `{PREP_PLACE}`.

### 8.3 Blank Chunk (the Tested Grammar Element)

- The generator automatically identifies the blank chunk as any chunk whose items have the **nested answer structure** below.

**Structure for each item in the blank chunk (e.g., in `VERB`, `AUX`, `MODAL`, `ARTICLE`, `PREP`):**

- `correct_forms` (array, required): one or more correct strings for the blank.
- `wrong_forms` (array of exactly 3 strings, required):
  - Each is a grammatically formed alternative that is incorrect for this context (wrong tense/aspect/agreement/etc.).
- One of these optional object arrays (can be empty `[]`):
  - `objects`: general objects; maps to `{OBJ}`.
  - `article_objects`: article+object phrases; maps to `{ARTICLE_OBJ}`.
  - `prep_objects`: preposition+object phrases; maps to `{PREP_OBJ}`.
  - `items`: generic list; treated as `{OBJ}`.
- `distractor` (string, required):
  - A single grammatically possible but semantically inappropriate option.

**Mandatory constraints:**

- Exactly 3 items in `wrong_forms`; no more, no fewer.
- Exactly one chunk in `chunks` must use this nested structure (the blank chunk).
- No extra or obsolete fields like `phrases`, `bases`, `context_distractors`, `wrong_collocations`, `activities`, `places`, etc.

**Grammar‑agnostic behavior:**

- The generator:
  - Scans `chunks` to find any chunk whose items have `correct_forms`, `wrong_forms`, and `distractor`.
  - Treats that chunk as the blank source, regardless of its name (`VERB`, `AUX`, `MODAL`, `ARTICLE`, `PREP`, etc.).
  - Builds 5 answer options: 1 from `correct_forms`, 3 from `wrong_forms`, 1 from `distractor`.

### 8.4 Object Handling and Semantic Pairing

**Semantic Pairing Principle**

- Use nested object arrays in the blank chunk (e.g., under each verb) to ensure only natural verb–object combinations are generated.
- Do **not** create separate object chunks that would mix incompatible items.

**Rules:**

- If blank items define:
  - `objects`: do **not** define a separate `OBJ` chunk.
  - `article_objects`: do **not** define a separate `ARTICLE_OBJ` chunk.
  - `prep_objects`: do **not** define a separate `PREP_OBJ` or conflicting time/place chunk.
- The generator:
  - If `{OBJ}` (or `{ARTICLE_OBJ}`, `{PREP_OBJ}`) appears in the template and the blank item has corresponding objects, it chooses an appropriate one from that nested array.
  - If no `{OBJ}`‑style placeholder is used, it can still automatically append object text after the blank when configured to do so, but you must be consistent.
- Redundant chunks (both nested objects in the blank and a separate OBJ/ARTICLE_OBJ chunk) cause semantic mismatches and must be avoided.

### 8.5 Non‑Blank Chunks (Context & Structure)

- Simple array chunks with no nested answer structure, e.g.:
  - `SUBJ`: subject pronouns or domain nouns.
  - `TIME` / `PRESENT_MARKER` / `PAST_MARKER` / `PRESENT_PERFECT_MARKER`: time expressions.
  - `FREQUENCY`: often, usually, always, etc.
  - `PLACE` / `PREP_PLACE`: location expressions.
  - `REASON`, `RELATIVE_CLAUSE`, etc., for added complexity.

- Combined chunks (when grammar and lexis are tightly coupled):
  - `ARTICLE_OBJ`: article + noun together, when article choice depends on the noun.
  - `PREP_TIME`: preposition + time expression.
  - `PREP_PLACE`: preposition + place expression.

### 8.6 Recognized Object Field Names

- Valid object field names (inside blank items):
  - `objects` → `{OBJ}`
  - `article_objects` → `{ARTICLE_OBJ}`
  - `prep_objects` → `{PREP_OBJ}`
  - `items` → `{OBJ}`
- Any other field name (e.g., `activities`, `places`) is ignored by the generator and must not be used.

---

## 9. Answer Option Generation Rules

For each generated question:

- 1 correct option: one string from `correct_forms`.
- 3 wrong options: each one string from `wrong_forms[0..2]`.
- 1 distractor: the `distractor` string.

Constraints:

- Wrong options must be **grammatical** transformations related to the target form (wrong tense/aspect/agreement, different auxiliary, etc.).
- The distractor:
  - Must be grammatically possible in general but semantically wrong in the context (e.g., different verb incompatible with the object or situation).
  - Must **not** duplicate or overlap with a wrong form.

---

## 10. Grammar‑Specific Guidelines

Below: key design decisions per grammar type. They build on the subject grouping and context marker rules already given.

### 10.1 Present Simple

- Subject Grouping: as in Section 4 (Group A: I/you/we/they; Group B: he/she/it).
- Types:
  - Type 1: Affirmatives (full verb form).
  - Type 2: Negatives with aux+verb.
  - Type 3: aux‑only negatives (don’t/doesn’t).
- Context: habits, routines, general truths; frequency/time markers.
- Common distractor patterns for wrong forms:
  - wrong_conjugation (drinks instead of drink with I/you/we/they),
  - past_simple (drank),
  - present_continuous (am drinking / is drinking),
  - future_simple (will drink).

### 10.2 Past Simple

- Subject Grouping: all subjects use the same past form; negative uses didn’t + base.
- Types:
  - Type 1: Affirmatives.
  - Type 2: Negatives with didn’t + base.
  - Type 3: aux‑only (didn’t vs doesn’t).
- Context: specific past time markers.
- Distractor patterns:
  - present_simple, present_perfect, past_continuous forms.

### 10.3 Past Continuous

- Subject Grouping:
  - Group A: you / we / they → were + ‑ing
  - Group B: I / he / she / it → was + ‑ing
- Types:
  - Type 1: full form.
  - Type 2: aux + verb‑ing.
  - Type 3: aux‑only (was/were vs others).
- Context: specific past moment, interrupted actions (“at 8pm yesterday”, “when you called”, “while…”).
- Distractor patterns:
  - wrong auxiliary (was/were swapped),
  - past_simple,
  - present_continuous,
  - present_perfect_continuous.

### 10.4 Present Continuous

- Subject Grouping: I (am), you/we/they (are), he/she/it (is).
- Types:
  - Type 1: full form.
  - Type 2: aux + verb‑ing.
  - Type 3: aux‑only (is/are/am vs others).
- Context: right now, at the moment, currently, today/this week.
- Distractor patterns:
  - wrong auxiliary,
  - present_simple,
  - past_continuous.

### 10.5 Present Perfect

- Subject Grouping:
  - Group A: I / you / we / they → have + p.p.
  - Group B: he / she / it → has + p.p.
- Types:
  - Type 1: full form.
  - Type 2: aux + past participle.
  - Type 3: aux‑only (have/has/had).
- Context: before, already, yet, just, recently, ever, never, since, for, so far.
- Distractor patterns:
  - wrong auxiliary (has vs have),
  - past_simple,
  - past_perfect,
  - present_continuous/present_perfect_continuous where appropriate.

### 10.6 Past Perfect

- Subject Grouping: all subjects use had + past participle.
- Typically tested similarly to present perfect but contrasted with other past forms.

### 10.7 Future Simple (will)

- Subject Grouping: all → will + base.
- Use clear future time markers.
- Distractors can use present simple, going to, or other modals, depending on focus.

### 10.8 Modals

- Subject Grouping: same for all subjects (no conjugation).
- Types:
  - Type 1: modal + verb in blank.
  - Type 3: modal only with base verb in template.
- Context:
  - Ability: “well/easily/fluently”.
  - Obligation: context requiring strong/weak obligation.
  - Advice: suggestions.
  - Possibility: maybe, perhaps, possibly.
- Distractor design:
  - Use contrasting modals based on meaning function (e.g., should vs must vs can vs might).

### 10.9 Gerund vs Infinitive

- Focus: verbs that require particular complements (enjoy + gerund, want + infinitive, etc.).
- Typically Type 1: entire complement phrase in blank.
- Context: determined by the controlling verb; no specific time marker required.
- Distractor patterns:
  - to_infinitive vs gerund vs bare_infinitive vs conjugated forms,
  - ensure exactly 3 wrong complement forms plus one semantic distractor where appropriate.

### 10.10 Passive Voice

- Grouping: as in Section 4 (by tense and subject).
- Types:
  - Usually Type 2: be‑auxiliary + past participle in blank.
- Context: time markers appropriate to the passive tense chosen.
- Distractor patterns:
  - wrong auxiliary (was/were/is/are/has been),
  - active voice forms,
  - wrong tense.

---

## 11. Pattern Creation Workflow

Use this condensed workflow:

1. **Select Grammar + Domain + Level**
   - Choose precise grammar focus (e.g., `present_simple_negative`), domain (e.g., journalism), and CEFR level.

2. **Determine Subject Grouping**
   - Apply the correct grouping for the chosen grammar.
   - Create separate patterns/subject_group values if needed (e.g., Group A vs Group B).

3. **Choose Template Type**
   - Decide whether to test:
     - full structure (Type 1),
     - aux+verb coordination (Type 2),
     - aux/modal only (Type 3).

4. **Design Template with Context Markers**
   - Include at least one marker that disambiguates the target grammar (time adverbials, semantic cues).

5. **Gather Domain‑Specific Vocabulary**
   - Select realistic subjects, verbs, and objects relevant to the domain.
   - Plan verb‑specific object lists for semantic pairing.

6. **Define Blank Chunk**
   - Implement nested structure with `correct_forms`, `wrong_forms` (exactly 3), object field(s), and `distractor`.
   - Choose wrong_forms according to recommended distractor methods for the grammar.

7. **Define Other Chunks**
   - Add SUBJ, TIME, PLACE, FREQUENCY, REASON, etc., ensuring:
     - no redundant OBJ/ARTICLE_OBJ/PREP_OBJ chunk if objects are nested in the blank chunk,
     - at least 3 items where possible.

8. **Check Uniqueness**
   - Compute the product of chunk sizes.
   - Compare against level target; adjust chunks/items if needed.

9. **Validate Structure**
   - Ensure:
     - Single blank chunk with nested structure.
     - Template placeholders match chunk names and standard object placeholders.
     - No obsolete/custom field names.
     - Pattern ID follows convention.

10. **Test Generate and Review**
    - Generate sample questions.
    - Verify:
      - Only one option is clearly correct.
      - All sentences are grammatical and natural.
      - Distractors are plausible but clearly wrong semantically.

---

## 12. Best Practices & Common Mistakes

### 12.1 Best Practices / Checklist

- **Before building:**
  - Clearly define grammar focus, domain, level, and subject grouping.
  - Decide template type (1, 2, or 3).

- **While building:**
  - Always include context markers to force a single correct answer.
  - Use at least 3 variable chunks; each chunk ideally ≥3 items.
  - Use domain‑appropriate vocabulary.
  - Use nested objects on the blank chunk for semantic pairing.
  - For each blank item:
    - provide `correct_forms`,
    - exactly 3 `wrong_forms`,
    - a single `distractor`,
    - an appropriate object field (even if empty).
  - Write a clear `explanation` for learners.

- **After building:**
  - Validate JSON syntax.
  - Confirm pattern_id format.
  - Recompute uniqueness.
  - Manually review several generated questions for grammaticality and naturalness.

### 12.2 Common Mistakes to Avoid (with Fixes)

1. **Wrong Subject Grouping**
   - Past continuous: do **not** group I with you/we/they; I goes with he/she/it under “was + ‑ing”.

2. **Missing Context Markers**
   - Templates like “She ____ coffee.” allow multiple tenses; always add clear time/semantic markers.

3. **Testing Vocabulary Instead of Grammar**
   - Avoid blanks where all options are different content words (e.g., nouns) and only one fits by meaning; blank must target the grammar structure.

4. **Insufficient Uniqueness**
   - If total combinations are below the level target:
     - add chunks (e.g., TIME, PLACE),
     - or increase items per chunk.

5. **Unnatural Verb‑Object Combinations**
   - Don’t use a separate OBJ chunk if the blank chunk already holds verb‑specific `objects`—this causes mismatches.
   - Always use nested objects to control semantic pairings.

6. **Redundant Chunks**
   - Do not define both:
     - nested `objects` in the blank chunk, and
     - separate `OBJ` (or `ARTICLE_OBJ`, `PREP_OBJ`) chunks.

7. **Non‑Standard Field Names**
   - Do not use `activities`, `places`, `phrases`, etc., as object fields.
   - Always use `objects`, `article_objects`, `prep_objects`, or `items`.

8. **Custom Placeholder Names in Template**
   - Avoid `{ACTIVITY}`, `{PHRASE}`, `{ITEM}`, etc.
   - Always use standardized placeholders (`{OBJ}`, `{ARTICLE_OBJ}`, `{PREP_OBJ}`, etc.) that the generator can map.

9. **Old Structure Format**
   - Do not use:
     - `phrases`, `bases`, `context_distractors`, etc.
   - Replace with:
     - `correct_forms`, `wrong_forms`, appropriate object field, and `distractor`.

10. **Wrong Number of `wrong_forms`**
    - Must be exactly three. Not two, not four.

11. **Poor Distractors**
    - Avoid:
      - adding an adverb to the correct verb as distractor (e.g., “practice daily”),
      - using a grammatical error as distractor (should be in `wrong_forms` if used at all).
    - Use semantically incompatible verbs or actions that make sense in isolation but clash with the given object/marker.
    - Adjust sophistication by level (simpler opposites at A1–A2, more nuanced or advanced verbs at B1–C1).

12. **Missing `{OBJ}` When Objects Are Defined**
    - If the blank item has `objects` and you want them visible in the sentence, include `{OBJ}` (or equivalent) in the template and do not duplicate them in a separate OBJ chunk.

---

## 13. Quick Reference Tables

### 13.1 Subject Grouping Summary

| Grammar              | Group A Subjects     | Group A Form            | Group B Subjects     | Group B Form            |
|----------------------|----------------------|-------------------------|----------------------|-------------------------|
| Present Simple       | I/you/we/they        | base verb               | he/she/it            | verb‑s                  |
| Past Simple          | ALL                  | past form               | –                    | –                       |
| Present Continuous   | I                    | am + ‑ing              | you/we/they          | are + ‑ing             |
|                      |                      |                         | he/she/it            | is + ‑ing              |
| Past Continuous      | you/we/they          | were + ‑ing            | I/he/she/it          | was + ‑ing             |
| Present Perfect      | I/you/we/they        | have + past participle  | he/she/it            | has + past participle   |
| Past Perfect         | ALL                  | had + past participle   | –                    | –                       |
| Future (will)        | ALL                  | will + base             | –                    | –                       |
| Modals               | ALL                  | modal + base            | –                    | –                       |
| Pres. Simple Passive | I/you/we/they        | are + past participle   | he/she/it            | is + past participle    |
| Past Simple Passive  | you/we/they          | were + past participle  | I/he/she/it          | was + past participle   |

### 13.2 Uniqueness Targets by Level

| Level | Min. Questions | Typical Chunks | Typical Items/Chunk |
|-------|----------------|----------------|---------------------|
| A1    | 30–50          | 2–3            | 3–5                 |
| A2    | 80–120         | 3–4            | 3–5                 |
| B1    | 150–250        | 4–5            | 3–5                 |
| B2    | 300–500        | 5–6            | 4–6                 |
| C1    | 500+           | 6–7+           | 5+                  |