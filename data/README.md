# Data Directory

Place your Excel files here for table extraction.

## Expected Files

### Arla Example Files

According to the project requirements, there should be 3 Arla Excel files demonstrating different table structures:

1. **Arla file 1**: Tables with and without merged headers
   - Media Type to 100% (no big header)
   - Full year ... to Budget variation (with Jan-Dec as big header)

2. **Arla file 2**: Complex merged headers
   - Buy Specifics: Target audience to If excluded reason
   - L3 Benchmark: Multiple tables with different big headers
     - Cost Guarantee
     - Budget Variation Index
     - Seasonality

3. **Arla file 3**: Mixed header scenarios

## File Structure

```
data/
├── README.md (this file)
├── Arla_file1.xlsx
├── Arla_file2.xlsx
├── Arla_file3.xlsx
└── examples/
    └── (place additional test files here)
```

## Usage

Once you've placed the Excel files here, run:

```bash
# Extract tables from a file
python -m dashboard.extract_tables data/Arla_file1.xlsx

# Export to JSON
python -m dashboard.extract_tables data/Arla_file1.xlsx --output output/arla1_tables.json

# See all options
python -m dashboard.extract_tables --help
```

## File Requirements

- File format: `.xlsx` (Excel 2007+)
- Headers should be in the first few rows
- Multiple tables per sheet are supported
- Tables should be separated by empty/unnamed columns

## Adding Your Own Files

You can add any Excel file to this directory and extract tables from it:

```bash
python -m dashboard.extract_tables data/your_file.xlsx
```

The extractor will automatically:
- Detect merged headers
- Identify table boundaries
- Tag sub-headers with big headers
- Recognize patterns (months, percentages, etc.)
