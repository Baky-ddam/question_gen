"""
Example script demonstrating how to use the Excel Table Extractor.

This script shows various ways to extract and work with tables from Excel files.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dashboard.extractors import ExcelTableExtractor


def example_basic_extraction():
    """Basic table extraction example."""
    print("="*80)
    print("Example 1: Basic Table Extraction")
    print("="*80)

    # Initialize extractor with default settings
    # header_row=2 means sub-headers are in row 2
    # big_header_row=1 means big/merged headers are in row 1
    extractor = ExcelTableExtractor(header_row=2, big_header_row=1)

    # Extract tables from file
    # Replace with your actual file path
    excel_file = "data/Arla_file1.xlsx"

    try:
        workbook_tables = extractor.extract_from_file(excel_file)

        print(f"\nExtracted from: {workbook_tables.filename}")
        print(f"Total sheets: {workbook_tables.get_sheet_count()}")
        print(f"Total tables: {workbook_tables.get_total_tables()}")

        return workbook_tables

    except FileNotFoundError:
        print(f"\nFile not found: {excel_file}")
        print("Please place your Excel file in the data/ directory")
        return None


def example_iterate_tables(workbook_tables):
    """Example of iterating through extracted tables."""
    if not workbook_tables:
        return

    print("\n" + "="*80)
    print("Example 2: Iterating Through Tables")
    print("="*80)

    for sheet_name, sheet_tables in workbook_tables.sheets.items():
        print(f"\n📄 Sheet: {sheet_name}")

        for table in sheet_tables.tables:
            print(f"\n  📊 Table {table.table_id}")
            print(f"     Rows: {table.get_row_count()}")
            print(f"     Columns: {table.get_column_count()}")
            print(f"     Has merged headers: {table.has_merged_headers}")

            # Show column structure
            print(f"\n     Column structure:")
            for col in table.columns:
                if col.big_header:
                    print(f"       - {col.big_header} > {col.sub_header}")
                else:
                    print(f"       - {col.sub_header}")


def example_access_data(workbook_tables):
    """Example of accessing table data."""
    if not workbook_tables:
        return

    print("\n" + "="*80)
    print("Example 3: Accessing Table Data")
    print("="*80)

    # Get first sheet
    first_sheet = list(workbook_tables.sheets.values())[0]

    if not first_sheet.tables:
        print("No tables found in first sheet")
        return

    # Get first table
    first_table = first_sheet.tables[0]

    print(f"\nAccessing data from: {first_table.sheet_name}, Table {first_table.table_id}")
    print(f"\nColumn paths:")
    for i, col in enumerate(first_table.columns[:5], 1):  # Show first 5 columns
        print(f"  {i}. {col.get_full_path()}")

    if len(first_table.columns) > 5:
        print(f"  ... and {len(first_table.columns) - 5} more columns")

    # Access data rows
    print(f"\nFirst 3 data rows:")
    for i, row_data in enumerate(first_table.data[:3], 1):
        print(f"\n  Row {i}:")
        for col_path, value in list(row_data.items())[:3]:  # Show first 3 values
            print(f"    {col_path}: {value}")
        if len(row_data) > 3:
            print(f"    ... ({len(row_data) - 3} more values)")


def example_filter_by_header(workbook_tables):
    """Example of filtering data by big header."""
    if not workbook_tables:
        return

    print("\n" + "="*80)
    print("Example 4: Filtering Data by Big Header")
    print("="*80)

    # Get first table
    first_sheet = list(workbook_tables.sheets.values())[0]
    if not first_sheet.tables:
        return

    first_table = first_sheet.tables[0]

    # Group columns by big header
    headers_groups = {}
    for col in first_table.columns:
        big_header = col.big_header or "No Big Header"
        if big_header not in headers_groups:
            headers_groups[big_header] = []
        headers_groups[big_header].append(col.sub_header)

    print(f"\nColumn groups in Table {first_table.table_id}:")
    for big_header, sub_headers in headers_groups.items():
        print(f"\n  {big_header}:")
        for sub_header in sub_headers[:5]:  # Show first 5
            print(f"    - {sub_header}")
        if len(sub_headers) > 5:
            print(f"    ... and {len(sub_headers) - 5} more")


def example_export_data(workbook_tables):
    """Example of exporting data to JSON."""
    if not workbook_tables:
        return

    print("\n" + "="*80)
    print("Example 5: Exporting Data")
    print("="*80)

    extractor = ExcelTableExtractor()

    # Export full data
    output_file = "output/extracted_tables.json"
    try:
        extractor.export_to_json(workbook_tables, output_file)
        print(f"\n✅ Full data exported to: {output_file}")
    except Exception as e:
        print(f"\n❌ Export failed: {e}")

    # Export summary
    summary_file = "output/summary.json"
    try:
        extractor.export_summary(workbook_tables, summary_file)
        print(f"✅ Summary exported to: {summary_file}")
    except Exception as e:
        print(f"❌ Summary export failed: {e}")


def example_custom_header_rows():
    """Example with custom header row numbers."""
    print("\n" + "="*80)
    print("Example 6: Custom Header Row Configuration")
    print("="*80)

    # If your Excel has headers in different rows
    # For example: big headers in row 3, sub-headers in row 4
    extractor = ExcelTableExtractor(header_row=4, big_header_row=3)

    print("\nConfigured for:")
    print("  - Big headers in row 3")
    print("  - Sub-headers in row 4")

    # Or if there are no big headers at all
    extractor_no_big_headers = ExcelTableExtractor(header_row=1, big_header_row=None)
    print("\nOr with no big headers:")
    print("  - Only sub-headers in row 1")


def example_process_specific_sheets():
    """Example of processing specific sheets only."""
    print("\n" + "="*80)
    print("Example 7: Process Specific Sheets")
    print("="*80)

    extractor = ExcelTableExtractor()
    excel_file = "data/Arla_file1.xlsx"

    try:
        # Process only specific sheets
        workbook_tables = extractor.extract_from_file(
            excel_file,
            sheet_names=["Sheet1", "Summary"]  # Only these sheets
        )

        print(f"\nProcessed sheets: {list(workbook_tables.sheets.keys())}")

    except FileNotFoundError:
        print(f"\nFile not found: {excel_file}")
        print("This is just a demonstration of how to specify sheets")


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "Excel Table Extractor Examples" + " "*28 + "║")
    print("╚" + "="*78 + "╝")

    # Run examples
    workbook_tables = example_basic_extraction()

    if workbook_tables:
        example_iterate_tables(workbook_tables)
        example_access_data(workbook_tables)
        example_filter_by_header(workbook_tables)
        example_export_data(workbook_tables)

    example_custom_header_rows()
    example_process_specific_sheets()

    print("\n" + "="*80)
    print("Examples completed!")
    print("="*80 + "\n")


if __name__ == '__main__':
    main()
