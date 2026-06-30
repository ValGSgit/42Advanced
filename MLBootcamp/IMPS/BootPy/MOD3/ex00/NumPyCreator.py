import numpy as np


class NumPyCreator:

    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return None
        try:
            # Detect jagged nested lists before letting NumPy produce an object array
            if lst and isinstance(lst[0], list):
                first_len = len(lst[0])
                if any(not isinstance(row, list) or len(row) != first_len for row in lst):
                    return None
            arr = np.array(lst, dtype=dtype)
            return arr
        except Exception:
            return None

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        try:
            return np.array(tpl, dtype=dtype)
        except Exception:
            return None

    def from_iterable(self, itr, dtype=None):
        try:
            return np.array(list(itr), dtype=dtype)
        except Exception:
            return None

    def from_shape(self, shape, value=0, dtype=None):
        try:
            return np.full(shape, value, dtype=dtype)
        except Exception:
            return None

    def random(self, shape, dtype=None):
        try:
            arr = np.random.random(shape)
            if dtype is not None:
                arr = arr.astype(dtype)
            return arr
        except Exception:
            return None

    def identity(self, n, dtype=None):
        try:
            return np.eye(n, dtype=dtype)
        except Exception:
            return None
