import argparse
from typing import List
from parser.csv_parser import CsvParser
from utils.report_factory import ReportFactory
from formatters.json_formatter import JsonFormatter
from models.record import Record

cmd_line_parser = argparse.ArgumentParser(
    description=(
        "Генерация отчётов о сотрудниках по заданным CSV-файлам.\n"
    )
)

cmd_line_parser.add_argument("files", nargs="+", help=".csv файлы для генерации отчёта")
cmd_line_parser.add_argument("--report", required=True, help="Тип отчёта (например, payout)")

args = cmd_line_parser.parse_args()

try:
    all_records: List[Record] = []
    for file in args.files:
        csv_parser = CsvParser(file)
        all_records.extend(csv_parser.parse())

    report_cls = ReportFactory.get_report(args.report)
    report = report_cls(all_records).generate() # Создал экземпляр и сразу вызвал метод generate() экземпляра класса report_cls

    output = JsonFormatter.format(report)
    print(output)

except Exception as e:
    print(f"Ошибка: {e}")