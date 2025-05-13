from typing import List, Dict
from models.record import Record
from models.employee import Employee
from models.department import Department

def build_departments(records: List[Record]) -> Dict[str, Department]:
    departments: Dict[str, Department] = {}

    for record in records:
        if record.department not in departments:
            departments[record.department] = Department(record.department)

        department = departments[record.department]
        Employee(
            employee_id=record.employee_id,
            email=record.email,
            name=record.name,
            department=department,
            hourly_rate=record.hourly_rate,
            hours_worked=record.hours_worked
        )

    return departments
