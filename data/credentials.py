import os
from dotenv import load_dotenv  # импорт метода для подгрузки переменных из файла .env

load_dotenv()  # Вызов метода сразу после всех импортов


class Credentials:
    EXISTING_LOGIN = os.getenv("EXISTING_LOGIN")
    EXISTING_PASSWORD = os.getenv("EXISTING_PASSWORD")
    NON_EXISTING_LOGIN = os.getenv("NON-EXISTING_LOGIN")
    NON_EXISTING_PASSWORD = os.getenv("NON-EXISTING_PASSWORD")
