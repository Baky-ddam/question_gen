# Grammar Coverage Status

> Last Updated: 2025-12-27

## Quick Status

### Completed Grammars (770 patterns)

| Grammar | Status | Patterns | Levels | Quality |
|---------|--------|----------|--------|---------|
| Present Simple | COMPLETE | 50 | A1-C1 | Validated |
| Past Simple | COMPLETE | 50 | A1-C1 | Created |
| Present Continuous | COMPLETE | 50 | A1-C1 | Validated |
| Past Continuous | COMPLETE | 50 | A1-C1 | Created |
| Present Perfect | COMPLETE | 50 | A1-C1 | Created |
| Past Perfect | COMPLETE | 30 | B1-C1 | Created |
| Future Simple | COMPLETE | 50 | A1-C1 | Created |
| Modals | COMPLETE | 50 | A1-C1 | Created |
| Passive Voice | COMPLETE | 50 | A2-C1 | Created |
| Gerund/Infinitive | COMPLETE | 40 | A2-C1 | Created |
| Phrasal Verbs | COMPLETE | 50 | A2-C1 | Created |
| Relative Clauses | COMPLETE | 40 | A2-C1 | Created |
| Reported Speech | COMPLETE | 40 | B1-C1 | Created |
| Conditional Structures | COMPLETE | 40 | B2-C1 | Created |
| Adjective Order | COMPLETE | 30 | B1-B2 | Created |
| Word Formation | COMPLETE | 40 | B1-C1 | Created |
| Vocabulary | COMPLETE | 60 | B1 | Validated |

### Planned Grammars - EYESH Gap (380 patterns)

| Grammar | Status | Target | Levels | Priority |
|---------|--------|--------|--------|----------|
| Relative Clauses | COMPLETE | 40 | A2-C1 | Tier 1 |
| Reported Speech | COMPLETE | 40 | B1-C1 | Tier 1 |
| Conditional Structures | COMPLETE | 40 | B2-C1 | Tier 1 |
| Phrasal Verbs | COMPLETE | 50 | A2-C1 | Tier 1 |
| Adjective Order | COMPLETE | 30 | B1-B2 | Tier 1 |
| Prefix/Suffix | COMPLETE | 40 | B1-C1 | Tier 2 |
| Quantifiers | NOT STARTED | 30 | A2-B1 | Tier 2 |
| Question Tags | NOT STARTED | 25 | B1-B2 | Tier 2 |
| Emphatic Structures | NOT STARTED | 25 | B2-C1 | Tier 2 |
| Causatives | NOT STARTED | 20 | B2-C1 | Tier 3 |
| Participle Clauses | NOT STARTED | 20 | B2-C1 | Tier 3 |
| Cleft Sentences | NOT STARTED | 20 | B2-C1 | Tier 3 |

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

### Present Continuous (COMPLETE)

**Priority:** 2

**Subject Grouping:**
- Group A: I -> am + verb-ing
- Group B: you/we/they -> are + verb-ing
- Group C: he/she/it -> is + verb-ing

**Context Markers:** right now, at the moment, currently, now, Look!

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness |
|-------|----------|---------|------------|
| A1 | 10 | cooking, home, family, shopping, pets | 276 |
| A2 | 10 | hobbies, fitness, outdoor_activities, wellness, training | 108-576 |
| B1 | 10 | research, history, psychology, writing, theater | 64-1024 |
| B2 | 10 | journalism, engineering, marketing, software, data_science | 300-500+ |
| C1 | 10 | climate, conservation, cybersecurity, urban_life, logistics | 500+ |

**Template Types Used:**
- Type 1 (Full form with context markers): 50 patterns
- Template complexity increases with level (A1: simple SVO, C1: multi-clause structures)

**Location:** `pattern/present_continuous/`

---

### Past Continuous (COMPLETE)

**Status:** 50 patterns created

**Subject Grouping (CRITICAL - different from present simple):**
- Group A: you/we/they --> were + verb-ing
- Group B: I/he/she/it --> was + verb-ing

**Context Markers:** at [time] yesterday, when [event], while, during, all day

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness |
|-------|----------|---------|------------|
| A1 | 10 | playground, classroom, kitchen, park, bedroom | 80-120 each |
| A2 | 10 | restaurants, hotels, driving, nightlife, tourism | 144 each (1440 total) |
| B1 | 10 | healthcare, events, volunteering, media, culture | 150+ each |
| B2 | 10 | aviation, maritime, infrastructure, automation, immigration | 300-500+ each |
| C1 | 10 | philosophy, sociology, demographics, physics, agriculture | 500+ each |

**Template Types Used:**
- Type 1 (Full form with context markers): 50 patterns
- A1 Templates: `{SUBJ} ____ {OBJ} {TIME}.` (simple past time reference)
- A2 Templates: `{SUBJ} ____ {OBJ} {TIME}.`, `{SUBJ} ____ {OBJ} when {INTERRUPTION}.`, `At {TIME}, {SUBJ} ____ {OBJ}.`
- C1 Templates (sophisticated multi-clause structures):
  - `While {SUBJ} ____ {OBJ}, {CONTRAST_ACTION}.`
  - `{SUBJ} ____ {OBJ} {PLACE}, a situation that {BROADER_IMPLICATION}.`
  - `Given that {CONTEXT}, {SUBJ} ____ {OBJ} when {CRITICAL_MOMENT}.`
  - `As {SUBJ} ____ {OBJ}, {UNEXPECTED_DEVELOPMENT}, thereby {CONSEQUENCE}.`
- B1 Templates (sophisticated structures):
  - `{SUBJ} ____ {OBJ} when {INTERRUPTION}.` (interruption pattern)
  - `While {SUBJ} ____ {OBJ}, {PARALLEL_ACTION}.` (parallel actions)
  - `{TIME}, {SUBJ} ____ {OBJ} because {REASON}.` (time + reason)
  - `{TIME}, {SUBJ} ____ {OBJ}.` (time reference)
  - `{SUBJ} ____ {OBJ} while {SOMEONE_ELSE} {PARALLEL}.` (parallel with while)
