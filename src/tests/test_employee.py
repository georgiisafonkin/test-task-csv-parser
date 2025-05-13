from models.employee import Employee
from models.department import Department

def test_employee_payout_calculation():
    dept = Department("Engineering")
    emp = Employee("001", "john@example.com", "John", dept, 50.0, 10.0)
    assert emp.payout == 500.0
