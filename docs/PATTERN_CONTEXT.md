# Pattern Context

> Quick reference for agents creating new patterns

---

## Directory Structure

```
pattern/
├── present_simple/     (50 files)
├── vocabulary/         (61 files)
└── infinite_gerund/    (2 files)
```

---

## Existing Patterns by Grammar

### Present Simple (50 patterns)

**By Level:**

| Level | Domains | Patterns |
|-------|---------|----------|
| A1 | entertainment, food, leisure, sports, technology, travel | 10* |
| A2 | business, education, healthcare, nature, socialmedia | 10 |
| B1 | art, environment, finance, music, science | 10 |
| B2 | architecture, economics, law, literature, politics | 10 |
| C1 | automotive, design, fashion, photography, realestate | 10 |

*Note: A1 has 10 patterns but leisure only has GROUPB

**Full Pattern List:**
```
PRESENT_SIMPLE_ARCHITECTURE_B2_TYPE3_GROUPA
PRESENT_SIMPLE_ARCHITECTURE_B2_TYPE3_GROUPB
PRESENT_SIMPLE_ART_B1_TYPE1_GROUPA
PRESENT_SIMPLE_ART_B1_TYPE1_GROUPB
PRESENT_SIMPLE_AUTOMOTIVE_C1_TYPE2_GROUPA
PRESENT_SIMPLE_AUTOMOTIVE_C1_TYPE2_GROUPB
PRESENT_SIMPLE_BUSINESS_A2_TYPE1_GROUPA
PRESENT_SIMPLE_BUSINESS_A2_TYPE1_GROUPB
PRESENT_SIMPLE_DESIGN_C1_TYPE1_GROUPA
PRESENT_SIMPLE_DESIGN_C1_TYPE1_GROUPB
PRESENT_SIMPLE_ECONOMICS_B2_TYPE1_GROUPA
PRESENT_SIMPLE_ECONOMICS_B2_TYPE1_GROUPB
PRESENT_SIMPLE_EDUCATION_A2_TYPE1_GROUPA
PRESENT_SIMPLE_EDUCATION_A2_TYPE1_GROUPB
PRESENT_SIMPLE_ENTERTAINMENT_A1_TYPE1_GROUPA
PRESENT_SIMPLE_ENTERTAINMENT_A1_TYPE1_GROUPB
PRESENT_SIMPLE_ENVIRONMENT_B1_TYPE3_GROUPA
PRESENT_SIMPLE_ENVIRONMENT_B1_TYPE3_GROUPB
PRESENT_SIMPLE_FASHION_C1_TYPE1_GROUPA
PRESENT_SIMPLE_FASHION_C1_TYPE1_GROUPB
PRESENT_SIMPLE_FINANCE_B1_TYPE1_GROUPA
PRESENT_SIMPLE_FINANCE_B1_TYPE1_GROUPB
PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPA
PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPB
PRESENT_SIMPLE_HEALTHCARE_A2_TYPE2_GROUPA
PRESENT_SIMPLE_HEALTHCARE_A2_TYPE2_GROUPB
PRESENT_SIMPLE_LAW_B2_TYPE1_GROUPA
PRESENT_SIMPLE_LAW_B2_TYPE1_GROUPB
PRESENT_SIMPLE_LEISURE_A1_TYPE1_GROUPB
PRESENT_SIMPLE_LITERATURE_B2_TYPE1_GROUPA
PRESENT_SIMPLE_LITERATURE_B2_TYPE1_GROUPB
PRESENT_SIMPLE_MUSIC_B1_TYPE1_GROUPA
PRESENT_SIMPLE_MUSIC_B1_TYPE1_GROUPB
PRESENT_SIMPLE_NATURE_A2_TYPE1_GROUPA
PRESENT_SIMPLE_NATURE_A2_TYPE1_GROUPB
PRESENT_SIMPLE_PHOTOGRAPHY_C1_TYPE3_GROUPA
PRESENT_SIMPLE_PHOTOGRAPHY_C1_TYPE3_GROUPB
PRESENT_SIMPLE_POLITICS_B2_TYPE2_GROUPA
PRESENT_SIMPLE_POLITICS_B2_TYPE2_GROUPB
PRESENT_SIMPLE_REALESTATE_C1_TYPE1_GROUPA
PRESENT_SIMPLE_REALESTATE_C1_TYPE1_GROUPB
PRESENT_SIMPLE_SCIENCE_B1_TYPE2_GROUPA
PRESENT_SIMPLE_SCIENCE_B1_TYPE2_GROUPB
PRESENT_SIMPLE_SOCIALMEDIA_A2_TYPE2_GROUPA
PRESENT_SIMPLE_SOCIALMEDIA_A2_TYPE2_GROUPB
PRESENT_SIMPLE_SPORTS_A1_TYPE1_GROUPA
PRESENT_SIMPLE_SPORTS_A1_TYPE1_GROUPB
PRESENT_SIMPLE_TECHNOLOGY_A1_TYPE1_GROUPA
PRESENT_SIMPLE_TECHNOLOGY_A1_TYPE1_GROUPB
PRESENT_SIMPLE_TRAVEL_A1_TYPE1_GROUPA
```