- B2 Templates (complex professional structures):
  - `{SUBJ} ____ {OBJ} {PREP_PLACE} when {INTERRUPTION}, which {CONSEQUENCE}.`
  - `{SUBJ} ____ {OBJ} all {DURATION} because {REASON}.`
  - `While {SUBJ} ____ {OBJ} {PLACE}, {COMPLEX_EVENT} occurred.`

**Location:** `pattern/past_continuous/`

---

### Present Perfect (COMPLETE)

**Status:** 50 patterns created

**Subject Grouping:**
- Group A: I/you/we/they --> have + past participle
- Group B: he/she/it --> has + past participle

**Context Markers:** already, yet, just, ever, never, since, for, recently, before

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness |
|-------|----------|---------|------------|
| A1 | 10 | animals, toys, snacks, places, activities | 80-120 each |
| A2 | 10 | travel, food, entertainment, sports, technology | 80-120 each |
| B1 | 10 | career, education, relationships, health, hobbies | 150-250 each |
| B2 | 10 | finance, real_estate, research, management, innovation | 300-500+ each |
| C1 | 10 | diplomacy, academia, biotechnology, economics, environmental_policy | 500+ each |

**Template Types Used:**
- A1 Templates:
  - `{SUBJ} ____ {OBJ} before.` (simple experience pattern)
- A2 Templates:
  - `{SUBJ} ____ {OBJ} {EXPERIENCE_MARKER}.` (experience pattern)
  - `{SUBJ} ____ already {OBJ}.` (completion pattern)
  - `{SUBJ} ____ just {OBJ}.` (recent action pattern)
  - `{SUBJ} ____ recently {OBJ}.` (recent discovery pattern)
- B1 Templates:
  - `{SUBJ} ____ {OBJ} {DURATION}.` (duration pattern with for/since)
  - `{SUBJ} ____ {OBJ} since {SINCE_EVENT}.` (since pattern)
  - `{SUBJ} ____ {COMPLETION_MARKER} {OBJ}.` (completion pattern)
- B1-level distractors: abandon, demolish, neglect, overlook, dismiss, postpone, cancel, terminate
- B2 Templates (sophisticated structures):
  - `{SUBJ} ____ {OBJ}, so {RESULT}.` (result clause)
  - `{SUBJ} ____ {OBJ} since {SINCE_CLAUSE}.` (complex since clause)
  - `{SUBJ} ____ {OBJ}, which {CONSEQUENCE}.` (relative clause consequence)
- B2-level distractors: disregard, overlook, suppress, undermine, circumvent, obstruct, impede, hinder
- C1 Templates (highly sophisticated multi-clause structures):
  - `{SUBJ} ____ {OBJ}, which {IMPACT}.` (achievement with impact clause)
  - `Never before ____ {SUBJ} {OBJ}.` (emphatic inversion structure)
  - `{SUBJ} ____ {OBJ} {PLACE}, a development that {IMPLICATION}.` (appositive implication)
- C1-level distractors: forsake, obliterate, renounce, repudiate, nullify, abrogate, rescind, countermand

**Location:** `pattern/present_perfect/`

---

### Future Simple (COMPLETE)

**Priority:** 6

**Subject Grouping:** Single group "all" (all subjects use 'will + base verb')

**Context Markers:** tomorrow, next week, next month, next year, soon, later, probably

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness |
|-------|----------|---------|------------|
| A1 | 10 | weather, birthdays, meals, school_plans, weekend, movies, games, visits, parties, vacations | 200+ each |
| A2 | 10 | appointments, celebrations, schedules, goals, seasons, holidays, plans, errands, meetings, trips | 300+ each |
| B1 | 10 | exams, projects, savings, habits, skills, decisions, changes, opportunities, challenges, milestones | 400+ each |
| B2 | 10 | markets, trends, strategies, investments, regulations, innovations, expansions, partnerships, forecasts, developments | 500+ each |
| C1 | 10 | geopolitics, climate_policy, technological_disruption, demographic_shifts, economic_reform, scientific_breakthroughs, institutional_change, global_trade, energy_transition, societal_transformation | 600+ each |

**Template Types Used:**
- A1: `{SUBJ} ____ {OBJ} {FUTURE_TIME}.` (basic future)
- A2: `{SUBJ} ____ probably {OBJ} {FUTURE_TIME}.` / `{SUBJ} ____ {OBJ} {FUTURE_TIME} {PLACE}.`
- B1: `If {CONDITION}, {SUBJ} ____ {OBJ}.` / `When {TRIGGER}, {SUBJ} ____ {OBJ}.`
- B2: `{SUBJ} ____ {OBJ} because {REASON}.` / `By {FUTURE_TIME}, {SUBJ} ____ {OBJ}.`
- C1: `Experts predict that {SUBJ} ____ {OBJ} as {TREND}.`

**Wrong Forms:**
- Present simple (base verb): "visit" instead of "will visit"
- Going to: "is going to visit" instead of "will visit"
- Would: "would visit" instead of "will visit"

**Distractors by Level:**
- A1: stop, avoid, ignore, forget, cancel, lose
- A2: quit, skip, waste, refuse, abandon, neglect
- B1: abandon, neglect, overlook, dismiss, postpone, cancel
- B2: disregard, suppress, undermine, circumvent, obstruct, impede
- C1: forsake, obliterate, renounce, repudiate, nullify, abrogate

**Location:** `pattern/future_simple/`

---

### Past Perfect (COMPLETE)

**Status:** 30 patterns created (B1-C1 only - too complex for A1/A2)

**Subject Grouping:** Single group "all" (all subjects use 'had' + past participle)

