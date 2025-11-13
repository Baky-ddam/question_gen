"""
CLI tool for extracting tables from Excel files.

Usage:
    python -m dashboard.extract_tables <excel_file> [options]

Examples:
    python -m dashboard.extract_tables data/Arla_file1.xlsx
    python -m dashboard.extract_tables data/Arla_file1.xlsx --sheets "Sheet1" "Sheet2"
    python -m dashboard.extract_tables data/Arla_file1.xlsx --output results.json
"""

import argparse
import sys
import os
import json
from pathlib import Path

# Add parent directory to path to import dashboard modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from dashboard.extractors import ExcelTableExtractor


def print_table_summary(workbook_tables):
    """Print a human-readable summary of extracted tables."""
    print(f"\n{'='*80}")
    print(f"Excel File: {workbook_tables.filename}")
    print(f"{'='*80}\n")

    print(f"Total Sheets: {workbook_tables.get_sheet_count()}")
    print(f"Total Tables: {workbook_tables.get_total_tables()}\n")

    for sheet_name, sheet_tables in workbook_tables.sheets.items():
        print(f"\n📄 Sheet: {sheet_name}")
        print(f"   Tables found: {sheet_tables.get_table_count()}")

        for table in sheet_tables.tables:
            print(f"\n   📊 Table {table.table_id}:")
            print(f"      Dimensions: {table.get_row_count()} rows x {table.get_column_count()} columns")
            print(f"      Has merged headers: {table.has_merged_headers}")
            print(f"      Range: Row {table.start_row}-{table.end_row}, Col {table.start_col}-{table.end_col}")

            print(f"\n      Columns:")
            for i, col in enumerate(table.columns, 1):
                if col.big_header:
                    print(f"         {i}. {col.get_full_path()}")
                else:
                    print(f"         {i}. {sheet_name} > {col.sub_header}")

            # Show first few rows of data
            if table.data:
                print(f"\n      Sample data (first 3 rows):")
                for i, row in enumerate(table.data[:3], 1):
                    print(f"         Row {i}:")
                    for key, value in list(row.items())[:5]:  # Show first 5 columns
                        print(f"            {key}: {value}")
                    if len(row) > 5:
                        print(f"            ... ({len(row) - 5} more columns)")

    print(f"\n{'='*80}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Extract tables from Excel files with support for merged headers',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument('excel_file', help='Path to Excel file')
    parser.add_argument('--sheets', nargs='+', help='Specific sheets to process (default: all)')
    parser.add_argument('--header-row', type=int, default=2,
                        help='Row number for sub-headers (default: 2)')
    parser.add_argument('--big-header-row', type=int, default=1,
                        help='Row number for big headers (default: 1)')
    parser.add_argument('--output', '-o', help='Output JSON file path')
    parser.add_argument('--summary', '-s', help='Output summary JSON file path')
    parser.add_argument('--quiet', '-q', action='store_true',
                        help='Suppress console output')

    args = parser.parse_args()

    # Validate input file
    if not os.path.exists(args.excel_file):
        print(f"Error: File not found: {args.excel_file}", file=sys.stderr)
        return 1

    try:
        # Initialize extractor
        extractor = ExcelTableExtractor(
            header_row=args.header_row,
            big_header_row=args.big_header_row if args.big_header_row > 0 else None
        )

        # Extract tables
        if not args.quiet:
            print(f"Extracting tables from: {args.excel_file}")
            if args.sheets:
                print(f"Processing sheets: {', '.join(args.sheets)}")

        workbook_tables = extractor.extract_from_file(
            args.excel_file,
            sheet_names=args.sheets
        )

        # Print summary to console
        if not args.quiet:
            print_table_summary(workbook_tables)

        # Export to JSON if requested
        if args.output:
            extractor.export_to_json(workbook_tables, args.output)
            if not args.quiet:
                print(f"✅ Full data exported to: {args.output}")

        # Export summary if requested
        if args.summary:
            extractor.export_summary(workbook_tables, args.summary)
            if not args.quiet:
                print(f"✅ Summary exported to: {args.summary}")

        if not args.quiet:
            print(f"\n✅ Extraction complete!")
            print(f"   Total tables extracted: {workbook_tables.get_total_tables()}")

        return 0

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
