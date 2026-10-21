import pytest
from validators import validate_amount, validate_type, validate_category, validate_date, validate_date_with_future

def test_correct_validate_amount():
    assert validate_amount('50') == 50.0

def test_incorrect_validate_amount():
    with pytest.raises(ValueError):
        validate_amount('-90')

def test_incorrect_validate_amount_by_zero():
    with pytest.raises(ValueError):
        validate_amount('0')

def test_word_in_validate_amount():
    with pytest.raises(ValueError):
        validate_amount('asd')

def test_correct_validate_type():
    assert validate_type('income') == 'income'

def test_correct_validate_type_number_two():
    assert validate_type('      InCoMe          ') == 'income'

def test_incorrect_validate_type_first():
    with pytest.raises(ValueError):
        validate_type('other')

def test_incorrect_validate_type_second():
    with pytest.raises(ValueError):
        validate_type('   ')

def test_correct_validate_category():
    assert validate_category(' FOOd           ') == 'food'

def test_incorrect_validate_category():
    with pytest.raises(ValueError):
        validate_category('               ')

def test_validate_date_correct():
    assert validate_date('2026-09-09              ') == '2026-09-09'

def test_incorrect_date_validate_date_with_future():
    with pytest.raises(ValueError):
        validate_date_with_future('2100-09-09')

def test_correct_future_time_for_period():
    assert validate_date('2100-9-9') == '2100-09-09'

def test_incorrect_format_validate_date():
    with pytest.raises(ValueError):
        validate_date('09.09.2026')

def test_correct_formatted_function():
    assert validate_date('2026-2-2') == '2026-02-02'