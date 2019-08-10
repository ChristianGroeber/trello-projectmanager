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

    def add_board_from_csv(self, file):
        head = csv_reader.read(file)[0]
        for board in head[0].split(self.separator):
            full_board = self.name + " - " + board
            if "NR" not in str(board) and "id" not in str(board):
                self.project.add_board(full_board, board)


name = input("please enter the project's name (and make sure the file has the same name)")
extension = input("Enter the file extension you'd like to use (default: csv)")
separator = input("Please enter the csv separator (default: ,)")
if not extension:
    extension = "csv"
if not separator:
    separator = ","
project = Trello(name, extension, separator)
# project.add_board_from_csv(project.file)


# lines = csv_reader.read()
# for line in lines:
#     category = line[2]
#     print(category)
#     if not my_board.check_if_list_is_in_board(category):
#         print("adding " + category + " to trello")
#         my_board.add_list(category)
#
# for card in lines:
#     if not my_board.check_if_card_in_list(card[1], card[2]):
#         my_board.get_list(card[2]).add_card(name=card[1])
