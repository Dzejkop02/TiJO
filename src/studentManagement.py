class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """

    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli dodanie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            return False
        else:
            self.students[id] = [name, age]
            return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejacego studenta na podstawie identyfikatora.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli aktualizacja zakonczyla sie sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            self.students[id] = [name, age]
            return True
        else:
            return False

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli usuniecie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            self.students.pop(id)
            return True
        else:
            return False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocene z danego przedmiotu dla okreslonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jesli dodanie oceny zakonczylo sie sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0),
            False w przeciwnym razie.
        """
        if (student_id, subject) in self.grades:
            self.grades[(student_id, subject)].append(grade)
            return True
        else:
            self.grades[(student_id, subject)] = [grade]
            return True

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza srednia ocen z danego przedmiotu dla wszystkich studentow.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Srednia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        pass  # Implementacja obliczania sredniej ocen

    def get_students(self):
        return list(self.students.values())

    def get_student_grades(self, id, subject):
        return list(self.grades[(id, subject)])
