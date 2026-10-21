import heapq

def balance(transactions):
    total = 0.0
    if not transactions:
        return total
    for transaction in transactions:
        if transaction['type'] == 'income':
            total += transaction['amount']
        else:
            total -= transaction['amount']
    return total

def total_by_category(transactions, kind='expense'):
    total = {}
    if not transactions:
        return total
    for transaction in transactions:
        if transaction['type'] == kind:
            category = transaction['category']
            total[category] = total.get(category, 0) + transaction['amount']
    return total

def get_stats(transactions, kind='expense'):
    if not transactions:
        return (0.0, 0.0, 0.0)
    if kind in ['expense', 'income']:
        elements = []
        for transaction in transactions:
            if transaction['type'] == kind:
                elements.append(transaction['amount'])
        return (min(elements), max(elements), sum(elements)/len(elements)) if elements else (0.0, 0.0, 0.0)
    return (0.0, 0.0, 0.0)

def top_expenses(transactions, n=3):
    if not transactions:
        return []
    expenses = []
    for transaction in transactions:
        if transaction['type'] == 'expense':
            expenses.append(transaction)
    expenses = heapq.nlargest(n, expenses, key=lambda t: t['amount'])
    return expenses

def top_categories(transactions, n=3, kind='expense'):
    if not transactions:
        return []
    expenses = total_by_category(transactions, kind)

    total = sorted(expenses.items(), reverse=True, key=lambda t: t[1])
    return total[:n]

def search(transactions, keyword):
    if not transactions:
        return []
    result = []
    for t in transactions:
        if keyword.lower() in t['category'] or keyword.lower() in t['description'].lower():
            result.append(t)
    return result

def merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if not reverse:
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if key(left[i]) >= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(items, key=lambda x: x, reverse=False):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid], key, reverse)
    right = merge_sort(items[mid:], key, reverse)
    return merge(left, right, key, reverse)

def sort_by_date(transactions):
    if not transactions:
        return []
    sorted_transactions = merge_sort(transactions, key=lambda t: t['date'], reverse=True)
    return [t for t in sorted_transactions]

def filter_by_period(transactions, start, end):
    if not transactions:
        return []
    result = []
    for transaction in transactions:
        if start <= transaction['date'] <= end:
            result.append(transaction)
    return result

def monthly_report(transactions):
    result = {}
    if not transactions:
        return result
    for t in transactions:
        if t['date'][:7] not in result:
            result[t['date'][:7]] = {'income': 0.0, 'expense': 0.0}
        if t['type'] == 'expense':
            result[t['date'][:7]]['expense'] += t['amount']
        if t['type'] == 'income':
            result[t['date'][:7]]['income'] += t['amount']
    return result