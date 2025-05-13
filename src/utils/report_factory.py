from reports.payout import PayoutReport
from reports.report import Report
from typing import Dict, Type

class ReportFactory:
    report_map: Dict[str, Type[Report]] = {
        "payout": PayoutReport,
    }

    @staticmethod
    def get_report(report_type: str) -> Type[Report]:
        if report_type not in ReportFactory.report_map:
            raise ValueError(f"Unknown report type: {report_type}")
        return ReportFactory.report_map[report_type]