**Context Markers:** before, by the time, after, until, when, already, just, never...before

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness |
|-------|----------|---------|------------|
| B1 | 10 | school, cooking, travel, shopping, work, exercise, reading, cleaning, studying, appointments | 150-250 each |
| B2 | 10 | business, projects, negotiations, research, events, investments, careers, deadlines, meetings, presentations | 300-500+ each |
| C1 | 10 | diplomacy, economics, policy, science, law, technology, history, philosophy, strategy, medicine | 500+ each |

**Template Types Used:**
- B1: `{SUBJ} ____ {OBJ} before {PAST_EVENT}.` (sequence before past event)
- B2: `By the time {PAST_EVENT}, {SUBJ} ____ {OBJ}.` (by the time emphasis)
- B2: `After {SUBJ} ____ {OBJ}, {SUBSEQUENT_ACTION}.` (after sequence)
- C1: `If {SUBJ} ____ {OBJ}, {RESULT_CLAUSE}.` (third conditional)
- C1: `{SUBJ} ____ never {OBJ} until {PAST_EVENT}.` (never before pattern)

**Wrong Forms:**
- have/has + past participle (present perfect confusion)
- past simple (e.g., "finished" instead of "had finished")
- past continuous (e.g., "was finishing" instead of "had finished")

**Distractors by Level:**
- B1: abandon, neglect, skip, forget, cancel, overlook
- B2: forfeit, discard, withhold, dismiss, concentrate, fragment
- C1: sever, repeal, falsify, endorse, relinquish, obscure

**Location:** `pattern/past_perfect/`

---

### Modals (COMPLETE)

**Priority:** 5

**Types:** can, could, should, must, may, might, would, will

**Subject Grouping:** Single group "all" (no conjugation - all subjects use same modal form)

**Context Markers:** Semantic (ability, obligation, advice, possibility)

**Coverage by Level:**
| Level | Patterns | Domains | Uniqueness |
|-------|----------|---------|------------|
| A1 | 10 | languages, sports, swimming, music, art, cooking, driving, reading, computers, daily_skills | 80-120 each |
| A2 | 10 | language_skills, parking, photography, shopping, library, gym, office, restaurant, museum, park | 96 each |
| B1 | 10 | fitness, study, work, relationships, finance (should), workplace, safety, legal, school, travel (must) | 288 each |
| B2 | 10 | project_management, market, weather, career, technology, health, economy, negotiations, research, investment | 576 each |
| C1 | 10 | policy, diplomacy, scientific_research, global_economics, environmental, healthcare_policy, education_reform, technology_ethics, international_law, social_policy | 500+ each |

**A2 Template Types Used:**
- `{SUBJ} ____ {OBJ} {ADVERB}.` (ability with adverb: "She can speak English well.")
- `{SUBJ} ____ {OBJ} {LOCATION}.` (permission: "You can park here.")

**A2 Wrong Forms:**
- "could" (past/tentative)
- "must" (obligation)
- "should" (advice)

**A2-level distractors:** quit, skip, destroy, waste, reject, refuse, abandon, neglect

**B1 Template Types Used:**
- `{SUBJ} ____ {OBJ} {PURPOSE}.` (advice: "You should exercise regularly to stay healthy.")
- `{SUBJ} ____ {OBJ} {REQUIREMENT}.` (obligation: "Employees must wear badges at all times.")

**B1 Focus:** modal_should (advice) and modal_must (obligation)

**B1 Wrong Forms:**
- For "should": must (stronger), can (ability), could (tentative)
- For "must": should (weaker), can (ability), have to (alternative)

**B1-level distractors:** abandon, demolish, neglect, overlook, dismiss, postpone, cancel, terminate

**B2 Template Types Used:**
- `{SUBJ} ____ {OBJ} if {CONDITION}.` (possibility with condition: "The project might succeed if we secure funding.")
- `{SUBJ} ____ {OBJ} because {REASON}.` (speculation with reason: "The stock prices may rise because investor confidence is growing.")
- `{SUBJ} ____ {OBJ}, which {CONSEQUENCE}.` (possibility with consequence: "The weather might change suddenly, which could disrupt outdoor activities.")

**B2 Focus:** modal_might, modal_may, modal_could (possibility/speculation)

**B2 Wrong Forms:**
- For "might": will (certainty), can (ability), should (advice)
- For "may": will (certainty), must (obligation), can (ability)
- For "could": can (present), would (conditional), should (advice)

**B2-level distractors:** disregard, overlook, suppress, undermine, circumvent, obstruct, impede, hinder

**C1 Template Types Used:**
- `{SUBJ} ____ {OBJ}, which {IMPLICATION}.` (speculation with implication: "The proposed legislation could transform the regulatory landscape, which would reshape public discourse for decades.")
- `While {CONTRAST}, {SUBJ} ____ {OBJ}.` (obligation with contrast: "While geopolitical tensions continue to escalate, diplomatic envoys must negotiate comprehensive peace accords.")
- `{SUBJ} ____ {OBJ} {CONTEXT}, a possibility that {BROADER_IMPACT}.` (possibility with broader impact: "The research team might discover novel molecular mechanisms through rigorous empirical analysis, a possibility that could fundamentally reshape scientific understanding.")

**C1 Focus:** modal_speculation, modal_obligation, modal_possibility (could/might/must/should/may)

**C1 Wrong Forms:**
- Conjugated modals (e.g., "could transforms", "might resolves")
- Progressive modals (e.g., "might discovering", "could negotiating")
- Past participle modals (e.g., "should addressed", "could implemented")

**C1-level distractors:** forsake, obliterate, renounce, repudiate, nullify, abrogate, rescind, countermand

**Location:** `pattern/modals/`

---

### Passive Voice (COMPLETE)

**Status:** 50 patterns created (A2-C1)

**Tense Variants:**
- Past Passive (was/were + pp) - A2, B1
- Present Passive (is/are + pp) - B2
- Present Perfect Passive (has been/have been + pp) - C1

