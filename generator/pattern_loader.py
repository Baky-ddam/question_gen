"""
Pattern Loader Module
---------------------
Loads and validates JSON pattern files from the pattern directory.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional


class PatternLoader:
    """Loads and validates pattern files from the pattern directory."""

    def __init__(self, pattern_dir: str = "pattern"):
        """
        Initialize the PatternLoader.

        Args:
            pattern_dir: Path to the directory containing pattern files
        """
        self.pattern_dir = Path(pattern_dir)
        self.patterns: List[Dict] = []

    def load_all_patterns(self) -> List[Dict]:
        """
        Recursively load all JSON pattern files from the pattern directory.

        Returns:
            List of loaded and validated pattern dictionaries
        """
        self.patterns = []

        if not self.pattern_dir.exists():
            raise FileNotFoundError(f"Pattern directory not found: {self.pattern_dir}")

        # Recursively find all .json files
        json_files = list(self.pattern_dir.rglob("*.json"))

        if not json_files:
            raise ValueError(f"No JSON pattern files found in {self.pattern_dir}")

        print(f"Found {len(json_files)} pattern file(s)")

        for json_file in json_files:
            try:
                pattern = self._load_pattern_file(json_file)
                if self._validate_pattern(pattern):
                    self.patterns.append(pattern)
                    print(f"✓ Loaded: {json_file.name}")
                else:
                    print(f"✗ Skipped (invalid): {json_file.name}")
            except Exception as e:
                print(f"✗ Error loading {json_file.name}: {str(e)}")

        print(f"\nSuccessfully loaded {len(self.patterns)} pattern(s)\n")
        return self.patterns

    def _load_pattern_file(self, filepath: Path) -> Dict:
        """
        Load a single JSON pattern file.

        Args:
            filepath: Path to the JSON file

        Returns:
            Pattern dictionary
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            pattern = json.load(f)

        # Add filepath metadata
        pattern['_filepath'] = str(filepath)
        pattern['_filename'] = filepath.name

        return pattern

    def _validate_pattern(self, pattern: Dict) -> bool:
        """
        Validate that a pattern has all required fields.

        Args:
            pattern: Pattern dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = [
            'pattern_id',
            'focus',
            'level',
            'category',
            'template',
            'explanation',
            'chunks'
        ]

        # Check required fields
        for field in required_fields:
            if field not in pattern:
                print(f"  Missing required field: {field}")
                return False

        # Validate chunks structure
        if 'chunks' not in pattern or not isinstance(pattern['chunks'], dict):
            print(f"  Invalid 'chunks' structure")
            return False

        # Validate VERB structure if present
        if 'VERB' in pattern['chunks']:
            verbs = pattern['chunks']['VERB']

            # VERB can be either a list (for _auxonly patterns) or a dict
            if isinstance(verbs, list):
                # For list format, just validate it's not empty
                if len(verbs) == 0:
                    print(f"  'VERB' list is empty")
                    return False
                # Continue to other validations
            elif isinstance(verbs, dict):
                # For dict format, validate the new structure
                for verb_name, verb_data in verbs.items():
                    if not isinstance(verb_data, dict):
                        print(f"  Verb '{verb_name}' must have a dictionary structure")
                        return False

                    # Check for new required fields: correct_forms, wrong_forms, distractor
                    if 'correct_forms' not in verb_data:
                        print(f"  Verb '{verb_name}' missing 'correct_forms'")
                        return False

                    if 'wrong_forms' not in verb_data:
                        print(f"  Verb '{verb_name}' missing 'wrong_forms'")
                        return False

                    if 'distractor' not in verb_data:
                        print(f"  Verb '{verb_name}' missing 'distractor'")
                        return False

                    # Validate that wrong_forms has exactly 3 items
                    if len(verb_data['wrong_forms']) != 3:
                        print(f"  Verb '{verb_name}': wrong_forms must have exactly 3 items (has {len(verb_data['wrong_forms'])})")
                        return False

                    # Objects field is optional (some patterns may not need it)
                    # Check for old structure and warn if found
                    if 'phrases' in verb_data or 'bases' in verb_data:
                        print(f"  ⚠ Warning: Verb '{verb_name}' uses old structure (phrases/bases) - please update to new structure (correct_forms/wrong_forms)")
            else:
                print(f"  'VERB' must be a dictionary or list")
                return False

        return True

    def get_pattern_by_id(self, pattern_id: str) -> Optional[Dict]:
        """
        Get a specific pattern by its pattern_id.

        Args:
            pattern_id: The pattern_id to search for

        Returns:
            Pattern dictionary if found, None otherwise
        """
        for pattern in self.patterns:
            if pattern.get('pattern_id') == pattern_id:
                return pattern
        return None

    def get_patterns_by_focus(self, focus: str) -> List[Dict]:
        """
        Get all patterns matching a specific focus.

        Args:
            focus: The grammar focus (e.g., 'gerund_verbs', 'infinitive_verbs')

        Returns:
            List of matching patterns
        """
        return [p for p in self.patterns if p.get('focus') == focus]

    def get_patterns_by_level(self, level: str) -> List[Dict]:
        """
        Get all patterns for a specific CEFR level.

        Args:
            level: CEFR level (A2, B1, B2)

        Returns:
            List of matching patterns
        """
        return [p for p in self.patterns if p.get('level') == level]

    def get_patterns_by_domain(self, domain: str) -> List[Dict]:
        """
        Get all patterns for a specific domain.

        Args:
            domain: Domain (e.g., 'daily_life', 'work', 'travel')

        Returns:
            List of matching patterns
        """
        return [p for p in self.patterns if p.get('domain') == domain]

    def list_all_pattern_ids(self) -> List[str]:
        """
        Get a list of all pattern IDs.

        Returns:
            List of pattern ID strings
        """
        return [p.get('pattern_id', 'UNKNOWN') for p in self.patterns]
