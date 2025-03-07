import unittest

from src.studentManagement import StudentManagement


class TaskListTestCase(unittest.TestCase):

    def test_add_student_should_add_student(self):
        # given
        student_mgmt = StudentManagement()

        # when
        result = student_mgmt.add_student('asd', 'Testowy', 22)

        # then
        self.assertTrue(result)
        self.assertEqual(student_mgmt.get_students(), [['Testowy', 22]])

    def test_update_student_should_update_student(self):
        # given
        student_mgmt = StudentManagement()

        # when
        student_mgmt.add_student('asd', 'Testowy', 22)
        result = student_mgmt.update_student('asd', 'Testowy2', 33)

        # then
        self.assertTrue(result)
        self.assertEqual(student_mgmt.get_students(), [['Testowy2', 33]])

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
        result = student_mgmt.add_grade('asd', 'it', 3.0)
        result2 = student_mgmt.add_grade('asd', 'it', 4.5)

        # then
        self.assertTrue(result)
        self.assertTrue(result2)
        self.assertEqual(student_mgmt.get_student_grades('asd', 'id'), [3.0, 4.5])


if __name__ == '__main__':
    unittest.main()
