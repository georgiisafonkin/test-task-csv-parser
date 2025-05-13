from reports.payout import PayoutReport
from models.department import Department
from models.employee import Employee

def test_payout_report_structure():
    dept = Department("Support")
    emp1 = Employee("001", "a@a.com", "Alice", dept, 15, 10)
    emp2 = Employee("002", "b@b.com", "Bob", dept, 10, 5)

    report = PayoutReport([emp1, emp2])
    result = report.generate()

    assert result["report_type"] == "payout"
    assert isinstance(result["departments"], list)
    assert result["departments"][0]["department"] == "Support"
