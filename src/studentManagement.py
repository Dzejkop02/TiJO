class StudentManagement:
    """
    Klasa zarządzająca studentami i ich ocenami.
    """

    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            id: Unikalny identyfikator studenta.
            name: Imię studenta.
            age: Wiek studenta.

        Returns:
            True, jeśli dodanie zakończyło się sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            return False
        self.students[id] = [name, age]
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejącego studenta na podstawie identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.
            name: Imię studenta.
            age: Wiek studenta.

        Returns:
            True, jeśli aktualizacja zakończyła się sukcesem.
            False w przeciwnym wypadku.
        """
        if id not in self.students:
            return False
        self.students[id] = [name, age]
        return True

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jeśli usunięcie zakończyło się sukcesem.
            False w przeciwnym wypadku.
        """
        if id in self.students:
            del self.students[id]
            return True
        return False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocenę z danego przedmiotu dla określonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jeśli dodanie oceny zakończyło się sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0),
            False w przeciwnym razie.
        """
        allowed_grades = {2.0, 3.0, 3.5, 4.0, 4.5, 5.0}
        if student_id not in self.students or grade not in allowed_grades:
            return False

        key = (student_id, subject)
        if key in self.grades:
            self.grades[key].append(grade)
        else:
            self.grades[key] = [grade]
        return True

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza średnią ocen z danego przedmiotu dla wszystkich studentów.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Średnia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        total = 0.0
        count = 0
        for (sid, subj), grades in self.grades.items():
            if subj == subject:
                total += sum(grades)
                count += len(grades)
        return total / count if count != 0 else 0.0

    def get_students(self):
        return list(self.students.values())

    def get_student_grades(self, id: str, subject: str):
        return list(self.grades.get((id, subject), []))