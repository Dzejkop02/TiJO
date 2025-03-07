import unittest

from studentManagement import StudentManagement


class TaskListTestCase(unittest.TestCase):

    def test_add_student_should_add_student(self):
        # given
        student_mgmt = StudentManagement()

        # when
        result = student_mgmt.add_student('asd', 'Testowy', 22)

        # then
        self.assertTrue(result)
        self.assertEqual(student_mgmt.get_students(), [['Testowy', 22]])

    def test_add_duplicate_student_should_fail(self):
        # given
        student_mgmt = StudentManagement()

        # when
        student_mgmt.add_student('1', 'Jan Kowalski', 22)
        result = student_mgmt.add_student('1', 'Anna Nowak', 23)

        # then
        self.assertFalse(result)

    def test_update_student_should_update_student(self):
        # given
        student_mgmt = StudentManagement()

        # when
        student_mgmt.add_student('asd', 'Testowy', 22)
        result = student_mgmt.update_student('asd', 'Testowy2', 33)

        # then
        self.assertTrue(result)
        self.assertEqual(student_mgmt.get_students(), [['Testowy2', 33]])

    def test_update_nonexistent_student_should_fail(self):
        # given
        student_mgmt = StudentManagement()

        # when
        result = student_mgmt.update_student('999', 'Test', 0)

        # then
        self.assertFalse(result)

    def test_remove_student_should_remove_student(self):
        # given
        student_mgmt = StudentManagement()

        # when
        student_mgmt.add_student('asd', 'Testowy', 22)
        result = student_mgmt.remove_student('asd')
        result2 = student_mgmt.remove_student('qwe')

        # then
        self.assertTrue(result)
        self.assertFalse(result2)
        self.assertEqual(student_mgmt.get_students(), [])

    def test_add_grade_should_add_grade(self):
        # given
        student_mgmt = StudentManagement()

        # when
        student_mgmt.add_student('1', 'Test', 22)
        result = student_mgmt.add_grade('1', 'Math', 4.5)

        # then
        self.assertTrue(result)
        self.assertEqual(student_mgmt.get_student_grades('1', 'Math'), [4.5])

    def test_avg_grades_with_multiple_grades(self):
        # given
        student_mgmt = StudentManagement()

        # when
        student_mgmt.add_student('1', 'A', 20)
        student_mgmt.add_student('2', 'B', 21)
        student_mgmt.add_grade('1', 'Math', 2.0)
        student_mgmt.add_grade('1', 'Math', 4.0)
        student_mgmt.add_grade('2', 'Math', 5.0)

        avg = student_mgmt.avg_grades('Math')

        # then
        self.assertAlmostEqual(avg, (2.0 + 4.0 + 5.0) / 3, places=2)

    def test_avg_grades_no_grades(self):
        # given
        student_mgmt = StudentManagement()

        # when
        avg = student_mgmt.avg_grades('Physics')

        # then
        self.assertEqual(avg, 0.0)


if __name__ == '__main__':
    unittest.main()
