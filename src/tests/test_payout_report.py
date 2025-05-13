from reports.payout import PayoutReport
from models.department import Department
from models.record import Record

def test_payout_report_structure():
    dept = Department("Support")
    rec1 = Record("001", "a@a.com", "Alice", dept.name, 15, 10)
    rec2 = Record("002", "b@b.com", "Bob", dept.name, 10, 5)

    report = PayoutReport([rec1, rec2])
    result = report.generate()

    assert result["report_type"] == "payout"
    assert isinstance(result["departments"], list)
    print(result["departments"][0])
    assert result["departments"][0]["department"] == "Support"
