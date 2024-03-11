import unittest
import turtle
from snake import check_border_collision

class TestBorderCollision(unittest.TestCase):
    def setUp(self):
        # Set up a turtle for testing
        self.head = turtle.Turtle()

    def test_border_collision(self):
        # Set head position outside the border
        self.head.goto(300, 0)
        # Assert that collision is detected
        self.assertTrue(check_border_collision(self.head))

if __name__ == "__main__":
    unittest.main()