**Subject Grouping:**
- Group A: you/we/they (and plurals) → are/were/have been + pp
- Group B: I/he/she/it (and singulars) → is/was/has been + pp

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| A2 | 10 | inventions, buildings, books, movies, food | Past passive (was/were) |
| B1 | 20 | reports, products, artworks, music, events, sports, news, construction, awards, decisions | Past passive with agent |
| B2 | 10 | environment, technology, healthcare, education, business | Present passive with reason |
| C1 | 10 | legislation, research, global_affairs, infrastructure, finance | Present perfect passive with purpose |

**Template Types:**
- A2: `{SUBJ} ____ {TIME}.` (basic passive)
- B1: `{SUBJ} ____ by {AGENT}.` (passive with agent)
- B2: `{SUBJ} ____ because {REASON}.` (passive with reason)
- C1: `{SUBJ} ____ by {AGENT} to {PURPOSE}.` (complex passive)

**Wrong Forms:**
- Wrong auxiliary (was vs were, is vs are, has been vs have been)
- Wrong tense (present for past, past for present perfect)
- Active form confusion

**Location:** `pattern/passive_voice/`

---

### Gerund/Infinitive (COMPLETE)

**Status:** 40 patterns created (A2-C1)

**Subject Grouping:**
- Group A: I/you/we/they --> base main verb (enjoy, want, etc.)
- Group B: he/she/it --> verb-s main verb (enjoys, wants, etc.)

**Pattern Types:**
- Gerund patterns: Verbs that require -ing form (enjoy, avoid, mind, finish, suggest, consider, keep, practice, love, prefer, recommend, advocate)
- Infinitive patterns: Verbs that require to + verb form (want, plan, hope, decide, need, promise, agree, expect, learn, try, refuse, intend)

**Coverage by Level:**
| Level | Patterns | Domains | Template Complexity |
|-------|----------|---------|---------------------|
| A2 | 10 | food, sports, music, shopping, travel, school | Basic SVO with time/place |
| B1 | 10 | daily_life, travel, work, hobbies, career, education, health, relationships | Purpose clauses |
| B2 | 10 | business, research, environment, technology, finance, law, management, innovation | Reason/condition/consequence clauses |
| C1 | 10 | policy, academia, economics, diplomacy, strategy, governance, science, ethics | Multi-clause sophisticated structures |

**Template Types:**
- A2: `{SUBJ} {MAINVERB} ____ {TIME/PLACE}.`
- B1: `{SUBJ} {MAINVERB} ____ {CONTEXT}.`
- B2: `{SUBJ} {MAINVERB} ____ because/if/despite {CLAUSE}.` or `..., which {CONSEQUENCE}.`
- C1: `While/Given/As {CONTEXT}, {SUBJ} {MAINVERB} ____, which/thereby {IMPLICATION}.`

**Wrong Forms:**
- Gerund patterns: infinitive form ("to verb"), bare infinitive ("verb"), past form
- Infinitive patterns: gerund form ("verbing"), bare infinitive ("verb"), past form

**Distractors by Level:**
- A2: quit, skip, destroy, waste, reject, refuse
- B1: abandon, neglect, overlook, dismiss, postpone, cancel
- B2: disregard, suppress, undermine, circumvent, obstruct, impede
- C1: forsake, obliterate, renounce, repudiate, nullify, abrogate

**Location:** `pattern/infinite_gerund/`

---

### Phrasal Verbs (COMPLETE)

**Status:** 50 patterns created (A2-C1)

**Subject Grouping:**
- Group A: I/you/we/they (base verb + particle)
- Group B: he/she/it (verb-s + particle)

**Pattern Types:**
- Separable: Object can go between verb and particle (turn off, pick up)
- Inseparable: Object must follow the whole phrase (look after, get over)
- Three-word: Verb + adverb + preposition (look forward to, put up with)

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| A2 | 10 | home, shopping, daily_routines, electronics, cleaning | Separable basics |
| B1 | 15 | work, relationships, health, communication, lifestyle | Separable + Inseparable |
| B2 | 15 | business, technology, negotiations, problems, decisions | All types + idiomatic |
| C1 | 10 | policy, strategy, academia, leadership, innovation | Three-word + advanced |

**Template Types:**
- A2: `{SUBJ} ____ the {NOUN} {TIME/PLACE}.`
- B1: `{SUBJ} ____ {OBJ} {PURPOSE/CONTEXT}.`
- B2: `{SUBJ} ____ {OBJ} because {REASON}.` / `..., which {CONSEQUENCE}.`
- C1: `While/Given {CONTEXT}, {SUBJ} ____ {OBJ}, which {IMPLICATION}.`

**Wrong Forms Strategy:**
- Separable verbs: Test particle errors (turn off vs turn on/up/down)
- Inseparable verbs: Test preposition errors (look after vs look for/at)
- Three-word: Test complete phrase errors (look forward to vs look forward for)

**Distractors by Level:**
- A2: leave, ignore, break, forget, drop
- B1: abandon, neglect, dismiss, avoid, reject
- B2: disregard, overlook, circumvent, evade, undermine
- C1: forsake, renounce, perpetuate, abdicate, repudiate

**Location:** `pattern/phrasal_verbs/`

---

### Relative Clauses (COMPLETE)

**Status:** 40 patterns created (A2-C1)

**Relative Pronouns:**
- who: for people (subject position)
- whom: for people (object position, formal)
- which: for things, animals, concepts
- that: for people or things (defining clauses)
- where: for places
- whose: for possession

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| A2 | 10 | people, things, places, animals, objects | Basic who/which/that/where |
| B1 | 10 | professions, possessions, experiences, locations, events | +whom, +whose |
| B2 | 10 | concepts, institutions, research, analysis, processes | Complex clauses |
| C1 | 10 | theories, policies, phenomena, mechanisms, frameworks | Academic discourse |

