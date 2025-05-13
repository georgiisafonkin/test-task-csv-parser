import argparse

cmd_line_parser = argparse.ArgumentParser(
    description=(
        "Генерация отчётов о сотрудниках по заданным CSV-файлам.\n"
        "Использование: python main.py <файл1.csv> <файл2.csv> ... --report <тип_отчёта>"
    )
)
