import os
import unittest
import csv_reader


class CsvTests(unittest.TestCase):
    def get_file_name(self):
        project_name = "file.csv".split(".")[-2]
        self.assertEqual(project_name, "file")

    def check_read(self):
        trello = csv_reader.read(os.path.join("csv", "smartGarantie.CSV"), separator=";")
        print(trello)
        self.assertEqual(True, True)


class BoardTests(unittest.TestCase):

    def get_simple_name_for_board(self):
        """
        Gets the simple name (corresponding column in the table) for a board
        :param board_name: <project_name> - <column_name>
        :return: boolean
        """
        board_name = "smartGarantie - Kategorie"
        project_name = "smartGarantie"
        arr_board = board_name.split()
        if str(arr_board[0]) == project_name:
            arr_board.pop(0)
            arr_board.pop(0)
            arr_board = ''.join(arr_board)
        else:
            print("KeyError")
        self.assertEqual(arr_board, "Kategorie")


CsvTests().check_read()
CsvTests().get_file_name()


if __name__ == '__main__':
    unittest.main()
