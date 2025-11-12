# #!/usr/bin/env python3
# """
# Generate 50 Present Simple Grammar Patterns
# Following UNIVERSAL_PATTERN_GUIDE.md specifications
# """

# import json
# import os
# from pathlib import Path

# BASE_PATH = Path("/Users/baky/Documents/edu_mining/question_generator/pattern/present_simple")
# BASE_PATH.mkdir(parents=True, exist_ok=True)


# def create_pattern(
#     pattern_id,
#     level,
#     template_type,
#     domain,
#     subject_group,
#     template,
#     chunks,
#     explanation,
#     example,
# ):
#     """Create a single pattern file"""
#     pattern = {
#         "pattern_id": pattern_id,
#         "focus": "present_simple",
#         "level": level,
#         "domain": domain,
#         "category": "grammar",
#         "template_type": template_type,
#         "subject_group": subject_group,
#         "sub_grammar": ["present_simple"],
#         "template": template,
#         "example": example,
#         "explanation": explanation,
#         "chunks": chunks,
#     }

#     filename = f"{pattern_id}.json"
#     filepath = BASE_PATH / filename

#     with open(filepath, "w") as f:
#         json.dump(pattern, f, indent=2)

#     print(f"Created: {filename}")
#     return filepath


# # A1 LEVEL PATTERNS (10 patterns)

# # 1. PRESENT_SIMPLE_TRAVEL_A1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_TRAVEL_A1_TYPE1_GROUPA",
#     level="A1",
#     template_type="type_1",
#     domain="travel",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["I", "you", "we"],
#         "VERB": {
#             "visit": {
#                 "correct_forms": ["visit"],
#                 "wrong_forms": ["visits", "visited", "am visiting"],
#                 "objects": ["countries", "cities", "beaches"],
#                 "distractor": "visit hotels",
#             },
#             "travel": {
#                 "correct_forms": ["travel"],
#                 "wrong_forms": ["travels", "travelled", "am travelling"],
#                 "objects": ["around Europe", "to Asia", "by plane"],
#                 "distractor": "travel safely",
#             },
#             "explore": {
#                 "correct_forms": ["explore"],
#                 "wrong_forms": ["explores", "explored", "am exploring"],
#                 "objects": ["new places", "destinations", "monuments"],
#                 "distractor": "explore carefully",
#             },
#         },
#         "OBJ": ["countries", "cities", "beaches", "destinations"],
#         "FREQUENCY": ["every day", "usually"],
#     },
#     explanation="Present simple Group A uses base verb form (I/you/we). Frequency markers like 'every day' indicate habitual action.",
#     example="We visit countries usually.",
# )

# # 2. PRESENT_SIMPLE_LEISURE_A1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_LEISURE_A1_TYPE1_GROUPB",
#     level="A1",
#     template_type="type_1",
#     domain="leisure",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["he", "she", "it"],
#         "VERB": {
#             "play": {
#                 "correct_forms": ["plays"],
#                 "wrong_forms": ["play", "played", "is playing"],
#                 "objects": ["games", "sports", "music"],
#                 "distractor": "plays well",
#             },
#             "watch": {
#                 "correct_forms": ["watches"],
#                 "wrong_forms": ["watch", "watched", "is watching"],
#                 "objects": ["movies", "TV", "shows"],
#                 "distractor": "watches carefully",
#             },
#             "enjoy": {
#                 "correct_forms": ["enjoys"],
#                 "wrong_forms": ["enjoy", "enjoyed", "is enjoying"],
#                 "objects": ["reading", "sports", "hobbies"],
#                 "distractor": "enjoys life",
#             },
#         },
#         "OBJ": ["games", "movies", "reading", "sports"],
#         "FREQUENCY": ["every day", "usually"],
#     },
#     explanation="Present simple Group B (he/she/it) adds -s to the verb. Use with frequency markers for habitual actions.",
#     example="She watches movies usually.",
# )

# # 3. PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPA",
#     level="A1",
#     template_type="type_1",
#     domain="food",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ}.",
#     chunks={
#         "SUBJ": ["I", "you", "they"],
#         "VERB": {
#             "eat": {
#                 "correct_forms": ["eat"],
#                 "wrong_forms": ["eats", "ate", "am eating"],
#                 "objects": ["bread", "rice", "vegetables"],
#                 "distractor": "eat quickly",
#             },
#             "drink": {
#                 "correct_forms": ["drink"],
#                 "wrong_forms": ["drinks", "drank", "am drinking"],
#                 "objects": ["water", "milk", "juice"],
#                 "distractor": "drink slowly",
#             },
#             "cook": {
#                 "correct_forms": ["cook"],
#                 "wrong_forms": ["cooks", "cooked", "am cooking"],
#                 "objects": ["pasta", "soup", "rice"],
#                 "distractor": "cook well",
#             },
#             "prepare": {
#                 "correct_forms": ["prepare"],
#                 "wrong_forms": ["prepares", "prepared", "am preparing"],
#                 "objects": ["meals", "food", "lunch"],
#                 "distractor": "prepare carefully",
#             },
#         },
#         "OBJ": ["bread", "water", "pasta", "meals"],
#     },
#     explanation="Group A verbs use base form without -s. Works with all simple actions.",
#     example="I eat bread.",
# )

# # 4. PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPB",
#     level="A1",
#     template_type="type_1",
#     domain="food",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ}.",
#     chunks={
#         "SUBJ": ["he", "she", "my friend"],
#         "VERB": {
#             "eats": {
#                 "correct_forms": ["eats"],
#                 "wrong_forms": ["eat", "ate", "is eating"],
#                 "objects": ["bread", "rice", "vegetables"],
#                 "distractor": "eats fast",
#             },
#             "drinks": {
#                 "correct_forms": ["drinks"],
#                 "wrong_forms": ["drink", "drank", "is drinking"],
#                 "objects": ["water", "milk", "juice"],
#                 "distractor": "drinks much",
#             },
#             "cooks": {
#                 "correct_forms": ["cooks"],
#                 "wrong_forms": ["cook", "cooked", "is cooking"],
#                 "objects": ["pasta", "soup", "rice"],
#                 "distractor": "cooks badly",
#             },
#             "prepares": {
#                 "correct_forms": ["prepares"],
#                 "wrong_forms": ["prepare", "prepared", "is preparing"],
#                 "objects": ["meals", "food", "lunch"],
#                 "distractor": "prepares quickly",
#             },
#         },
#         "OBJ": ["bread", "water", "pasta", "meals"],
#     },
#     explanation="Group B verbs (he/she/it) add -s to the base form.",
#     example="She eats bread.",
# )

# # 5. PRESENT_SIMPLE_SPORTS_A1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_SPORTS_A1_TYPE1_GROUPA",
#     level="A1",
#     template_type="type_1",
#     domain="sports",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ACTIVITY} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["we", "you", "they"],
#         "VERB": {
#             "play": {
#                 "correct_forms": ["play"],
#                 "wrong_forms": ["plays", "played", "are playing"],
#                 "activities": ["football", "tennis", "basketball"],
#                 "distractor": "play hard",
#             },
#             "practice": {
#                 "correct_forms": ["practice"],
#                 "wrong_forms": ["practices", "practiced", "are practicing"],
#                 "activities": ["drills", "exercises", "techniques"],
#                 "distractor": "practice daily",
#             },
#             "do": {
#                 "correct_forms": ["do"],
#                 "wrong_forms": ["does", "did", "are doing"],
#                 "activities": ["yoga", "gymnastics", "training"],
#                 "distractor": "do well",
#             },
#         },
#         "ACTIVITY": ["football", "tennis", "yoga"],
#         "FREQUENCY": ["every day", "usually"],
#     },
#     explanation="Use base form verbs with Group A subjects for routine sports activities.",
#     example="We play football every day.",
# )

# # 6. PRESENT_SIMPLE_SPORTS_A1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_SPORTS_A1_TYPE1_GROUPB",
#     level="A1",
#     template_type="type_1",
#     domain="sports",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ACTIVITY} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["he", "she", "Tom"],
#         "VERB": {
#             "plays": {
#                 "correct_forms": ["plays"],
#                 "wrong_forms": ["play", "played", "is playing"],
#                 "activities": ["football", "tennis", "basketball"],
#                 "distractor": "plays well",
#             },
#             "practices": {
#                 "correct_forms": ["practices"],
#                 "wrong_forms": ["practice", "practiced", "is practicing"],
#                 "activities": ["drills", "exercises", "techniques"],
#                 "distractor": "practices hard",
#             },
#             "does": {
#                 "correct_forms": ["does"],
#                 "wrong_forms": ["do", "did", "is doing"],
#                 "activities": ["yoga", "gymnastics", "training"],
#                 "distractor": "does well",
#             },
#         },
#         "ACTIVITY": ["football", "tennis", "yoga"],
#         "FREQUENCY": ["every day", "usually"],
#     },
#     explanation="Group B verbs add -s for habitual sports activities.",
#     example="He plays football usually.",
# )

# # 7. PRESENT_SIMPLE_TECHNOLOGY_A1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_TECHNOLOGY_A1_TYPE1_GROUPA",
#     level="A1",
#     template_type="type_1",
#     domain="technology",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {TIME}.",
#     chunks={
#         "SUBJ": ["I", "you", "we"],
#         "VERB": {
#             "use": {
#                 "correct_forms": ["use"],
#                 "wrong_forms": ["uses", "used", "am using"],
#                 "objects": ["computers", "phones", "tablets"],
#                 "distractor": "use devices",
#             },
#             "check": {
#                 "correct_forms": ["check"],
#                 "wrong_forms": ["checks", "checked", "am checking"],
#                 "objects": ["email", "messages", "notifications"],
#                 "distractor": "check often",
#             },
#             "browse": {
#                 "correct_forms": ["browse"],
#                 "wrong_forms": ["browses", "browsed", "am browsing"],
#                 "objects": ["websites", "apps", "the internet"],
#                 "distractor": "browse safely",
#             },
#         },
#         "OBJ": ["computers", "email", "websites"],
#         "TIME": ["in the morning", "at night"],
#     },
#     explanation="Base form for Group A with technology-related activities.",
#     example="I use computers in the morning.",
# )

