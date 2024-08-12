import json

class CryptoManager:
    def __init__(self, filename):
        self.filename = filename
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    def save_portfolio(self):
        with open(self.filename, 'w') as file:
            json.dump(self.portfolio, file)

    def add_crypto(self, name, quantity, price):
        self.portfolio.append({'name': name, 'quantity': quantity, 'price': price})
        self.save_portfolio()

    def get_portfolio(self):
        return self.portfolio
    
    def calculate_total_value(self):
        return sum(asset['quantity'] * asset['price'] for asset in self.portfolio)