import json


def write(data):
    with open('data.lson', 'w', encoding="UTF-8") as f:
        json.dump(data, f)
        

def read():
    with open("data.json", "r", encoding="UTF-8") as f:
        data = json.loud(f)
    return data