# # 8. PRESENT_SIMPLE_TECHNOLOGY_A1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_TECHNOLOGY_A1_TYPE1_GROUPB",
#     level="A1",
#     template_type="type_1",
#     domain="technology",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {TIME}.",
#     chunks={
#         "SUBJ": ["he", "she", "it"],
#         "VERB": {
#             "uses": {
#                 "correct_forms": ["uses"],
#                 "wrong_forms": ["use", "used", "is using"],
#                 "objects": ["computers", "phones", "tablets"],
#                 "distractor": "uses often",
#             },
#             "checks": {
#                 "correct_forms": ["checks"],
#                 "wrong_forms": ["check", "checked", "is checking"],
#                 "objects": ["email", "messages", "notifications"],
#                 "distractor": "checks daily",
#             },
#             "browses": {
#                 "correct_forms": ["browses"],
#                 "wrong_forms": ["browse", "browsed", "is browsing"],
#                 "objects": ["websites", "apps", "the internet"],
#                 "distractor": "browses always",
#             },
#         },
#         "OBJ": ["computers", "email", "websites"],
#         "TIME": ["in the morning", "at night"],
#     },
#     explanation="-s form for Group B subjects with technology vocabulary.",
#     example="She checks email at night.",
# )

# # 9. PRESENT_SIMPLE_ENTERTAINMENT_A1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ENTERTAINMENT_A1_TYPE1_GROUPA",
#     level="A1",
#     template_type="type_1",
#     domain="entertainment",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ACTIVITY}.",
#     chunks={
#         "SUBJ": ["I", "you", "we", "they"],
#         "VERB": {
#             "watch": {
#                 "correct_forms": ["watch"],
#                 "wrong_forms": ["watches", "watched", "are watching"],
#                 "activities": ["movies", "TV shows", "videos"],
#                 "distractor": "watch carefully",
#             },
#             "listen": {
#                 "correct_forms": ["listen"],
#                 "wrong_forms": ["listens", "listened", "are listening"],
#                 "activities": ["music", "podcasts", "songs"],
#                 "distractor": "listen attentively",
#             },
#             "read": {
#                 "correct_forms": ["read"],
#                 "wrong_forms": ["reads", "read", "are reading"],
#                 "activities": ["books", "magazines", "comics"],
#                 "distractor": "read fast",
#             },
#             "play": {
#                 "correct_forms": ["play"],
#                 "wrong_forms": ["plays", "played", "are playing"],
#                 "activities": ["games", "video games", "sports"],
#                 "distractor": "play well",
#             },
#         },
#         "ACTIVITY": ["movies", "music", "books", "games"],
#     },
#     explanation="Group A base form for entertainment activities.",
#     example="They watch movies.",
# )

# # 10. PRESENT_SIMPLE_ENTERTAINMENT_A1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ENTERTAINMENT_A1_TYPE1_GROUPB",
#     level="A1",
#     template_type="type_1",
#     domain="entertainment",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ACTIVITY}.",
#     chunks={
#         "SUBJ": ["he", "she", "it", "John"],
#         "VERB": {
#             "watches": {
#                 "correct_forms": ["watches"],
#                 "wrong_forms": ["watch", "watched", "is watching"],
#                 "activities": ["movies", "TV shows", "videos"],
#                 "distractor": "watches always",
#             },
#             "listens": {
#                 "correct_forms": ["listens"],
#                 "wrong_forms": ["listen", "listened", "is listening"],
#                 "activities": ["music", "podcasts", "songs"],
#                 "distractor": "listens daily",
#             },
#             "reads": {
#                 "correct_forms": ["reads"],
#                 "wrong_forms": ["read", "read", "is reading"],
#                 "activities": ["books", "magazines", "comics"],
#                 "distractor": "reads often",
#             },
#             "plays": {
#                 "correct_forms": ["plays"],
#                 "wrong_forms": ["play", "played", "is playing"],
#                 "activities": ["games", "video games", "sports"],
#                 "distractor": "plays hard",
#             },
#         },
#         "ACTIVITY": ["movies", "music", "books", "games"],
#     },
#     explanation="Group B -s form for entertainment domain.",
#     example="John listens to music.",
# )

# print("\n=== A1 LEVEL COMPLETE (10 patterns) ===")

# # A2 LEVEL PATTERNS (10 patterns)

# # 11. PRESENT_SIMPLE_EDUCATION_A2_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_EDUCATION_A2_TYPE1_GROUPA",
#     level="A2",
#     template_type="type_1",
#     domain="education",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["students", "we", "they"],
#         "VERB": {
#             "study": {
#                 "correct_forms": ["study"],
#                 "wrong_forms": ["studies", "studied", "are studying"],
#                 "objects": ["English", "mathematics", "history"],
#                 "distractor": "study hard",
#             },
#             "learn": {
#                 "correct_forms": ["learn"],
#                 "wrong_forms": ["learns", "learned", "are learning"],
#                 "objects": ["languages", "skills", "subjects"],
#                 "distractor": "learn quickly",
#             },
#             "practice": {
#                 "correct_forms": ["practice"],
#                 "wrong_forms": ["practices", "practiced", "are practicing"],
#                 "objects": ["grammar", "writing", "speaking"],
#                 "distractor": "practice daily",
#             },
#             "review": {
#                 "correct_forms": ["review"],
#                 "wrong_forms": ["reviews", "reviewed", "are reviewing"],
#                 "objects": ["notes", "lessons", "materials"],
#                 "distractor": "review often",
#             },
#         },
#         "OBJ": ["English", "languages", "grammar", "lessons"],
#         "PREP_TIME": ["in the morning", "after school", "during class"],
#     },
#     explanation="Group A verbs in education context with prep+time for specific timing.",
#     example="Students study English after school.",
# )

# # 12. PRESENT_SIMPLE_EDUCATION_A2_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_EDUCATION_A2_TYPE1_GROUPB",
#     level="A2",
#     template_type="type_1",
#     domain="education",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["the student", "he", "she"],
#         "VERB": {
#             "studies": {
#                 "correct_forms": ["studies"],
#                 "wrong_forms": ["study", "studied", "is studying"],
#                 "objects": ["English", "mathematics", "history"],
#                 "distractor": "studies well",
#             },
#             "learns": {
#                 "correct_forms": ["learns"],
#                 "wrong_forms": ["learn", "learned", "is learning"],
#                 "objects": ["languages", "skills", "subjects"],
#                 "distractor": "learns easily",
#             },
#             "practices": {
#                 "correct_forms": ["practices"],
#                 "wrong_forms": ["practice", "practiced", "is practicing"],
#                 "objects": ["grammar", "writing", "speaking"],
#                 "distractor": "practices daily",
#             },
#             "reviews": {
#                 "correct_forms": ["reviews"],
#                 "wrong_forms": ["review", "reviewed", "is reviewing"],
#                 "objects": ["notes", "lessons", "materials"],
#                 "distractor": "reviews frequently",
#             },
#         },
#         "OBJ": ["English", "languages", "grammar", "lessons"],
#         "PREP_TIME": ["in the morning", "after school", "during class"],
#     },
#     explanation="Group B -s form in education with temporal context.",
#     example="She reviews lessons during class.",
# )

# # 13. PRESENT_SIMPLE_HEALTHCARE_A2_TYPE2_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_HEALTHCARE_A2_TYPE2_GROUPA",
#     level="A2",
#     template_type="type_2",
#     domain="healthcare",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {TIME}.",
#     chunks={
#         "SUBJ": ["I", "you", "they"],
#         "VERB": {
#             "exercise": {
#                 "correct_forms": ["don't exercise"],
#                 "wrong_forms": ["doesn't exercise", "didn't exercise", "am not exercising"],
#                 "objects": ["regularly", "enough", "daily"],
#                 "distractor": "don't rest",
#             },
#             "sleep": {
#                 "correct_forms": ["don't sleep"],
#                 "wrong_forms": ["doesn't sleep", "didn't sleep", "am not sleeping"],
#                 "objects": ["well", "enough", "much"],
#                 "distractor": "don't wake",
#             },
#             "eat": {
#                 "correct_forms": ["don't eat"],
#                 "wrong_forms": ["doesn't eat", "didn't eat", "am not eating"],
#                 "objects": ["vegetables", "healthily", "enough"],
#                 "distractor": "don't cook",
#             },
#             "drink": {
#                 "correct_forms": ["don't drink"],
#                 "wrong_forms": ["doesn't drink", "didn't drink", "am not drinking"],
#                 "objects": ["water", "milk", "juice"],
#                 "distractor": "don't pour",
#             },
#         },
#         "OBJ": ["regularly", "well", "enough"],
#         "TIME": ["every day", "usually", "often"],
#     },
#     explanation="Negative present simple: Group A uses 'don't' + base verb.",
#     example="I don't exercise every day.",
# )

