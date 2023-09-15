import math
import unittest
from test_tasks.mindbox.oop_task import Circle, Triangle


class TestFigures(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle = Triangle(1, 2, 2)
        self.triangle_right = Triangle(3, 5, 4)
        self.circle = Circle(2)

    def test_triangle_is_right_false(self):
        self.assertEqual(self.triangle.is_right, False)

    def test_triangle_is_right_true(self):
        self.assertEqual(self.triangle_right.is_right, True)

    def test_triangle_perimeter(self):
        self.assertEqual(self.triangle.perimeter, 5)

    def test_area_triangle(self):
        self.assertEqual(self.triangle_right.area, 6)

    def test_perimeter_circle(self):
        self.assertEqual(self.circle.perimeter, 2 * math.pi * 2)

    def test_area_circle(self):
        self.assertEqual(self.circle.area, math.pi * 2 ** 2)


if __name__ == "__main__":
    unittest.main()

