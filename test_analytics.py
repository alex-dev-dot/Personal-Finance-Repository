import pytest
from analytics import balance, total_by_category, get_stats, top_expenses, top_categories, search, sort_by_date, filter_by_period, monthly_report

DATA = [
    {"id": 1, "type": "income",  "amount": 50000.0, "category": "зарплата",    "description": "зарплата за октябрь", "date": "2026-10-01"},
    {"id": 2, "type": "expense", "amount": 1200.0,  "category": "еда",         "description": "продукты",            "date": "2026-10-03"},
    {"id": 3, "type": "expense", "amount": 800.0,   "category": "транспорт",   "description": "метро на месяц",      "date": "2026-10-02"},
    {"id": 4, "type": "expense", "amount": 1200.0,  "category": "еда",         "description": "кафе с друзьями",     "date": "2026-10-05"},
    {"id": 5, "type": "expense", "amount": 15000.0, "category": "жильё",       "description": "аренда комнаты",      "date": "2026-10-01"},
    {"id": 6, "type": "expense", "amount": 3000.0,  "category": "развлечения", "description": "кино и боулинг",      "date": "2026-09-28"},
    {"id": 7, "type": "income",  "amount": 5000.0,  "category": "подработка",  "description": "фриланс",             "date": "2026-09-30"},
]

def test_correct_balance():
    assert balance(DATA) == 33800.0

def test_empty_balance():
    assert balance([]) == 0

def test_correct_total_by_category_expense():
    assert total_by_category(DATA) == {'еда': 2400.0, 'транспорт': 800.0, 'жильё': 15000.0, 'развлечения': 3000.0}

def test_correct_total_by_category_income():
    assert total_by_category(DATA, 'income') == {'зарплата': 50000.0, 'подработка': 5000.0}

def test_empty_total_by_category():
    assert total_by_category([]) == {}

def test_correct_get_stats_expense():
    assert get_stats(DATA) == (800.0, 15000.0, 4240.0)

def test_correct_get_stats_income():
    assert get_stats(DATA, 'income') == (5000.0, 50000.0, 27500.0)

def test_empty_get_stats():
    assert get_stats([]) == (0.0, 0.0, 0.0)

def test_incorrect_type():
    assert get_stats(DATA, 'other') == (0.0, 0.0, 0.0)

def test_correct_top_expenses():
    assert top_expenses(DATA) == [{'id': 5, 'type': 'expense', 'amount': 15000.0, 'category': 'жильё', 'description': 'аренда комнаты', 'date': '2026-10-01'},
                                  {'id': 6, 'type': 'expense', 'amount': 3000.0, 'category': 'развлечения', 'description': 'кино и боулинг', 'date': '2026-09-28'},
                                  {'id': 2, 'type': 'expense', 'amount': 1200.0, 'category': 'еда', 'description': 'продукты', 'date': '2026-10-03'}]

def test_empty_top_expenses():
    assert top_expenses([]) == []

def test_top_categories_expense():
    assert top_categories(DATA) == [('жильё', 15000.0), ('развлечения', 3000.0), ('еда', 2400.0)]

def test_top_categories_income():
    assert top_categories(DATA, 3, 'income') == [('зарплата', 50000.0), ('подработка', 5000.0)]

def test_empty_top_categories():
    assert top_categories([]) == []

def test_correct_search():
    assert search(DATA, 'Каф') == [{'id': 4, 'type': 'expense', 'amount': 1200.0, 'category': 'еда', 'description': 'кафе с друзьями', 'date': '2026-10-05'}]

def test_not_found_search():
    assert search(DATA, 'asd') == []

def test_empty_search():
    assert search([], 'Каф') == []

def test_sort_by_date():
    assert sort_by_date(DATA) == [{'id': 4, 'type': 'expense', 'amount': 1200.0, 'category': 'еда', 'description': 'кафе с друзьями', 'date': '2026-10-05'},
                                  {'id': 2, 'type': 'expense', 'amount': 1200.0, 'category': 'еда', 'description': 'продукты', 'date': '2026-10-03'},
                                  {'id': 3, 'type': 'expense', 'amount': 800.0, 'category': 'транспорт', 'description': 'метро на месяц', 'date': '2026-10-02'},
                                  {'id': 1, 'type': 'income', 'amount': 50000.0, 'category': 'зарплата', 'description': 'зарплата за октябрь', 'date': '2026-10-01'},
                                  {'id': 5, 'type': 'expense', 'amount': 15000.0, 'category': 'жильё', 'description': 'аренда комнаты', 'date': '2026-10-01'},
                                  {'id': 7, 'type': 'income', 'amount': 5000.0, 'category': 'подработка', 'description': 'фриланс', 'date': '2026-09-30'},
                                  {'id': 6, 'type': 'expense', 'amount': 3000.0, 'category': 'развлечения', 'description': 'кино и боулинг', 'date': '2026-09-28'}
                                  ]

def test_empty_sort_by_date():
    assert sort_by_date([]) == []

def test_filter_by_period():
    assert filter_by_period(DATA, '2026-10-01', '2026-10-02') == [
                                {'id': 1, 'type': 'income', 'amount': 50000.0, 'category': 'зарплата', 'description': 'зарплата за октябрь', 'date': '2026-10-01'},
                                {'id': 3, 'type': 'expense', 'amount': 800.0, 'category': 'транспорт', 'description': 'метро на месяц', 'date': '2026-10-02'},
                                {'id': 5, 'type': 'expense', 'amount': 15000.0, 'category': 'жильё', 'description': 'аренда комнаты', 'date': '2026-10-01'}]

def test_empty_filter_by_period():
    assert filter_by_period([], "2026-10-01", "2026-10-02") == []

def test_monthly_report():
    assert monthly_report(DATA) == {'2026-10': {'income': 50000.0, 'expense': 18200.0},
                                '2026-09': {'income': 5000.0, 'expense': 3000.0}}

def test_empty_monthly_report():
    assert monthly_report([]) == {}