from dataclasses import dataclass

@dataclass
class Record:
    employee_id: str
    email: str
    name: str
    department: str
    hourly_rate: float
    hours_worked: float