# # 14. PRESENT_SIMPLE_HEALTHCARE_A2_TYPE2_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_HEALTHCARE_A2_TYPE2_GROUPB",
#     level="A2",
#     template_type="type_2",
#     domain="healthcare",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {TIME}.",
#     chunks={
#         "SUBJ": ["he", "she", "the patient"],
#         "VERB": {
#             "exercise": {
#                 "correct_forms": ["doesn't exercise"],
#                 "wrong_forms": ["don't exercise", "didn't exercise", "isn't exercising"],
#                 "objects": ["regularly", "enough", "daily"],
#                 "distractor": "doesn't rest",
#             },
#             "sleep": {
#                 "correct_forms": ["doesn't sleep"],
#                 "wrong_forms": ["don't sleep", "didn't sleep", "isn't sleeping"],
#                 "objects": ["well", "enough", "much"],
#                 "distractor": "doesn't wake",
#             },
#             "eat": {
#                 "correct_forms": ["doesn't eat"],
#                 "wrong_forms": ["don't eat", "didn't eat", "isn't eating"],
#                 "objects": ["vegetables", "healthily", "enough"],
#                 "distractor": "doesn't cook",
#             },
#             "drink": {
#                 "correct_forms": ["doesn't drink"],
#                 "wrong_forms": ["don't drink", "didn't drink", "isn't drinking"],
#                 "objects": ["water", "milk", "juice"],
#                 "distractor": "doesn't pour",
#             },
#         },
#         "OBJ": ["regularly", "well", "enough"],
#         "TIME": ["every day", "usually", "often"],
#     },
#     explanation="Negative Group B: 'doesn't' + base verb.",
#     example="She doesn't sleep enough usually.",
# )

# # 15. PRESENT_SIMPLE_BUSINESS_A2_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_BUSINESS_A2_TYPE1_GROUPA",
#     level="A2",
#     template_type="type_1",
#     domain="business",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["we", "employees", "they"],
#         "VERB": {
#             "attend": {
#                 "correct_forms": ["attend"],
#                 "wrong_forms": ["attends", "attended", "are attending"],
#                 "objects": ["meetings", "conferences", "events"],
#                 "distractor": "attend carefully",
#             },
#             "organize": {
#                 "correct_forms": ["organize"],
#                 "wrong_forms": ["organizes", "organized", "are organizing"],
#                 "objects": ["meetings", "projects", "events"],
#                 "distractor": "organize well",
#             },
#             "prepare": {
#                 "correct_forms": ["prepare"],
#                 "wrong_forms": ["prepares", "prepared", "are preparing"],
#                 "objects": ["reports", "documents", "presentations"],
#                 "distractor": "prepare carefully",
#             },
#             "review": {
#                 "correct_forms": ["review"],
#                 "wrong_forms": ["reviews", "reviewed", "are reviewing"],
#                 "objects": ["contracts", "proposals", "budgets"],
#                 "distractor": "review daily",
#             },
#         },
#         "OBJ": ["meetings", "reports", "presentations", "documents"],
#         "FREQUENCY": ["every day", "usually", "often"],
#     },
#     explanation="Business domain with Group A base forms.",
#     example="Employees prepare reports every day.",
# )

# # 16. PRESENT_SIMPLE_BUSINESS_A2_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_BUSINESS_A2_TYPE1_GROUPB",
#     level="A2",
#     template_type="type_1",
#     domain="business",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["he", "she", "the manager"],
#         "VERB": {
#             "attends": {
#                 "correct_forms": ["attends"],
#                 "wrong_forms": ["attend", "attended", "is attending"],
#                 "objects": ["meetings", "conferences", "events"],
#                 "distractor": "attends actively",
#             },
#             "organizes": {
#                 "correct_forms": ["organizes"],
#                 "wrong_forms": ["organize", "organized", "is organizing"],
#                 "objects": ["meetings", "projects", "events"],
#                 "distractor": "organizes efficiently",
#             },
#             "prepares": {
#                 "correct_forms": ["prepares"],
#                 "wrong_forms": ["prepare", "prepared", "is preparing"],
#                 "objects": ["reports", "documents", "presentations"],
#                 "distractor": "prepares thoroughly",
#             },
#             "reviews": {
#                 "correct_forms": ["reviews"],
#                 "wrong_forms": ["review", "reviewed", "is reviewing"],
#                 "objects": ["contracts", "proposals", "budgets"],
#                 "distractor": "reviews carefully",
#             },
#         },
#         "OBJ": ["meetings", "reports", "presentations", "documents"],
#         "FREQUENCY": ["every day", "usually", "often"],
#     },
#     explanation="Group B -s form in business context.",
#     example="The manager organizes meetings usually.",
# )

# # 17. PRESENT_SIMPLE_NATURE_A2_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_NATURE_A2_TYPE1_GROUPA",
#     level="A2",
#     template_type="type_1",
#     domain="nature",
#     subject_group="group_a",
#     template="{SUBJ} ____ {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["we", "you", "animals", "they"],
#         "VERB": {
#             "walk": {
#                 "correct_forms": ["walk"],
#                 "wrong_forms": ["walks", "walked", "are walking"],
#                 "places": ["in the forest", "by the river", "near the mountains"],
#                 "distractor": "walk slowly",
#             },
#             "explore": {
#                 "correct_forms": ["explore"],
#                 "wrong_forms": ["explores", "explored", "are exploring"],
#                 "places": ["in the forest", "by the river", "in nature"],
#                 "distractor": "explore carefully",
#             },
#             "observe": {
#                 "correct_forms": ["observe"],
#                 "wrong_forms": ["observes", "observed", "are observing"],
#                 "places": ["in the forest", "by the river", "in the field"],
#                 "distractor": "observe closely",
#             },
#         },
#         "PREP_PLACE": ["in the forest", "by the river", "near the mountains"],
#         "TIME": ["every day", "usually", "often"],
#     },
#     explanation="Nature domain with spatial + temporal context.",
#     example="We walk in the forest every day.",
# )

# # 18. PRESENT_SIMPLE_NATURE_A2_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_NATURE_A2_TYPE1_GROUPB",
#     level="A2",
#     template_type="type_1",
#     domain="nature",
#     subject_group="group_b",
#     template="{SUBJ} ____ {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["he", "she", "the bird", "it"],
#         "VERB": {
#             "walks": {
#                 "correct_forms": ["walks"],
#                 "wrong_forms": ["walk", "walked", "is walking"],
#                 "places": ["in the forest", "by the river", "near the mountains"],
#                 "distractor": "walks alone",
#             },
#             "explores": {
#                 "correct_forms": ["explores"],
#                 "wrong_forms": ["explore", "explored", "is exploring"],
#                 "places": ["in the forest", "by the river", "in nature"],
#                 "distractor": "explores freely",
#             },
#             "observes": {
#                 "correct_forms": ["observes"],
#                 "wrong_forms": ["observe", "observed", "is observing"],
#                 "places": ["in the forest", "by the river", "in the field"],
#                 "distractor": "observes intently",
#             },
#         },
#         "PREP_PLACE": ["in the forest", "by the river", "near the mountains"],
#         "TIME": ["every day", "usually", "often"],
#     },
#     explanation="Group B in nature domain.",
#     example="The bird observes by the river usually.",
# )

# # 19. PRESENT_SIMPLE_SOCIALMEDIA_A2_TYPE2_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_SOCIALMEDIA_A2_TYPE2_GROUPA",
#     level="A2",
#     template_type="type_2",
#     domain="social_media",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["I", "you", "we"],
#         "VERB": {
#             "post": {
#                 "correct_forms": ["don't post"],
#                 "wrong_forms": ["doesn't post", "didn't post", "am not posting"],
#                 "objects": ["photos", "videos", "updates"],
#                 "distractor": "don't share",
#             },
#             "share": {
#                 "correct_forms": ["don't share"],
#                 "wrong_forms": ["doesn't share", "didn't share", "am not sharing"],
#                 "objects": ["photos", "news", "stories"],
#                 "distractor": "don't post",
#             },
#             "like": {
#                 "correct_forms": ["don't like"],
#                 "wrong_forms": ["doesn't like", "didn't like", "am not liking"],
#                 "objects": ["posts", "comments", "pictures"],
#                 "distractor": "don't dislike",
#             },
#             "follow": {
#                 "correct_forms": ["don't follow"],
#                 "wrong_forms": ["doesn't follow", "didn't follow", "am not following"],
#                 "objects": ["accounts", "pages", "friends"],
#                 "distractor": "don't unfollow",
#             },
#         },
#         "OBJ": ["photos", "posts", "accounts", "pages"],
#         "FREQUENCY": ["every day", "usually", "often"],
#     },
#     explanation="Negative present simple: Group A don't + verb.",
#     example="I don't post photos every day.",
# )

# # 20. PRESENT_SIMPLE_SOCIALMEDIA_A2_TYPE2_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_SOCIALMEDIA_A2_TYPE2_GROUPB",
#     level="A2",
#     template_type="type_2",
#     domain="social_media",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["he", "she", "my friend"],
#         "VERB": {
#             "post": {
#                 "correct_forms": ["doesn't post"],
#                 "wrong_forms": ["don't post", "didn't post", "isn't posting"],
#                 "objects": ["photos", "videos", "updates"],
#                 "distractor": "doesn't share",
#             },
#             "share": {
#                 "correct_forms": ["doesn't share"],
#                 "wrong_forms": ["don't share", "didn't share", "isn't sharing"],
#                 "objects": ["photos", "news", "stories"],
#                 "distractor": "doesn't post",
#             },
#             "like": {
#                 "correct_forms": ["doesn't like"],
#                 "wrong_forms": ["don't like", "didn't like", "isn't liking"],
#                 "objects": ["posts", "comments", "pictures"],
#                 "distractor": "doesn't dislike",
#             },
#             "follow": {
#                 "correct_forms": ["doesn't follow"],
#                 "wrong_forms": ["don't follow", "didn't follow", "isn't following"],
#                 "objects": ["accounts", "pages", "friends"],
#                 "distractor": "doesn't unfollow",
#             },
#         },
#         "OBJ": ["photos", "posts", "accounts", "pages"],
#         "FREQUENCY": ["every day", "usually", "often"],
#     },
#     explanation="Negative Group B: doesn't + verb.",
#     example="She doesn't follow accounts usually.",
# )

