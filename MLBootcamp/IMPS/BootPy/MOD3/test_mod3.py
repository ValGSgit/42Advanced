"""
Tests for MOD3 exercises:
  ex00 - NumPyCreator
  ex01 - ImageProcessor
  ex02 - ScrapBooker
  ex03 - ColorFilter
  ex04 - KmeansClustering

Run with:  python test_mod3.py
"""
import sys
import os
import unittest
from unittest.mock import patch

import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
for _ex in ("ex00", "ex01", "ex02", "ex03", "ex04"):
    sys.path.insert(0, os.path.join(BASE, _ex))

from NumPyCreator import NumPyCreator
from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
from ColorFilter import ColorFilter
from Kmeans import KmeansClustering, identify_region


# ── ex00: NumPyCreator ─────────────────────────────────────────────────────

class TestNumPyCreatorFromList(unittest.TestCase):
    def setUp(self):
        self.nc = NumPyCreator()

    def test_1d_list(self):
        arr = self.nc.from_list([1, 2, 3])
        self.assertIsInstance(arr, np.ndarray)
        np.testing.assert_array_equal(arr, [1, 2, 3])

    def test_2d_uniform_list(self):
        arr = self.nc.from_list([[1, 2], [3, 4]])
        self.assertEqual(arr.shape, (2, 2))

    def test_jagged_list_returns_none(self):
        self.assertIsNone(self.nc.from_list([[1, 2], [3]]))

    def test_non_list_returns_none(self):
        self.assertIsNone(self.nc.from_list((1, 2, 3)))

    def test_dtype_cast(self):
        arr = self.nc.from_list([1, 2, 3], dtype=float)
        self.assertEqual(arr.dtype, float)

    def test_empty_list(self):
        arr = self.nc.from_list([])
        self.assertIsInstance(arr, np.ndarray)
        self.assertEqual(len(arr), 0)


class TestNumPyCreatorFromTuple(unittest.TestCase):
    def setUp(self):
        self.nc = NumPyCreator()

    def test_basic_tuple(self):
        arr = self.nc.from_tuple((10, 20, 30))
        np.testing.assert_array_equal(arr, [10, 20, 30])

    def test_nested_tuple(self):
        arr = self.nc.from_tuple(((1, 2), (3, 4)))
        self.assertEqual(arr.shape, (2, 2))

    def test_non_tuple_returns_none(self):
        self.assertIsNone(self.nc.from_tuple([1, 2]))

    def test_dtype(self):
        arr = self.nc.from_tuple((1, 2, 3), dtype=np.float64)
        self.assertEqual(arr.dtype, np.float64)


class TestNumPyCreatorFromIterable(unittest.TestCase):
    def setUp(self):
        self.nc = NumPyCreator()

    def test_range(self):
        arr = self.nc.from_iterable(range(5))
        np.testing.assert_array_equal(arr, [0, 1, 2, 3, 4])

    def test_generator(self):
        arr = self.nc.from_iterable(x ** 2 for x in range(5))
        np.testing.assert_array_equal(arr, [0, 1, 4, 9, 16])

    def test_set_produces_array(self):
        arr = self.nc.from_iterable({7, 8, 9})
        self.assertIsInstance(arr, np.ndarray)
        self.assertEqual(sorted(arr), [7, 8, 9])


class TestNumPyCreatorFromShape(unittest.TestCase):
    def setUp(self):
        self.nc = NumPyCreator()

    def test_default_zeros(self):
        arr = self.nc.from_shape((2, 3))
        self.assertEqual(arr.shape, (2, 3))
        self.assertTrue((arr == 0).all())

    def test_custom_value(self):
        arr = self.nc.from_shape((3,), value=7)
        np.testing.assert_array_equal(arr, [7, 7, 7])

    def test_3d_shape(self):
        arr = self.nc.from_shape((2, 3, 4), value=1)
        self.assertEqual(arr.shape, (2, 3, 4))
        self.assertTrue((arr == 1).all())


class TestNumPyCreatorRandom(unittest.TestCase):
    def setUp(self):
        self.nc = NumPyCreator()

    def test_shape(self):
        arr = self.nc.random((4, 5))
        self.assertEqual(arr.shape, (4, 5))

    def test_values_in_unit_interval(self):
        arr = self.nc.random((100, 100))
        self.assertGreaterEqual(arr.min(), 0.0)
        self.assertLessEqual(arr.max(), 1.0)

    def test_invalid_shape_returns_none(self):
        self.assertIsNone(self.nc.random("bad"))


