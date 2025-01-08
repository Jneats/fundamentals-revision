from oop.staff import Staff, FireNotApproved
import pytest

# 1. Build a test for `increase_salary` that checks what happens when value passed is `'four_pounds'` rather than `4`.

def test_increase_salary_passed_string():
    test_staff = Staff('Apple', 'Worker', "Department")
    with pytest.raises(Exception):
        test_staff.increase_salary('four_pounds')
    assert test_staff.salary == 26000

# 2. Build a test that utilises a custom Exception for the `fire` method, when the `hr_report = {"approved": False}`.

def test_fire_exception():
    test_staff = Staff('Apple', 'Worker', "Department")
    with pytest.raises(FireNotApproved):
        test_staff.fire({"approved": False})
