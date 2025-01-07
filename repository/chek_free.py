import json
from datetime import datetime


def examination(user_id):
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Файл пустой или отсутствует.")
        return False

    for record in data:
        if record.get("user_id") == user_id:
            return True

    return False


def add_record(json_file, user_id, date=None):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if date is None:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data.append({"user_id": user_id, "date": date})

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Запись добавлена: {{'user_id': {user_id}, 'date': {date}}}")
if __name__ == "__main__":
    print(examination(1234))