# print("=== A2 LEVEL COMPLETE (10 patterns) ===")

# # B1 LEVEL PATTERNS (10 patterns)

# # 21. PRESENT_SIMPLE_FINANCE_B1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_FINANCE_B1_TYPE1_GROUPA",
#     level="B1",
#     template_type="type_1",
#     domain="finance",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["investors", "we", "they"],
#         "VERB": {
#             "invest": {
#                 "correct_forms": ["invest"],
#                 "wrong_forms": ["invests", "invested", "are investing"],
#                 "article_objects": ["the portfolio", "a budget", "the savings"],
#                 "distractor": "invest wisely",
#             },
#             "save": {
#                 "correct_forms": ["save"],
#                 "wrong_forms": ["saves", "saved", "are saving"],
#                 "article_objects": ["the money", "a fund", "the savings"],
#                 "distractor": "save diligently",
#             },
#             "manage": {
#                 "correct_forms": ["manage"],
#                 "wrong_forms": ["manages", "managed", "are managing"],
#                 "article_objects": ["the assets", "the portfolio", "their finances"],
#                 "distractor": "manage carefully",
#             },
#             "track": {
#                 "correct_forms": ["track"],
#                 "wrong_forms": ["tracks", "tracked", "are tracking"],
#                 "article_objects": ["their expenses", "the budget", "investments"],
#                 "distractor": "track closely",
#             },
#         },
#         "ARTICLE_OBJ": ["the portfolio", "a budget", "the money", "their expenses"],
#         "PREP_TIME": ["in the morning", "every month", "regularly", "daily"],
#     },
#     explanation="B1 finance vocabulary with article+noun combinations.",
#     example="Investors invest the portfolio regularly.",
# )

# # 22. PRESENT_SIMPLE_FINANCE_B1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_FINANCE_B1_TYPE1_GROUPB",
#     level="B1",
#     template_type="type_1",
#     domain="finance",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["the investor", "he", "she"],
#         "VERB": {
#             "invests": {
#                 "correct_forms": ["invests"],
#                 "wrong_forms": ["invest", "invested", "is investing"],
#                 "article_objects": ["the portfolio", "a budget", "the savings"],
#                 "distractor": "invests safely",
#             },
#             "saves": {
#                 "correct_forms": ["saves"],
#                 "wrong_forms": ["save", "saved", "is saving"],
#                 "article_objects": ["the money", "a fund", "the savings"],
#                 "distractor": "saves regularly",
#             },
#             "manages": {
#                 "correct_forms": ["manages"],
#                 "wrong_forms": ["manage", "managed", "is managing"],
#                 "article_objects": ["the assets", "the portfolio", "their finances"],
#                 "distractor": "manages effectively",
#             },
#             "tracks": {
#                 "correct_forms": ["tracks"],
#                 "wrong_forms": ["track", "tracked", "is tracking"],
#                 "article_objects": ["their expenses", "the budget", "investments"],
#                 "distractor": "tracks meticulously",
#             },
#         },
#         "ARTICLE_OBJ": ["the portfolio", "a budget", "the money", "their expenses"],
#         "PREP_TIME": ["in the morning", "every month", "regularly", "daily"],
#     },
#     explanation="Group B -s form with finance complexity.",
#     example="She manages the portfolio every month.",
# )

# # 23. PRESENT_SIMPLE_SCIENCE_B1_TYPE2_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_SCIENCE_B1_TYPE2_GROUPA",
#     level="B1",
#     template_type="type_2",
#     domain="science",
#     subject_group="group_a",
#     template="{SUBJ} ____ {OBJ} {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["scientists", "researchers", "they"],
#         "VERB": {
#             "conduct": {
#                 "correct_forms": ["don't conduct"],
#                 "wrong_forms": ["doesn't conduct", "didn't conduct", "are not conducting"],
#                 "objects": ["experiments", "research", "studies"],
#                 "distractor": "don't perform",
#             },
#             "perform": {
#                 "correct_forms": ["don't perform"],
#                 "wrong_forms": ["doesn't perform", "didn't perform", "are not performing"],
#                 "objects": ["tests", "procedures", "analyses"],
#                 "distractor": "don't conduct",
#             },
#             "analyze": {
#                 "correct_forms": ["don't analyze"],
#                 "wrong_forms": ["doesn't analyze", "didn't analyze", "are not analyzing"],
#                 "objects": ["data", "samples", "results"],
#                 "distractor": "don't examine",
#             },
#             "observe": {
#                 "correct_forms": ["don't observe"],
#                 "wrong_forms": ["doesn't observe", "didn't observe", "are not observing"],
#                 "objects": ["phenomena", "patterns", "changes"],
#                 "distractor": "don't notice",
#             },
#         },
#         "OBJ": ["experiments", "tests", "data", "phenomena"],
#         "PREP_PLACE": ["in the lab", "at the center", "in the field"],
#         "TIME": ["every day", "regularly", "usually"],
#     },
#     explanation="B1 science with spatial + temporal markers.",
#     example="Researchers don't conduct experiments in the lab regularly.",
# )

# # 24. PRESENT_SIMPLE_SCIENCE_B1_TYPE2_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_SCIENCE_B1_TYPE2_GROUPB",
#     level="B1",
#     template_type="type_2",
#     domain="science",
#     subject_group="group_b",
#     template="{SUBJ} ____ {OBJ} {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["the scientist", "he", "she"],
#         "VERB": {
#             "conduct": {
#                 "correct_forms": ["doesn't conduct"],
#                 "wrong_forms": ["don't conduct", "didn't conduct", "isn't conducting"],
#                 "objects": ["experiments", "research", "studies"],
#                 "distractor": "doesn't perform",
#             },
#             "perform": {
#                 "correct_forms": ["doesn't perform"],
#                 "wrong_forms": ["don't perform", "didn't perform", "isn't performing"],
#                 "objects": ["tests", "procedures", "analyses"],
#                 "distractor": "doesn't conduct",
#             },
#             "analyze": {
#                 "correct_forms": ["doesn't analyze"],
#                 "wrong_forms": ["don't analyze", "didn't analyze", "isn't analyzing"],
#                 "objects": ["data", "samples", "results"],
#                 "distractor": "doesn't examine",
#             },
#             "observe": {
#                 "correct_forms": ["doesn't observe"],
#                 "wrong_forms": ["don't observe", "didn't observe", "isn't observing"],
#                 "objects": ["phenomena", "patterns", "changes"],
#                 "distractor": "doesn't notice",
#             },
#         },
#         "OBJ": ["experiments", "tests", "data", "phenomena"],
#         "PREP_PLACE": ["in the lab", "at the center", "in the field"],
#         "TIME": ["every day", "regularly", "usually"],
#     },
#     explanation="Group B negative in science domain.",
#     example="The scientist doesn't analyze data at the center usually.",
# )

# # 25. PRESENT_SIMPLE_ART_B1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ART_B1_TYPE1_GROUPA",
#     level="B1",
#     template_type="type_1",
#     domain="art",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["artists", "we", "they"],
#         "VERB": {
#             "create": {
#                 "correct_forms": ["create"],
#                 "wrong_forms": ["creates", "created", "are creating"],
#                 "article_objects": ["artwork", "paintings", "sculptures"],
#                 "distractor": "create skillfully",
#             },
#             "paint": {
#                 "correct_forms": ["paint"],
#                 "wrong_forms": ["paints", "painted", "are painting"],
#                 "article_objects": ["masterpieces", "canvases", "murals"],
#                 "distractor": "paint carefully",
#             },
#             "design": {
#                 "correct_forms": ["design"],
#                 "wrong_forms": ["designs", "designed", "are designing"],
#                 "article_objects": ["installations", "sculptures", "concepts"],
#                 "distractor": "design creatively",
#             },
#             "exhibit": {
#                 "correct_forms": ["exhibit"],
#                 "wrong_forms": ["exhibits", "exhibited", "are exhibiting"],
#                 "article_objects": ["artworks", "collections", "pieces"],
#                 "distractor": "exhibit proudly",
#             },
#         },
#         "ARTICLE_OBJ": ["artwork", "paintings", "sculptures", "collections"],
#         "FREQUENCY": ["daily", "regularly", "often", "frequently"],
#     },
#     explanation="Art domain with frequency markers.",
#     example="Artists create artwork regularly.",
# )

# # 26. PRESENT_SIMPLE_ART_B1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ART_B1_TYPE1_GROUPB",
#     level="B1",
#     template_type="type_1",
#     domain="art",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["the artist", "he", "she"],
#         "VERB": {
#             "creates": {
#                 "correct_forms": ["creates"],
#                 "wrong_forms": ["create", "created", "is creating"],
#                 "article_objects": ["artwork", "paintings", "sculptures"],
#                 "distractor": "creates masterfully",
#             },
#             "paints": {
#                 "correct_forms": ["paints"],
#                 "wrong_forms": ["paint", "painted", "is painting"],
#                 "article_objects": ["masterpieces", "canvases", "murals"],
#                 "distractor": "paints beautifully",
#             },
#             "designs": {
#                 "correct_forms": ["designs"],
#                 "wrong_forms": ["design", "designed", "is designing"],
#                 "article_objects": ["installations", "sculptures", "concepts"],
#                 "distractor": "designs artistically",
#             },
#             "exhibits": {
#                 "correct_forms": ["exhibits"],
#                 "wrong_forms": ["exhibit", "exhibited", "is exhibiting"],
#                 "article_objects": ["artworks", "collections", "pieces"],
#                 "distractor": "exhibits globally",
#             },
#         },
#         "ARTICLE_OBJ": ["artwork", "paintings", "sculptures", "collections"],
#         "FREQUENCY": ["daily", "regularly", "often", "frequently"],
#     },
#     explanation="Group B in art with -s form.",
#     example="She designs sculptures regularly.",
# )

