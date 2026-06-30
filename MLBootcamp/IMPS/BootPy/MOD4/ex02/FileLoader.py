import pandas as pd


class FileLoader:

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
            return df
        except Exception:
            return None

    def display(self, df, n):
        try:
            if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
                return
            if n > 0:
                print(df.head(n))
            elif n < 0:
                print(df.tail(-n))
        except Exception:
            return
