import pytest
import io

from user_functions import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

def test_user_name_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('AfraMuhammad'))
    assert get_user_name_from_input() == 'AfraMuhammad'


def test_user_name_with_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Afra Muhammad'))
    result = get_user_name_from_input()
    assert ' ' not in result and len(result) > 0, "User name cannot have spaces."


def test_user_name_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(''))
    result = get_user_name_from_input()
    assert result != '', "User name cannot be empty."


def test_password_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Valid@123'))
    assert get_password_from_input() == 'Valid@123'


def test_password_too_short(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Short1@'))
    result = get_password_from_input()
    assert len(result) >= 8, "Password must be at least 8 characters long."


def test_password_no_special_character(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Password1'))
    result = get_password_from_input()
    assert any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for char in result), "Password must contain at least one special character."


def test_password_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Password@'))
    result = get_password_from_input()
    assert any(char.isdigit() for char in result), "Password must contain at least one number."


def test_password_no_letter(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12345678@'))
    result = get_password_from_input()
    assert any(char.isalpha() for char in result), "Password must contain at least one letter."
