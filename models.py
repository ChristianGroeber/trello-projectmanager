class TrelloProject:
    def __init__(self, name, client):
        self.name = name
        self.client = client
        self.boards = self.download_boards(boards={"nothing": None})

    def get_board(self, board_name):
        """
        Gets a board by it's name
        :param board_name:
        :return: Board
        """
        for board in self.boards:
            if board_name in board:
                return board

    def get_board_from_simple_name(self, simple_name):
        ret = self.get_board(simple_name)
        print(ret)
        return ret

    def download_boards(self, boards=None):
        """
        Gets all boards that belong to a Trello Project
        :return: dictionary with board objects
        """
        if not boards:
            boards = self.boards
        ret = boards
        for board in self.client.list_boards():
            if self.name in board.name:
                ret[board.id] = Board(board.name, self.get_simple_name_for_board(board.name), board.id, board)
        return ret

    def find_project(self):
        boards = self.client.list_boards()
        for board in boards:
            if self.name in str(board.name):
                return board

    def board_in_project(self, board_name):
        for board in self.client.list_boards():
            if str(board.name) == board_name:
                return True
        return False

    def add_board(self, board_name, simple_name):
        new_board = self.client.add_board(board_name, simple_name)
        self.boards[new_board.id] = Board(board_name, self.get_simple_name_for_board(board_name), new_board.id, new_board)

    def get_simple_name_for_board(self, board_name):
        """
        Gets the simple name (corresponding column in the table) for a board
        :param board_name: <project_name> - <column_name>
        :return: boolean
        """
        arr_board = board_name.split()
        print(arr_board)
        if str(arr_board[0]) == self.name:
            arr_board.pop(0)
            arr_board.pop(0)
            arr_board = ''.join(arr_board)
            return arr_board
        else:
            return KeyError


class Board:
    def __init__(self, board_name, simple_name, id, trello_board):
        self.id = id
        self.board_name = board_name
        self.simple_name = simple_name  # the corresponding column in the table
        self.trello_board = trello_board
        self.trello_lists = trello_board.open_lists()
        self.lists = self.download_lists()

    def get_simple_name(self):
        arr_board = self.board_name.split()
        arr_board.pop(0)
        arr_board.pop(0)
        return ''.join(arr_board)

    def download_lists(self):
        ret = {}
        for list in self.trello_board.open_lists():
            ret[list.id] = List(name=list.name, id=list.id, trello_list=list)
        return ret

    def get_board(self):
        return self.trello_board

    def get_lists(self):
        return self.lists

    def print_lists(self):
        for list in self.get_lists():
            # print(list)
            pass

    def check_if_list_is_in_board(self, list_name):
        for list in self.trello_lists:
            if str(list.name) == str(list_name):
                return True
        return False

    def get_list(self, list_name):
        for list in self.trello_lists:
            if list.name == list_name:
                return list

    def check_if_card_in_list(self, card_text, list):
        try:
            for card in self.get_list(list).list_cards():
                if card.name == card_text:
                    return True
            return False
        except AttributeError:
            print("Attribute Error")
            return False

    def add_list(self, list_name):
        new_list = self.get_board().add_list(name=list_name)
        self.trello_lists = self.get_board().open_lists()
        self.lists[new_list.id] = List(list_name, new_list.id, trello_list=new_list)

    def add_list_from_dict(self, lists):
        for my_list in lists:
            self.add_list(lists[my_list])

    def delete_all_lists(self):
        for list in self.trello_lists:
            print("deleting" + list.name)
            list.close()


class List:
    def __init__(self, name, id, trello_list):
        self.name = name
        self.id = id
        self.trello_list = trello_list
        self.cards = self.download_cards(cards={'nothing': None})

    def __str__(self):
        print(self.name)

    def download_cards(self, cards=None):
        if not cards:
            cards = self.cards
        ret = cards
        for card in self.trello_list.list_cards():
            ret[card.id] = Card(card.name, card.id, card, description=card.description)
        return ret

    def add_card(self, card_name):
        new_card = self.trello_list.add_card(name=card_name)
        self.cards[new_card.id] = Card(card_name, new_card.id, new_card, description=new_card.description)

    def save(self):
        self.trello_list.close_all_cards()
        for card in self.cards:
            if card.trello_card in self.trello_list.closed_cards():
                card.trello_card.open()
            else:
                self.add_card(card.name)


class Card:
    def __init__(self, name, id, trello_card, description=None):
        self.trello_card = trello_card
        self.id = id
        self.name = name
        self.description = description