### Gerund/Infinitive (2 patterns)

```
gerund_verbs_daily
infinitive_verbs_daily
```

### Vocabulary (61 patterns)

B1 level verb-noun collocations across 10 domains.

---

## Domain Usage Tracking

### Domains Already Used (by grammar)

| Domain | present_simple | past_simple | other |
|--------|---------------|-------------|-------|
| architecture | B2 | - | - |
| art | B1 | - | - |
| automotive | C1 | - | - |
| business | A2 | - | - |
| design | C1 | - | - |
| economics | B2 | - | - |
| education | A2 | - | - |
| entertainment | A1 | - | - |
| environment | B1 | - | - |
| fashion | C1 | - | - |
| finance | B1 | - | - |
| food | A1 | - | - |
| healthcare | A2 | - | - |
| law | B2 | - | - |
| leisure | A1 | - | - |
| literature | B2 | - | - |
| music | B1 | - | - |
| nature | A2 | - | - |
| photography | C1 | - | - |
| politics | B2 | - | - |
| realestate | C1 | - | - |
| science | B1 | - | - |
| socialmedia | A2 | - | - |
| sports | A1 | - | - |
| technology | A1 | - | - |
| travel | A1 | - | - |

### Available Domains (not yet used)

From `grammar_registry.json` categories:

**Daily Life:** cooking, home, family, shopping, clothing, pets, hobbies
**Professional:** journalism, engineering, marketing, human_resources
**Academic:** research, history, philosophy, psychology, sociology, mathematics, physics
**Creative:** writing, theater, dance, crafts
**Sports/Fitness:** fitness, outdoor_activities, team_sports, individual_sports, extreme_sports, wellness, nutrition, training, competition
**Environment:** climate, conservation, wildlife, sustainability, recycling, energy, agriculture, gardening
**Technology:** software, hardware, internet, artificial_intelligence, data_science, cybersecurity, mobile, gaming, automation
**Society:** culture, religion, community, volunteering, social_issues, urban_life, rural_life, immigration, demographics
**Entertainment:** media, celebrities, events, festivals, nightlife, restaurants, hotels, tourism, leisure_activities
**Transport:** aviation, maritime, public_transport, logistics, driving, vehicles, traffic, infrastructure, commuting

---

## JSON Structure Quick Reference

```json
{
  "pattern_id": "GRAMMAR_DOMAIN_LEVEL_TYPE_GROUP",
  "focus": "grammar_type",
  "level": "A1|A2|B1|B2|C1",
  "domain": "domain_name",
  "category": "grammar",
  "template_type": "type_1|type_2|type_3",
  "subject_group": "group_a|group_b|all",
  "sub_grammar": ["optional_subgrammars"],
  "template": "{SUBJ} ____ {OBJ}.",
  "example": "Example sentence.",
  "explanation": "Grammar explanation for learners.",
  "chunks": {
    "SUBJ": ["I", "you", "they"],
    "VERB": {
      "verb_name": {
        "correct_forms": ["correct"],
        "wrong_forms": ["wrong1", "wrong2", "wrong3"],
        "objects": ["obj1", "obj2", "obj3"],
        "distractor": "semantic_distractor"
      }
    }
  }
}
```

### Naming Convention

```
{GRAMMAR}_{DOMAIN}_{LEVEL}_{TYPE}_{GROUP}.json

Examples:
PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL.json
PRESENT_CONTINUOUS_FOOD_A2_TYPE2_GROUPB.json
```

---

## Uniqueness Targets

| Level | Minimum Questions | Typical Chunk Count |
|-------|-------------------|---------------------|
| A1 | 30-50 | 2-3 |
| A2 | 80-120 | 3-4 |
| B1 | 150-250 | 4-5 |
| B2 | 300-500 | 5-6 |
| C1 | 500+ | 6-7 |

**Calculation:** `uniqueness = |SUBJ| × |VERB| × |OBJ| × |TIME| × ...`

---

## Dataset Reference

Location: `/Users/baky/Documents/edu_mining/question_generator/dataset/`

Contains EYESH exam images (2021, 2024) for vocabulary/context reference.

---

## Files Reference

| File | Purpose |
|------|---------|
| `grammar_registry.json` | All grammar rules, subject groups, context markers |
| `GRAMMAR_COVERAGE.md` | Overall coverage status |
| `TODO.md` | Current work queue |
| `validate_patterns.py` | Pattern validation script |
| `main.py` | CLI for question generation |
