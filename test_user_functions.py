import io
import pytest
from user_functions import *

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

# Check for incorrect email format
def test_email_with_user_input_regex_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input_regex() is None

# Check for incorrect email format
def test_email_with_user_input_regex_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('yoel_turner99@adaltas.com'))
    assert get_email_from_input_regex() == 'yoel_turner99@adaltas.com'