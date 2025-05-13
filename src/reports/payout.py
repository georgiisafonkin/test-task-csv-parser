from reports.report import Report
from models.department import Department
from models.employee import Employee
from typing import List, Dict

class PayoutReport(Report):
    def __init__(self, records):
        super().__init__(records)
        self._report_type = "payout"
        self.departments: List[Department]        

    def generate(self):
        
        # for r in self.records:
        #     department_name = r.department
        
        report_data: Dict = {
            "report_type" : self._report_type,
            "departments" : {}
        }

        # return {
        #     "report_type": "payout",
        #     "total_payout": round(sum(r.payout for r in self.records), 2),
        #     "employees": [
        #         {
        #             "id": r.employee_id,
        #             "name": r.name,
        #             "payout": round(r.payout, 2)
        #         }
        #         for r in self.records
        #     ]
        # }
