import unittest
from script2 import LunarRover


class TestLunarRover(unittest.TestCase):
    def test_default_initialization(self):
        rover = LunarRover()
        self.assertEqual(rover.get_position(), (0, 0))
        self.assertEqual(rover.get_orientation(), 'N')

    def test_custom_initialization(self):
        rover = LunarRover(x=5, y=-3, orientation='S')
        self.assertEqual(rover.get_position(), (5, -3))
        self.assertEqual(rover.get_orientation(), 'S')

    def test_invalid_orientation(self):
        with self.assertRaises(ValueError):
            LunarRover(0, 0, orientation='X')  # Niepoprawna orientacja

    def test_move_forward_north(self):
        rover = LunarRover(0, 0, 'N')
        rover.move_forward(3)
        self.assertEqual(rover.get_position(), (0, 3))
        self.assertEqual(rover.get_orientation(), 'N')

    def test_move_forward_east(self):
        rover = LunarRover(0, 0, 'E')
        rover.move_forward(2)
        self.assertEqual(rover.get_position(), (2, 0))
        self.assertEqual(rover.get_orientation(), 'E')

    def test_move_backward_north(self):
        rover = LunarRover(0, 0, 'N')
        rover.move_backward(2)
        self.assertEqual(rover.get_position(), (0, -2))
        self.assertEqual(rover.get_orientation(), 'N')

    def test_rotate_left(self):
        rover = LunarRover(0, 0, 'N')
        rover.rotate_left()  # N -> W
        self.assertEqual(rover.get_orientation(), 'W')
        rover.rotate_left()  # W -> S
        self.assertEqual(rover.get_orientation(), 'S')

    def test_rotate_right(self):
        rover = LunarRover(0, 0, 'N')
        rover.rotate_right()  # N -> E
        self.assertEqual(rover.get_orientation(), 'E')
        rover.rotate_right()  # E -> S
        self.assertEqual(rover.get_orientation(), 'S')

    def test_sequence_of_moves(self):
        # Start na (0, 0, 'N')
        rover = LunarRover()
        # Idziemy 2 pola do przodu -> (0, 2, 'N')
        rover.move_forward(2)
        # Skręt w prawo -> orientacja E
        rover.rotate_right()
        # Jeszcze 3 pola do przodu -> (3, 2, 'E')
        rover.move_forward(3)
        # Skręt w lewo -> orientacja N
        rover.rotate_left()
        # 1 do tyłu -> (3, 1, 'N')
        rover.move_backward(1)

        self.assertEqual(rover.get_position(), (3, 1))
        self.assertEqual(rover.get_orientation(), 'N')


if __name__ == '__main__':
    unittest.main()