class TestNumPyCreatorIdentity(unittest.TestCase):
    def setUp(self):
        self.nc = NumPyCreator()

    def test_3x3(self):
        arr = self.nc.identity(3)
        np.testing.assert_array_equal(arr, np.eye(3))

    def test_1x1(self):
        arr = self.nc.identity(1)
        self.assertEqual(arr.shape, (1, 1))
        self.assertEqual(arr[0, 0], 1.0)

    def test_dtype_int(self):
        arr = self.nc.identity(3, dtype=int)
        self.assertEqual(arr.dtype, int)
        self.assertEqual(arr[0, 0], 1)
        self.assertEqual(arr[0, 1], 0)


# ── ex01: ImageProcessor ───────────────────────────────────────────────────

IMG_PATH = os.path.join(BASE, "ex01", "elon_canaGAN.png")


class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.ip = ImageProcessor()

    def test_load_returns_ndarray(self):
        arr = self.ip.load(IMG_PATH)
        self.assertIsNotNone(arr)
        self.assertIsInstance(arr, np.ndarray)

    def test_load_is_float32_normalised(self):
        arr = self.ip.load(IMG_PATH)
        self.assertEqual(arr.dtype, np.float32)
        self.assertGreaterEqual(arr.min(), 0.0)
        self.assertLessEqual(arr.max(), 1.0)

    def test_load_has_spatial_and_channel_dims(self):
        arr = self.ip.load(IMG_PATH)
        self.assertEqual(arr.ndim, 3)
        self.assertIn(arr.shape[2], (3, 4))  # RGB or RGBA

    def test_load_missing_file_returns_none(self):
        arr = self.ip.load("/no/such/image.png")
        self.assertIsNone(arr)

    @patch("matplotlib.pyplot.show")
    def test_display_does_not_raise(self, _mock_show):
        arr = self.ip.load(IMG_PATH)
        self.ip.display(arr)  # must not raise


# ── ex02: ScrapBooker ──────────────────────────────────────────────────────

class TestScrapBookerCrop(unittest.TestCase):
    def setUp(self):
        self.sb = ScrapBooker()
        self.arr = np.arange(25).reshape(5, 5)

    def test_basic_shape(self):
        result = self.sb.crop(self.arr, (2, 3), (1, 1))
        self.assertEqual(result.shape, (2, 3))

    def test_correct_values(self):
        result = self.sb.crop(self.arr, (2, 3), (1, 1))
        np.testing.assert_array_equal(result, self.arr[1:3, 1:4])

    def test_default_position(self):
        result = self.sb.crop(self.arr, (2, 2))
        np.testing.assert_array_equal(result, self.arr[:2, :2])

    def test_out_of_bounds_returns_none(self):
        self.assertIsNone(self.sb.crop(self.arr, (4, 4), (3, 3)))

    def test_negative_position_returns_none(self):
        self.assertIsNone(self.sb.crop(self.arr, (2, 2), (-1, 0)))

    def test_zero_dim_returns_none(self):
        self.assertIsNone(self.sb.crop(self.arr, (0, 2), (0, 0)))

    def test_non_array_returns_none(self):
        self.assertIsNone(self.sb.crop([[1, 2], [3, 4]], (1, 1), (0, 0)))


class TestScrapBookerThin(unittest.TestCase):
    def setUp(self):
        self.sb = ScrapBooker()
        self.arr = np.arange(25).reshape(5, 5)

    def test_thin_columns_shape(self):
        # Delete every 2nd column (indices 1, 3) → keep 0, 2, 4
        result = self.sb.thin(self.arr, 2, axis=0)
        self.assertEqual(result.shape, (5, 3))

    def test_thin_columns_values(self):
        result = self.sb.thin(self.arr, 2, axis=0)
        np.testing.assert_array_equal(result[:, 0], self.arr[:, 0])
        np.testing.assert_array_equal(result[:, 1], self.arr[:, 2])
        np.testing.assert_array_equal(result[:, 2], self.arr[:, 4])

    def test_thin_rows_shape(self):
        # Delete every 2nd row → keep rows 0, 2, 4
        result = self.sb.thin(self.arr, 2, axis=1)
        self.assertEqual(result.shape, (3, 5))

    def test_n_zero_returns_none(self):
        self.assertIsNone(self.sb.thin(self.arr, 0, axis=0))

    def test_n_exceeds_dim_returns_none(self):
        self.assertIsNone(self.sb.thin(self.arr, 10, axis=0))

    def test_non_array_returns_none(self):
        self.assertIsNone(self.sb.thin([[1, 2, 3]], 1, axis=0))


