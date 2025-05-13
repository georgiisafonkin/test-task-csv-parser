from reports.report import Report

class PayoutReport(Report):
    def generate(self):
        return {
            "report_type": "payout",
            "total_payout": round(sum(r.payout for r in self.records), 2),
            "employees": [
                {
                    "id": r.employee_id,
                    "name": r.name,
                    "payout": round(r.payout, 2)
                }
                for r in self.records
            ]
        }
