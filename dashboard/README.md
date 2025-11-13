# Excel Table Extraction System

Automatic table extraction from Excel files with support for merged headers and hierarchical column structures.

## Features

- **Merged Header Detection**: Automatically detects and handles merged cells in header rows
- **Hierarchical Column Mapping**: Tags sub-headers with their parent big headers (Sheet > Big Header > Sub-header)
- **Table Boundary Detection**: Identifies multiple tables in a single sheet based on "Unnamed" columns
- **Pattern Recognition**: Recognizes common patterns like:
  - Month sequences (Jan-Dec)
  - Percentage sequences (0%-100%)
  - Numeric sequences
- **Flexible Export**: Export to JSON with full data or summary

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Command Line Interface

```bash
# Extract all tables from an Excel file
python -m dashboard.extract_tables data/example.xlsx

# Process specific sheets only
python -m dashboard.extract_tables data/example.xlsx --sheets "Sheet1" "Sheet2"

# Export to JSON
python -m dashboard.extract_tables data/example.xlsx --output results.json

# Export summary only
python -m dashboard.extract_tables data/example.xlsx --summary summary.json

# Custom header rows
python -m dashboard.extract_tables data/example.xlsx --header-row 3 --big-header-row 2
```

### Programmatic Usage

```python
from dashboard.extractors import ExcelTableExtractor

# Initialize extractor
extractor = ExcelTableExtractor(
    header_row=2,      # Row with sub-headers
    big_header_row=1   # Row with big/merged headers
)

# Extract tables
workbook_tables = extractor.extract_from_file('data/example.xlsx')

# Access extracted data
for sheet_name, sheet_tables in workbook_tables.sheets.items():
    print(f"Sheet: {sheet_name}")

    for table in sheet_tables.tables:
        print(f"  Table {table.table_id}: {table.get_row_count()} rows x {table.get_column_count()} cols")

        # Access columns with full path
        for col in table.columns:
            print(f"    {col.get_full_path()}")
            # Example: "Sheet1 > Budget > January"

        # Access data
        for row in table.data:
            for column_path, value in row.items():
                print(f"    {column_path}: {value}")

# Export to JSON
extractor.export_to_json(workbook_tables, 'output.json')
extractor.export_summary(workbook_tables, 'summary.json')
```

## How It Works

### 1. Header Detection

The system detects two levels of headers:

- **Big Headers**: Merged cells or parent headers that span multiple columns
- **Sub-headers**: Individual column headers under big headers

Example:
```
|        Budget        |     Actual      |
| Jan | Feb | Mar | ... | Jan | Feb | ... |
```

Result:
- Column 1: `Sheet1 > Budget > Jan`
- Column 2: `Sheet1 > Budget > Feb`
- Column 4: `Sheet1 > Actual > Jan`

### 2. Pattern Recognition

The system recognizes common patterns even without merged headers:

**Month Sequences**:
```
| Jan | Feb | Mar | Apr | May | Jun | ... |
```
→ Automatically groups under "Monthly Data" big header

**Percentage Sequences**:
```
| 0% | 10% | 20% | 30% | ... | 100% |
```
→ Automatically groups under "Percentage Distribution"

### 3. Table Boundary Detection

Multiple tables in one sheet are detected using "Unnamed" columns:

```
| Media Type | Budget | (empty) | Campaign | Budget | (empty) |
|   Table 1 data...   |         |    Table 2 data...  |
```

The empty/unnamed columns act as separators between tables.

### 4. Data Structure

Each table is represented with:

```python
TableStructure(
    sheet_name='Sheet1',
    table_id=1,
    start_row=2,
    end_row=100,
    start_col=1,
    end_col=10,
    columns=[ColumnMapping(...), ...],
    data=[{column_path: value, ...}, ...],
    has_merged_headers=True
)
```

Each column mapping contains:
- `sheet_name`: Sheet name
- `big_header`: Parent header (if exists)
- `sub_header`: Column header
- `column_index`: Excel column number
- `column_letter`: Excel column letter (A, B, C...)
- `header_type`: BIG_HEADER, SUB_HEADER, or STANDALONE

## Examples

### Example 1: Media Type Table

Excel structure:
```
Row 1: |                    (no big header)                     |
Row 2: | Media Type | Budget | Impressions | CTR | Conversions |
```

Extracted columns:
- `Sheet1 > Media Type`
- `Sheet1 > Budget`
- `Sheet1 > Impressions`
- `Sheet1 > CTR`
- `Sheet1 > Conversions`

### Example 2: Monthly Budget with Merged Header

Excel structure:
```
Row 1: |            Budget (Jan-Dec)              |
Row 2: | Jan | Feb | Mar | ... | Nov | Dec |
```

Extracted columns:
- `Sheet1 > Budget (Jan-Dec) > Jan`
- `Sheet1 > Budget (Jan-Dec) > Feb`
- ...

### Example 3: Multiple Tables

Excel structure:
```
Row 1: | Budget Header |      | Actual Header |
Row 2: | Jan | Feb | (empty) | Jan | Feb |
```

Result: 2 separate tables
- Table 1: Budget columns
- Table 2: Actual columns

## Architecture

```
dashboard/
├── __init__.py
├── extractors/
│   ├── __init__.py
│   ├── table_extractor.py      # Main extraction engine
│   ├── header_detector.py      # Header detection logic
│   └── table_structure.py      # Data structures
├── extract_tables.py           # CLI tool
└── README.md
```

## Configuration

### Header Rows

By default:
- `header_row=2`: Sub-headers are in row 2
- `big_header_row=1`: Big headers are in row 1

Adjust these based on your Excel structure:

```python
# Headers start at row 3, big headers at row 2
extractor = ExcelTableExtractor(header_row=3, big_header_row=2)

# No big headers
extractor = ExcelTableExtractor(header_row=1, big_header_row=None)
```

## Use Cases

- **Dashboard Systems**: Automatically extract data for visualization
- **Data Migration**: Convert Excel reports to structured JSON
- **Report Processing**: Parse complex Excel reports with multiple tables
- **Data Analysis**: Extract and analyze multi-level header tables

## Limitations

- Currently supports `.xlsx` files only (OpenPyXL format)
- Assumes headers are in consecutive rows
- Table boundaries detected using "Unnamed" or empty columns

## Future Enhancements

- Support for `.xls` format
- Custom boundary detection rules
- Direct database export
- CSV export option
- Multi-level big headers (3+ levels)