# # 27. PRESENT_SIMPLE_ENVIRONMENT_B1_TYPE3_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ENVIRONMENT_B1_TYPE3_GROUPA",
#     level="B1",
#     template_type="type_3",
#     domain="environment",
#     subject_group="group_a",
#     template="{SUBJ} ____ {BASE_VERB} {OBJ} {TIME}.",
#     chunks={
#         "SUBJ": ["people", "we", "they"],
#         "AUX": "don't",
#         "BASE_VERB": ["recycle", "waste", "pollute", "conserve"],
#         "OBJ": ["plastic", "resources", "water", "energy"],
#         "TIME": ["enough", "often", "regularly", "frequently"],
#     },
#     explanation="Type 3: Negative auxiliary only. Tests auxiliary selection.",
#     example="People don't recycle plastic enough.",
# )

# # 28. PRESENT_SIMPLE_ENVIRONMENT_B1_TYPE3_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ENVIRONMENT_B1_TYPE3_GROUPB",
#     level="B1",
#     template_type="type_3",
#     domain="environment",
#     subject_group="group_b",
#     template="{SUBJ} ____ {BASE_VERB} {OBJ} {TIME}.",
#     chunks={
#         "SUBJ": ["the company", "he", "she"],
#         "AUX": "doesn't",
#         "BASE_VERB": ["recycle", "waste", "pollute", "conserve"],
#         "OBJ": ["plastic", "resources", "water", "energy"],
#         "TIME": ["enough", "often", "regularly", "frequently"],
#     },
#     explanation="Type 3 Group B: doesn't + base verb.",
#     example="The company doesn't conserve water regularly.",
# )

# # 29. PRESENT_SIMPLE_MUSIC_B1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_MUSIC_B1_TYPE1_GROUPA",
#     level="B1",
#     template_type="type_1",
#     domain="music",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["musicians", "we", "they"],
#         "VERB": {
#             "compose": {
#                 "correct_forms": ["compose"],
#                 "wrong_forms": ["composes", "composed", "are composing"],
#                 "article_objects": ["symphonies", "concertos", "sonatas"],
#                 "distractor": "compose beautifully",
#             },
#             "perform": {
#                 "correct_forms": ["perform"],
#                 "wrong_forms": ["performs", "performed", "are performing"],
#                 "article_objects": ["concerts", "pieces", "recitals"],
#                 "distractor": "perform excellently",
#             },
#             "practice": {
#                 "correct_forms": ["practice"],
#                 "wrong_forms": ["practices", "practiced", "are practicing"],
#                 "article_objects": ["scales", "exercises", "techniques"],
#                 "distractor": "practice diligently",
#             },
#             "record": {
#                 "correct_forms": ["record"],
#                 "wrong_forms": ["records", "recorded", "are recording"],
#                 "article_objects": ["albums", "tracks", "songs"],
#                 "distractor": "record professionally",
#             },
#         },
#         "ARTICLE_OBJ": ["symphonies", "concerts", "scales", "albums"],
#         "PREP_TIME": ["in the morning", "every day", "after school", "regularly"],
#     },
#     explanation="Music domain with article+noun for B1 level.",
#     example="Musicians perform concerts regularly.",
# )

# # 30. PRESENT_SIMPLE_MUSIC_B1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_MUSIC_B1_TYPE1_GROUPB",
#     level="B1",
#     template_type="type_1",
#     domain="music",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["the musician", "he", "she"],
#         "VERB": {
#             "composes": {
#                 "correct_forms": ["composes"],
#                 "wrong_forms": ["compose", "composed", "is composing"],
#                 "article_objects": ["symphonies", "concertos", "sonatas"],
#                 "distractor": "composes melodiously",
#             },
#             "performs": {
#                 "correct_forms": ["performs"],
#                 "wrong_forms": ["perform", "performed", "is performing"],
#                 "article_objects": ["concerts", "pieces", "recitals"],
#                 "distractor": "performs brilliantly",
#             },
#             "practices": {
#                 "correct_forms": ["practices"],
#                 "wrong_forms": ["practice", "practiced", "is practicing"],
#                 "article_objects": ["scales", "exercises", "techniques"],
#                 "distractor": "practices conscientiously",
#             },
#             "records": {
#                 "correct_forms": ["records"],
#                 "wrong_forms": ["record", "recorded", "is recording"],
#                 "article_objects": ["albums", "tracks", "songs"],
#                 "distractor": "records flawlessly",
#             },
#         },
#         "ARTICLE_OBJ": ["symphonies", "concerts", "scales", "albums"],
#         "PREP_TIME": ["in the morning", "every day", "after school", "regularly"],
#     },
#     explanation="Group B in music domain with -s form.",
#     example="She records albums regularly.",
# )

# print("=== B1 LEVEL COMPLETE (10 patterns) ===")

# # B2 LEVEL PATTERNS (10 patterns)

# # 31. PRESENT_SIMPLE_LAW_B2_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_LAW_B2_TYPE1_GROUPA",
#     level="B2",
#     template_type="type_1",
#     domain="law",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["lawyers", "attorneys", "they"],
#         "VERB": {
#             "represent": {
#                 "correct_forms": ["represent"],
#                 "wrong_forms": ["represents", "represented", "are representing"],
#                 "article_objects": ["clients", "defendants", "plaintiffs"],
#                 "distractor": "represent loyally",
#             },
#             "defend": {
#                 "correct_forms": ["defend"],
#                 "wrong_forms": ["defends", "defended", "are defending"],
#                 "article_objects": ["cases", "rights", "interests"],
#                 "distractor": "defend vigorously",
#             },
#             "prosecute": {
#                 "correct_forms": ["prosecute"],
#                 "wrong_forms": ["prosecutes", "prosecuted", "are prosecuting"],
#                 "article_objects": ["offenders", "criminals", "cases"],
#                 "distractor": "prosecute aggressively",
#             },
#             "advise": {
#                 "correct_forms": ["advise"],
#                 "wrong_forms": ["advises", "advised", "are advising"],
#                 "article_objects": ["clients", "organizations", "corporations"],
#                 "distractor": "advise wisely",
#             },
#         },
#         "ARTICLE_OBJ": ["clients", "cases", "defendants", "organizations"],
#         "PREP_PLACE": ["in court", "at the office", "during trials"],
#         "TIME": ["daily", "regularly", "frequently"],
#     },
#     explanation="B2 legal domain with complex sentence structure.",
#     example="Lawyers represent clients in court daily.",
# )

# # 32. PRESENT_SIMPLE_LAW_B2_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_LAW_B2_TYPE1_GROUPB",
#     level="B2",
#     template_type="type_1",
#     domain="law",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["the lawyer", "he", "she"],
#         "VERB": {
#             "represents": {
#                 "correct_forms": ["represents"],
#                 "wrong_forms": ["represent", "represented", "is representing"],
#                 "article_objects": ["clients", "defendants", "plaintiffs"],
#                 "distractor": "represents faithfully",
#             },
#             "defends": {
#                 "correct_forms": ["defends"],
#                 "wrong_forms": ["defend", "defended", "is defending"],
#                 "article_objects": ["cases", "rights", "interests"],
#                 "distractor": "defends tenaciously",
#             },
#             "prosecutes": {
#                 "correct_forms": ["prosecutes"],
#                 "wrong_forms": ["prosecute", "prosecuted", "is prosecuting"],
#                 "article_objects": ["offenders", "criminals", "cases"],
#                 "distractor": "prosecutes relentlessly",
#             },
#             "advises": {
#                 "correct_forms": ["advises"],
#                 "wrong_forms": ["advise", "advised", "is advising"],
#                 "article_objects": ["clients", "organizations", "corporations"],
#                 "distractor": "advises expertly",
#             },
#         },
#         "ARTICLE_OBJ": ["clients", "cases", "defendants", "organizations"],
#         "PREP_PLACE": ["in court", "at the office", "during trials"],
#         "TIME": ["daily", "regularly", "frequently"],
#     },
#     explanation="Group B in legal context with -s form.",
#     example="The attorney defends cases in court regularly.",
# )

# # 33. PRESENT_SIMPLE_POLITICS_B2_TYPE2_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_POLITICS_B2_TYPE2_GROUPA",
#     level="B2",
#     template_type="type_2",
#     domain="politics",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME} because {REASON}.",
#     chunks={
#         "SUBJ": ["politicians", "they", "we"],
#         "VERB": {
#             "support": {
#                 "correct_forms": ["don't support"],
#                 "wrong_forms": ["doesn't support", "didn't support", "are not supporting"],
#                 "article_objects": ["policies", "reforms", "initiatives"],
#                 "distractor": "don't oppose",
#             },
#             "implement": {
#                 "correct_forms": ["don't implement"],
#                 "wrong_forms": ["doesn't implement", "didn't implement", "are not implementing"],
#                 "article_objects": ["laws", "changes", "measures"],
#                 "distractor": "don't introduce",
#             },
#             "propose": {
#                 "correct_forms": ["don't propose"],
#                 "wrong_forms": ["doesn't propose", "didn't propose", "are not proposing"],
#                 "article_objects": ["bills", "amendments", "solutions"],
#                 "distractor": "don't suggest",
#             },
#             "approve": {
#                 "correct_forms": ["don't approve"],
#                 "wrong_forms": ["doesn't approve", "didn't approve", "are not approving"],
#                 "article_objects": ["budgets", "legislation", "decisions"],
#                 "distractor": "don't authorize",
#             },
#         },
#         "ARTICLE_OBJ": ["policies", "laws", "bills", "budgets"],
#         "PREP_TIME": ["in parliament", "at meetings", "during sessions"],
#         "REASON": ["it's controversial", "it's unpopular", "it's ineffective"],
#     },
#     explanation="B2 politics with reason clauses and negatives.",
#     example="Politicians don't support policies in parliament because it's controversial.",
# )

