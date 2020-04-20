import math


def square_area(side):
    return side * side

def rectangle_area(base, height):
    return base * height

def triangle_area(base, height):
	return (base * height)/2

def rhombus_area(diagonal_1, diagonal_2):
	return (diagonal_1 * diagonal_2) / 2

def trapezoid_area(base_minor, base_major, height):
	return (base_minor + base_major) * height/2

def regular_polygon_area(perimeter, apothem):
	return (perimeter*apothem)/2

def circumference_area(radius):
	return math.pi * radius**2

if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            pass

        def test_square_area(self):
            self.assertEqual(25, square_area(5))

        def test_rectangle_area(self):
            self.assertEqual(10 ,rectangle_area(5,2))

        def test_triangle_area(self):
            self.assertEqual(5, triangle_area(5,2))

        def test_rhombus_area(self):
            self.assertEqual(25, rhombus_area(10, 5))

        def test_trapezoid_area(self):
            self.assertEqual(30, trapezoid_area(10, 5, 4))

        def test_regular_polygon_area(self):
            self.assertEqual(25, regular_polygon_area(10, 5))

        def test_circumference_area(self):
            self.assertEqual(math.pi*25, circumference_area(5))

        def tearDown(self):
            # Delete the needed values for the tests
            pass

    unittest.main()
