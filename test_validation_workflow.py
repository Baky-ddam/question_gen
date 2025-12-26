"""
Test Validation Workflow
Tests the validation process for PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPA pattern
"""

import json
import random
from typing import Dict, List, Tuple

def load_pattern(pattern_path: str) -> Dict:
    """Load a pattern JSON file."""
    with open(pattern_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_questions(pattern: Dict, num_per_verb: int = 3) -> List[Dict]:
    """Generate sample questions from a pattern."""
    questions = []

    # Get the template
    template = pattern['template']
    chunks = pattern['chunks']

    # Find the blank chunk (VERB in this case)
    verb_chunk = chunks.get('VERB', {})
    if not verb_chunk:
        return []

    # Get other chunks
    subjects = chunks.get('SUBJ', [])

    # Generate questions for each verb
    for verb, verb_data in verb_chunk.items():
        correct_forms = verb_data.get('correct_forms', [])
        wrong_forms = verb_data.get('wrong_forms', [])
        objects = verb_data.get('objects', [])
        distractor = verb_data.get('distractor', '')

        # Generate N questions per verb
        for i in range(min(num_per_verb, len(subjects) * len(objects))):
            subj = random.choice(subjects)
            obj = random.choice(objects) if objects else ''

            # Create the question
            question_text = template.replace('{SUBJ}', subj).replace('{OBJ}', obj)

            # Build answer options
            correct = random.choice(correct_forms) if correct_forms else ''
            options = [correct] + wrong_forms + [distractor]
            random.shuffle(options)

            question = {
                'id': f"{pattern['pattern_id']}_{verb}_{i+1}",
                'text': question_text,
                'options': options,
                'correct_answer': correct,
                'verb': verb,
                'subject': subj,
                'object': obj,
                'distractor': distractor
            }

            questions.append(question)

    return questions

def validate_question(question: Dict, pattern: Dict) -> Tuple[bool, List[str]]:
    """
    Validate a single question.
    Returns (is_valid, list_of_issues)
    """
    issues = []

    # Check 1: Does it have exactly 5 options?
    if len(question['options']) != 5:
        issues.append(f"Expected 5 options, got {len(question['options'])}")

    # Check 2: Is the correct answer in the options?
    if question['correct_answer'] not in question['options']:
        issues.append("Correct answer not in options")

    # Check 3: Are all options unique?
    if len(question['options']) != len(set(question['options'])):
        issues.append("Duplicate options found")

    # Check 4: Does the question have a blank?
    if '____' not in question['text']:
        issues.append("No blank (____) in question text")

    # Check 5: Is the distractor different from wrong forms?
    verb_data = pattern['chunks']['VERB'][question['verb']]
    wrong_forms = verb_data.get('wrong_forms', [])
    distractor = question['distractor']

    if distractor in wrong_forms:
        issues.append(f"Distractor '{distractor}' duplicates a wrong form")

    # Check 6: Basic naturalness - does the sentence make sense?
    # (This is a simple check - just verify subject-object pairing seems reasonable)
    if not question['object']:
        issues.append("No object found in generated question")

    return (len(issues) == 0, issues)

def validate_pattern_structure(pattern: Dict) -> Tuple[bool, List[str]]:
    """
    Validate the pattern JSON structure itself.
    Returns (is_valid, list_of_issues)
    """
    issues = []

    # Required top-level fields
    required_fields = ['pattern_id', 'focus', 'level', 'domain', 'category',
                      'template_type', 'template', 'example', 'explanation', 'chunks']

    for field in required_fields:
        if field not in pattern:
            issues.append(f"Missing required field: {field}")

    # Check template has exactly one blank
    template = pattern.get('template', '')
    blank_count = template.count('____')
    if blank_count != 1:
        issues.append(f"Template should have exactly 1 blank, found {blank_count}")

    # Check VERB chunk structure
    verb_chunk = pattern.get('chunks', {}).get('VERB', {})
    if not verb_chunk:
        issues.append("No VERB chunk found")
    else:
        for verb, verb_data in verb_chunk.items():
            # Check required fields in verb data
            if 'correct_forms' not in verb_data:
                issues.append(f"Verb '{verb}' missing 'correct_forms'")
            if 'wrong_forms' not in verb_data:
                issues.append(f"Verb '{verb}' missing 'wrong_forms'")
            elif len(verb_data['wrong_forms']) != 3:
                issues.append(f"Verb '{verb}' should have exactly 3 wrong_forms, has {len(verb_data['wrong_forms'])}")
            if 'distractor' not in verb_data:
                issues.append(f"Verb '{verb}' missing 'distractor'")
            if 'objects' not in verb_data:
                issues.append(f"Verb '{verb}' missing 'objects'")

    # Check subject grouping
    if pattern.get('subject_group') == 'group_a':
        subjects = pattern.get('chunks', {}).get('SUBJ', [])
        expected_group_a = ['I', 'you', 'they']
        # Check if subjects match group_a expectations
        for subj in subjects:
            if subj not in ['I', 'you', 'we', 'they']:
                issues.append(f"Subject '{subj}' not appropriate for group_a")

    return (len(issues) == 0, issues)

def run_validation_test():
    """Run the full validation test."""
    print("=" * 70)
    print("VALIDATION WORKFLOW TEST")
    print("=" * 70)
    print()

    pattern_path = '/Users/baky/Documents/edu_mining/question_generator/pattern/present_simple/PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPA.json'

    # Step 1: Load pattern
    print("Step 1: Loading pattern...")
    try:
        pattern = load_pattern(pattern_path)
        print(f"✓ Pattern loaded: {pattern['pattern_id']}")
        print(f"  Domain: {pattern['domain']}")
        print(f"  Level: {pattern['level']}")
        print(f"  Template: {pattern['template']}")
        print()
    except Exception as e:
        print(f"✗ Failed to load pattern: {e}")
        return

    # Step 2: Validate pattern structure
    print("Step 2: Validating pattern structure...")
    is_valid, issues = validate_pattern_structure(pattern)
    if is_valid:
        print("✓ Pattern structure is valid")
    else:
        print("✗ Pattern structure has issues:")
        for issue in issues:
            print(f"  - {issue}")
    print()

    # Step 3: Generate sample questions
    print("Step 3: Generating sample questions (3-5 per verb)...")
    questions = generate_questions(pattern, num_per_verb=3)
    print(f"✓ Generated {len(questions)} questions")
    print()

    # Step 4: Display sample questions
    print("Step 4: Sample generated questions:")
    print("-" * 70)
    for i, q in enumerate(questions[:5], 1):  # Show first 5
        print(f"\nQuestion {i}: {q['text']}")
        print(f"Options: {', '.join(q['options'])}")
        print(f"Correct: {q['correct_answer']}")
        print(f"Verb: {q['verb']}, Subject: {q['subject']}, Object: {q['object']}")
    print()
    print("-" * 70)
    print()

    # Step 5: Validate each question
    print("Step 5: Validating generated questions...")
    validation_results = []
    for q in questions:
        is_valid, issues = validate_question(q, pattern)
        validation_results.append((q, is_valid, issues))

    # Count results
    valid_count = sum(1 for _, is_valid, _ in validation_results if is_valid)
    invalid_count = len(validation_results) - valid_count

    print(f"✓ Valid questions: {valid_count}/{len(questions)}")
    if invalid_count > 0:
        print(f"✗ Invalid questions: {invalid_count}/{len(questions)}")
        print("\nIssues found:")
        for q, is_valid, issues in validation_results:
            if not is_valid:
                print(f"  Question '{q['id']}':")
                for issue in issues:
                    print(f"    - {issue}")
    print()

    # Step 6: Subject grouping validation
    print("Step 6: Subject grouping validation...")
    verb_chunk = pattern['chunks']['VERB']
    subjects = pattern['chunks']['SUBJ']

    # For group_a present_simple, correct form should be base verb
    print(f"Subject group: {pattern.get('subject_group', 'not specified')}")
    print(f"Subjects: {', '.join(subjects)}")
    print("Checking verb forms for group_a (should use base form):")

    all_correct = True
    for verb, verb_data in verb_chunk.items():
        correct_forms = verb_data['correct_forms']
        # For group_a, correct form should be base verb (no -s)
        if correct_forms[0] == verb:
            print(f"  ✓ '{verb}' → correct form is '{correct_forms[0]}' (base form)")
        else:
            print(f"  ✗ '{verb}' → correct form is '{correct_forms[0]}' (expected base form)")
            all_correct = False

    if all_correct:
        print("✓ All verb forms match subject group requirements")
    print()

    # Final summary
    print("=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Pattern Structure: {'PASS ✓' if is_valid else 'FAIL ✗'}")
    print(f"Questions Generated: {len(questions)}")
    print(f"Questions Valid: {valid_count}/{len(questions)} ({100*valid_count/len(questions):.1f}%)")
    print(f"Subject Grouping: {'PASS ✓' if all_correct else 'FAIL ✗'}")
    print()

    if is_valid and invalid_count == 0 and all_correct:
        print("OVERALL: VALIDATION PASSED ✓")
    else:
        print("OVERALL: VALIDATION FAILED ✗")
    print("=" * 70)

if __name__ == '__main__':
    run_validation_test()