# # 34. PRESENT_SIMPLE_POLITICS_B2_TYPE2_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_POLITICS_B2_TYPE2_GROUPB",
#     level="B2",
#     template_type="type_2",
#     domain="politics",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME} because {REASON}.",
#     chunks={
#         "SUBJ": ["the politician", "he", "she"],
#         "VERB": {
#             "support": {
#                 "correct_forms": ["doesn't support"],
#                 "wrong_forms": ["don't support", "didn't support", "isn't supporting"],
#                 "article_objects": ["policies", "reforms", "initiatives"],
#                 "distractor": "doesn't oppose",
#             },
#             "implement": {
#                 "correct_forms": ["doesn't implement"],
#                 "wrong_forms": ["don't implement", "didn't implement", "isn't implementing"],
#                 "article_objects": ["laws", "changes", "measures"],
#                 "distractor": "doesn't introduce",
#             },
#             "propose": {
#                 "correct_forms": ["doesn't propose"],
#                 "wrong_forms": ["don't propose", "didn't propose", "isn't proposing"],
#                 "article_objects": ["bills", "amendments", "solutions"],
#                 "distractor": "doesn't suggest",
#             },
#             "approve": {
#                 "correct_forms": ["doesn't approve"],
#                 "wrong_forms": ["don't approve", "didn't approve", "isn't approving"],
#                 "article_objects": ["budgets", "legislation", "decisions"],
#                 "distractor": "doesn't authorize",
#             },
#         },
#         "ARTICLE_OBJ": ["policies", "laws", "bills", "budgets"],
#         "PREP_TIME": ["in parliament", "at meetings", "during sessions"],
#         "REASON": ["it's controversial", "it's unpopular", "it's ineffective"],
#     },
#     explanation="Group B negative with political context.",
#     example="She doesn't approve budgets at meetings because it's ineffective.",
# )

# # 35. PRESENT_SIMPLE_ECONOMICS_B2_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ECONOMICS_B2_TYPE1_GROUPA",
#     level="B2",
#     template_type="type_1",
#     domain="economics",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["economists", "analysts", "they"],
#         "VERB": {
#             "analyze": {
#                 "correct_forms": ["analyze"],
#                 "wrong_forms": ["analyzes", "analyzed", "are analyzing"],
#                 "article_objects": ["markets", "trends", "data"],
#                 "distractor": "analyze thoroughly",
#             },
#             "forecast": {
#                 "correct_forms": ["forecast"],
#                 "wrong_forms": ["forecasts", "forecasted", "are forecasting"],
#                 "article_objects": ["growth", "inflation", "recession"],
#                 "distractor": "forecast accurately",
#             },
#             "evaluate": {
#                 "correct_forms": ["evaluate"],
#                 "wrong_forms": ["evaluates", "evaluated", "are evaluating"],
#                 "article_objects": ["policies", "strategies", "outcomes"],
#                 "distractor": "evaluate carefully",
#             },
#             "monitor": {
#                 "correct_forms": ["monitor"],
#                 "wrong_forms": ["monitors", "monitored", "are monitoring"],
#                 "article_objects": ["indicators", "rates", "indices"],
#                 "distractor": "monitor closely",
#             },
#         },
#         "ARTICLE_OBJ": ["markets", "growth", "policies", "indicators"],
#         "PREP_PLACE": ["in the markets", "in research", "at institutions"],
#         "FREQUENCY": ["daily", "regularly", "constantly"],
#     },
#     explanation="B2 economics with sophisticated vocabulary.",
#     example="Economists analyze markets in research regularly.",
# )

# # 36. PRESENT_SIMPLE_ECONOMICS_B2_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ECONOMICS_B2_TYPE1_GROUPB",
#     level="B2",
#     template_type="type_1",
#     domain="economics",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["the economist", "he", "she"],
#         "VERB": {
#             "analyzes": {
#                 "correct_forms": ["analyzes"],
#                 "wrong_forms": ["analyze", "analyzed", "is analyzing"],
#                 "article_objects": ["markets", "trends", "data"],
#                 "distractor": "analyzes objectively",
#             },
#             "forecasts": {
#                 "correct_forms": ["forecasts"],
#                 "wrong_forms": ["forecast", "forecasted", "is forecasting"],
#                 "article_objects": ["growth", "inflation", "recession"],
#                 "distractor": "forecasts precisely",
#             },
#             "evaluates": {
#                 "correct_forms": ["evaluates"],
#                 "wrong_forms": ["evaluate", "evaluated", "is evaluating"],
#                 "article_objects": ["policies", "strategies", "outcomes"],
#                 "distractor": "evaluates judiciously",
#             },
#             "monitors": {
#                 "correct_forms": ["monitors"],
#                 "wrong_forms": ["monitor", "monitored", "is monitoring"],
#                 "article_objects": ["indicators", "rates", "indices"],
#                 "distractor": "monitors vigilantly",
#             },
#         },
#         "ARTICLE_OBJ": ["markets", "growth", "policies", "indicators"],
#         "PREP_PLACE": ["in the markets", "in research", "at institutions"],
#         "FREQUENCY": ["daily", "regularly", "constantly"],
#     },
#     explanation="Group B in economics with -s form.",
#     example="She forecasts growth at institutions daily.",
# )

# # 37. PRESENT_SIMPLE_ARCHITECTURE_B2_TYPE3_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ARCHITECTURE_B2_TYPE3_GROUPA",
#     level="B2",
#     template_type="type_3",
#     domain="architecture",
#     subject_group="group_a",
#     template="{SUBJ} ____ {BASE_VERB} {ARTICLE_OBJ} {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["architects", "designers", "they"],
#         "AUX": "don't",
#         "BASE_VERB": ["design", "construct", "renovate", "plan"],
#         "ARTICLE_OBJ": ["buildings", "structures", "spaces", "projects"],
#         "PREP_PLACE": ["in urban areas", "in residential zones", "downtown"],
#         "TIME": ["without consultation", "hastily", "carelessly"],
#     },
#     explanation="Type 3 B2: Tests auxiliary selection with architecture context.",
#     example="Architects don't design buildings downtown carelessly.",
# )

# # 38. PRESENT_SIMPLE_ARCHITECTURE_B2_TYPE3_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_ARCHITECTURE_B2_TYPE3_GROUPB",
#     level="B2",
#     template_type="type_3",
#     domain="architecture",
#     subject_group="group_b",
#     template="{SUBJ} ____ {BASE_VERB} {ARTICLE_OBJ} {PREP_PLACE} {TIME}.",
#     chunks={
#         "SUBJ": ["the architect", "he", "she"],
#         "AUX": "doesn't",
#         "BASE_VERB": ["design", "construct", "renovate", "plan"],
#         "ARTICLE_OBJ": ["buildings", "structures", "spaces", "projects"],
#         "PREP_PLACE": ["in urban areas", "in residential zones", "downtown"],
#         "TIME": ["without consultation", "hastily", "carelessly"],
#     },
#     explanation="Type 3 Group B: doesn't + base verb in architecture.",
#     example="She doesn't renovate structures downtown hastily.",
# )

# # 39. PRESENT_SIMPLE_LITERATURE_B2_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_LITERATURE_B2_TYPE1_GROUPA",
#     level="B2",
#     template_type="type_1",
#     domain="literature",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME} because {REASON}.",
#     chunks={
#         "SUBJ": ["authors", "writers", "they"],
#         "VERB": {
#             "write": {
#                 "correct_forms": ["write"],
#                 "wrong_forms": ["writes", "wrote", "are writing"],
#                 "article_objects": ["novels", "essays", "poetry"],
#                 "distractor": "write beautifully",
#             },
#             "publish": {
#                 "correct_forms": ["publish"],
#                 "wrong_forms": ["publishes", "published", "are publishing"],
#                 "article_objects": ["books", "articles", "works"],
#                 "distractor": "publish regularly",
#             },
#             "revise": {
#                 "correct_forms": ["revise"],
#                 "wrong_forms": ["revises", "revised", "are revising"],
#                 "article_objects": ["manuscripts", "drafts", "texts"],
#                 "distractor": "revise thoroughly",
#             },
#             "critique": {
#                 "correct_forms": ["critique"],
#                 "wrong_forms": ["critiques", "critiqued", "are critiquing"],
#                 "article_objects": ["works", "pieces", "publications"],
#                 "distractor": "critique harshly",
#             },
#         },
#         "ARTICLE_OBJ": ["novels", "books", "manuscripts", "works"],
#         "PREP_TIME": ["every year", "regularly", "frequently"],
#         "REASON": ["readers demand it", "it's their passion", "the market requires it"],
#     },
#     explanation="B2 literature with reason clauses.",
#     example="Authors write novels regularly because readers demand it.",
# )

