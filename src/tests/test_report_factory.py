from utils.report_factory import ReportFactory
from reports.payout import PayoutReport
import pytest

def test_get_known_report():
    report_cls = ReportFactory.get_report("payout")
    assert report_cls is PayoutReport

def test_unknown_report_raises():
    with pytest.raises(ValueError, match="Неизвестный тип отчёта"):
        ReportFactory.get_report("unknown")
