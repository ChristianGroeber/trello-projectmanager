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

    def add_list_from_csv(self):
        cols_to_ignore = ["NR", "Anforderung"]
        boards = {}
        self.csv = csv_reader.read(os.path.join('csv', 'smartGarantie.CSV'), ';')
        for board in range(len(self.csv[0])):
            boards[board] = []
        for y in range(len(self.csv)):
            for x in range(len(self.csv[y])):
                if not y == 0 and self.csv[0][x] not in cols_to_ignore:
                    boards[x].append(self.csv[y][x])
        dict_len = len(boards.keys())
        for z in range(dict_len):
            if len(boards[z]) == 0:
                boards.pop(z)
            else:
                boards[self.csv[0][z]] = boards[z]
                boards.pop(z)
        print(boards)
        for board in boards.keys():
            print(board)
            boards[board] = list(dict.fromkeys(boards[board]))
        print(boards)
        for board in boards:
            for my_list in boards[board]:
                print(my_list)


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


CsvTests().add_list_from_csv()


if __name__ == '__main__':
    unittest.main()
