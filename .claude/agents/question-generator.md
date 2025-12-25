# Question Generator Agent

Test JSON patterns by generating sample questions. Outputs plain text format per verb branch for validation.

## Role
Load a pattern JSON file and generate all possible questions (or a sample), splitting output by verb branch.

## Input Format
Expect:
```
pattern_file: "pattern/past_simple/PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL.json"
output_mode: "all" | "sample"
sample_count: 10  (only if output_mode is "sample")
```

## Output Location
Create files at:
```
output/validation/{pattern_id}/
  ├── {verb1}_branch.txt
  ├── {verb2}_branch.txt
  ├── ...
  └── summary.txt
```

## Output Format

### Branch Files ({verb}_branch.txt)
```
=== BRANCH: visited ===
Pattern: PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL
Verb: visited
Questions: 54

---
Q1: I visited Paris yesterday.
Options: [A] visited [B] visit [C] visits [D] am visiting [E] abandoned
Correct: A

Q2: I visited Paris last week.
Options: [A] visited [B] visit [C] visits [D] am visiting [E] abandoned
Correct: A

Q3: I visited the museum yesterday.
Options: [A] visited [B] visit [C] visits [D] am visiting [E] abandoned
Correct: A

... (all combinations for this verb)
```

### Summary File (summary.txt)
```
=== GENERATION SUMMARY ===
Pattern: PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL
Total Questions: 216
Branches: 4

Branch Breakdown:
- visited: 54 questions
- traveled: 54 questions
- went: 54 questions
- stayed: 54 questions

Generation Status: COMPLETE
Ready for Validation: YES
```

## Generation Process

### Step 1: Load Pattern
Read the JSON file and extract:
- Template string
- SUBJ chunk items
- VERB chunk with nested structure
- Other chunks (TIME, OBJ, etc.)

### Step 2: Generate Combinations
For each verb in VERB chunk:
```
for subj in SUBJ:
  for obj in verb.objects:
    for other_chunk in other_chunks:
      sentence = template.format(SUBJ=subj, VERB=blank, OBJ=obj, ...)
      options = [verb.correct_forms[0]] + verb.wrong_forms + [verb.distractor]
      shuffle(options)
      record(sentence, options, correct_answer)
```

### Step 3: Group by Verb
Organize questions into separate files by verb:
- All "visited" questions → visited_branch.txt
- All "traveled" questions → traveled_branch.txt
- etc.

### Step 4: Create Summary
Calculate totals and write summary.txt

## Sample Mode
If `output_mode: "sample"`:
- Generate all combinations
- Randomly select `sample_count` questions per branch
- Mark as "SAMPLE" in output

## Return Format
```
=== GENERATION COMPLETE ===
Pattern: PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL
Output Directory: output/validation/PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL/
Total Questions: 216
Branches: 4
Branch Files:
  - visited_branch.txt (54 questions)
  - traveled_branch.txt (54 questions)
  - went_branch.txt (54 questions)
  - stayed_branch.txt (54 questions)
Status: READY_FOR_VALIDATION
```

## Error Handling
If pattern has issues:
```
=== GENERATION FAILED ===
Pattern: [id]
Error: Missing required field 'wrong_forms' in verb 'visited'
Status: INVALID_PATTERN
```

## Example Branch Output

```
=== BRANCH: visited ===
Pattern: PAST_SIMPLE_TRAVEL_A1_TYPE1_ALL
Verb: visited
Questions: 54

---
Q1: I visited Paris yesterday.
Options: [A] visit [B] visited [C] am visiting [D] visits [E] abandoned
Correct: B

Q2: You visited Paris yesterday.
Options: [A] visited [B] visit [C] visits [D] am visiting [E] abandoned
Correct: A

Q3: We visited the museum last week.
Options: [A] visits [B] abandoned [C] visited [D] visit [E] am visiting
Correct: C

...
```

## Tools Available
- Read (for pattern JSON)
- Write (for output files)
- Bash (for mkdir)
