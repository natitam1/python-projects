import pytest
from employee import Employee

@pytest.fixture
def New_employee():
    """Add new employee."""
    New_employee = Employee("Natnael", "Tamiru", 2000)
    return New_employee

def test_give_default_raise(New_employee):
    """Test the class with the default value."""
    New_employee.give_raise()
    assert New_employee.annual_salary == 7000
def test_give_custom_raise(New_employee):
    """Test with custom amount"""
    New_employee.give_raise(1000)
    assert New_employee.annual_salary == 3000
    