**Template Types:**
- A2: `The {NOUN} ____ {DESCRIPTION} is {QUALITY}.`
- B1: `The {PERSON} ____ {POSSESSION} {SITUATION}.`
- B2: `The {CONCEPT} ____ {DESCRIPTION} has {IMPACT}.`
- C1: `The {THEORY} ____ {CONTRIBUTION}, has {SIGNIFICANCE}.`

**Wrong Forms Strategy:**
- who vs which: Test person/thing confusion
- that vs which: Test defining vs non-defining
- whose vs whom: Test possession vs object
- where vs which: Test place vs thing

**Distractors by Level:**
- A2: ignore, lose, break, forget
- B1: neglect, overlook, dismiss, abandon
- B2: disregard, suppress, undermine, bypass
- C1: repudiate, circumvent, subvert, nullify

**Location:** `pattern/relative_clauses/`

---

### Reported Speech (COMPLETE)

**Status:** 40 patterns created (B1-C1)

**Subject Grouping:**
- Group A: Reported subject uses plural verb forms (they/we/the team → were, had)
- Group B: Reported subject uses singular verb forms (she/he/it → was, had)

**Tense Backshift Rules:**
- Present → Past: is/are → was/were, has/have → had
- Past → Past Perfect: finished → had finished
- Modal Backshift: will → would, can → could, must → had to

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| B1 | 15 | conversations, news, school, family, friends | Basic backshift (present→past, past→past perfect) |
| B2 | 15 | business, media, interviews, meetings, announcements | Modal backshift + reporting verbs variety |
| C1 | 10 | diplomacy, academia, legal, journalism, negotiations | Complex structures + sophisticated verbs |

**Reporting Verbs by Level:**
- B1: said, told, asked, answered, replied
- B2: explained, mentioned, claimed, admitted, denied, suggested, promised, warned, reminded, announced, stated, confirmed
- C1: asserted, contended, maintained, conceded, acknowledged, alleged, insinuated, emphasized, reiterated, stipulated, proposed, insisted

**Template Types:**
- B1: `{REPORTER} said that {SUBJ} ____ {COMPLEMENT}.`
- B1: `{REPORTER} told me that {SUBJ} ____ {ACTION} {TIME}.`
- B1: `The teacher asked if {SUBJ} ____ {QUESTION_CONTENT}.`
- B2: `The manager explained that the team ____ {TASK} {TIMEFRAME}.`
- B2: `The {AUTHORITY} {REPORTING_VERB} that {SUBJ} ____ {STATEMENT}.`
- C1: `The {OFFICIAL} {REPORTING_VERB} that {SUBJ} ____ {ACTION}, a claim that {IMPLICATION}.`
- C1: `The {PARTY} {REPORTING_VERB} that the {OTHER_PARTY} ____ {DEMAND}, before any further progress {CONDITION}.`

**Wrong Forms Strategy:**
- Present→Past: "is" instead of "was", "are" instead of "were"
- Past→Past Perfect: "finished" instead of "had finished"
- Modal: "will" instead of "would", "can" instead of "could"

**Distractors by Level:**
- B1: deny, refuse, forget, ignore, neglect
- B2: contradict, dispute, refute, challenge, admit
- C1: repudiate, disavow, gainsay, exonerate, incriminate

**Location:** `pattern/reported_speech/`

---

### Conditional Structures (COMPLETE)

**Status:** 40 patterns created (B2-C1)

**Conditional Types:**
- Type 2 (Second Conditional): If + past, would + base (hypothetical present/future)
- Type 3 (Third Conditional): If + had + pp, would have + pp (unreal past)
- Mixed Conditional: Past condition + present result OR present condition + past result
- Inverted Conditional: Had + subject (formal), Were + subject + to (formal)

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| B2 | 20 | hypotheticals, regrets, advice, business, decisions, careers, education | Type 2, Type 3 |
| C1 | 20 | policy, diplomacy, academia, strategy, economics | Mixed, Inverted |

**Template Types:**
- B2 Type 2: `If {SUBJ} ____ {CONDITION}, {SUBJ} would {RESULT}.`
- B2 Type 3: `If {SUBJ} ____ {PAST_ACTION}, {SUBJ} would have {PAST_RESULT}.`
- C1 Mixed: `If {SUBJ} ____ {PAST_ACTION}, {SUBJ} would {PRESENT_RESULT} today.`
- C1 Inverted Had: `____ the {ENTITY} {PAST_ACTION}, {SUBJ} would have {PAST_RESULT}.`
- C1 Inverted Were: `____ the {ENTITY} to {ACTION}, the outcome would {RESULT}.`

**Wrong Forms Strategy:**
- Type 2: Present instead of past in if-clause (have vs had, is vs were)
- Type 3: Simple past instead of past perfect (studied vs had studied)
- Inverted: "If" instead of "Had"/"Were"
- Would in if-clause (common learner error)

**Distractors by Level:**
- B2: squander, neglect, overlook, reject, dismiss, stagnate
- C1: repeal, violate, sever, obstruct, destabilize, mitigate

**Location:** `pattern/conditionals/`

---

### Adjective Order (COMPLETE)

**Status:** 30 patterns created (B1-B2)

**OSASCOMP Order:**
1. Opinion (beautiful, lovely, stunning, gorgeous)
2. Size (big, small, large, tall, long)
3. Age (old, new, young, ancient, vintage)
4. Shape (round, square, rectangular, oval)
5. Color (red, blue, green, black, white)
6. Origin (French, Italian, Japanese, German)
7. Material (wooden, leather, silk, metal, glass)
8. Purpose (sleeping, running, cooking)

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| B1 | 15 | clothing, furniture, food, vehicles, animals | Two-adjective combinations |
| B2 | 15 | architecture, design, art, antiques, fashion | Three-adjective combinations |

