"""
Export mapping table to CSV format for easy viewing in Excel or spreadsheet tools.
"""

import sys
import csv
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dashboard.extractors import ExcelTableExtractor


def export_mapping_to_csv(excel_file, output_csv):
    """Export column mappings to CSV file."""

    # Extract tables
    extractor = ExcelTableExtractor(header_row=2, big_header_row=1)
    workbook_tables = extractor.extract_from_file(excel_file)

    # Prepare CSV data
    headers = ['Sheet Name', 'Table ID', 'Column #', 'Column Letter', 'Big Header', 'Sub-header', 'Full Path', 'Has Merged Headers']
    rows = []

    for sheet_name, sheet_tables in workbook_tables.sheets.items():
        for table in sheet_tables.tables:
            for i, col in enumerate(table.columns, 1):
                row = [
                    sheet_name,
                    table.table_id,
                    i,
                    col.column_letter,
                    col.big_header if col.big_header else '',
                    col.sub_header,
                    col.get_full_path(),
                    'Yes' if table.has_merged_headers else 'No'
                ]
                rows.append(row)

    # Write CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"✅ Mapping table exported to: {output_csv}")
    print(f"   Total columns mapped: {len(rows)}")

    return rows


if __name__ == '__main__':
    excel_file = sys.argv[1] if len(sys.argv) > 1 else 'data/Demo_Arla_Example.xlsx'
    output_csv = sys.argv[2] if len(sys.argv) > 2 else 'output/column_mapping.csv'

    try:
        export_mapping_to_csv(excel_file, output_csv)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
