class LunarRover:
    # Mapowanie obrotów w lewo (rotate_left)
    _left_turn_map = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }

    # Mapowanie obrotów w prawo (rotate_right)
    _right_turn_map = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    def __init__(self, x=0, y=0, orientation='N'):
        self.x = x
        self.y = y

        if orientation not in ('N', 'E', 'S', 'W'):
            raise ValueError("Orientation must be one of: 'N', 'E', 'S', 'W'.")
        self.orientation = orientation

    def move_forward(self, steps=1):
        if self.orientation == 'N':
            self.y += steps
        elif self.orientation == 'S':
            self.y -= steps
        elif self.orientation == 'E':
            self.x += steps
        elif self.orientation == 'W':
            self.x -= steps

    def move_backward(self, steps=1):
        if self.orientation == 'N':
            self.y -= steps
        elif self.orientation == 'S':
            self.y += steps
        elif self.orientation == 'E':
            self.x -= steps
        elif self.orientation == 'W':
            self.x += steps

    def rotate_left(self):
        self.orientation = self._left_turn_map[self.orientation]

    def rotate_right(self):
        self.orientation = self._right_turn_map[self.orientation]

    def get_position(self):
        return (self.x, self.y)

    def get_orientation(self):
        return self.orientation

    def __repr__(self):
        return f"<LunarRover x={self.x}, y={self.y}, orientation={self.orientation}>"