# # 40. PRESENT_SIMPLE_LITERATURE_B2_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_LITERATURE_B2_TYPE1_GROUPB",
#     level="B2",
#     template_type="type_1",
#     domain="literature",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_TIME} because {REASON}.",
#     chunks={
#         "SUBJ": ["the author", "he", "she"],
#         "VERB": {
#             "writes": {
#                 "correct_forms": ["writes"],
#                 "wrong_forms": ["write", "wrote", "is writing"],
#                 "article_objects": ["novels", "essays", "poetry"],
#                 "distractor": "writes elegantly",
#             },
#             "publishes": {
#                 "correct_forms": ["publishes"],
#                 "wrong_forms": ["publish", "published", "is publishing"],
#                 "article_objects": ["books", "articles", "works"],
#                 "distractor": "publishes annually",
#             },
#             "revises": {
#                 "correct_forms": ["revises"],
#                 "wrong_forms": ["revise", "revised", "is revising"],
#                 "article_objects": ["manuscripts", "drafts", "texts"],
#                 "distractor": "revises meticulously",
#             },
#             "critiques": {
#                 "correct_forms": ["critiques"],
#                 "wrong_forms": ["critique", "critiqued", "is critiquing"],
#                 "article_objects": ["works", "pieces", "publications"],
#                 "distractor": "critiques constructively",
#             },
#         },
#         "ARTICLE_OBJ": ["novels", "books", "manuscripts", "works"],
#         "PREP_TIME": ["every year", "regularly", "frequently"],
#         "REASON": ["readers demand it", "it's their passion", "the market requires it"],
#     },
#     explanation="Group B in literature with -s form.",
#     example="She publishes books regularly because the market requires it.",
# )

# print("=== B2 LEVEL COMPLETE (10 patterns) ===")

# # C1 LEVEL PATTERNS (10 patterns)

# # 41. PRESENT_SIMPLE_REALESTATE_C1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_REALESTATE_C1_TYPE1_GROUPA",
#     level="C1",
#     template_type="type_1",
#     domain="real_estate",
#     subject_group="group_a",
#     template="{PREP_TIME}, {SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} because {REASON}.",
#     chunks={
#         "SUBJ": ["investors", "developers", "they"],
#         "VERB": {
#             "acquire": {
#                 "correct_forms": ["acquire"],
#                 "wrong_forms": ["acquires", "acquired", "are acquiring"],
#                 "article_objects": ["properties", "portfolios", "assets"],
#                 "distractor": "acquire cautiously",
#             },
#             "develop": {
#                 "correct_forms": ["develop"],
#                 "wrong_forms": ["develops", "developed", "are developing"],
#                 "article_objects": ["projects", "sites", "infrastructure"],
#                 "distractor": "develop rapidly",
#             },
#             "lease": {
#                 "correct_forms": ["lease"],
#                 "wrong_forms": ["leases", "leased", "are leasing"],
#                 "article_objects": ["spaces", "units", "properties"],
#                 "distractor": "lease generously",
#             },
#             "appraise": {
#                 "correct_forms": ["appraise"],
#                 "wrong_forms": ["appraises", "appraised", "are appraising"],
#                 "article_objects": ["valuations", "assessments", "properties"],
#                 "distractor": "appraise fairly",
#             },
#         },
#         "PREP_TIME": ["Currently", "Increasingly", "Strategically", "Typically"],
#         "ARTICLE_OBJ": ["properties", "projects", "spaces", "assets"],
#         "PREP_PLACE": ["in prime locations", "in emerging markets", "downtown"],
#         "REASON": ["it's profitable", "demand is high", "location is strategic"],
#     },
#     explanation="C1 real estate with fronted adverbial and complex structure.",
#     example="Currently, investors acquire properties in prime locations because it's profitable.",
# )

# # 42. PRESENT_SIMPLE_REALESTATE_C1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_REALESTATE_C1_TYPE1_GROUPB",
#     level="C1",
#     template_type="type_1",
#     domain="real_estate",
#     subject_group="group_b",
#     template="{PREP_TIME}, {SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} because {REASON}.",
#     chunks={
#         "SUBJ": ["the investor", "he", "she"],
#         "VERB": {
#             "acquires": {
#                 "correct_forms": ["acquires"],
#                 "wrong_forms": ["acquire", "acquired", "is acquiring"],
#                 "article_objects": ["properties", "portfolios", "assets"],
#                 "distractor": "acquires meticulously",
#             },
#             "develops": {
#                 "correct_forms": ["develops"],
#                 "wrong_forms": ["develop", "developed", "is developing"],
#                 "article_objects": ["projects", "sites", "infrastructure"],
#                 "distractor": "develops expeditiously",
#             },
#             "leases": {
#                 "correct_forms": ["leases"],
#                 "wrong_forms": ["lease", "leased", "is leasing"],
#                 "article_objects": ["spaces", "units", "properties"],
#                 "distractor": "leases selectively",
#             },
#             "appraises": {
#                 "correct_forms": ["appraises"],
#                 "wrong_forms": ["appraise", "appraised", "is appraising"],
#                 "article_objects": ["valuations", "assessments", "properties"],
#                 "distractor": "appraises conservatively",
#             },
#         },
#         "PREP_TIME": ["Currently", "Increasingly", "Strategically", "Typically"],
#         "ARTICLE_OBJ": ["properties", "projects", "spaces", "assets"],
#         "PREP_PLACE": ["in prime locations", "in emerging markets", "downtown"],
#         "REASON": ["it's profitable", "demand is high", "location is strategic"],
#     },
#     explanation="C1 Group B in real estate with -s form.",
#     example="Strategically, she develops projects downtown because location is strategic.",
# )

# # 43. PRESENT_SIMPLE_AUTOMOTIVE_C1_TYPE2_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_AUTOMOTIVE_C1_TYPE2_GROUPA",
#     level="C1",
#     template_type="type_2",
#     domain="automotive",
#     subject_group="group_a",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} {TIME} because {REASON}.",
#     chunks={
#         "SUBJ": ["manufacturers", "engineers", "they"],
#         "VERB": {
#             "manufacture": {
#                 "correct_forms": ["don't manufacture"],
#                 "wrong_forms": ["doesn't manufacture", "didn't manufacture", "are not manufacturing"],
#                 "article_objects": ["vehicles", "components", "prototypes"],
#                 "distractor": "don't produce",
#             },
#             "assemble": {
#                 "correct_forms": ["don't assemble"],
#                 "wrong_forms": ["doesn't assemble", "didn't assemble", "are not assembling"],
#                 "article_objects": ["cars", "engines", "units"],
#                 "distractor": "don't construct",
#             },
#             "test": {
#                 "correct_forms": ["don't test"],
#                 "wrong_forms": ["doesn't test", "didn't test", "are not testing"],
#                 "article_objects": ["vehicles", "systems", "prototypes"],
#                 "distractor": "don't examine",
#             },
#             "distribute": {
#                 "correct_forms": ["don't distribute"],
#                 "wrong_forms": ["doesn't distribute", "didn't distribute", "are not distributing"],
#                 "article_objects": ["vehicles", "models", "products"],
#                 "distractor": "don't market",
#             },
#         },
#         "ARTICLE_OBJ": ["vehicles", "cars", "engines", "prototypes"],
#         "PREP_PLACE": ["in factories", "at facilities", "on assembly lines"],
#         "TIME": ["without certification", "hastily", "without inspection"],
#         "REASON": ["safety standards require it", "regulations demand it", "liability concerns exist"],
#     },
#     explanation="C1 automotive negative with multiple complex clauses.",
#     example="Manufacturers don't distribute vehicles at facilities without certification because regulations demand it.",
# )

# # 44. PRESENT_SIMPLE_AUTOMOTIVE_C1_TYPE2_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_AUTOMOTIVE_C1_TYPE2_GROUPB",
#     level="C1",
#     template_type="type_2",
#     domain="automotive",
#     subject_group="group_b",
#     template="{SUBJ} ____ {ARTICLE_OBJ} {PREP_PLACE} {TIME} because {REASON}.",
#     chunks={
#         "SUBJ": ["the manufacturer", "he", "she"],
#         "VERB": {
#             "manufacture": {
#                 "correct_forms": ["doesn't manufacture"],
#                 "wrong_forms": ["don't manufacture", "didn't manufacture", "isn't manufacturing"],
#                 "article_objects": ["vehicles", "components", "prototypes"],
#                 "distractor": "doesn't produce",
#             },
#             "assemble": {
#                 "correct_forms": ["doesn't assemble"],
#                 "wrong_forms": ["don't assemble", "didn't assemble", "isn't assembling"],
#                 "article_objects": ["cars", "engines", "units"],
#                 "distractor": "doesn't construct",
#             },
#             "test": {
#                 "correct_forms": ["doesn't test"],
#                 "wrong_forms": ["don't test", "didn't test", "isn't testing"],
#                 "article_objects": ["vehicles", "systems", "prototypes"],
#                 "distractor": "doesn't examine",
#             },
#             "distribute": {
#                 "correct_forms": ["doesn't distribute"],
#                 "wrong_forms": ["don't distribute", "didn't distribute", "isn't distributing"],
#                 "article_objects": ["vehicles", "models", "products"],
#                 "distractor": "doesn't market",
#             },
#         },
#         "ARTICLE_OBJ": ["vehicles", "cars", "engines", "prototypes"],
#         "PREP_PLACE": ["in factories", "at facilities", "on assembly lines"],
#         "TIME": ["without certification", "hastily", "without inspection"],
#         "REASON": ["safety standards require it", "regulations demand it", "liability concerns exist"],
#     },
#     explanation="C1 Group B automotive negative.",
#     example="The engineer doesn't test prototypes at facilities without certification because regulations demand it.",
# )

