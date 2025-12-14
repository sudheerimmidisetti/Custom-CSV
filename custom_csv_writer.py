"""custom_csv_writer.py

CustomCsvWriter: Writes lists of strings to CSV, quoting and escaping
as required.
"""

from typing import Iterable, List, TextIO


class CustomCsvWriter:
    """Simple CSV writer.

    Usage:
        with CustomCsvWriter('out.csv') as w:
            w.write_row(['a', 'b,c', 'd"e'])

    The writer will automatically quote fields that contain
    the delimiter, quotechar, or newline.
    """

    def __init__(
        self,
        filepath: str,
        delimiter: str = ",",
        quotechar: str = '"',
    ) -> None:
        self.filepath = filepath
        self.delimiter = delimiter
        self.quotechar = quotechar
        self._f: TextIO = None

    def __enter__(self):
        self._f = open(
            self.filepath,
            "w",
            encoding="utf-8",
            newline="",
        )
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._f:
            self._f.close()
            self._f = None

    def _needs_quotes(self, field: str) -> bool:
        return (
            self.delimiter in field
            or self.quotechar in field
            or "\n" in field
            or "\r" in field
        )

    def _escape(self, field: str) -> str:
        # Escape quotes by doubling them
        return field.replace(self.quotechar, self.quotechar * 2)

    def write_row(self, fields: Iterable[str]) -> None:
        if self._f is None:
            raise ValueError("Writer not opened. Use as a context manager.")

        out_fields: List[str] = []

        for f in fields:
            if f is None:
                f = ""
            if self._needs_quotes(f):
                out_fields.append(
                    f'{self.quotechar}{self._escape(f)}{self.quotechar}'
                )
            else:
                out_fields.append(f)

        line = self.delimiter.join(out_fields) + "\n"
        self._f.write(line)

    def write_rows(self, rows: Iterable[Iterable[str]]) -> None:
        for row in rows:
            self.write_row(row)