"""custom_csv_reader.py

CustomCsvReader: A streaming CSV reader implemented as an iterator.

Reads files character-by-character and yields rows as lists of strings.
Handles:
- fields enclosed in double quotes
- escaped quotes represented by two double quotes inside quoted fields
- embedded newlines within quoted fields
- streaming behaviour (does not load the entire file in memory)
"""
from typing import List, Optional


class CustomCsvReader:
    """A simple CSV reader implemented as an iterator.

    Example:
        with CustomCsvReader('file.csv') as reader:
            for row in reader:
                print(row)
    """

    def __init__(
        self, filepath: str, delimiter: str = ",", quotechar: str = '"'
    ) -> None:
        self.filepath = filepath
        self.delimiter = delimiter
        self.quotechar = quotechar
        self._f = None

    def __enter__(self):
        self._f = open(self.filepath, "r", encoding="utf-8", newline="")
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._f:
            self._f.close()
            self._f = None

    def __iter__(self):
        return self

    def __next__(self) -> List[str]:
        if self._f is None:
            raise StopIteration
        row = self._read_row()
        if row is None:
            raise StopIteration
        return row

    def _read_row(self) -> Optional[List[str]]:
        """Read characters until a full row is parsed or EOF is reached.

        Returns None on EOF (no data read), otherwise a list of field strings.
        """
        f = self._f
        if f is None:
            return None

        field_chars = []
        row: List[str] = []
        in_quotes = False
        saw_any = False

        while True:
            ch = f.read(1)
            if ch == "":
                # EOF reached
                if not saw_any:
                    return None
                # finish last field
                row.append("".join(field_chars))
                return row

            saw_any = True

            if in_quotes:
                if ch == self.quotechar:
                    # peek next char
                    nxt = f.read(1)
                    if nxt == "":
                        # EOF after quote => close quote and finish
                        in_quotes = False
                        row.append("".join(field_chars))
                        return row
                    if nxt == self.quotechar:
                        # escaped quote -> append a single quotechar
                        field_chars.append(self.quotechar)
                        continue
                    if nxt == self.delimiter:
                        # end of field
                        in_quotes = False
                        row.append("".join(field_chars))
                        field_chars = []
                        continue
                    if nxt == "\n":
                        # end of row
                        in_quotes = False
                        row.append("".join(field_chars))
                        return row
                    # Some implementations allow whitespace after closing quote
                    # before delimiter. If we encounter other characters,
                    # we'll treat them as part of the field (conservative).
                    field_chars.append(nxt)
                else:
                    field_chars.append(ch)
            else:
                if ch == self.delimiter:
                    row.append("".join(field_chars))
                    field_chars = []
                elif ch == self.quotechar:
                    # If quote is at start of field (or after whitespace),
                    # enter quoted mode. A quote inside an unquoted field
                    # will be treated as a literal (conservative choice).
                    if len(field_chars) == 0:
                        in_quotes = True
                    else:
                        # quote inside unquoted field; treat as literal
                        field_chars.append(ch)
                elif ch == "\n":
                    row.append("".join(field_chars))
                    return row
                else:
                    field_chars.append(ch)