class TestScrapBookerJuxtapose(unittest.TestCase):
    def setUp(self):
        self.sb = ScrapBooker()
        self.arr = np.arange(25).reshape(5, 5)

    def test_horizontal_shape(self):
        result = self.sb.juxtapose(self.arr, 3, axis=1)
        self.assertEqual(result.shape, (5, 15))

    def test_vertical_shape(self):
        result = self.sb.juxtapose(self.arr, 2, axis=0)
        self.assertEqual(result.shape, (10, 5))

    def test_n1_identity(self):
        result = self.sb.juxtapose(self.arr, 1, axis=0)
        np.testing.assert_array_equal(result, self.arr)

    def test_n_zero_returns_none(self):
        self.assertIsNone(self.sb.juxtapose(self.arr, 0, axis=0))

    def test_bad_axis_returns_none(self):
        self.assertIsNone(self.sb.juxtapose(self.arr, 2, axis=2))


class TestScrapBookerMosaic(unittest.TestCase):
    def setUp(self):
        self.sb = ScrapBooker()
        self.arr = np.arange(25).reshape(5, 5)

    def test_shape(self):
        result = self.sb.mosaic(self.arr, (2, 3))
        self.assertEqual(result.shape, (10, 15))

    def test_1x1_identity(self):
        result = self.sb.mosaic(self.arr, (1, 1))
        np.testing.assert_array_equal(result, self.arr)

    def test_zero_rows_returns_none(self):
        self.assertIsNone(self.sb.mosaic(self.arr, (0, 3)))

    def test_non_array_returns_none(self):
        self.assertIsNone(self.sb.mosaic([[1, 2]], (2, 2)))


# ── ex03: ColorFilter ──────────────────────────────────────────────────────

class TestColorFilter(unittest.TestCase):
    def setUp(self):
        self.cf = ColorFilter()
        self.img = np.array(
            [[[0.2, 0.5, 0.8], [0.1, 0.9, 0.3]],
             [[0.6, 0.4, 0.0], [0.8, 0.2, 0.7]]],
            dtype=np.float32,
        )

    def test_invert_values(self):
        result = self.cf.invert(self.img)
        np.testing.assert_allclose(result, 1 - self.img, atol=1e-6)

    def test_invert_does_not_mutate_original(self):
        original = self.img.copy()
        self.cf.invert(self.img)
        np.testing.assert_array_equal(self.img, original)

    def test_invert_shape_preserved(self):
        self.assertEqual(self.cf.invert(self.img).shape, self.img.shape)

    def test_to_blue_zeroes_red_and_green(self):
        result = self.cf.to_blue(self.img)
        np.testing.assert_array_equal(result[:, :, 0], 0)
        np.testing.assert_array_equal(result[:, :, 1], 0)

    def test_to_blue_keeps_blue_channel(self):
        result = self.cf.to_blue(self.img)
        np.testing.assert_allclose(result[:, :, 2], self.img[:, :, 2], atol=1e-6)

    def test_to_green_zeroes_red_and_blue(self):
        result = self.cf.to_green(self.img)
        np.testing.assert_allclose(result[:, :, 0], 0, atol=1e-6)
        np.testing.assert_allclose(result[:, :, 2], 0, atol=1e-6)

    def test_to_green_keeps_green_channel(self):
        result = self.cf.to_green(self.img)
        np.testing.assert_allclose(result[:, :, 1], self.img[:, :, 1], atol=1e-6)

    def test_to_red_zeroes_green_and_blue(self):
        result = self.cf.to_red(self.img)
        np.testing.assert_allclose(result[:, :, 1], 0, atol=1e-6)
        np.testing.assert_allclose(result[:, :, 2], 0, atol=1e-6)

    def test_to_red_keeps_red_channel(self):
        result = self.cf.to_red(self.img)
        np.testing.assert_allclose(result[:, :, 0], self.img[:, :, 0], atol=1e-6)

    def test_to_grayscale_mean_shape(self):
        result = self.cf.to_grayscale(self.img, "mean")
        self.assertEqual(result.shape, self.img.shape)

    def test_to_grayscale_mean_all_channels_equal(self):
        result = self.cf.to_grayscale(self.img, "mean")
        np.testing.assert_allclose(result[:, :, 0], result[:, :, 1], atol=1e-6)
        np.testing.assert_allclose(result[:, :, 1], result[:, :, 2], atol=1e-6)

    def test_to_grayscale_mean_correct_value(self):
        result = self.cf.to_grayscale(self.img, "m")
        expected = self.img.mean(axis=2)
        np.testing.assert_allclose(result[:, :, 0], expected, atol=1e-5)

    def test_to_grayscale_weight_pure_red(self):
        result = self.cf.to_grayscale(self.img, "weight",
                                      r_weight=1.0, g_weight=0.0, b_weight=0.0)
        np.testing.assert_allclose(result[:, :, 0], self.img[:, :, 0], atol=1e-6)

    def test_to_grayscale_invalid_filter_returns_none(self):
        self.assertIsNone(self.cf.to_grayscale(self.img, "xyz"))

    def test_to_celluloid_shape_preserved(self):
        result = self.cf.to_celluloid(self.img)
        self.assertEqual(result.shape, self.img.shape)

    def test_to_celluloid_reduces_unique_values(self):
        np.random.seed(0)
        img_large = np.random.rand(20, 20, 3).astype(np.float32)
        result = self.cf.to_celluloid(img_large)
        self.assertLessEqual(len(np.unique(result)), len(np.unique(img_large)))

    def test_to_celluloid_values_within_original_range(self):
        result = self.cf.to_celluloid(self.img)
        self.assertGreaterEqual(result.min(), self.img.min() - 1e-6)
        self.assertLessEqual(result.max(), self.img.max() + 1e-6)


