from models.department import Department
from models.employee import Employee

def test_department_total_payout_and_employees():
    dept = Department("QA")
    emp1 = Employee("001", "a@a.com", "Alice", dept, 20.0, 5)
    emp2 = Employee("002", "b@b.com", "Bob", dept, 25.0, 4)

    assert len(dept.employees) == 2
    assert round(dept.total_payout, 2) == 20*5 + 25*4
