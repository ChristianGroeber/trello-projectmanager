import os

import auth
import csv_reader
import models


class Trello:
    def __init__(self, file):
        self.project_name = file.split(".")[-2]
        self.file = file
        self.client = auth.authorize()
        self.project = models.TrelloProject(self.project_name, self.client)

    def add_boards_from_csv(self, file):
        head = csv_reader.read(file)[0]
        print(head)
        for board in head[0].split(";"):
            if str(board) is not "NR" and "id" not in str(board):
                self.project.add_board(board)


Trello(os.path.join("csv", "smartGarantie.CSV")).add_boards_from_csv(os.path.join("csv", "smartGarantie.CSV"))

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
