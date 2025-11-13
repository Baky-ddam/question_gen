# How to Extract Tables from Your Arla Excel Files

## Quick Start

### 1. Add Your Arla Files

Place your 3 Arla Excel files in the `data/` directory:

```
data/
├── Arla_file1.xlsx  ← Add this file
├── Arla_file2.xlsx  ← Add this file
├── Arla_file3.xlsx  ← Add this file
└── Demo_Arla_Example.xlsx (example file, already created)
```

### 2. Extract Tables

Run the extraction for each file:

```bash
# File 1
python -m dashboard.extract_tables data/Arla_file1.xlsx

# File 2
python -m dashboard.extract_tables data/Arla_file2.xlsx

# File 3
python -m dashboard.extract_tables data/Arla_file3.xlsx
```

### 3. Get Mapping Tables

For a detailed mapping table (Sheet × Big Header × Sub-header):

```bash
# Show in terminal
python show_mapping_table.py data/Arla_file1.xlsx

# Export to CSV (can open in Excel)
python export_mapping_csv.py data/Arla_file1.xlsx output/arla1_mapping.csv

# Export to JSON
python -m dashboard.extract_tables data/Arla_file1.xlsx --output output/arla1_data.json --summary output/arla1_summary.json
```

---

## What You'll Get

### 1. Terminal Output

Shows a visual summary like this:

```
📄 Sheet: Media Plan
   Tables found: 2

   📊 Table 1:
      Dimensions: 10 rows x 8 columns
      Has merged headers: False

      Columns:
         1. Media Plan > Media Type
         2. Media Plan > Channel
         3. Media Plan > Budget
         ...

   📊 Table 2:
      Dimensions: 10 rows x 12 columns
      Has merged headers: True

      Columns:
         1. Media Plan > Budget (Jan-Dec) > Jan
         2. Media Plan > Budget (Jan-Dec) > Feb
         ...
```

### 2. Mapping Table (CSV)

Format: `Sheet Name, Table ID, Column #, Column Letter, Big Header, Sub-header, Full Path`

```csv
Sheet Name,Table ID,Column #,Column Letter,Big Header,Sub-header,Full Path
Media Plan,1,1,A,,Media Type,Media Plan > Media Type
Media Plan,1,10,J,Budget (Jan-Dec),Jan,Media Plan > Budget (Jan-Dec) > Jan
```

**Open this in Excel** to see the mapping clearly!

### 3. JSON Output

Complete data structure with all rows and columns:

```json
{
  "filename": "Arla_file1.xlsx",
  "sheets": {
    "Media Plan": {
      "tables": [
        {
          "columns": [
            {
              "full_path": "Media Plan > Budget (Jan-Dec) > Jan",
              "big_header": "Budget (Jan-Dec)",
              "sub_header": "Jan"
            }
          ],
          "data": [
            {
              "Media Plan > Budget (Jan-Dec) > Jan": 50000,
              "Media Plan > Budget (Jan-Dec) > Feb": 52000
            }
          ]
        }
      ]
    }
  }
}
```

---

## Expected Scenarios from Arla Files

Based on your requirements, the system handles:

### Scenario 1: Tables Without Big Headers
```
Row 2: | Media Type | Channel | Budget | 0% | 25% | 50% | 75% | 100% |
```

**Expected Output**:
- `Sheet1 > Media Type`
- `Sheet1 > Channel`
- `Sheet1 > Budget`
- `Sheet1 > 0%` ... `Sheet1 > 100%`

### Scenario 2: Tables With Merged Headers (Jan-Dec)
```
Row 1: |          Budget (Jan-Dec)                |
Row 2: | Jan | Feb | Mar | Apr | May | ... | Dec |
```

**Expected Output**:
- `Sheet1 > Budget (Jan-Dec) > Jan`
- `Sheet1 > Budget (Jan-Dec) > Feb`
- ... through Dec

### Scenario 3: Buy Specifics Table
```
Row 1: |         Buy Specifics                    |
Row 2: | Target Audience | Age Range | Gender | ... |
```

**Expected Output**:
- `Sheet1 > Buy Specifics > Target Audience`
- `Sheet1 > Buy Specifics > Age Range`
- `Sheet1 > Buy Specifics > Gender`

