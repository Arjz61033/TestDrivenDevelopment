from volume_cube import *
import unittest
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(volume_cube(2), 8)
        self.assertAlmostEqual(volume_cube(2), 9)

    def test_input_type(self):
        self.assertAlmostEqual(volume_cube(5.5), 166.375)
        volume_cube('hello')

    def test_zero_input(self):
        volume_cube(0)

    def test_negative_input(self):
        self.assertGreater(volume_cube(-1), 0)