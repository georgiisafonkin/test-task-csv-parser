import argparse

cmd_line_parser = argparse.ArgumentParser(
    description=(
        "Генерация отчётов о сотрудниках по заданным CSV-файлам.\n"
    )
)

cmd_line_parser.add_argument("files", nargs="+", help=".csv файлы для генерации отчёта")
cmd_line_parser.add_argument("--report", required=True, help="Тип отчёта (например, payout)")

args = cmd_line_parser.parse_args()

print(args)