from reports.report import Report
from models.department import Department
from models.employee import Employee
from typing import List, Dict
from utils.builders import build_departments

class PayoutReport(Report):
    def __init__(self, records):
        super().__init__(records)
        self._report_type = "payout"
        self.departments: List[Department]        

    def generate(self) -> dict:
        departments = build_departments(self.records)

        return {
            "report_type": "payout",
            "departments": [dept.to_dict() for dept in departments.values()]
        }
