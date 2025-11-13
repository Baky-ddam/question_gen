"""
Data structures for representing extracted Excel tables.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum


class HeaderType(Enum):
    """Types of headers in Excel tables."""
    BIG_HEADER = "big_header"  # Merged header or parent header
    SUB_HEADER = "sub_header"  # Column header under big header
    STANDALONE = "standalone"  # No big header above


@dataclass
class ColumnMapping:
    """
    Represents a column mapping with its hierarchy.
    Format: Sheet x Table Header x Sub-header
    """
    sheet_name: str
    big_header: Optional[str]  # Can be None for standalone columns
    sub_header: str
    column_index: int
    column_letter: str
    header_type: HeaderType

    def get_full_path(self) -> str:
        """Get full hierarchical path: Sheet > BigHeader > SubHeader"""
        if self.big_header:
            return f"{self.sheet_name} > {self.big_header} > {self.sub_header}"
        return f"{self.sheet_name} > {self.sub_header}"

    def __repr__(self):
        return f"ColumnMapping({self.get_full_path()})"


@dataclass
class TableStructure:
    """Represents a detected table in an Excel sheet."""
    sheet_name: str
    table_id: int
    start_row: int
    end_row: int
    start_col: int
    end_col: int
    columns: List[ColumnMapping] = field(default_factory=list)
    data: List[Dict[str, Any]] = field(default_factory=list)
    has_merged_headers: bool = False

    def get_column_count(self) -> int:
        """Get number of columns in this table."""
        return len(self.columns)

    def get_row_count(self) -> int:
        """Get number of data rows in this table."""
        return len(self.data)

    def to_dict(self) -> Dict:
        """Convert table structure to dictionary format."""
        return {
            'sheet_name': self.sheet_name,
            'table_id': self.table_id,
            'dimensions': {
                'start_row': self.start_row,
                'end_row': self.end_row,
                'start_col': self.start_col,
                'end_col': self.end_col,
                'rows': self.get_row_count(),
                'columns': self.get_column_count()
            },
            'has_merged_headers': self.has_merged_headers,
            'columns': [
                {
                    'full_path': col.get_full_path(),
                    'sheet': col.sheet_name,
                    'big_header': col.big_header,
                    'sub_header': col.sub_header,
                    'column_index': col.column_index,
                    'column_letter': col.column_letter,
                    'type': col.header_type.value
                }
                for col in self.columns
            ],
            'data': self.data
        }

    def __repr__(self):
        return (f"TableStructure(sheet='{self.sheet_name}', table_id={self.table_id}, "
                f"rows={self.get_row_count()}, cols={self.get_column_count()})")


@dataclass
class SheetTables:
    """Collection of tables from a single sheet."""
    sheet_name: str
    tables: List[TableStructure] = field(default_factory=list)

    def add_table(self, table: TableStructure):
        """Add a table to this sheet."""
        self.tables.append(table)

    def get_table_count(self) -> int:
        """Get number of tables in this sheet."""
        return len(self.tables)

    def to_dict(self) -> Dict:
        """Convert to dictionary format."""
        return {
            'sheet_name': self.sheet_name,
            'table_count': self.get_table_count(),
            'tables': [table.to_dict() for table in self.tables]
        }


@dataclass
class WorkbookTables:
    """Collection of tables from an entire workbook."""
    filename: str
    sheets: Dict[str, SheetTables] = field(default_factory=dict)

    def add_sheet(self, sheet: SheetTables):
        """Add a sheet to the workbook."""
        self.sheets[sheet.sheet_name] = sheet

    def get_sheet_count(self) -> int:
        """Get number of sheets."""
        return len(self.sheets)

    def get_total_tables(self) -> int:
        """Get total number of tables across all sheets."""
        return sum(sheet.get_table_count() for sheet in self.sheets.values())

    def to_dict(self) -> Dict:
        """Convert to dictionary format."""
        return {
            'filename': self.filename,
            'sheet_count': self.get_sheet_count(),
            'total_tables': self.get_total_tables(),
            'sheets': {
                name: sheet.to_dict()
                for name, sheet in self.sheets.items()
            }
        }
