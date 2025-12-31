"""
Question Generator Module
-------------------------
Main question generation logic for EYESH English exam questions.
"""

import random
import json
from typing import Dict, List, Optional, Tuple
from pathlib import Path

from .pattern_loader import PatternLoader
from .grammar_engine import GrammarEngine


class QuestionGenerator:
    """Generates exam questions from pattern templates."""

    def __init__(self, pattern_dir: str = "pattern"):
        """
        Initialize the QuestionGenerator.

        Args:
            pattern_dir: Directory containing pattern JSON files
        """
        self.pattern_loader = PatternLoader(pattern_dir)
        self.patterns: List[Dict] = []
        self.grammar_engine = GrammarEngine()
        self.question_counter = 0

    def load_patterns(self) -> int:
        """
        Load all patterns from the pattern directory.

        Returns:
            Number of patterns loaded
        """
        self.patterns = self.pattern_loader.load_all_patterns()
        return len(self.patterns)

    def generate_question(
        self,
        pattern_id: Optional[str] = None,
        pattern: Optional[Dict] = None
    ) -> Dict:
        """
        Generate a single question from a pattern.

        Args:
            pattern_id: Specific pattern ID to use (optional)
            pattern: Specific pattern dict to use (optional)

        Returns:
            Generated question dictionary
        """
        # Select pattern
        if pattern is None:
            if pattern_id:
                pattern = self.pattern_loader.get_pattern_by_id(pattern_id)
                if pattern is None:
                    raise ValueError(f"Pattern not found: {pattern_id}")
            else:
                if not self.patterns:
                    raise ValueError("No patterns loaded. Call load_patterns() first.")
                pattern = random.choice(self.patterns)

        # Generate question from pattern
        question = self._generate_from_pattern(pattern)

        self.question_counter += 1
        return question

    # Level mapping for filtering
    LEVEL_MAP = {
        'beginner': ['A1', 'A2'],
        'intermediate': ['B1', 'B2'],
        'advanced': ['C1', 'C2']
    }

    def _filter_patterns_by_level(self, level: Optional[str]) -> List[Dict]:
        """
        Filter patterns by proficiency level.

        Args:
            level: Level name (beginner, intermediate, advanced) or None for all

        Returns:
            List of filtered patterns
        """
        if not level:
            return self.patterns

        allowed_levels = self.LEVEL_MAP.get(level, [])
        if not allowed_levels:
            return self.patterns

        filtered = [p for p in self.patterns if p.get('level', '').upper() in allowed_levels]
        return filtered

    def generate_multiple(
        self,
        count: int,
        pattern_id: Optional[str] = None,
        shuffle_patterns: bool = True,
        level: Optional[str] = None
    ) -> List[Dict]:
        """
        Generate multiple questions.

        Args:
            count: Number of questions to generate
            pattern_id: Specific pattern ID to use (optional)
            shuffle_patterns: If True, randomly select from all patterns
            level: Proficiency level filter (beginner, intermediate, advanced)

        Returns:
            List of generated questions
        """
        questions = []

        # Get filtered patterns based on level
        available_patterns = self._filter_patterns_by_level(level)

        if not available_patterns:
            print(f"⚠ No patterns found for level '{level}'")
            return questions

        for i in range(count):
            try:
                if pattern_id:
                    question = self.generate_question(pattern_id=pattern_id)
                elif shuffle_patterns:
                    # Select from filtered patterns
                    pattern = random.choice(available_patterns)
                    question = self.generate_question(pattern=pattern)
                else:
                    # Cycle through filtered patterns
                    pattern_idx = i % len(available_patterns)
                    pattern = available_patterns[pattern_idx]
                    question = self.generate_question(pattern=pattern)

                questions.append(question)
            except Exception as e:
                print(f"Error generating question {i+1}: {str(e)}")

        return questions

    def _generate_from_pattern(self, pattern: Dict) -> Dict:
        """
        Generate a question from a specific pattern.

        Args:
            pattern: Pattern dictionary

        Returns:
            Question dictionary
        """
        chunks = pattern['chunks']
        template = pattern['template']

        # Select chunks
        selected_chunks = self._select_chunks(chunks)

        # Build sentence
        sentence, correct_answer, blank_item_used = self._build_sentence(
            template, chunks, selected_chunks
        )

        # Generate distractors
        distractors = self._generate_distractors(
            pattern, correct_answer, blank_item_used, selected_chunks
        )

        # Create options (1 correct + 4 distractors = 5 total for EYESH format A-E)
        all_options = [correct_answer] + distractors[:4]

        # Shuffle and assign letters
        random.shuffle(all_options)
        options_dict = {
            chr(65 + i): option  # 65 = 'A' in ASCII, so A, B, C, D, E
            for i, option in enumerate(all_options)
        }

        # Find correct answer letter
        correct_letter = None
        for letter, option in options_dict.items():
            if option == correct_answer:
                correct_letter = letter
                break

        # Generate explanation
        item_explanation = None
        # Use the stored item data if available
        if 'BLANK_ITEM_DATA' in selected_chunks:
            item_explanation = selected_chunks['BLANK_ITEM_DATA'].get('explanation')

        explanation = self.grammar_engine.generate_answer_explanation(
            pattern, blank_item_used, correct_answer, item_explanation
        )

        # Build question dictionary
        question = {
            'question_id': self.grammar_engine.format_question_id(
                pattern['pattern_id'], self.question_counter
            ),
            'pattern_id': pattern['pattern_id'],
            'focus': pattern['focus'],
            'level': pattern['level'],
            'domain': pattern.get('domain', ''),
            'category': pattern['category'],
            'sub_grammar': pattern.get('sub_grammar', []),
            'sentence': sentence,
            'options': options_dict,
            'correct_answer': correct_letter,
            'explanation': explanation
        }

        return question

    def _select_chunks(self, chunks: Dict) -> Dict:
        """
        Select random values for each chunk type.

        Args:
            chunks: Chunks dictionary from pattern

        Returns:
            Dictionary of selected chunk values
        """
        selected = {}

        for chunk_name, chunk_values in chunks.items():
            # Check if this is a "blank chunk" (has nested structure with correct_forms)
            if self._is_blank_chunk(chunk_values):
                # This is the chunk that goes in the blank (VERB, AUX, MODAL, etc.)

                # Handle list structure (e.g., past_simple patterns, relative clauses)
                if isinstance(chunk_values, list):
                    # Select a random item from the list
                    item_data = random.choice(chunk_values)
                    # Use index as identifier for list-based chunks
                    selected_item = chunk_values.index(item_data)
                    selected[chunk_name] = selected_item
                # Handle dict structure (e.g., modal patterns)
                else:
                    chunk_dict = chunk_values
                    selected_item = random.choice(list(chunk_dict.keys()))
                    selected[chunk_name] = selected_item
                    item_data = chunk_dict[selected_item]

                # Select correct form (usually just one item in the list)
                selected['CORRECT_FORM'] = random.choice(item_data['correct_forms'])

                # Select objects from this item if available
                # Check for different object field names: objects, article_objects, etc.
                for obj_field in ['objects', 'article_objects', 'prep_objects', 'items']:
                    if obj_field in item_data and item_data[obj_field]:
                        obj = random.choice(item_data[obj_field])
                        # Map to template placeholders
                        if obj_field == 'article_objects':
                            selected['ARTICLE_OBJ'] = obj
                        elif obj_field == 'prep_objects':
                            selected['PREP_OBJ'] = obj
                        else:
                            selected['OBJ'] = obj
                        break

                # Copy any coordinated chunks from item_data to selected
                # This handles patterns where multiple placeholders need to be selected together
                # (e.g., THING, DESCRIPTION, QUALITY in relative clauses)
                for key, value in item_data.items():
                    if key.isupper() and isinstance(value, str):
                        # This is a template placeholder field (all caps, string value)
                        selected[key] = value

                # Store the selected item data for later use (for explanations, distractors)
                selected['BLANK_ITEM'] = selected_item
                # Also store the actual item data for list-based chunks
                selected['BLANK_ITEM_DATA'] = item_data

            elif isinstance(chunk_values, list):
                # Simple list - select random item
                selected[chunk_name] = random.choice(chunk_values)

            elif isinstance(chunk_values, dict):
                # Dictionary - select random key and then random value from that key
                random_key = random.choice(list(chunk_values.keys()))
                random_value = random.choice(chunk_values[random_key])
                selected[chunk_name] = random_value

        return selected

    def _is_blank_chunk(self, chunk_value) -> bool:
        """
        Check if a chunk is a "blank chunk" (contains correct_forms, wrong_forms, etc.).
        Handles both dict structure (modals) and list structure (past_simple).

        Args:
            chunk_value: Chunk value to check (can be dict or list)

        Returns:
            True if this is a blank chunk (VERB, AUX, MODAL, etc.)
        """
        # Handle list structure (e.g., past_simple patterns)
        if isinstance(chunk_value, list):
            for item in chunk_value:
                if isinstance(item, dict) and 'correct_forms' in item and 'wrong_forms' in item:
                    return True
            return False

        # Handle dict structure (e.g., modal patterns)
        if not isinstance(chunk_value, dict):
            return False

        # Check if at least one value has the required structure
        for value in chunk_value.values():
            if isinstance(value, dict) and 'correct_forms' in value and 'wrong_forms' in value:
                return True

        return False

    def _build_sentence(
        self,
        template: str,
        chunks: Dict,
        selected_chunks: Dict
    ) -> Tuple[str, str, str]:
        """
        Build the question sentence from template and selected chunks.

        Args:
            template: Template string
            chunks: All chunks from pattern
            selected_chunks: Selected chunk values

        Returns:
            Tuple of (sentence, correct_answer, blank_item_used)
        """
        # Get correct answer from selected chunks
        correct_answer = selected_chunks.get('CORRECT_FORM', '')
        blank_item_used = selected_chunks.get('BLANK_ITEM', '')

        # Prepare replacements for template
        replacements = {}

        for placeholder in self.grammar_engine.extract_placeholders(template):
            if placeholder in selected_chunks:
                replacements[placeholder] = selected_chunks[placeholder]

        # Replace placeholders
        sentence = self.grammar_engine.replace_template_placeholders(
            template, replacements
        )

        # Find and preserve blank marker
        blank_marker = self.grammar_engine.find_blank_marker(template)
        if not blank_marker:
            blank_marker = "________"

        # Ensure sentence is properly formatted
        sentence = self.grammar_engine.capitalize_first_letter(sentence)

        return sentence, correct_answer, blank_item_used

    def _generate_distractors(
        self,
        pattern: Dict,
        correct_answer: str,
        blank_item_used: str,
        selected_chunks: Optional[Dict] = None
    ) -> List[str]:
        """
        Generate distractor options from the blank chunk data.
        Uses wrong_forms + distractor directly from JSON.

        Args:
            pattern: Pattern dictionary
            correct_answer: The correct answer
            blank_item_used: The item that was selected from the blank chunk (verb, aux, etc.)
            selected_chunks: Selected chunks dict containing BLANK_ITEM_DATA

        Returns:
            List of distractor strings (exactly 4 for EYESH format)
        """
        distractors = []

        # Try to get item_data from selected_chunks first (handles both list and dict structures)
        item_data = None
        if selected_chunks and 'BLANK_ITEM_DATA' in selected_chunks:
            item_data = selected_chunks['BLANK_ITEM_DATA']
        else:
            # Fallback: Find the blank chunk (the one with nested structure)
            if 'chunks' in pattern:
                for chunk_name, chunk_values in pattern['chunks'].items():
                    if self._is_blank_chunk(chunk_values):
                        # Handle dict structure
                        if isinstance(chunk_values, dict) and blank_item_used in chunk_values:
                            item_data = chunk_values[blank_item_used]
                        # Handle list structure
                        elif isinstance(chunk_values, list) and isinstance(blank_item_used, int):
                            if 0 <= blank_item_used < len(chunk_values):
                                item_data = chunk_values[blank_item_used]
                        break

        # Extract distractors from item_data
        if item_data:
            # Add wrong_forms (3 grammatical transformations)
            if 'wrong_forms' in item_data:
                distractors.extend(item_data['wrong_forms'])

            # Add distractor (semantically inappropriate option)
            if 'distractor' in item_data:
                distractors.append(item_data['distractor'])

        # Ensure distractors are unique and different from correct answer
        distractors = self.grammar_engine.ensure_unique_options(
            distractors, correct_answer
        )

        # EYESH exams use 5 options (A-E), so we need exactly 4 distractors
        # If we don't have enough distractors, add generic ones
        while len(distractors) < 4:
            generic_distractors = [
                "incorrect form",
                "wrong answer",
                "not applicable",
                "invalid option"
            ]
            for generic in generic_distractors:
                if generic not in distractors and generic != correct_answer:
                    distractors.append(generic)
                    if len(distractors) >= 4:
                        break

        # Return exactly 4 distractors
        return distractors[:4]

    def export_json(
        self,
        questions: List[Dict],
        filepath: str = "output/questions.json",
        indent: int = 2
    ) -> None:
        """
        Export questions to JSON file.

        Args:
            questions: List of question dictionaries
            filepath: Output file path
            indent: JSON indentation level
        """
        output_path = Path(filepath)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=indent, ensure_ascii=False)

        print(f"\n✓ Exported {len(questions)} questions to {filepath}")

    def export_txt(
        self,
        questions: List[Dict],
        filepath: str = "output/questions.txt",
        test_mode: bool = False
    ) -> None:
        """
        Export questions to human-readable text file.

        Args:
            questions: List of question dictionaries
            filepath: Output file path
            test_mode: If True, hide correct answers and explanations
        """
        output_path = Path(filepath)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            header = "EYESH ENGLISH EXAM - TEST" if test_mode else "EYESH ENGLISH EXAM - GENERATED QUESTIONS"
            f.write("=" * 80 + "\n")
            f.write(f"{header}\n")
            f.write("=" * 80 + "\n\n")

            for i, q in enumerate(questions, 1):
                f.write(f"Question {i}\n")
                f.write("-" * 80 + "\n")

                if not test_mode:
                    f.write(f"ID: {q['question_id']}\n")
                    f.write(f"Pattern: {q['pattern_id']}\n")
                    f.write(f"Focus: {q['focus']}\n")
                    f.write(f"Level: {q['level']}\n")
                    if q.get('domain'):
                        f.write(f"Domain: {q['domain']}\n")
                f.write("\n")

                f.write(f"{q['sentence']}\n\n")

                # Write options (without markers in test mode)
                for letter in sorted(q['options'].keys()):
                    if test_mode:
                        f.write(f"  {letter}. {q['options'][letter]}\n")
                    else:
                        marker = " ✓" if letter == q['correct_answer'] else ""
                        f.write(f"  {letter}. {q['options'][letter]}{marker}\n")

                if not test_mode:
                    f.write(f"\nCorrect Answer: {q['correct_answer']}\n")
                    f.write(f"Explanation: {q['explanation']}\n")

                f.write("\n" + "=" * 80 + "\n\n")

        print(f"✓ Exported {len(questions)} questions to {filepath}")

    def get_stats(self) -> Dict:
        """
        Get statistics about loaded patterns.

        Returns:
            Dictionary with statistics
        """
        if not self.patterns:
            return {'total_patterns': 0}

        stats = {
            'total_patterns': len(self.patterns),
            'by_focus': {},
            'by_level': {},
            'by_domain': {},
        }

        for pattern in self.patterns:
            # Count by focus
            focus = pattern.get('focus', 'unknown')
            stats['by_focus'][focus] = stats['by_focus'].get(focus, 0) + 1

            # Count by level
            level = pattern.get('level', 'unknown')
            stats['by_level'][level] = stats['by_level'].get(level, 0) + 1

            # Count by domain
            domain = pattern.get('domain', 'unknown')
            stats['by_domain'][domain] = stats['by_domain'].get(domain, 0) + 1

        return stats