**Template Types:**
- B1: `{SUBJ} bought/wore/saw a ____ {NOUN}.` (2 adjectives)
- B2: `The {CONTEXT} featured/acquired a ____ {NOUN}.` (3 adjectives)

**Wrong Forms Strategy:**
- Reversed order (e.g., "red beautiful" instead of "beautiful red")
- Using "and" between adjectives (e.g., "large and wooden" instead of "large wooden")

**Distractors by Level:**
- B1: ugly, hideous, awful, terrible, tiny, huge
- B2: mundane, mediocre, crude, ordinary, unremarkable

**Location:** `pattern/adjective_order/`

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

## EYESH Exam Gap Analysis - New Grammars Required

> Based on analysis of 135 exam images from 2021-2025 (see `docs/EYESH_DATASET.md`)

---

### Relative Clauses (NOT STARTED)

**Priority:** Tier 1 - Very High Frequency in EYESH

**Target Patterns:** 40 (A2-C1)

**What:** Who/whom/which/that/where clauses for defining and non-defining relative clauses

**Template Types:**
- Type 1: `The {NOUN} {RELATIVE_PRONOUN} {VERB} {OBJ} was {DESCRIPTION}.`
- Type 2: `{SUBJ} {VERB} the {NOUN} ___ {CLAUSE}.`

**Subject Groups:**
- Group A: Antecedent is person → who/whom/that
- Group B: Antecedent is thing → which/that
- Group C: Antecedent is place → where

**Examples:**
- "The person ___ helped me was very kind." (who)
- "The book ___ I read was interesting." (which/that)
- "The restaurant ___ we ate was expensive." (where)

**Wrong Forms:** who/which confusion, that vs. which, whom vs. who, missing pronoun

**Location:** `pattern/relative_clauses/` (to be created)

---

### Reported Speech (NOT STARTED)

**Priority:** Tier 1 - Very High Frequency in EYESH

**Target Patterns:** 40 (B1-C1)

**What:** Indirect statements, questions, and commands with tense backshift

**Template Types:**
- Statement: `{PERSON} said that {SUBJ} ___ {OBJ}.`
- Question: `{PERSON} asked if/whether {SUBJ} ___ {OBJ}.`
- Command: `{PERSON} told {OBJ_PERSON} to ___ {OBJ}.`

**Tense Backshift Rules:**
- Present Simple → Past Simple
- Present Continuous → Past Continuous
- Past Simple → Past Perfect
- Will → Would
- Can → Could
- Must → Had to

**Examples:**
- "She said that she ___ to the store." (had gone / went)
- "He asked if I ___ the homework." (had finished)
- "The teacher told us ___ quiet." (to be)

**Wrong Forms:** Incorrect tense shift, modal changes, pronoun confusion

**Location:** `pattern/reported_speech/` (to be created)

---

### Conditional Structures (NOT STARTED)

**Priority:** Tier 1 - High Frequency in EYESH

**Target Patterns:** 40 (B2-C1)

**What:** Second and Third conditional structures for hypothetical situations

**Template Types:**
- Type 2: `If {SUBJ} {PAST_SUBJUNCTIVE}, {SUBJ} would {VERB} {OBJ}.`
- Type 3: `If {SUBJ} had {PAST_PARTICIPLE}, {SUBJ} would have {PP} {OBJ}.`
- Mixed: `If {SUBJ} had {PP}, {SUBJ} would {VERB} now.`

**Subject Groups:** Single group (all subjects use same conditional form)

**Examples:**
- "If I ___ rich, I would buy a house." (were)
- "If she ___ the train, she wouldn't have been late." (had caught)
- "If I ___ harder, I would be successful now." (had worked)

**Wrong Forms:** would in if-clause, tense mixing, incorrect result clause

**Location:** `pattern/conditionals/` (to be created)

---

### Phrasal Verbs (NOT STARTED)

**Priority:** Tier 1 - Very High Frequency in EYESH

**Target Patterns:** 50 (A2-C1)

**What:** Two/three-word verbs with idiomatic meanings

**Template Types:**
- Separable: `{SUBJ} {VERB} ___ the {NOUN}.` (particle position)
- Inseparable: `{SUBJ} {VERB} ___ {NOUN}.` (particle attached)
- Three-word: `{SUBJ} {VERB} {PARTICLE} ___ {NOUN}.`

**Categories:**
- Separable: turn off/on, pick up, put on, take off
- Inseparable: look after, get over, run into
- Three-word: look forward to, put up with, get along with

**Examples:**
- "Please turn ___ the light." (off)
- "She looks ___ her grandmother." (after)
- "I'm looking forward ___ the party." (to)

**Wrong Forms:** Wrong particle, literal vs. idiomatic meaning, word order errors

**Location:** `pattern/phrasal_verbs/` (to be created)

---

### Adjective Order (NOT STARTED)

**Priority:** Tier 1 - High Frequency in EYESH

**Target Patterns:** 30 (B1-B2)

**What:** Proper ordering of multiple adjectives before a noun

**Template Types:**
- `{SUBJ} {VERB} a ___ ___ {NOUN}.` (two adjectives)
- `{SUBJ} {VERB} a ___ ___ ___ {NOUN}.` (three adjectives)

**OSASCOMP Order:**
1. Opinion (beautiful, ugly, nice)
2. Size (big, small, tall)
3. Age (old, new, young)
4. Shape (round, square, flat)
5. Color (red, blue, green)
6. Origin (French, Japanese)
7. Material (wooden, plastic, leather)
8. Purpose (sleeping, running)

**Examples:**
- "She wore a beautiful new leather jacket." (Opinion-Age-Material)
- "He bought a small round wooden table." (Size-Shape-Material)

**Wrong Forms:** Incorrect order, missing adjectives

**Location:** `pattern/adjective_order/` (to be created)

---

### Prefix/Suffix Transformations (NOT STARTED)

