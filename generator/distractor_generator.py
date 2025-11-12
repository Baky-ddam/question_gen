"""
Distractor Generator Module
---------------------------
Generates plausible but incorrect answer options (distractors)
using systematic grammar transformations.
"""

import re
from typing import List, Optional


class DistractorGenerator:
    """Generates distractors using grammar transformation methods."""

    @staticmethod
    def to_infinitive(base: str) -> str:
        """
        Convert base form to infinitive (to + verb).

        Args:
            base: Base form phrase (e.g., "read books")

        Returns:
            Infinitive form (e.g., "to read books")
        """
        if not base:
            return ""

        # Remove any existing "to " prefix to avoid duplication
        base_clean = base.strip()
        if base_clean.startswith("to "):
            return base_clean

        return f"to {base_clean}"

    @staticmethod
    def to_gerund(base: str) -> str:
        """
        Convert base form to gerund (verb + -ing).

        Args:
            base: Base form phrase (e.g., "read books")

        Returns:
            Gerund form (e.g., "reading books")
        """
        if not base:
            return ""

        base_clean = base.strip()

        # Remove "to " prefix if present
        if base_clean.startswith("to "):
            base_clean = base_clean[3:]

        # Extract first word (the verb)
        words = base_clean.split()
        if not words:
            return base_clean

        verb = words[0]
        rest = " ".join(words[1:]) if len(words) > 1 else ""

        # Apply -ing rules
        gerund_verb = DistractorGenerator._apply_gerund_rules(verb)

        return f"{gerund_verb} {rest}".strip() if rest else gerund_verb

    @staticmethod
    def _apply_gerund_rules(verb: str) -> str:
        """
        Apply English gerund formation rules to a verb.

        Args:
            verb: Base verb form

        Returns:
            Verb with -ing added according to rules
        """
        if not verb:
            return ""

        verb = verb.lower()

        # Already a gerund
        if verb.endswith('ing'):
            return verb

        # Rule 1: Silent 'e' at the end → drop 'e' and add -ing
        # (e.g., make → making, write → writing)
        if verb.endswith('e') and len(verb) > 2:
            # Exception: words ending in 'ee', 'ye', 'oe' keep the 'e'
            if not (verb.endswith('ee') or verb.endswith('ye') or verb.endswith('oe')):
                return verb[:-1] + 'ing'

        # Rule 2: One syllable, CVC pattern → double final consonant
        # (e.g., run → running, sit → sitting, get → getting)
        if len(verb) >= 3 and DistractorGenerator._is_cvc_pattern(verb):
            return verb + verb[-1] + 'ing'

        # Rule 3: Two syllables ending in stressed CVC → double final consonant
        # (e.g., prefer → preferring, begin → beginning)
        # Simplified: just check if ends in CVC
        if len(verb) >= 4 and verb[-3] not in 'aeiou' and verb[-2] in 'aeiou' and verb[-1] not in 'aeiouy':
            # Common verbs that double (simplified list)
            doubling_verbs = ['prefer', 'begin', 'commit', 'occur', 'permit', 'refer', 'submit']
            if verb in doubling_verbs:
                return verb + verb[-1] + 'ing'

        # Rule 4: Default - just add -ing
        return verb + 'ing'

    @staticmethod
    def _is_cvc_pattern(word: str) -> bool:
        """
        Check if word ends with Consonant-Vowel-Consonant pattern.

        Args:
            word: Word to check

        Returns:
            True if ends with CVC pattern
        """
        if len(word) < 3:
            return False

        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'

        # Check last 3 characters: consonant, vowel, consonant
        # But not if last letter is w, x, y (these don't double)
        return (
            word[-3] in consonants and
            word[-2] in vowels and
            word[-1] in consonants and
            word[-1] not in 'wxy'
        )

    @staticmethod
    def bare_infinitive(base: str) -> str:
        """
        Convert to bare infinitive (base form without 'to').

        Args:
            base: Base form phrase (e.g., "read books" or "to read books")

        Returns:
            Bare infinitive (e.g., "read books")
        """
        if not base:
            return ""

        base_clean = base.strip()

        # Remove "to " prefix if present
        if base_clean.startswith("to "):
            return base_clean[3:].strip()

        return base_clean

    @staticmethod
    def wrong_conjugation(base: str) -> str:
        """
        Apply wrong conjugation by adding -s to the first verb.
        Useful for subject-verb agreement errors.

        Args:
            base: Base form phrase (e.g., "read books")

        Returns:
            Wrongly conjugated form (e.g., "reads books")
        """
        if not base:
            return ""

        base_clean = base.strip()

        # Remove "to " prefix if present
        if base_clean.startswith("to "):
            base_clean = base_clean[3:]

        # Extract first word (the verb)
        words = base_clean.split()
        if not words:
            return base_clean

        verb = words[0]
        rest = " ".join(words[1:]) if len(words) > 1 else ""

        # Add -s to verb (simplified - doesn't handle all irregular forms)
        conjugated_verb = DistractorGenerator._add_third_person_s(verb)

        return f"{conjugated_verb} {rest}".strip() if rest else conjugated_verb

    @staticmethod
    def _add_third_person_s(verb: str) -> str:
        """
        Add third person singular -s/-es to a verb.

        Args:
            verb: Base verb form

        Returns:
            Third person form
        """
        if not verb:
            return ""

        verb = verb.lower()

        # Already has -s or -es
        if verb.endswith('s') or verb.endswith('es'):
            return verb

        # Ends in -y preceded by consonant → -ies
        if verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou':
            return verb[:-1] + 'ies'

        # Ends in -ch, -sh, -ss, -x, -z, -o → add -es
        if verb.endswith(('ch', 'sh', 'ss', 'x', 'z', 'o')):
            return verb + 'es'

        # Default: add -s
        return verb + 's'

    @staticmethod
    def generate_from_method(method: str, base: str) -> Optional[str]:
        """
        Generate a distractor using the specified method.

        Args:
            method: Transformation method name
            base: Base form to transform

        Returns:
            Transformed distractor, or None if method unknown
        """
        method_map = {
            'to_infinitive': DistractorGenerator.to_infinitive,
            'to_gerund': DistractorGenerator.to_gerund,
            'bare_infinitive': DistractorGenerator.bare_infinitive,
            'wrong_conjugation': DistractorGenerator.wrong_conjugation,
        }

        if method in method_map:
            return method_map[method](base)

        return None

    @staticmethod
    def get_context_distractors(pattern: dict, current_verb: str, count: int = 3) -> List[str]:
        """
        Get context distractors from the current verb's context_distractors field.
        These are phrases in correct grammatical form but semantically incompatible.

        Args:
            pattern: Pattern dictionary
            current_verb: Current verb being used
            count: Number of distractors to return

        Returns:
            List of context distractor phrases
        """
        if 'chunks' not in pattern or 'VERB' not in pattern['chunks']:
            return []

        verbs = pattern['chunks']['VERB']

        # Get context_distractors from current verb
        if current_verb in verbs:
            verb_data = verbs[current_verb]
            if 'context_distractors' in verb_data:
                distractors = verb_data['context_distractors']
                # Return up to 'count' distractors
                return distractors[:count] if distractors else []

        return []

    @staticmethod
    def get_wrong_context_phrases(pattern: dict, current_verb: str, count: int = 5) -> List[str]:
        """
        Get phrases from other verbs in the pattern (wrong context).
        DEPRECATED: Use get_context_distractors instead for better semantic control.

        Args:
            pattern: Pattern dictionary
            current_verb: Current verb being used
            count: Number of phrases to return

        Returns:
            List of phrases from other verbs
        """
        if 'chunks' not in pattern or 'VERB' not in pattern['chunks']:
            return []

        verbs = pattern['chunks']['VERB']
        wrong_phrases = []

        for verb_name, verb_data in verbs.items():
            if verb_name != current_verb:
                if 'phrases' in verb_data:
                    wrong_phrases.extend(verb_data['phrases'])

        # Return up to 'count' phrases
        return wrong_phrases[:count] if wrong_phrases else []
