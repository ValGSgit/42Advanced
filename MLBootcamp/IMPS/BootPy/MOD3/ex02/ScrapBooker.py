import numpy as np


class ScrapBooker:

    def crop(self, array, dim, position=(0, 0)):
        """
        Crops array to shape dim starting at position (row, col).
        Returns None if parameters are incompatible.
        np.ndarray is multidimensional array
        """
        try:
            if not isinstance(array, np.ndarray):
                return None
            r, c = position
            h, w = dim
            if r < 0 or c < 0 or h <= 0 or w <= 0:
                return None
            if r + h > array.shape[0] or c + w > array.shape[1]:
                return None
            return array[r:r + h, c:c + w]
        except Exception:
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th column (axis=0) or row (axis=1).
        Returns None if parameters are incompatible.
        """
        try:
            if not isinstance(array, np.ndarray):
                return None
            if n <= 0:
                return None
            if axis == 0:
                # delete columns at indices n-1, 2n-1, 3n-1, ...
                if n > array.shape[1]:
                    return None
                indices = np.arange(n - 1, array.shape[1], n)
                return np.delete(array, indices, axis=1)
            elif axis == 1:
                # delete rows at indices n-1, 2n-1, ...
                if n > array.shape[0]:
                    return None
                indices = np.arange(n - 1, array.shape[0], n)
                return np.delete(array, indices, axis=0)
            return None
        except Exception:
            return None

    def juxtapose(self, array, n, axis):
        """
        Concatenates n copies of array along axis (0=vertical, 1=horizontal).
        Returns None if parameters are incompatible.
        """
        try:
            if not isinstance(array, np.ndarray):
                return None
            if n <= 0 or axis not in (0, 1):
                return None
            return np.concatenate([array] * n, axis=axis)
        except Exception:
            return None

    def mosaic(self, array, dim):
        """
        Tiles array dim[0] times vertically and dim[1] times horizontally.
        Returns None if parameters are incompatible.
        """
        try:
            if not isinstance(array, np.ndarray):
                return None
            rows, cols = dim
            if rows <= 0 or cols <= 0:
                return None
            return np.tile(array, (rows, cols))
        except Exception:
            return None
