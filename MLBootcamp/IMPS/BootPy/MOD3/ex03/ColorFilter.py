import numpy as np


class ColorFilter:

    def invert(self, array):
        """Inverts colours: new = 1 - old (for float images in [0,1])."""
        try:
            result = array.copy()
            result = 1 - result
            return result
        except Exception:
            return None

    def to_blue(self, array):
        """Keeps only the blue channel; red and green become 0."""
        try:
            result = array.copy()
            zeros = np.zeros(array.shape[:2])
            result = np.dstack((zeros, zeros, result[:, :, 2]))
            return result
        except Exception:
            return None

    def to_green(self, array):
        """Keeps only the green channel; red and blue are multiplied by 0."""
        try:
            result = array.copy()
            result[:, :, 0] = result[:, :, 0] * 0
            result[:, :, 2] = result[:, :, 2] * 0
            return result
        except Exception:
            return None

    def to_red(self, array):
        """Keeps only the red channel using to_green and to_blue."""
        try:
            result = array.copy()
            result = result - self.to_green(result) - self.to_blue(result)
            return result
        except Exception:
            return None

    def to_celluloid(self, array):
        """
        Applies cel-shading: quantises pixel values to a fixed number of shade
        levels (thresholds). Uses at least 4 thresholds.
        """
        try:
            result = array.copy()
            thresholds = np.linspace(array.min(), array.max(), 5)
            for i in np.arange(len(thresholds) - 1):
                low = thresholds[i]
                high = thresholds[i + 1]
                mask = (result >= low) & (result <= high)
                result[mask] = low
            return result
        except Exception:
            return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Converts to grayscale.
        filter='mean'/'m'   : average of R, G, B channels.
        filter='weight'/'w' : weighted average using r_weight, g_weight, b_weight.
        """
        try:
            if filter in ('m', 'mean'):
                weights = np.array([1 / 3, 1 / 3, 1 / 3])
            elif filter in ('w', 'weight'):
                weights = np.array([
                    kwargs.get('r_weight', 1 / 3),
                    kwargs.get('g_weight', 1 / 3),
                    kwargs.get('b_weight', 1 / 3),
                ])
            else:
                return None

            # weighted sum over channel axis → shape (H, W)
            gray = (array[:, :, :3] * weights).sum(axis=2)

            # broadcast back to (H, W, 3) so it's still a valid image array
            gray = gray.reshape(gray.shape[0], gray.shape[1], 1)
            gray = np.broadcast_to(gray, array[:, :, :3].shape).astype(array.dtype)
            return gray
        except Exception:
            return None
