from datetime import datetime

def validate_amount(text):
    try:
        result = float(text)
    except ValueError:
        raise ValueError('Enter a number only!')
    if result <= 0:
        raise ValueError('Enter only positive number!')
    return result

def validate_type(text):
    text = text.strip().lower()
    if text in ['income', 'expense']:
        return text
    else:
        raise ValueError('Enter a correct type!')

def validate_category(text):
    if not text.strip():
        raise ValueError('Enter a correct category!')
    return text.strip().lower()

def validate_date(text):
    text = text.strip()
    current_time = datetime.now()
    if text.strip() == '':
        return current_time.strftime('%Y-%m-%d')
    try:
        date = datetime.strptime(text, '%Y-%m-%d')
    except ValueError:
        raise ValueError('The date should be in the format "YYYY-MM-DD"!')
    return date.strftime('%Y-%m-%d')

def validate_date_with_future(text):
    formatted_date = validate_date(text)
    current_time = datetime.now()
    date = datetime.strptime(formatted_date, '%Y-%m-%d')

    if date > current_time:
        raise ValueError('The date cannot be in the future!')
    return formatted_date