
import os

def parse_directory(directory):
    try:
        # Получаем список всех файлов и папок в указанной директории
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)  # Полный путь к элементу
            if os.path.isdir(item_path):
                print(f'Папка: {item_path}')  # Если это папка
                parse_directory(item_path)  # Рекурсивно парсим вложенные папки
            else:
                print(f'Файл: {item_path}')  # Если это файл
    except PermissionError:
        print(f'Нет доступа к {directory}')  # Обработка ошибки доступа

if __name__ == "__main__":
    disk_c = "E:"
    print(f'Парсинг диска {disk_c}...')
    parse_directory(disk_c)
