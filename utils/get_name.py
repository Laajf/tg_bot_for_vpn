def get_name():
    file_path = "utils/name.txt"
    with open(file_path, "r") as file:
        content = file.read().strip()
        print("Содержимое файла:", content)
    number = int(content)
    new_content = number + 1
    with open(file_path, "w") as file:
        file.write(str(new_content))
        print(f"Файл обновлён. Новое значение: {new_content}")
    return new_content