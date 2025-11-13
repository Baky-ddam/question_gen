"""
Generate a clear mapping table showing Sheet x Big Header x Sub-header structure.
"""

import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))

from dashboard.extractors import ExcelTableExtractor


def print_mapping_table(excel_file):
    """Print a formatted mapping table."""

    # Extract tables
    extractor = ExcelTableExtractor(header_row=2, big_header_row=1)
    workbook_tables = extractor.extract_from_file(excel_file)

    print("\n" + "="*100)
    print(f"MAPPING TABLE: {workbook_tables.filename}")
    print("="*100)
    print(f"\nFormat: Sheet Name > Big Header > Sub-header")
    print("-"*100)

    # Group by sheet
    for sheet_name, sheet_tables in workbook_tables.sheets.items():
        print(f"\n{'='*100}")
        print(f"📄 SHEET: {sheet_name}")
        print(f"{'='*100}")

        for table in sheet_tables.tables:
            print(f"\n📊 TABLE {table.table_id} ({table.get_row_count()} rows × {table.get_column_count()} columns)")
            print(f"   Range: Row {table.start_row}-{table.end_row}, Col {table.start_col}-{table.end_col}")
            print(f"   Has Merged Headers: {table.has_merged_headers}")
            print(f"\n   {'No.':<5} {'Column Letter':<15} {'Big Header':<30} {'Sub-header':<25} {'Full Path'}")
            print(f"   {'-'*5} {'-'*15} {'-'*30} {'-'*25} {'-'*50}")

            for i, col in enumerate(table.columns, 1):
                big_header = col.big_header if col.big_header else "(none)"
                full_path = col.get_full_path()

                print(f"   {i:<5} {col.column_letter:<15} {big_header:<30} {col.sub_header:<25}")

    # Create a summary grouped by big headers
    print(f"\n\n{'='*100}")
    print("SUMMARY: Columns Grouped by Big Header")
    print(f"{'='*100}\n")

    for sheet_name, sheet_tables in workbook_tables.sheets.items():
        for table in sheet_tables.tables:
            # Group columns by big header
            groups = defaultdict(list)
            for col in table.columns:
                key = col.big_header if col.big_header else "(No Big Header)"
                groups[key].append(col.sub_header)

            print(f"📄 {sheet_name} - Table {table.table_id}:")
            for big_header, sub_headers in groups.items():
                print(f"\n   {big_header}:")
                for sub_header in sub_headers:
                    print(f"      └─ {sub_header}")
            print()


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        excel_file = sys.argv[1]
    else:
        excel_file = 'data/Demo_Arla_Example.xlsx'

    try:
        print_mapping_table(excel_file)
    except FileNotFoundError:
        print(f"❌ File not found: {excel_file}")
        print("\nUsage: python show_mapping_table.py <excel_file>")
        print("Example: python show_mapping_table.py data/Arla_file1.xlsx")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
