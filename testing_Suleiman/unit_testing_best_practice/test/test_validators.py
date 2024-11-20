import sys
sys.path += [('testing_Suleiman/unit_testing_best_practice/src')]
from validators import validate_username, validate_password, validate_email

def test_validate_username():
    assert validate_username("john_doe") == (True, "Username is valid.")
    assert validate_username("") == (False, "Username cannot be empty.")
    assert validate_username("john doe") == (False, "Username cannot contain spaces.")

def test_validate_password():
    assert validate_password("Pass@123") == (True, "Password is valid.")
    assert validate_password("short") == (False, "Password must be at least 8 characters long.")
    assert validate_password("NoNumber!") == (False, "Password must contain at least one number.")
    assert validate_password("12345678") == (False, "Password must contain at least one letter.")
    assert validate_password("Password1") == (False, "Password must contain at least one special character.")

def test_validate_email():
    assert validate_email("user@example.com") == (True, "Email is valid.")
    assert validate_email("userexample.com") == (False, "Email must contain '@' and '.'.")
    assert validate_email("user@examplecom") == (False, "Email must contain '@' and '.'.")
