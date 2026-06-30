import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    def load(self, path):
        try:
            arr = mpimg.imread(path)
            # Normalise uint8 images to float32 in [0.0, 1.0]
            if arr.dtype == np.uint8:
                arr = arr.astype(np.float32) / 255.0 #typecasting uint8 array to float32
            h, w = arr.shape[:2] #tuple of first 2 dimensions
            print(f"Loading image of dimensions {w} x {h}")
            return arr
        except FileNotFoundError as e:
            print(f"Exception: FileNotFoundError -- strerror: {e.strerror}")
            return None
        except OSError as e:
            print(f"Exception: OSError -- strerror: {e.strerror}")
            return None
        except Exception as e:
            print(f"Exception: {type(e).__name__} -- {e}")
            return None

    def display(self, array):
        plt.imshow(array)
        plt.axis('off')
        plt.show()
