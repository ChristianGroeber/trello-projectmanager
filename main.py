from trello import ResourceUnavailable

import auth
import csv_reader
import models
import os


class Trello:
    def __init__(self, file):
        self.project_name = file.split(".")[-2]
        self.client = auth.authorize()
        self.project = models.TrelloProject(self.project_name, self.client)


    my_board = models.Board("smartGarantie", client)

    lines = csv_reader.read()
    for line in lines:
        category = line[2]
        print(category)
        if not my_board.check_if_list_is_in_board(category):
            print("adding " + category + " to trello")
            my_board.add_list(category)

    for card in lines:
        if not my_board.check_if_card_in_list(card[1], card[2]):
            my_board.get_list(card[2]).add_card(name=card[1])
