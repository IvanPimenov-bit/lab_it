from pathlib import Path
import json
import logging
from utils.statistics import calculate_average, find_min, find_max, validate_numbers
from utils.reader import read_numbers
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def main():
    logging.info("Программа запущена")
    print("Текущий каталог:", Path.cwd())
    data_file = Path(config["input_file"])
    if data_file.exists():
        print(f"Файл {data_file} найден")
    else:
        print(f"Файл {data_file} не найден")
    try:
        numbers = read_numbers(data_file)
        logging.info(f"Файл {data_file} успешно прочитан")
        logging.info(f"Прочитано значений: {len(numbers)}")
        validate_numbers(numbers)
        print("Количество значений:", len(numbers))
        print("Среднее арифметическое:", calculate_average(numbers))
        print("Минимальное число:", find_min(numbers))
        print("Максимальное число:", find_max(numbers))
        logging.info("Вычисления выполнены успешно")
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        logging.error("Файл не найден")
    except ValueError as e:
        print("Ошибка данных:", e)
        logging.error(f"Ошибка данных: {e}")
    logging.info("Программа завершена")
if __name__ == "__main__":
    main()