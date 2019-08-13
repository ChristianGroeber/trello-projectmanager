import os
import auth
import csv_reader
import models


class Trello:
    def __init__(self, name, extension, separator):
        self.extension = extension
        self.name = name
        self.separator = separator
        self.file = os.path.join("csv", name + "." + extension)
        self.client = auth.authorize()
        self.project = models.TrelloProject(self.name, self.client)
        self.csv = None

    def add_board_from_csv(self, file):
        head = csv_reader.read(file)[0]
        for board in head:
            full_board = self.name + " - " + board
            if "NR" not in str(board) and "id" not in str(board) and "Anforderung" not in str(board):
                self.project.add_board(full_board, board)

    def csv_as_dict(self):
        self.csv = csv_reader.read(self.file, self.separator)
        boards = {}
        for board in range(len(self.csv[0])):
            boards[board] = []
        for y in range(len(self.csv)):
            for x in range(len(self.csv[y])):
                if not y == 0:
                    boards[x].append(self.csv[y][x])
        dict_len = len(boards.keys())
        for z in range(dict_len):
            if len(boards[z]) == 0:
                boards.pop(z)
            else:
                # before, the list is just a number, now that number gets replaced by the list's name.
                boards[self.csv[0][z]] = boards[z]
                boards.pop(z)
        return boards

    def add_list_from_csv(self):
        cols_to_ignore = ["NR", "Anforderung"]
        boards = self.csv_as_dict()
        print(boards)
        for board in boards:
            print(boards[board])
            boards[board] = list(dict.fromkeys(boards[board]))
        print(boards)
        for board in boards:
            for my_list in boards[board]:
                trello_board = self.project.get_board_from_simple_name(board)
                trello_board.add_list(my_list)

    def add_cards_from_csv(self):
        boards = self.csv_as_dict()
        cards = boards['Anfoderung']
        for card in range(len(cards)):
            print(cards[card])
            for board in boards:
                list_to_add_to = boards[board][card]
                print(list_to_add_to)


name = input("please enter the project's name (and make sure the file has the same name)")
extension = input("Enter the file extension you'd like to use (default: csv)")
separator = input("Please enter the csv separator (default: ,)")
if not extension:
    extension = "csv"
if not separator:
    separator = ","
project = Trello(name, extension, separator)
# project.add_board_from_csv(project.file)
project.add_list_from_csv(project.file)