### Scenario 4: Multiple Tables (Separated by Unnamed Columns)
```
| Table 1 cols | (empty) | Table 2 cols | (empty) | Table 3 cols |
```

**Expected Output**: 3 separate tables detected

---

## Commands Reference

### Basic Extraction

```bash
# Extract and show in terminal
python -m dashboard.extract_tables data/Arla_file1.xlsx

# Extract specific sheets only
python -m dashboard.extract_tables data/Arla_file1.xlsx --sheets "Sheet1" "Summary"

# Quiet mode (no terminal output)
python -m dashboard.extract_tables data/Arla_file1.xlsx --output results.json --quiet
```

### Mapping Tables

```bash
# Show formatted mapping in terminal
python show_mapping_table.py data/Arla_file1.xlsx

# Export mapping to CSV
python export_mapping_csv.py data/Arla_file1.xlsx output/mapping.csv

# Export summary JSON
python -m dashboard.extract_tables data/Arla_file1.xlsx --summary output/summary.json
```

### Custom Header Rows

If your headers are in different rows:

```bash
# Headers in row 3, big headers in row 2
python -m dashboard.extract_tables data/file.xlsx --header-row 3 --big-header-row 2

# No big headers at all
python -m dashboard.extract_tables data/file.xlsx --header-row 1 --big-header-row 0
```

---

## Programmatic Usage (Python)

```python
from dashboard.extractors import ExcelTableExtractor

# Initialize
extractor = ExcelTableExtractor(header_row=2, big_header_row=1)

# Extract all tables
workbook_tables = extractor.extract_from_file('data/Arla_file1.xlsx')

# Iterate through sheets and tables
for sheet_name, sheet_tables in workbook_tables.sheets.items():
    print(f"Sheet: {sheet_name}")

    for table in sheet_tables.tables:
        print(f"  Table {table.table_id}: {table.get_row_count()} rows")

        # Print column mappings
        for col in table.columns:
            print(f"    {col.get_full_path()}")
            # Example: "Sheet1 > Budget > January"

        # Access data
        for row_data in table.data:
            for column_path, value in row_data.items():
                print(f"    {column_path}: {value}")

# Export to JSON
extractor.export_to_json(workbook_tables, 'output/results.json')
extractor.export_summary(workbook_tables, 'output/summary.json')
```

---

## Testing

Test the system with the demo file:

```bash
# Run all tests
python -m dashboard.test_extraction

# Or test with demo file specifically
python show_mapping_table.py data/Demo_Arla_Example.xlsx
```

Once you add your Arla files:

```bash
# Test all Arla files
for file in data/Arla_*.xlsx; do
    echo "Processing $file..."
    python show_mapping_table.py "$file"
    echo "---"
done
```

---

## Output Files

All outputs are saved to the `output/` directory:

```
output/
├── MAPPING_TABLE.md          # Human-readable mapping documentation
├── column_mapping.csv        # CSV format (open in Excel)
├── demo_summary.json         # JSON summary
├── arla1_data.json          # Full extraction (after you run it)
├── arla1_summary.json       # Summary (after you run it)
└── arla1_mapping.csv        # Mapping table (after you run it)
```

---

## Need Help?

See the documentation:
- **Dashboard README**: `dashboard/README.md`
- **Example Usage**: `dashboard/example_usage.py`
- **Test Script**: `dashboard/test_extraction.py`

Run examples:
```bash
python -m dashboard.example_usage
```

---

## Demo File

A demo file has been created at `data/Demo_Arla_Example.xlsx` showing:
1. Tables without big headers
2. Tables with merged headers (Jan-Dec)
3. Buy Specifics scenario
4. Multiple big headers

Try the extraction on this demo file first:

```bash
python show_mapping_table.py data/Demo_Arla_Example.xlsx
python export_mapping_csv.py data/Demo_Arla_Example.xlsx output/demo_mapping.csv
```

The demo mapping is already available at:
- **Markdown**: `output/MAPPING_TABLE.md`
- **CSV**: `output/column_mapping.csv`
- **JSON**: `output/demo_summary.json`
