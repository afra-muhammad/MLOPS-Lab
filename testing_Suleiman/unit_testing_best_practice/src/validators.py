import re

def validate_username(username):
    """
    Validate the username.
    Criteria:
    - Not empty
    - No spaces
    """
    if not username:
        return False, "Username cannot be empty."
    if " " in username:
        return False, "Username cannot contain spaces."
    return True, "Username is valid."

def validate_password(password):
    """
    Validate the password.
    Criteria:
    - At least 8 characters
    - At least one number
    - At least one letter
    - At least one special character
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Za-z]", password):
        return False, "Password must contain at least one letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Password is valid."

def validate_email(email):
    """
    Validate the email.
    Criteria:
    - Contains @ and .
    """
    if "@" not in email or "." not in email:
        return False, "Email must contain '@' and '.'."
    return True, "Email is valid."