**Priority:** Tier 2 - Medium Frequency in EYESH

**Target Patterns:** 40 (B1-C1)

**What:** Word formation using prefixes and suffixes

**Template Types:**
- Nominalization: `The ___ of the project was announced.` (completion)
- Negation: `It was ___ to finish on time.` (impossible)
- Adjective formation: `The report was very ___.` (helpful)

**Common Prefixes:**
- un-, in-/im-/il-/ir-, dis-, re-, pre-, mis-, over-

**Common Suffixes:**
- -tion/-sion, -ment, -ness, -ity, -able/-ible, -ful/-less, -er/-or, -ly

**Examples:**
- complete → completion, improve → improvement
- possible → impossible, legal → illegal
- help → helpful, hope → hopeless

**Wrong Forms:** Wrong affix, spelling errors, incorrect part of speech

**Location:** `pattern/word_formation/` (to be created)

---

### Quantifiers & Determiners (NOT STARTED)

**Priority:** Tier 2 - Medium Frequency in EYESH

**Target Patterns:** 30 (A2-B1)

**What:** Much/many/few/little/some/any and other quantifiers

**Template Types:**
- Countable: `There aren't ___ students.` (many)
- Uncountable: `There isn't ___ time.` (much)
- Positive/Negative: `Do you have ___ questions?` (any)

**Countable vs. Uncountable:**
| Countable | Uncountable |
| many, few, a few | much, little, a little |
| several, a number of | a great deal of |

**Examples:**
- "There isn't ___ time left." (much)
- "I have ___ friends in this city." (few / a few)
- "Would you like ___ tea?" (some)

**Wrong Forms:** much/many confusion, few/little confusion, some/any misuse

**Location:** `pattern/quantifiers/` (to be created)

---

### Question Tags (NOT STARTED)

**Priority:** Tier 2 - Medium Frequency in EYESH

**Target Patterns:** 25 (B1-B2)

**What:** Confirmatory questions at the end of statements

**Template Types:**
- Positive → Negative: `{SUBJ} {POSITIVE_VERB} {OBJ}, ___ {SUBJ}?`
- Negative → Positive: `{SUBJ} {NEGATIVE_VERB} {OBJ}, ___ {SUBJ}?`

**Rules:**
- Positive statement → Negative tag
- Negative statement → Positive tag
- Same auxiliary/modal in tag

