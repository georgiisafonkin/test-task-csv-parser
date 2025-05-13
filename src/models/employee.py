from models.department import Department

class Employee:
    def __init__(self, employee_id: str, email: str, name: str, department: Department, hourly_rate: float, hours_worked: float) -> None:
        self.employee_id = employee_id
        self.email = email
        self.name = name
        self.department = department
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

        department.add_employee(self)

    @property
    def payout(self) -> float:
        return self.hourly_rate * self.hours_worked
    
    def to_dict(self) -> dict:
        return {
            "id": self.employee_id,
            "name": self.name,
            "email": self.email,
            "hours_worked": self.hours_worked,
            "payout": round(self.payout, 2)
        }