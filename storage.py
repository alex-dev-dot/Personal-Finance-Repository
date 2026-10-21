import json
from pathlib import Path

def get_data_path(folder='data', file_name='transactions.json'):
    path_folder = Path(__file__).resolve().parent / folder
    if not path_folder.exists():
        path_folder.mkdir(exist_ok=True)
    path_file = path_folder / file_name
    return path_file

def load_transactions(path_file):
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            return transactions
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_transactions(path_file, transaction):
    with open(path_file, 'w', encoding='utf-8') as file:
        json.dump(transaction, file, ensure_ascii=False, indent=2)