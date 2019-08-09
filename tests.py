import unittest


class CsvTests(unittest.TestCase):
    def get_file_name(self):
        project_name = "file.csv".split(".")[-2]
        self.assertEqual(project_name, "file")


if __name__ == '__main__':
    unittest.main()
