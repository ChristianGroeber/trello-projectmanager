import json

from trello import TrelloClient


def authorize():
    with open("keys.json", "r") as f:
        keys = json.load(f)

    print(keys)

    client = TrelloClient(
        api_key=keys["api-key"],
        api_secret=keys["api-secret"],
    )

    return client
