from employee import employee
def test_give_default_raise():
    first_employee = employee("John", "Wright", 50000)
    first_employee.give_raise()
    assert first_employee.annual_salary == 55000


def test_give_custom_raise():
    first_employee = employee("John", "Wright", 50000)
    first_employee.give_raise(10000)
    assert first_employee.annual_salary == 60000