#!/usr/bin/env python3
"""
EYESH English Question Generator - Main Entry Point
---------------------------------------------------
Generate unlimited grammatically correct English exam questions
from JSON pattern templates.

Usage:
    python main.py --count 10
    python main.py --pattern GERUND_VERBS_DAILY --count 5
    python main.py --count 20 --format json --output my_questions.json
    python main.py --stats
"""

import argparse
import sys
from pathlib import Path

from generator.question_generator import QuestionGenerator


def print_banner():
    """Print application banner."""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        EYESH ENGLISH QUESTION GENERATOR v1.0                  ║
║        Grammatically Correct Questions from Templates        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_question(question: dict, index: int, test_mode: bool = False):
    """
    Print a question to console in formatted style.

    Args:
        question: Question dictionary
        index: Question number
        test_mode: If True, hide correct answer and explanation
    """
    print(f"\n{'='*70}")
    print(f"Question {index}")
    print(f"{'='*70}")

    if not test_mode:
        print(f"ID: {question['question_id']}")
        print(f"Pattern: {question['pattern_id']}")
        print(f"Focus: {question['focus']} | Level: {question['level']}", end="")
        if question.get('domain'):
            print(f" | Domain: {question['domain']}")
        else:
            print()
    print()

    print(question['sentence'])
    print()

    # Print options (without checkmark in test mode)
    for letter in sorted(question['options'].keys()):
        if test_mode:
            print(f"  {letter}. {question['options'][letter]}")
        else:
            marker = " ✓" if letter == question['correct_answer'] else ""
            print(f"  {letter}. {question['options'][letter]}{marker}")

    # Only show correct answer and explanation in non-test mode
    if not test_mode:
        print(f"\nCorrect Answer: {question['correct_answer']}")
        print(f"Explanation: {question['explanation']}")


def display_stats(generator: QuestionGenerator):
    """
    Display statistics about loaded patterns.

    Args:
        generator: QuestionGenerator instance
    """
    stats = generator.get_stats()

    print("\n" + "="*70)
    print("PATTERN STATISTICS")
    print("="*70)
    print(f"\nTotal Patterns Loaded: {stats['total_patterns']}")

    if stats['total_patterns'] == 0:
        print("\nNo patterns loaded. Please add pattern files to the 'pattern/' directory.")
        return

    print("\n--- By Grammar Focus ---")
    for focus, count in sorted(stats['by_focus'].items()):
        print(f"  {focus}: {count}")

    print("\n--- By CEFR Level ---")
    for level, count in sorted(stats['by_level'].items()):
        print(f"  {level}: {count}")

    print("\n--- By Domain ---")
    for domain, count in sorted(stats['by_domain'].items()):
        if domain and domain != 'unknown':
            print(f"  {domain}: {count}")

    print("\nAvailable Pattern IDs:")
    pattern_ids = generator.pattern_loader.list_all_pattern_ids()
    for pid in sorted(pattern_ids):
        print(f"  - {pid}")


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(
        description='Generate EYESH English exam questions from pattern templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --count 10
      Generate 10 random questions and display on screen

  python main.py --pattern GERUND_VERBS_DAILY --count 5
      Generate 5 questions from specific pattern

  python main.py --count 20 --format json --output output/my_questions.json
      Generate 20 questions and export to JSON

  python main.py --count 10 --format txt --output output/exam.txt
      Generate 10 questions and export to readable text file

  python main.py --stats
      Show statistics about loaded patterns

  python main.py --list
      List all available pattern IDs
        """
    )

    parser.add_argument(
        '--count', '-c',
        type=int,
        default=5,
        help='Number of questions to generate (default: 5)'
    )

    parser.add_argument(
        '--pattern', '-p',
        type=str,
        help='Specific pattern ID to use (optional)'
    )

    parser.add_argument(
        '--format', '-f',
        choices=['console', 'json', 'txt', 'both'],
        default='console',
        help='Output format (default: console)'
    )

    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (for json/txt formats)'
    )

    parser.add_argument(
        '--pattern-dir',
        type=str,
        default='pattern',
        help='Directory containing pattern files (default: pattern)'
    )

    parser.add_argument(
        '--stats', '-s',
        action='store_true',
        help='Show statistics about loaded patterns'
    )

    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all available pattern IDs'
    )

    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Don\'t show banner'
    )

    parser.add_argument(
        '--test-mode', '-t',
        action='store_true',
        help='Test mode: hide correct answers and explanations (exam format)'
    )

    parser.add_argument(
        '--level',
        choices=['beginner', 'intermediate', 'advanced'],
        help='Filter by proficiency level (beginner=A1/A2, intermediate=B1/B2, advanced=C1/C2)'
    )

    args = parser.parse_args()

    # Print banner
    if not args.no_banner:
        print_banner()

    # Initialize generator
    print("Initializing question generator...")
    generator = QuestionGenerator(pattern_dir=args.pattern_dir)

    # Load patterns
    try:
        num_patterns = generator.load_patterns()
        if num_patterns == 0:
            print("\n❌ Error: No patterns found!")
            print(f"Please add pattern JSON files to '{args.pattern_dir}/' directory")
            return 1
    except Exception as e:
        print(f"\n❌ Error loading patterns: {str(e)}")
        return 1

    # Handle stats display
    if args.stats:
        display_stats(generator)
        return 0

    # Handle list display
    if args.list:
        print("\nAvailable Pattern IDs:")
        print("="*70)
        pattern_ids = generator.pattern_loader.list_all_pattern_ids()
        for pid in sorted(pattern_ids):
            print(f"  {pid}")
        print()
        return 0

    # Generate questions
    level_msg = f" (level: {args.level})" if args.level else ""
    print(f"\nGenerating {args.count} question(s){level_msg}...")

    try:
        questions = generator.generate_multiple(
            count=args.count,
            pattern_id=args.pattern,
            level=args.level
        )

        if not questions:
            print("❌ No questions were generated!")
            return 1

        print(f"✓ Generated {len(questions)} question(s)")

        # Output based on format
        if args.format in ['console', 'both']:
            # Display questions on console
            for i, question in enumerate(questions, 1):
                print_question(question, i, test_mode=args.test_mode)

        if args.format in ['json', 'both']:
            # Export to JSON
            output_path = args.output or 'output/questions.json'
            generator.export_json(questions, output_path)

        if args.format == 'txt':
            # Export to TXT
            output_path = args.output or 'output/questions.txt'
            generator.export_txt(questions, output_path, test_mode=args.test_mode)

        print(f"\n{'='*70}")
        print("✓ Generation complete!")
        print(f"{'='*70}\n")

        return 0

    except Exception as e:
        print(f"\n❌ Error generating questions: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
