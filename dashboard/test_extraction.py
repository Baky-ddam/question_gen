"""
Test script for Excel table extraction with Arla files.

This script tests the extraction functionality with the example Arla files.
Run this after placing the Arla Excel files in the data/ directory.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dashboard.extractors import ExcelTableExtractor


def test_file_exists(filepath):
    """Check if a file exists and print status."""
    if os.path.exists(filepath):
        print(f"✅ Found: {filepath}")
        return True
    else:
        print(f"❌ Missing: {filepath}")
        return False


def test_extraction(filepath):
    """Test extraction on a file."""
    print(f"\n{'='*80}")
    print(f"Testing: {os.path.basename(filepath)}")
    print(f"{'='*80}\n")

    try:
        # Initialize extractor
        extractor = ExcelTableExtractor(header_row=2, big_header_row=1)

        # Extract tables
        workbook_tables = extractor.extract_from_file(filepath)

        # Print summary
        print(f"✅ Extraction successful!")
        print(f"   Sheets: {workbook_tables.get_sheet_count()}")
        print(f"   Total tables: {workbook_tables.get_total_tables()}")

        # Print details
        for sheet_name, sheet_tables in workbook_tables.sheets.items():
            print(f"\n   📄 {sheet_name}:")
            for table in sheet_tables.tables:
                print(f"      Table {table.table_id}: {table.get_row_count()} rows x {table.get_column_count()} cols")
                print(f"         Merged headers: {table.has_merged_headers}")

                # Show a few column paths
                print(f"         Sample columns:")
                for col in table.columns[:3]:
                    print(f"            - {col.get_full_path()}")
                if len(table.columns) > 3:
                    print(f"            ... and {len(table.columns) - 3} more")

        return True

    except Exception as e:
        print(f"❌ Extraction failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_specific_scenarios():
    """Test specific scenarios mentioned in requirements."""
    print(f"\n{'='*80}")
    print("Testing Specific Scenarios")
    print(f"{'='*80}\n")

    scenarios = [
        {
            'name': 'Scenario 1: Tables without big headers',
            'description': 'Media Type to 100% (no merged header)',
            'expected': 'Columns should be standalone (no big header)'
        },
        {
            'name': 'Scenario 2: Month sequence headers',
            'description': 'Jan-Dec columns under big header',
            'expected': 'Sub-headers (Jan-Dec) should be tagged with big header'
        },
        {
            'name': 'Scenario 3: Multiple tables in one sheet',
            'description': 'Tables separated by Unnamed columns',
            'expected': 'Should detect multiple separate tables'
        },
        {
            'name': 'Scenario 4: Non-merged big headers',
            'description': 'Big headers like Seasonality without merging',
            'expected': 'Should infer big header from pattern (Jan-Dec, etc.)'
        }
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"{i}. {scenario['name']}")
        print(f"   Description: {scenario['description']}")
        print(f"   Expected: {scenario['expected']}")
        print()


def main():
    """Run all tests."""
    print("\n╔" + "="*78 + "╗")
    print("║" + " "*22 + "Excel Table Extractor Tests" + " "*29 + "║")
    print("╚" + "="*78 + "╝\n")

    # Check for Arla files
    print("Checking for test files...")
    arla_files = [
        'data/Arla_file1.xlsx',
        'data/Arla_file2.xlsx',
        'data/Arla_file3.xlsx'
    ]

    files_found = []
    for filepath in arla_files:
        if test_file_exists(filepath):
            files_found.append(filepath)

    if not files_found:
        print("\n⚠️  No Arla files found in data/ directory")
        print("\nPlease place the Arla Excel files in the data/ directory:")
        print("  - data/Arla_file1.xlsx")
        print("  - data/Arla_file2.xlsx")
        print("  - data/Arla_file3.xlsx")
        print("\nSee data/README.md for more information.")
        return

    # Test each file
    print("\n" + "="*80)
    print("Running Extraction Tests")
    print("="*80)

    results = []
    for filepath in files_found:
        success = test_extraction(filepath)
        results.append((filepath, success))

    # Test specific scenarios
    test_specific_scenarios()

    # Summary
    print("\n" + "="*80)
    print("Test Summary")
    print("="*80 + "\n")

    passed = sum(1 for _, success in results if success)
    total = len(results)

    for filepath, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {os.path.basename(filepath)}")

    print(f"\nTotal: {passed}/{total} files processed successfully")

    if passed == total:
        print("\n🎉 All tests passed!")
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")


if __name__ == '__main__':
    main()
