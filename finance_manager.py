import json

class FinanceManager:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    def save_transactions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file)

    def add_transaction(self, description, amount):
        self.transactions.append({'description': description, 'amount': amount})
        self.save_transactions()

    def get_transactions(self):
        return self.transactions
    
    def calculate_balance(self):
        return sum(transaction['amount'] for transaction in self.transactions)