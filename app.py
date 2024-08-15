from flask import Flask, render_template, request, redirect, url_for
from finance_manager import FinanceManager
from crypto_manager import CryptoManager

app = Flask(__name__)
finance_manager = FinanceManager('data/transactions.json')
crypto_manager = CryptoManager('data/portfolio.json')

@app.route('/')
def index():
    transactions = finance_manager.get_transactions()
    balance = finance_manager.calculate_balance()
    return render_template('index.html', transactions=transactions, balance=balance)

@app.route('/portfolio')
def portfolio():
    portfolio = crypto_manager.get_portfolio()
    total_value = crypto_manager.calculate_total_value()
    return render_template('portfolio.html', portfolio=portfolio, total_value=total_value)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    description = request.form.get('description')
    amount = float(request.form.get('amount'))
    finance_manager.add_transaction(description, amount)
    return redirect(url_for('index'))

@app.route('/add_crypto', methods=['POST'])
def add_crypto():
    name = request.form.get('name')
    quantity = float(request.form.get('quantity'))
    price = float(request.form.get('price'))

    crypto_manager.add_crypto(name, quantity, price)

    return redirect(url_for('portfolio'))

@app.route('/edit_crypto/<int:index>', methods=['GET', 'POST'])
def edit_crypto(index):
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = float(request.form.get('quantity'))
        price = float(request.form.get('price'))
        crypto_manager.portfolio[index] = {'name': name, 'quantity': quantity, 'price': price}
        crypto_manager.save_portfolio()
        return redirect(url_for('portfolio'))

    asset = crypto_manager.portfolio[index]
    return render_template('edit_crypto.html', asset=asset, index=index)

@app.route('/delete_crypto/<int:index>', methods=['POST'])
def delete_crypto(index):
    del crypto_manager.portfolio[index]
    #crypto_manager.portfolio[index]
    return redirect(url_for('portfolio'))

if __name__ == '__main__':
    app.run(debug=True)


