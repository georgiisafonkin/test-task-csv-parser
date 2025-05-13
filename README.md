# test-task-scv-parser
Тестовое задание для Workmate


## Описание

Этот проект представляет собой скрипт для парсинга CSV-файлов с данными сотрудников. Он автоматически сопоставляет заголовки входного файла с внутренними именами полей, используя предопределённые алиасы. Это позволяет гибко обрабатывать данные, независимо от формата или формулировок заголовков в CSV.

## Основные возможности

- ✅ Поддержка алиасов для заголовков (например, `emp_id`, `id` → `employee_id`)
- ✅ Преобразование строковых значений в числовые (`hourly_rate`, `hours_worked`)
- ✅ Обработка и валидация заголовков
- ✅ Объектно-ориентированная архитектура
- ✅ Простота расширения: легко добавить новые поля и логику обработки

## Выполненные задачи

- ✅ Основная задача реализована: корректный парсинг CSV с учетом синонимов заголовков
- ✅ Дополнительные задачи также выполнены: использование аннотаций, сообщения об ошибках, --help/-h
- ✅ Покрытие тестами: **85%** (юнит-тесты для ключевых компонентов)

## Технологии и подходы

- **Python 3.7+**
- **ООП-подход**: код структурирован в виде классов, что облегчает расширение и сопровождение
- **Аннотации типов** для улучшения читаемости и удобства разработки
- **Модульное тестирование** с покрытием ключевой бизнес-логики

## Структура проекта
```
src
├── formatters
│   ├── formatter.py
│   └── json_formatter.py
├── main.py
├── models
│   ├── department.py
│   ├── employee.py
│   └── record.py
├── parser
│   └── csv_parser.py
├── reports
│   ├── payout.py
│   └── report.py
├── tests
│   ├── test_department.py
│   ├── test_employee.py
│   ├── test_formatter_json.py
│   ├── test_payout_report.py
│   └── test_report_factory.py
└── utils
    ├── builders.py
    └── report_factory.py
```
## Что ещё можно добавить?

- Логирование
- Оформленный вывод отчётов в командную строку


## Пример работы

```bash
python main.py ../data3.csv ../data2.csv ../data1.csv --report payout
{
    "report_type": "payout",
    "departments": [
        {
            "department": "Sales",
            "total_payout": 14170.0,
            "employees": [
                {
                    "id": "201",
                    "name": "Karen White",
                    "email": "karen@example.com",
                    "hours_worked": 165.0,
                    "payout": 8250.0
                },
                {
                    "id": "203",
                    "name": "Mia Young",
                    "email": "mia@example.com",
                    "hours_worked": 160.0,
                    "payout": 5920.0
                }
            ]
        },
        {
            "department": "HR",
            "total_payout": 19714.0,
            "employees": [
                {
                    "id": "202",
                    "name": "Liam Harris",
                    "email": "liam@example.com",
                    "hours_worked": 155.0,
                    "payout": 6510.0
                },
                {
                    "id": "101",
                    "name": "Grace Lee",
                    "email": "grace@example.com",
                    "hours_worked": 160.0,
                    "payout": 7200.0
                },
                {
                    "id": "103",
                    "name": "Ivy Clark",
                    "email": "ivy@example.com",
                    "hours_worked": 158.0,
                    "payout": 6004.0
                }
            ]
        },
        {
            "department": "Marketing",
            "total_payout": 13250.0,
            "employees": [
                {
                    "id": "102",
                    "name": "Henry Martin",
                    "email": "henry@example.com",
                    "hours_worked": 150.0,
                    "payout": 5250.0
                },
                {
                    "id": "1",
                    "name": "Alice Johnson",
                    "email": "alice@example.com",
                    "hours_worked": 160.0,
                    "payout": 8000.0
                }
            ]
        },
        {
            "department": "Design",
            "total_payout": 16200.0,
            "employees": [
                {
                    "id": "2",
                    "name": "Bob Smith",
                    "email": "bob@example.com",
                    "hours_worked": 150.0,
                    "payout": 6000.0
                },
                {
                    "id": "3",
                    "name": "Carol Williams",
                    "email": "carol@example.com",
                    "hours_worked": 170.0,
                    "payout": 10200.0
                }
            ]
        }
    ]
}
```