**Examples:**
- "You're coming, ___ you?" (aren't)
- "She doesn't like coffee, ___ she?" (does)
- "They haven't finished, ___ they?" (have)

**Special Cases:**
- I am → aren't I?
- Let's → shall we?
- Imperatives → will you? / won't you?

**Wrong Forms:** Wrong auxiliary, wrong pronoun, incorrect polarity

**Location:** `pattern/question_tags/` (to be created)

---

### Emphatic Structures (NOT STARTED)

**Priority:** Tier 2 - Medium Frequency in EYESH

**Target Patterns:** 25 (B2-C1)

**What:** Inversion and cleft sentences for emphasis

**Template Types:**
- Negative inversion: `Never ___ {SUBJ} {PP} such a thing.` (have)
- It-cleft: `It ___ {PERSON} who {VERB} {OBJ}.` (was)
- What-cleft: `What {SUBJ} {VERB} ___ a vacation.` (is)

**Negative Adverbs Triggering Inversion:**
- Never, Rarely, Seldom, Hardly, Barely, Scarcely
- Not only... but also
- No sooner... than

**Examples:**
- "Never ___ I seen such a sight." (have)
- "It ___ John who broke the window." (was)
- "What I want ___ more time." (is)

**Wrong Forms:** Missing inversion, wrong auxiliary, incorrect structure

**Location:** `pattern/emphatic_structures/` (to be created)

---

### Causatives & Perception Verbs (NOT STARTED)

**Priority:** Tier 3 - Low Frequency in EYESH

**Target Patterns:** 20 (B2-C1)

**What:** Causative structures (have/get something done) and perception verb patterns

**Template Types:**
- Causative: `{SUBJ} {CAUSATIVE} {OBJ} {PP/BASE}.`
- Perception: `{SUBJ} {PERCEPTION_VERB} {OBJ} {-ING/BASE}.`

**Causative Verbs:**
- have + object + past participle
- get + object + past participle
- make + object + base verb
- let + object + base verb

**Perception Verbs:**
- see, hear, watch, feel + object + -ing OR base

**Examples:**
- "She had her car ___." (repaired)
- "I got my hair ___." (cut)
- "I saw him ___ the building." (enter / entering)

**Wrong Forms:** Wrong verb form after causative/perception, tense errors

**Location:** `pattern/causatives/` (to be created)

---

### Participle Clauses (NOT STARTED)

**Priority:** Tier 3 - Low Frequency in EYESH

**Target Patterns:** 20 (B2-C1)

**What:** Present and past participle clauses for sentence reduction

**Template Types:**
- Present: `{-ING CLAUSE}, {SUBJ} {VERB} {OBJ}.`
- Past: `{PP CLAUSE}, {SUBJ} {VERB} {OBJ}.`
- Perfect: `Having {PP}, {SUBJ} {VERB} {OBJ}.`

**Examples:**
- "___ late, she took a taxi." (Running)
- "___ from the journey, he went to bed." (Tired)
- "Having ___ the report, she submitted it." (finished)

**Wrong Forms:** Wrong participle form, dangling participle, subject mismatch

**Location:** `pattern/participle_clauses/` (to be created)

---

### Cleft Sentences (NOT STARTED)

**Priority:** Tier 3 - Low Frequency in EYESH

**Target Patterns:** 20 (B2-C1)

**What:** It-clefts and What-clefts for focus and emphasis

**Template Types:**
- It-cleft: `It {BE} {FOCUS} that/who {CLAUSE}.`
- What-cleft: `What {SUBJ} {VERB} {BE} {FOCUS}.`
- All-cleft: `All {SUBJ} {VERB} {BE} {FOCUS}.`

**Examples:**
- "It ___ in Paris that they met." (was)
- "What I need ___ more time." (is)
- "All I want ___ to sleep." (is)

**Wrong Forms:** Incorrect 'be' form, wrong relative pronoun, structure errors

**Location:** `pattern/cleft_sentences/` (to be created)

---

### Word Formation / Prefix-Suffix (COMPLETE)

**Status:** 40 patterns created (B1-C1)

**Pattern Types:**
- Prefixes: un-, dis-, re-, mis-, pre-, over-, under-, de-, multi-, trans-, anti-, counter-, il-/ir-
- Suffixes: -ment, -tion/-sion, -ness, -ity, -able/-ible, -ful/-less, -er/-or, -ly, -ive, -al/-ical, -ous, -ship, -ism, -ary, -ification

**Coverage by Level:**
| Level | Patterns | Domains | Focus |
|-------|----------|---------|-------|
| B1 | 15 | education, work, daily_life, health, communication | Basic prefixes (un-, dis-, re-, mis-) and suffixes (-ment, -ness, -ful, -less, -er, -able, -ity, -ly) |
| B2 | 15 | business, technology, science, law, media | Advanced suffixes (-ization, -ive, -ibility, -ical, -ance/-ence, -al, -ship, -ous) + prefixes (over-, under-, pre-, counter-, il-/ir-) |
| C1 | 10 | academia, policy, economics, philosophy, governance | Sophisticated affixes (-ification, -ism, -ary, -ation) + prefixes (de-, multi-, trans-, anti-) |

**Template Types:**
- B1: `The ____ of the students impressed the teacher.` (noun formation)
- B1: `I ____ with your opinion.` (prefix negation)
- B2: `The ____ of the company led to cost savings.` (process nouns)
- B2: `Critics believe the story was ____ by media.` (prefix under-/over-)
- C1: `The ____ of academic standards has been debated.` (abstract nouns)
- C1: `The ____ corporations dominate global supply chains.` (prefix multi-)

**Wrong Forms Strategy:**
- Base form instead of derived (improve vs improvement)
- Wrong affix (unhealthy vs inhealthy)
- Wrong part of speech (help vs helpful)
- Similar-sounding affixes (illegal vs unlegal)

**Distractors by Level:**
- B1: opposites (deterioration, cruelty, failure, concur)
- B2: antonyms (stagnation, incompatibility, anecdotal, violation)
- C1: sophisticated antonyms (homogenization, dilettantism, authoritarianism, centralization)

**Location:** `pattern/word_formation/`

---

## Coverage Metrics

```
Total Grammars: 23 (18 complete + 5 remaining)
Completed: 18 (78%)
In Progress: 0 (0%)
Not Started: 5 (22%)

Current Patterns: 770
Planned Patterns: 140
Target Total: 910

COMPLETED (770 patterns):
- Present Simple: 50
- Past Simple: 50
- Present Continuous: 50
- Past Continuous: 50
- Present Perfect: 50
- Past Perfect: 30
- Future Simple: 50
- Modals: 50
- Passive Voice: 50
- Gerund/Infinitive: 40
- Phrasal Verbs: 50
- Relative Clauses: 40
- Reported Speech: 40
- Conditional Structures: 40
- Adjective Order: 30
- Word Formation: 40
- Vocabulary: 60

REMAINING (140 patterns):
Tier 2 - Medium Priority (80 patterns):
- Quantifiers: 30
- Question Tags: 25
- Emphatic Structures: 25

Tier 3 - Low Priority (60 patterns):
- Causatives: 20
- Participle Clauses: 20
- Cleft Sentences: 20
```

---

## Next Actions

### Phase 1 Complete - Core Verb Tenses (530 patterns)

1. ~~Implement Present Continuous (50 patterns across 5 levels)~~ COMPLETE
2. ~~Implement Past Continuous (50 patterns across 5 levels)~~ COMPLETE
3. ~~Implement Present Perfect (50 patterns across 5 levels)~~ COMPLETE
4. ~~Implement Modals (50 patterns across 5 levels)~~ COMPLETE
5. ~~Implement Future Simple (50 patterns across 5 levels)~~ COMPLETE
6. ~~Implement Past Perfect (30 patterns: B1-C1)~~ COMPLETE
7. ~~Implement Passive Voice (50 patterns: A2-C1)~~ COMPLETE
8. ~~Expand Gerund/Infinitive patterns (40 patterns: A2-C1)~~ COMPLETE

**CORE GRAMMARS COMPLETE!** (530 patterns total)

---

### Phase 2 - EYESH Gap Grammars (380 patterns)

**Tier 1 - High Priority (200 patterns):**
1. [ ] Implement Phrasal Verbs (50 patterns: A2-C1)
2. [ ] Implement Relative Clauses (40 patterns: A2-C1)
3. [ ] Implement Reported Speech (40 patterns: B1-C1)
4. [ ] Implement Conditional Structures (40 patterns: B2-C1)
5. [ ] Implement Adjective Order (30 patterns: B1-B2)

**Tier 2 - Medium Priority (120 patterns):**
6. [ ] Implement Prefix/Suffix Transformations (40 patterns: B1-C1)
7. [ ] Implement Quantifiers & Determiners (30 patterns: A2-B1)
8. [ ] Implement Question Tags (25 patterns: B1-B2)
9. [ ] Implement Emphatic Structures (25 patterns: B2-C1)

**Tier 3 - Lower Priority (60 patterns):**
10. [ ] Implement Causatives & Perception Verbs (20 patterns: B2-C1)
11. [ ] Implement Participle Clauses (20 patterns: B2-C1)
12. [ ] Implement Cleft Sentences (20 patterns: B2-C1)

**TARGET: 910 total patterns for complete EYESH coverage**

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
