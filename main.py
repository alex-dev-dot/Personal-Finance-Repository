from validators import validate_amount, validate_type, validate_category, validate_date, validate_date_with_future
from analytics import balance, total_by_category, get_stats, top_expenses, top_categories, search, sort_by_date, filter_by_period, monthly_report
from storage import get_data_path, load_transactions, save_transactions

def show_menu():
    print()
    print('='*25)
    print('MENU'.center(25))
    print('='*25)
    print()
    choice = input('1. Add operation\n2. All operations (by date)\n3. Balance\n4. Show stats\n5. Top expenses\n6. Top category\n7. Search\n8. Operations by period\n9. Monthly report\n10. Delete operation by <id>\n0. Exit\n\n> ')
    while choice not in ['0','1','2','3','4','5','6','7','8','9','10']:
        choice = input('Enter a correct number: ')
    return choice

def main():
    path_file = get_data_path()
    data = load_transactions(path_file)

    while True:
        choice = show_menu()
        if choice == '1':
            add_transaction(data, path_file)
        elif choice == '2':
            show_operations_by_date(data)
        elif choice == '3':
            print(f'Your balance is {round(balance(data), 2)}')
        elif choice == '4':
            show_get_stats(data)
            print()
            show_get_stats(data, 'income')
        elif choice == '5':
            show_top_expenses(data)
        elif choice == '6':
            show_top_categories(data)
            print()
            show_top_categories(data, 3, 'income')
        elif choice == '7':
            show_search(data)
        elif choice == '8':
            show_filter_by_period(data)
        elif choice == '9':
            show_monthly_report(data)
        elif choice == '10':
            delete_transaction(data, path_file)
        elif choice == '0':
            exit_function()
            break

def add_transaction(data, path_file):
    while True:
        try:
            type_add = validate_type(input('Enter a type\n> '))
            break
        except ValueError as e:
            print(f'Error: {e}')

    while True:
        try:
            amount = validate_amount(input('Enter an amount\n> '))
            break
        except ValueError as e:
            print(f'Error: {e}')

    while True:
        try:
            category = validate_category(input('Enter a category\n> '))
            break
        except ValueError as e:
            print(f'Error: {e}')

    while True:
        try:
            date = validate_date_with_future(input('Enter a date (YYYY-MM-DD)\n> '))
            break
        except ValueError as e:
            print(f'Error: {e}')

    description = input('Enter your description\n> ')
    id_data = get_max_id(data)
    if id_data is None:
        id_data = 1
    else:
        id_data += 1

    data.append({
        'id': id_data,
        'type': type_add,
        'amount': amount,
        'category': category,
        'description': description,
        'date': date
    })
    save_transactions(path_file, data)
    print('The data has been successfully updated!')

def get_max_id(data):
    if not data:
        return None
    item_with_max = max(data, key=lambda m: m.get('id', float('-inf')))
    return item_with_max.get('id')

def validate_choice(data, text):
    text = text.strip()
    try:
        result = int(text)
    except ValueError:
        raise ValueError('Enter an integer only')
    all_ids = get_all_id(data)
    if result not in all_ids:
        raise ValueError('ID not found!')
    return result

def delete_transaction(data, path_file):
    if not data:
        print('There is no transactions to delete!')
        return
    show_operations_by_date(data)
    while True:
        try:
            user_input = input(f' Enter an id of operation that you want to delete.'
                               f'\n There are {len(data)} items.\n> ')
            choice = validate_choice(data, user_input)
            deleting_transaction(data, choice)
            break
        except ValueError as e:
            print(f'Error: {e}')
    save_transactions(path_file, data)
    print(f'Transaction with ID {choice} deleted.')

def deleting_transaction(data, choice):
    len_data = len(data)
    data[:] = [t for t in data if t['id'] != choice]
    if len(data) == len_data:
        raise ValueError('ID not found!')
    return data

def get_all_id(data):
    result = []
    if not data:
        return result
    return [d['id'] for d in data]

def print_transaction(el):
    return f'[*] ID: {el["id"]}\n    Type: {el["type"]}  || Amount: {el["amount"]}  ||  Category: {el["category"]}\n    Description: {el["description"]}\n    Date: {el["date"]}'

def show_operations_by_date(data):
    sorted_data = sort_by_date(data)
    if sorted_data == []:
        print('No operations to show!')
        return
    for el in sorted_data:
        print(print_transaction(el))
    return

def show_get_stats(data, kind='expense'):
    result = get_stats(data, kind)
    if result == (0.0, 0.0, 0.0):
        print('There is no transactions to take action.')
        return
    less, greater, average = result
    print(f'[*] Kind ==> {kind}\n    Min element: {less}\n    Max element: {greater}\n    Average value: {average}')
    return

def show_top_expenses(data):
    result = top_expenses(data)
    if result == []:
        print('There is no transactions to take action.')
        return
    for el in result:
        print(print_transaction(el))
    return

def show_top_categories(data, n=3, kind='expense'):
    result = top_categories(data, n, kind)
    if result == []:
        print('There is no transactions to take action.')
        return
    for first, second in result:
        print(f'[*] Category: {first}\n    Amount: {second}')
    return

def show_search(data):
    if not data:
        print('There is no transactions to take action.')
        return
    keyword = input('Enter your keyword: ')
    result = search(data, keyword)
    if result == []:
        print(f'"{keyword}" not found.')
        return
    for el in result:
        print(print_transaction(el))
    return

def show_filter_by_period(data):
    if not data:
        print('There is no transactions to take action.')
        return
    result = operations_by_period(data)
    for el in result:
        print(print_transaction(el))
    return

def operations_by_period(data):
    while True:
        try:
            date_1 = validate_date(input('Enter the date #1\n> '))
            break
        except ValueError as e:
            print(f'Error: {e}')

    while True:
        try:
            date_2 = validate_date(input('Enter the date #2\n> '))
            break
        except ValueError as e:
            print(f'Error: {e}')

    if date_1 > date_2:
        print('Warning: Start date is later than end date. Swapping dates automatically.')
        date_1, date_2 = date_2, date_1

    result = filter_by_period(data, date_1, date_2)
    if result == []:
        print(f'The period {date_1} - {date_2}\nNothing was found.')
        return []
    return result

def show_monthly_report(data):
    result = monthly_report(data)
    if result == {}:
        print('There is no transactions to take action.')
        return
    for key, value in result.items():
        print(f'Month: {key} || Income: {value.get('income')} || Expense: {value.get('expense')}')
    return

def exit_function():
    print()
    print('='*25)
    print('Have a nice day!'.center(25))
    print('='*25)

if __name__ == '__main__':
    main()