# # 45. PRESENT_SIMPLE_DESIGN_C1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_DESIGN_C1_TYPE1_GROUPA",
#     level="C1",
#     template_type="type_1",
#     domain="design",
#     subject_group="group_a",
#     template="{SUBJ}, who {RELATIVE_CLAUSE}, ____ {ARTICLE_OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["designers", "professionals", "they"],
#         "RELATIVE_CLAUSE": [
#             "specialize in branding",
#             "work remotely",
#             "focus on UX",
#             "collaborate with clients",
#         ],
#         "VERB": {
#             "conceptualize": {
#                 "correct_forms": ["conceptualize"],
#                 "wrong_forms": ["conceptualizes", "conceptualized", "are conceptualizing"],
#                 "article_objects": ["solutions", "systems", "frameworks"],
#                 "distractor": "conceptualize abstractly",
#             },
#             "prototype": {
#                 "correct_forms": ["prototype"],
#                 "wrong_forms": ["prototypes", "prototyped", "are prototyping"],
#                 "article_objects": ["models", "interfaces", "iterations"],
#                 "distractor": "prototype rapidly",
#             },
#             "refine": {
#                 "correct_forms": ["refine"],
#                 "wrong_forms": ["refines", "refined", "are refining"],
#                 "article_objects": ["concepts", "designs", "details"],
#                 "distractor": "refine meticulously",
#             },
#             "implement": {
#                 "correct_forms": ["implement"],
#                 "wrong_forms": ["implements", "implemented", "are implementing"],
#                 "article_objects": ["changes", "features", "solutions"],
#                 "distractor": "implement pragmatically",
#             },
#         },
#         "ARTICLE_OBJ": ["solutions", "models", "concepts", "changes"],
#         "PREP_TIME": ["throughout development", "during sprints", "in iterations"],
#     },
#     explanation="C1 design with relative clause introducing subject expertise.",
#     example="Designers, who specialize in branding, conceptualize solutions throughout development.",
# )

# # 46. PRESENT_SIMPLE_DESIGN_C1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_DESIGN_C1_TYPE1_GROUPB",
#     level="C1",
#     template_type="type_1",
#     domain="design",
#     subject_group="group_b",
#     template="{SUBJ}, who {RELATIVE_CLAUSE}, ____ {ARTICLE_OBJ} {PREP_TIME}.",
#     chunks={
#         "SUBJ": ["the designer", "he", "she"],
#         "RELATIVE_CLAUSE": [
#             "specializes in branding",
#             "works remotely",
#             "focuses on UX",
#             "collaborates with clients",
#         ],
#         "VERB": {
#             "conceptualizes": {
#                 "correct_forms": ["conceptualizes"],
#                 "wrong_forms": ["conceptualize", "conceptualized", "is conceptualizing"],
#                 "article_objects": ["solutions", "systems", "frameworks"],
#                 "distractor": "conceptualizes brilliantly",
#             },
#             "prototypes": {
#                 "correct_forms": ["prototypes"],
#                 "wrong_forms": ["prototype", "prototyped", "is prototyping"],
#                 "article_objects": ["models", "interfaces", "iterations"],
#                 "distractor": "prototypes innovatively",
#             },
#             "refines": {
#                 "correct_forms": ["refines"],
#                 "wrong_forms": ["refine", "refined", "is refining"],
#                 "article_objects": ["concepts", "designs", "details"],
#                 "distractor": "refines elegantly",
#             },
#             "implements": {
#                 "correct_forms": ["implements"],
#                 "wrong_forms": ["implement", "implemented", "is implementing"],
#                 "article_objects": ["changes", "features", "solutions"],
#                 "distractor": "implements efficiently",
#             },
#         },
#         "ARTICLE_OBJ": ["solutions", "models", "concepts", "changes"],
#         "PREP_TIME": ["throughout development", "during sprints", "in iterations"],
#     },
#     explanation="C1 Group B design with relative clause and -s form.",
#     example="The designer, who focuses on UX, prototypes models during sprints.",
# )

# # 47. PRESENT_SIMPLE_PHOTOGRAPHY_C1_TYPE3_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_PHOTOGRAPHY_C1_TYPE3_GROUPA",
#     level="C1",
#     template_type="type_3",
#     domain="photography",
#     subject_group="group_a",
#     template="{PREP_TIME}, {SUBJ} ____ {BASE_VERB} {ARTICLE_OBJ} {PREP_PLACE} because {REASON}.",
#     chunks={
#         "SUBJ": ["photographers", "professionals", "they"],
#         "AUX": "don't",
#         "BASE_VERB": ["manipulate", "enhance", "edit", "retouch", "compress"],
#         "ARTICLE_OBJ": ["images", "photos", "files", "content"],
#         "PREP_PLACE": ["in post-production", "during editing", "for publication"],
#         "REASON": [
#             "authenticity matters",
#             "credibility is essential",
#             "ethical standards apply",
#         ],
#         "PREP_TIME": ["Professionally", "Conscientiously", "Rigorously", "Consistently"],
#     },
#     explanation="C1 Type 3 with fronted adverbial and sophisticated reasoning.",
#     example="Professionally, photographers don't manipulate images during editing because authenticity matters.",
# )

# # 48. PRESENT_SIMPLE_PHOTOGRAPHY_C1_TYPE3_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_PHOTOGRAPHY_C1_TYPE3_GROUPB",
#     level="C1",
#     template_type="type_3",
#     domain="photography",
#     subject_group="group_b",
#     template="{PREP_TIME}, {SUBJ} ____ {BASE_VERB} {ARTICLE_OBJ} {PREP_PLACE} because {REASON}.",
#     chunks={
#         "SUBJ": ["the photographer", "he", "she"],
#         "AUX": "doesn't",
#         "BASE_VERB": ["manipulate", "enhance", "edit", "retouch", "compress"],
#         "ARTICLE_OBJ": ["images", "photos", "files", "content"],
#         "PREP_PLACE": ["in post-production", "during editing", "for publication"],
#         "REASON": [
#             "authenticity matters",
#             "credibility is essential",
#             "ethical standards apply",
#         ],
#         "PREP_TIME": ["Professionally", "Conscientiously", "Rigorously", "Consistently"],
#     },
#     explanation="C1 Group B Type 3.",
#     example="Rigorously, she doesn't retouch photos for publication because credibility is essential.",
# )

# # 49. PRESENT_SIMPLE_FASHION_C1_TYPE1_GROUPA
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_FASHION_C1_TYPE1_GROUPA",
#     level="C1",
#     template_type="type_1",
#     domain="fashion",
#     subject_group="group_a",
#     template="{GERUND}, {SUBJ} ____ {PREP_PLACE} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["designers", "brands", "they"],
#         "GERUND": [
#             "Following trends",
#             "Analyzing consumer behavior",
#             "Forecasting styles",
#             "Curating collections",
#         ],
#         "VERB": {
#             "showcase": {
#                 "correct_forms": ["showcase"],
#                 "wrong_forms": ["showcases", "showcased", "are showcasing"],
#                 "places": ["in showrooms", "at presentations", "online"],
#                 "distractor": "showcase elegantly",
#             },
#             "launch": {
#                 "correct_forms": ["launch"],
#                 "wrong_forms": ["launches", "launched", "are launching"],
#                 "places": ["in stores", "globally", "seasonally"],
#                 "distractor": "launch successfully",
#             },
#             "promote": {
#                 "correct_forms": ["promote"],
#                 "wrong_forms": ["promotes", "promoted", "are promoting"],
#                 "places": ["on social media", "in marketing", "through campaigns"],
#                 "distractor": "promote aggressively",
#             },
#             "distribute": {
#                 "correct_forms": ["distribute"],
#                 "wrong_forms": ["distributes", "distributed", "are distributing"],
#                 "places": ["to retailers", "internationally", "through channels"],
#                 "distractor": "distribute efficiently",
#             },
#         },
#         "PREP_PLACE": ["in showrooms", "in stores", "online"],
#         "FREQUENCY": ["seasonally", "quarterly", "annually"],
#     },
#     explanation="C1 with gerund fronted adverbial.",
#     example="Following trends, designers showcase collections in showrooms seasonally.",
# )

# # 50. PRESENT_SIMPLE_FASHION_C1_TYPE1_GROUPB
# create_pattern(
#     pattern_id="PRESENT_SIMPLE_FASHION_C1_TYPE1_GROUPB",
#     level="C1",
#     template_type="type_1",
#     domain="fashion",
#     subject_group="group_b",
#     template="{GERUND}, {SUBJ} ____ {PREP_PLACE} {FREQUENCY}.",
#     chunks={
#         "SUBJ": ["the designer", "he", "she"],
#         "GERUND": [
#             "Following trends",
#             "Analyzing consumer behavior",
#             "Forecasting styles",
#             "Curating collections",
#         ],
#         "VERB": {
#             "showcases": {
#                 "correct_forms": ["showcases"],
#                 "wrong_forms": ["showcase", "showcased", "is showcasing"],
#                 "places": ["in showrooms", "at presentations", "online"],
#                 "distractor": "showcases beautifully",
#             },
#             "launches": {
#                 "correct_forms": ["launches"],
#                 "wrong_forms": ["launch", "launched", "is launching"],
#                 "places": ["in stores", "globally", "seasonally"],
#                 "distractor": "launches triumphantly",
#             },
#             "promotes": {
#                 "correct_forms": ["promotes"],
#                 "wrong_forms": ["promote", "promoted", "is promoting"],
#                 "places": ["on social media", "in marketing", "through campaigns"],
#                 "distractor": "promotes strategically",
#             },
#             "distributes": {
#                 "correct_forms": ["distributes"],
#                 "wrong_forms": ["distribute", "distributed", "is distributing"],
#                 "places": ["to retailers", "internationally", "through channels"],
#                 "distractor": "distributes widely",
#             },
#         },
#         "PREP_PLACE": ["in showrooms", "in stores", "online"],
#         "FREQUENCY": ["seasonally", "quarterly", "annually"],
#     },
#     explanation="C1 Group B with gerund adverbial.",
#     example="Analyzing consumer behavior, she launches collections online quarterly.",
# )

# print("=== C1 LEVEL COMPLETE (10 patterns) ===")
# print("\n" + "=" * 60)
# print("SUCCESS: All 50 present simple patterns created!")
# print("=" * 60)
