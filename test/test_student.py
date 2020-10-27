import unittest
from class_definitions import student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = student.Student('Morishita', 'Elijah', 'Coding', 3.5)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Morishita')
        self.assertEqual(self.student.first_name, 'Elijah')
        self.assertEqual(self.student.major, "Coding")

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Morishita')
        self.assertEqual(self.student.first_name, 'Elijah')
        self.assertEqual(self.student.major, "Coding")
        self.assertEqual(self.student.gpa, 3.5)

    def test_student_str(self):
        test_string = str('Morishita' + ", " + 'Elijah' + " has major " + 'Coding' + "with gpa: " + str(3.5))
        self.assertEqual(self.student.__str__(), test_string)

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = student.Student("Morishita", "Elijah", 'Coding, 3.5')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = student.Student("Morishita", 887, 'Coding, 3.5')

    def test_object_not_created_error_first_name(self):
        pass

    def test_object_not_created_error_major(self):
        pass

    def test_object_not_created_error_gpa(self):
        pass

if __name__ == '__main__':
    unittest.main()
