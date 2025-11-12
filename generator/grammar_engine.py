"""
Grammar Engine Module
---------------------
Provides grammar utility functions and helpers for question generation.
"""

import re
from typing import Dict, List, Optional, Tuple


class GrammarEngine:
    """Helper utilities for grammar processing."""

    @staticmethod
    def extract_base_form(phrase: str) -> str:
        """
        Extract base form from a phrase by removing -ing or 'to'.

        Args:
            phrase: Phrase to process (e.g., "reading books" or "to read books")

        Returns:
            Base form (e.g., "read books")
        """
        phrase_clean = phrase.strip()

        # Remove "to " prefix
        if phrase_clean.startswith("to "):
            phrase_clean = phrase_clean[3:].strip()

        # Remove -ing suffix from first word
        words = phrase_clean.split()
        if words and words[0].endswith('ing'):
            verb = words[0]
            # Simple de-gerund (reverse common -ing rules)
            if len(verb) > 3:
                # Try to remove -ing
                base_verb = verb[:-3]
                # Handle doubled consonants (running → run)
                if len(base_verb) >= 2 and base_verb[-1] == base_verb[-2]:
                    base_verb = base_verb[:-1]
                # Handle dropped 'e' (making → make)
                # This is a simplification - not perfect for all cases
                words[0] = base_verb

        return " ".join(words)

    @staticmethod
    def validate_chunk_compatibility(chunks: Dict) -> bool:
        """
        Validate that chunk structure is compatible.

        Args:
            chunks: Chunks dictionary from pattern

        Returns:
            True if valid, False otherwise
        """
        if not isinstance(chunks, dict):
            return False

        # Check VERB structure if present
        if 'VERB' in chunks:
            verbs = chunks['VERB']
            if not isinstance(verbs, dict):
                return False

            for verb_name, verb_data in verbs.items():
                if not isinstance(verb_data, dict):
                    return False
                if 'phrases' not in verb_data or 'bases' not in verb_data:
                    return False
                if not isinstance(verb_data['phrases'], list) or not isinstance(verb_data['bases'], list):
                    return False
                if len(verb_data['phrases']) != len(verb_data['bases']):
                    return False

        return True

    @staticmethod
    def apply_subject_verb_agreement(verb: str, subject: str) -> str:
        """
        Apply subject-verb agreement rules.
        (Note: In the current system, verbs are pre-conjugated in patterns,
        so this is mainly for validation or future use)

        Args:
            verb: Base verb
            subject: Subject pronoun or noun

        Returns:
            Correctly conjugated verb
        """
        subject_lower = subject.lower().strip()

        # Third person singular subjects
        third_person_singular = ['he', 'she', 'it']

        # Check if subject requires third person singular form
        is_third_person = subject_lower in third_person_singular

        # For now, return verb as-is since we pre-conjugate in patterns
        # This function is here for potential future enhancements
        return verb

    @staticmethod
    def replace_template_placeholders(
        template: str,
        replacements: Dict[str, str]
    ) -> str:
        """
        Replace placeholders in template with actual values.

        Args:
            template: Template string with {PLACEHOLDER} markers
            replacements: Dictionary of placeholder -> value

        Returns:
            Template with placeholders replaced
        """
        result = template

        for placeholder, value in replacements.items():
            # Replace {PLACEHOLDER} with value
            result = result.replace(f"{{{placeholder}}}", value)

        return result

    @staticmethod
    def extract_placeholders(template: str) -> List[str]:
        """
        Extract all placeholder names from a template.

        Args:
            template: Template string

        Returns:
            List of placeholder names (without braces)
        """
        # Find all {PLACEHOLDER} patterns
        pattern = r'\{([A-Z_]+)\}'
        matches = re.findall(pattern, template)
        return matches

    @staticmethod
    def find_blank_marker(template: str) -> Optional[str]:
        """
        Find the blank marker in the template.

        Args:
            template: Template string

        Returns:
            Blank marker string (e.g., "____" or "__*") or None
        """
        # Common blank patterns
        blank_patterns = [
            r'____+',  # Four or more underscores
            r'__\*',   # Two underscores followed by asterisk
            r'__',     # Two underscores minimum
        ]

        for pattern in blank_patterns:
            match = re.search(pattern, template)
            if match:
                return match.group(0)

        return None

    @staticmethod
    def generate_answer_explanation(
        pattern: Dict,
        verb: str,
        correct_answer: str,
        verb_explanation: Optional[str] = None
    ) -> str:
        """
        Generate explanation for why an answer is correct.

        Args:
            pattern: Pattern dictionary
            verb: Selected verb
            correct_answer: The correct answer phrase
            verb_explanation: Optional specific explanation for this verb

        Returns:
            Explanation string
        """
        # Start with verb-specific explanation if available
        if verb_explanation:
            return verb_explanation

        # Fall back to pattern-level explanation
        pattern_explanation = pattern.get('explanation', '')

        # Add specific answer mention
        if pattern_explanation:
            return f"{pattern_explanation} The correct answer is '{correct_answer}'."

        # Generic fallback
        return f"The correct answer is '{correct_answer}'."

    @staticmethod
    def ensure_unique_options(options: List[str], correct_answer: str) -> List[str]:
        """
        Ensure all options are unique and different from correct answer.

        Args:
            options: List of option strings
            correct_answer: The correct answer

        Returns:
            Filtered list of unique options (excluding correct answer)
        """
        unique_options = []
        seen = set()
        seen.add(correct_answer.lower().strip())

        for option in options:
            option_clean = option.strip()
            option_lower = option_clean.lower()

            if option_lower and option_lower not in seen:
                unique_options.append(option_clean)
                seen.add(option_lower)

        return unique_options

    @staticmethod
    def format_question_id(pattern_id: str, index: int) -> str:
        """
        Generate a unique question ID.

        Args:
            pattern_id: Pattern identifier
            index: Question index number

        Returns:
            Formatted question ID
        """
        return f"{pattern_id}_{index:04d}"

    @staticmethod
    def capitalize_first_letter(sentence: str) -> str:
        """
        Ensure sentence starts with capital letter.

        Args:
            sentence: Sentence to capitalize

        Returns:
            Sentence with first letter capitalized
        """
        if not sentence:
            return sentence

        return sentence[0].upper() + sentence[1:] if len(sentence) > 1 else sentence.upper()

    @staticmethod
    def ensure_sentence_punctuation(sentence: str) -> str:
        """
        Ensure sentence ends with proper punctuation.

        Args:
            sentence: Sentence to check

        Returns:
            Sentence with proper ending punctuation
        """
        if not sentence:
            return sentence

        sentence = sentence.rstrip()

        # Check if already has ending punctuation
        if sentence and sentence[-1] not in '.!?':
            sentence += '.'

        return sentence
