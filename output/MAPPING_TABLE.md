# Excel Table Mapping: Sheet × Big Header × Sub-header

Generated from: `Demo_Arla_Example.xlsx`

---

## Overview

- **Total Sheets**: 2
- **Total Tables**: 2
- **Total Columns Mapped**: 38

---

## Sheet 1: Media Plan

### Table 1 (2 rows × 21 columns)

**Range**: Row 2-4, Columns A-U
**Has Merged Headers**: Yes

| # | Column | Big Header | Sub-header | Full Path |
|---|--------|------------|------------|-----------|
| 1 | A | *(none)* | Media Type | `Media Plan > Media Type` |
| 2 | B | *(none)* | Channel | `Media Plan > Channel` |
| 3 | C | *(none)* | Budget | `Media Plan > Budget` |
| 4 | D | *(none)* | 0% | `Media Plan > 0%` |
| 5 | E | *(none)* | 25% | `Media Plan > 25%` |
| 6 | F | *(none)* | 50% | `Media Plan > 50%` |
| 7 | G | *(none)* | 75% | `Media Plan > 75%` |
| 8 | H | *(none)* | 100% | `Media Plan > 100%` |
| 9 | I | *(none)* | *(empty)* | `Media Plan > ` |
| 10 | J | **Budget (Jan-Dec)** | Jan | `Media Plan > Budget (Jan-Dec) > Jan` |
| 11 | K | **Budget (Jan-Dec)** | Feb | `Media Plan > Budget (Jan-Dec) > Feb` |
| 12 | L | **Budget (Jan-Dec)** | Mar | `Media Plan > Budget (Jan-Dec) > Mar` |
| 13 | M | **Budget (Jan-Dec)** | Apr | `Media Plan > Budget (Jan-Dec) > Apr` |
| 14 | N | **Budget (Jan-Dec)** | May | `Media Plan > Budget (Jan-Dec) > May` |
| 15 | O | **Budget (Jan-Dec)** | Jun | `Media Plan > Budget (Jan-Dec) > Jun` |
| 16 | P | **Budget (Jan-Dec)** | Jul | `Media Plan > Budget (Jan-Dec) > Jul` |
| 17 | Q | **Budget (Jan-Dec)** | Aug | `Media Plan > Budget (Jan-Dec) > Aug` |
| 18 | R | **Budget (Jan-Dec)** | Sep | `Media Plan > Budget (Jan-Dec) > Sep` |
| 19 | S | **Budget (Jan-Dec)** | Oct | `Media Plan > Budget (Jan-Dec) > Oct` |
| 20 | T | **Budget (Jan-Dec)** | Nov | `Media Plan > Budget (Jan-Dec) > Nov` |
| 21 | U | **Budget (Jan-Dec)** | Dec | `Media Plan > Budget (Jan-Dec) > Dec` |

#### Grouped by Big Header:

**No Big Header** (8 columns):
- Media Type
- Channel
- Budget
- 0%, 25%, 50%, 75%, 100%
- *(1 empty column)*

**Budget (Jan-Dec)** (12 columns):
- Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

---

## Sheet 2: Campaign Details

### Table 1 (1 rows × 17 columns)

**Range**: Row 2-3, Columns A-Q
**Has Merged Headers**: Yes

| # | Column | Big Header | Sub-header | Full Path |
|---|--------|------------|------------|-----------|
| 1 | A | **Buy Specifics** | Target Audience | `Campaign Details > Buy Specifics > Target Audience` |
| 2 | B | **Buy Specifics** | Age Range | `Campaign Details > Buy Specifics > Age Range` |
| 3 | C | **Buy Specifics** | Gender | `Campaign Details > Buy Specifics > Gender` |
| 4 | D | **Buy Specifics** | Location | `Campaign Details > Buy Specifics > Location` |
| 5 | E | **Buy Specifics** | If excluded reason | `Campaign Details > Buy Specifics > If excluded reason` |
| 6 | F | *(none)* | *(empty)* | `Campaign Details > ` |
| 7 | G | **Cost Guarantee** | L3 Benchmark | `Campaign Details > Cost Guarantee > L3 Benchmark` |
| 8 | H | **Budget Variation Index** | Jan | `Campaign Details > Budget Variation Index > Jan` |
| 9 | I | *(none)* | Feb | `Campaign Details > Feb` |
| 10 | J | *(none)* | Mar | `Campaign Details > Mar` |
| 11 | K | *(none)* | Apr | `Campaign Details > Apr` |
| 12 | L | *(none)* | May | `Campaign Details > May` |
| 13 | M | **Seasonality** | Jan | `Campaign Details > Seasonality > Jan` |
| 14 | N | *(none)* | Feb | `Campaign Details > Feb` |
| 15 | O | *(none)* | Mar | `Campaign Details > Mar` |
| 16 | P | *(none)* | Apr | `Campaign Details > Apr` |
| 17 | Q | *(none)* | May | `Campaign Details > May` |

#### Grouped by Big Header:

**Buy Specifics** (5 columns):
- Target Audience
- Age Range
- Gender
- Location
- If excluded reason

**Cost Guarantee** (1 column):
- L3 Benchmark

**Budget Variation Index** (1 column):
- Jan

**Seasonality** (1 column):
- Jan

**No Big Header** (9 columns):
- *(1 empty column)*
- Feb, Mar, Apr, May (appearing twice)

---

## Data Structure Format

Each column is mapped using the hierarchical structure:

```
Sheet Name > Big Header > Sub-header
```

### Examples:

1. **With Big Header (Merged)**:
   ```
   Media Plan > Budget (Jan-Dec) > Jan
   ```
   - Sheet: Media Plan
   - Big Header: Budget (Jan-Dec) *(merged cell)*
   - Sub-header: Jan

2. **Without Big Header**:
   ```
   Media Plan > Media Type
   ```
   - Sheet: Media Plan
   - Big Header: *(none)*
   - Sub-header: Media Type

3. **Multi-level Hierarchy**:
   ```
   Campaign Details > Buy Specifics > Target Audience
   ```
   - Sheet: Campaign Details
   - Big Header: Buy Specifics *(merged cell)*
   - Sub-header: Target Audience

---

## How to Use This Mapping

### Python API:

```python
from dashboard.extractors import ExcelTableExtractor

extractor = ExcelTableExtractor(header_row=2, big_header_row=1)
workbook_tables = extractor.extract_from_file('your_file.xlsx')

# Access column mappings
for sheet_name, sheet_tables in workbook_tables.sheets.items():
    for table in sheet_tables.tables:
        for col in table.columns:
            print(f"{col.get_full_path()}")
            # Example output: "Sheet1 > Budget > January"
```

### CLI:

```bash
# Extract to JSON
python -m dashboard.extract_tables data/file.xlsx --output results.json

# Export summary
python -m dashboard.extract_tables data/file.xlsx --summary summary.json

# Export mapping table to CSV
python export_mapping_csv.py data/file.xlsx output/mapping.csv
```

---

## Files Generated

1. **MAPPING_TABLE.md** (this file) - Human-readable mapping documentation
2. **column_mapping.csv** - CSV format for Excel/spreadsheet tools
3. **demo_summary.json** - JSON summary with table dimensions
4. **Full extraction JSON** - Complete data with all rows and columns

---

## Notes

- Empty columns (unnamed) are detected but included in the table
- Pattern recognition works for Jan-Dec sequences and percentage ranges
- Big headers can be merged cells or inferred from patterns
- Each table can have mixed columns (some with big headers, some without)
