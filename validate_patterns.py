#!/usr/bin/env python3
"""
Pattern Validation Script
-------------------------
Generate ALL possible questions from each pattern file for validation.
This helps verify that all combinations make grammatical sense.

By default, skips surface variations (FREQUENCY, TIME, MANNER, PLACE) to avoid
redundant questions that differ only in adverbs/time expressions.

Usage:
    python validate_patterns.py --pattern-dir pattern/present_simple
    python validate_patterns.py --pattern-dir pattern/present_simple --pattern PRESENT_SIMPLE_FOOD_A1_TYPE1_GROUPA
    python validate_patterns.py --pattern-dir pattern/present_simple --output validation_results.txt
    python validate_patterns.py --pattern-dir pattern/present_simple --all-surface  # Include all variations
"""

import argparse
import json
import sys
import random
from pathlib import Path
from itertools import product
from typing import Dict, List, Tuple


class PatternValidator:
    """Generate all possible questions from a pattern for validation."""

    def __init__(self, skip_surface_chunks: bool = True):
        self.question_counter = 0
        self.skip_surface_chunks = skip_surface_chunks
        # Chunks that only add surface variation, not grammatical variation
        self.surface_chunk_names = ['FREQUENCY', 'TIME', 'MANNER', 'PLACE']

    def _is_blank_chunk(self, chunk_dict: Dict) -> bool:
        """
        Check if a chunk dictionary is a "blank chunk" (contains correct_forms, wrong_forms, etc.).

        Args:
            chunk_dict: Chunk dictionary to check

        Returns:
            True if this is a blank chunk (VERB, AUX, MODAL, etc.)
        """
        if not isinstance(chunk_dict, dict):
            return False

        # Check if at least one value has the required structure
        for value in chunk_dict.values():
            if isinstance(value, dict) and 'correct_forms' in value and 'wrong_forms' in value:
                return True

        return False

    def get_all_combinations(self, chunks: Dict) -> List[Dict]:
        """
        Generate all possible combinations of chunks.

        Args:
            chunks: Chunks dictionary from pattern

        Returns:
            List of all possible chunk combinations
        """
        # Collect all possible values for each chunk type
        chunk_options = {}

        for chunk_name, chunk_values in chunks.items():
            # Check if this is a blank chunk (VERB, AUX, MODAL, etc.)
            if isinstance(chunk_values, dict) and self._is_blank_chunk(chunk_values):
                # Blank chunk - need to create combinations for each item
                blank_combinations = []
                for item_name, item_data in chunk_values.items():
                    # For each item, combine correct_forms with objects
                    correct_forms = item_data.get('correct_forms', [])

                    # Check for different object field names
                    objects = []
                    if 'objects' in item_data and item_data['objects']:
                        objects = item_data['objects']
                    elif 'article_objects' in item_data and item_data['article_objects']:
                        objects = item_data['article_objects']
                    elif 'prep_objects' in item_data and item_data['prep_objects']:
                        objects = item_data['prep_objects']
                    else:
                        objects = ['']  # No objects for this item

                    for correct_form in correct_forms:
                        for obj in objects:
                            combo = {
                                chunk_name: item_name,  # Store as dynamic chunk name (VERB, AUX, etc.)
                                'CORRECT_FORM': correct_form,
                                'WRONG_FORMS': item_data.get('wrong_forms', []),
                                'DISTRACTOR': item_data.get('distractor', '')
                            }

                            # Add object to appropriate field
                            if 'article_objects' in item_data and item_data['article_objects']:
                                combo['ARTICLE_OBJ'] = obj
                            elif 'prep_objects' in item_data and item_data['prep_objects']:
                                combo['PREP_OBJ'] = obj
                            elif obj:  # Regular objects
                                combo['OBJ'] = obj

                            blank_combinations.append(combo)

                chunk_options['BLANK_COMBO'] = blank_combinations

            elif isinstance(chunk_values, list):
                # Simple list
                # If skip_surface_chunks is enabled and this is a surface chunk, only use first value
                if self.skip_surface_chunks and chunk_name in self.surface_chunk_names:
                    chunk_options[chunk_name] = chunk_values[:1]  # Only first value
                else:
                    chunk_options[chunk_name] = chunk_values

            elif isinstance(chunk_values, dict) and not self._is_blank_chunk(chunk_values):
                # Dictionary (but not a blank chunk) - flatten all values
                all_values = []
                for key, values in chunk_values.items():
                    if isinstance(values, list):
                        all_values.extend(values)
                    else:
                        all_values.append(values)
                chunk_options[chunk_name] = all_values

            elif isinstance(chunk_values, str):
                # Single string value
                chunk_options[chunk_name] = [chunk_values]

        # Generate all combinations
        if not chunk_options:
            return []

        # Get all keys and values
        keys = list(chunk_options.keys())
        value_lists = [chunk_options[k] for k in keys]

        # Create all combinations
        all_combinations = []
        for combination in product(*value_lists):
            combo_dict = {}
            for i, key in enumerate(keys):
                value = combination[i]
                if key == 'BLANK_COMBO' and isinstance(value, dict):
                    # Expand blank combo into separate fields
                    combo_dict.update(value)
                else:
                    combo_dict[key] = value

            all_combinations.append(combo_dict)

        return all_combinations

    def build_sentence(self, template: str, selected_chunks: Dict) -> str:
        """
        Build a sentence from template and selected chunks.

        Args:
            template: Template string with placeholders
            selected_chunks: Dictionary of chunk values

        Returns:
            Completed sentence
        """
        sentence = template

        # Replace all placeholders
        for placeholder, value in selected_chunks.items():
            placeholder_pattern = '{' + placeholder + '}'
            if placeholder_pattern in sentence:
                sentence = sentence.replace(placeholder_pattern, value)

        # Replace blank marker with correct form
        if 'CORRECT_FORM' in selected_chunks:
            sentence = sentence.replace('____', selected_chunks['CORRECT_FORM'])

        # Capitalize first letter
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]

        return sentence

    def generate_all_questions(self, pattern: Dict) -> List[Dict]:
        """
        Generate all possible questions from a pattern.

        Args:
            pattern: Pattern dictionary

        Returns:
            List of all possible questions
        """
        chunks = pattern.get('chunks', {})
        template = pattern.get('template', '')

        # Get all combinations
        all_combinations = self.get_all_combinations(chunks)

        questions = []
        for combo in all_combinations:
            self.question_counter += 1

            # Build sentence
            sentence = self.build_sentence(template, combo)

            # Get correct answer
            correct_answer = combo.get('CORRECT_FORM', '')

            # Build options (A-E)
            wrong_forms = combo.get('WRONG_FORMS', [])
            distractor = combo.get('DISTRACTOR', '')

            # Create all options
            all_options = [correct_answer]
            all_options.extend(wrong_forms[:3])  # Add 3 wrong forms
            if distractor:
                all_options.append(distractor)

            # Pad to 5 options if needed
            while len(all_options) < 5:
                all_options.append('N/A')

            # Create options dict
            options_dict = {
                chr(65 + i): option for i, option in enumerate(all_options[:5])
            }

            # Correct answer is always 'A' for validation purposes
            correct_letter = 'A'

            question = {
                'question_id': f"{pattern['pattern_id']}_Q{self.question_counter:04d}",
                'pattern_id': pattern['pattern_id'],
                'sentence': sentence,
                'options': options_dict,
                'correct_answer': correct_letter,
                'combination': combo,
            }

            questions.append(question)

        return questions

    def validate_pattern_file(self, filepath: Path) -> Tuple[Dict, List[Dict]]:
        """
        Validate a single pattern file.

        Args:
            filepath: Path to JSON pattern file

        Returns:
            Tuple of (pattern, questions)
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            pattern = json.load(f)

        questions = self.generate_all_questions(pattern)

        return pattern, questions

    def print_question(self, question: Dict, index: int):
        """Print a question in formatted style."""
        # print(f"\n{'='*80}")
        print(f"Question {index}: {question['question_id']}")
        # print(f"{'='*80}")
        print(f"\n{question['sentence']}\n")

        # Print options
        for letter in sorted(question['options'].keys()):
            marker = " ✓" if letter == question['correct_answer'] else ""
            print(f"  {letter}. {question['options'][letter]}{marker}")

        # Print combination details
        print(f"\nCombination: {question['combination']}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate all possible questions from patterns for validation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        '--pattern-dir',
        type=str,
        required=True,
        help='Directory containing pattern files (e.g., pattern/present_simple)'
    )

    parser.add_argument(
        '--pattern',
        type=str,
        help='Specific pattern file name (optional, validates all if not specified)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (optional, prints to console if not specified)'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Randomly sample N questions per pattern for display (optional)'
    )

    parser.add_argument(
        '--all-surface',
        action='store_true',
        help='Include all surface variations (FREQUENCY, TIME, etc.). Default: only first value'
    )

    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducible sampling (optional)'
    )

    args = parser.parse_args()

    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)

    # Find pattern files
    pattern_dir = Path(args.pattern_dir)
    if not pattern_dir.exists():
        print(f"Error: Directory not found: {pattern_dir}")
        return 1

    # Get JSON files
    if args.pattern:
        # Specific pattern
        json_files = list(pattern_dir.glob(f"{args.pattern}.json"))
        if not json_files:
            print(f"Error: Pattern not found: {args.pattern}")
            return 1
    else:
        # All patterns
        json_files = list(pattern_dir.glob("*.json"))

    if not json_files:
        print(f"Error: No JSON files found in {pattern_dir}")
        return 1

    print(f"\n{'='*80}")
    print(f"PATTERN VALIDATION")
    print(f"{'='*80}")
    print(f"Directory: {pattern_dir}")
    print(f"Files to validate: {len(json_files)}")
    print(f"{'='*80}\n")

    # Prepare output
    output_lines = []

    def write_output(line: str = ""):
        """Write to console and/or file."""
        print(line)
        output_lines.append(line)

    # Validate each file
    validator = PatternValidator(skip_surface_chunks=not args.all_surface)
    total_questions = 0

    # Show mode info
    if not args.all_surface:
        write_output("Mode: Skipping surface variations (FREQUENCY, TIME, etc.)")
        write_output("Use --all-surface to see all combinations")
    else:
        write_output("Mode: Showing ALL surface variations")
    write_output("")

    for json_file in sorted(json_files):
        try:
            pattern, questions = validator.validate_pattern_file(json_file)

            write_output(f"\n{'#'*80}")
            write_output(f"PATTERN: {pattern['pattern_id']}")
            write_output(f"File: {json_file.name}")
            write_output(f"{'#'*80}")
            write_output(f"Focus: {pattern.get('focus', 'N/A')}")
            write_output(f"Level: {pattern.get('level', 'N/A')}")
            write_output(f"Domain: {pattern.get('domain', 'N/A')}")
            write_output(f"Template: {pattern.get('template', 'N/A')}")
            write_output(f"\nTotal possible questions: {len(questions)}")
            write_output(f"{'#'*80}")

            # Display questions
            if args.limit and args.limit < len(questions):
                # Random sample
                display_count = args.limit
                sampled_questions = random.sample(questions, display_count)
                write_output(f"\nShowing {display_count} random samples from {len(questions)} total questions")
            else:
                # Show all
                display_count = len(questions)
                sampled_questions = questions
                write_output(f"\nShowing all {len(questions)} questions")

            for i, question in enumerate(sampled_questions, 1):
                write_output(f"\n{'='*80}")
                write_output(f"Question {i}: {question['question_id']}")
                write_output(f"{'='*80}")
                write_output(f"\n{question['sentence']}\n")

                # Print options
                for letter in sorted(question['options'].keys()):
                    marker = " ✓" if letter == question['correct_answer'] else ""
                    write_output(f"  {letter}. {question['options'][letter]}{marker}")

                # Print combination details
                combo_str = ", ".join([f"{k}={v}" for k, v in question['combination'].items()])
                write_output(f"\nChunks used: {combo_str}")


            total_questions += len(questions)

        except Exception as e:
            write_output(f"\nError validating {json_file.name}: {str(e)}")
            import traceback
            traceback.print_exc()

    # Summary
    write_output(f"\n\n{'='*80}")
    write_output(f"VALIDATION SUMMARY")
    write_output(f"{'='*80}")
    write_output(f"Total patterns validated: {len(json_files)}")
    write_output(f"Total possible questions: {total_questions}")
    write_output(f"{'='*80}\n")

    # Save to file if requested
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))

        print(f"\nResults saved to: {output_path}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
