from dataclasses import dataclass

@dataclass
class Record:
    employee_id: str
    name: str
    department: str
    hourly_rate: float
    hours_worked: float

    @property
    def payout(self) -> float:
        return self.hourly_rate * self.hours_worked