# ── ex04: KmeansClustering ─────────────────────────────────────────────────

class TestKmeansClustering(unittest.TestCase):

    def _two_cluster_data(self, seed=42):
        np.random.seed(seed)
        c1 = np.random.randn(60, 2) + np.array([0.0, 0.0])
        c2 = np.random.randn(60, 2) + np.array([20.0, 20.0])
        return np.vstack([c1, c2])

    def test_predict_separates_well_separated_clusters(self):
        X = self._two_cluster_data()
        km = KmeansClustering(max_iter=100, ncentroid=2)
        km.fit(X)
        labels = km.predict(X)
        self.assertEqual(len(set(labels[:60])), 1)
        self.assertEqual(len(set(labels[60:])), 1)
        self.assertNotEqual(labels[0], labels[60])

    def test_centroids_count(self):
        X = self._two_cluster_data()
        km = KmeansClustering(ncentroid=3)
        km.fit(X)
        self.assertEqual(np.array(km.centroids).shape[0], 3)

    def test_centroids_feature_dim(self):
        X = self._two_cluster_data()
        km = KmeansClustering(ncentroid=2)
        km.fit(X)
        self.assertEqual(np.array(km.centroids).shape[1], X.shape[1])

    def test_labels_in_valid_range(self):
        X = self._two_cluster_data()
        km = KmeansClustering(ncentroid=2)
        km.fit(X)
        labels = km.predict(X)
        self.assertTrue(set(labels).issubset({0, 1}))

    def test_predict_length_matches_input(self):
        X = self._two_cluster_data()
        km = KmeansClustering(ncentroid=2)
        km.fit(X)
        labels = km.predict(X)
        self.assertEqual(len(labels), len(X))

    def test_identify_region_ncentroid4(self):
        centroids = np.array([
            [1.50, 55.0, 1.40],  # Venus – shortest
            [1.70, 70.0, 1.20],  # Earth
            [1.85, 80.0, 1.10],  # Mars
            [2.00, 90.0, 0.90],  # Belt – tallest
        ])
        regions = identify_region(centroids)
        self.assertIn("Venus", regions)
        self.assertIn("Belt", regions)
        self.assertEqual(regions[0], "Venus")
        self.assertEqual(regions[3], "Belt")

    def test_identify_region_non4_returns_cluster_labels(self):
        centroids = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        regions = identify_region(centroids)
        self.assertEqual(len(regions), 3)
        self.assertTrue(all("Cluster" in r for r in regions))


if __name__ == "__main__":
    unittest.main(verbosity=2)
