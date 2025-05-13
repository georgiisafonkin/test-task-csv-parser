from typing import List
from models.employee import Employee

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []
        self._total_payout: float = 0.0

    def add_employee(self, employee: 'Employee') -> None:
        self.employees.append(employee)
        self._total_payout += employee.payout

    @property
    def total_payout(self) -> float:
        return self._total_payout
    
    def to_dict(self) -> dict:
        return {
            "department": self.name,
            "total_payout": round(self.total_payout, 2),
            "employees": [emp.to_dict() for emp in self.employees]
        }