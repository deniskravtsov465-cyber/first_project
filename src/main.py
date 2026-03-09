import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из .env
    load_dotenv()
    # Получаем значение AUTHOR
    author = os.getenv('AUTHOR')
    # Если переменная не задана, подставляем значение по умолчанию
    if author is None:
        author = "Неизвестный автор"
    print(f"Автор проекта: {author}")

if __name__ == "__main__":
    print_author()
