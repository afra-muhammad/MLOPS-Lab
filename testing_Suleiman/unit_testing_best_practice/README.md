

# **User Input Validation**

This task provides Python functions to validate **username**, **password**, and **email** inputs based on specified criteria. Automated tests using `pytest` ensure the functions work as expected.

---

## **Validation Criteria**

- **Username**:
  - Must not be empty.
  - Must not contain spaces.
- **Password**:
  - At least 8 characters.
  - At least one letter, one number, and one special character.
- **Email**:
  - Must contain `@` and `.`.

---

## **How to Use**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/afra-muhammad/MLOPS-Lab.git
   cd MLOPS-Lab/unit_testing_simple_Suleiman
   ```

2. **Run the Validation Functions**:
   ```python
   from validators import validate_username, validate_password, validate_email
   print(validate_username("john_doe"))
   print(validate_password("Pass@123"))
   print(validate_email("user@example.com"))
   ```

3. **Run Tests**:
   ```bash
   pytest
   ```

---

## **Example Outputs**

- **Valid Input**:
  - `validate_username("john_doe")` → `(True, "Username is valid.")`
  - `validate_password("Pass@123")` → `(True, "Password is valid.")`
  - `validate_email("user@example.com")` → `(True, "Email is valid.")`

- **Invalid Input**:
  - `validate_username("")` → `(False, "Username cannot be empty.")`
  - `validate_password("short")` → `(False, "Password must be at least 8 characters long.")`
  - `validate_email("userexample.com")` → `(False, "Email must contain '@' and '.'.")`

---

## **Dependencies**
- Python 3.x
- `pytest` (install via `pip install pytest`).

---

## **Testing**
Run all tests with:
```bash
pytest
```