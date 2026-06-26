class CsvReader():
    """A context-manager class that opens, reads and parses a CSV file.

    On a missing or corrupted file, __enter__ returns None so the caller
    can test `if file is None`.
    """

    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self._file = None
        self._header = None
        self._body = None

    def __enter__(self):
        try:
            self._file = open(self.filename)
            rows = [line.rstrip('\n').split(self.sep) for line in self._file]
            if len(set(len(r) for r in rows)) > 1:
                self._file.close()
                return None
            if self.header and rows:
                self._header = rows[0]
                rows = rows[1:]
            end = len(rows) - self.skip_bottom if self.skip_bottom else len(rows)
            self._body = rows[self.skip_top:end]
            return self
        except (FileNotFoundError, OSError):
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self._file:
            self._file.close()

    def getdata(self):
        """Retrieves the data/records from skip_top to skip_bottom.

        Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        return self._body

    def getheader(self):
        """Retrieves the header from the csv file.

        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        return self._header


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print("header:", header)
            for row in (data or []):
                print(row)

    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print("header:", header)
            for row in (data or []):
                print(row)