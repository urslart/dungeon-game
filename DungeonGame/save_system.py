import json

def save_game(player):
    data = {"health": player.health, "x": player.rect.x, "y": player.rect.y}
    with open("save.json", "w") as f:
        json.dump(data, f)

def load_game():
    try:
        with open("save.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
