class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)

        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        col_diff = abs(source_col - dest_col)
        row_diff = abs(source_row - dest_row)

        return max(col_diff, row_diff) == 1 and (col_diff + row_diff) > 0

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)

        m1 = (dx == dy and dx != 0)
        m2 = (dx == 0 and dy != 0)
        m3 = (dx != 0 and dy == 0)

        return m1 or m2 or m3

class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = abs(source_row - dest_row)

        m1 = (dx == 0 and dy != 0)
        m2 = (dx != 0 and dy == 0)

        return m1 or m2

class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        dx = abs(source_col - dest_col)
        dy = dest_row - source_row

        if dx != 0:
            return False

        if dy == 0:
            return False

        if dy == 1:
            return True

        if dy == 2 and source_row == 2:
            return True

        return False
