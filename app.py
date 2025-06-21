from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

DB = 'db.sqlite3'
def get_db_connection():
    conn = sqlite3.connect(DB)
    #access columns in db by name
    conn.row_factory = sqlite3.Row
    return conn

def calculate(amount, rate):
    return float(amount)*float(rate)

@app.route('/', methods = ('GET', 'POST'))
def index():
    #default values
    result = 0.00
    rate = 10
    selected_base_currency = 'GBP'  
    selected_target_currency = 'INR'
    input_amount = 0  
    error_message = None          

    if request.method == 'POST':
        selected_base_currency = request.form.get('base_currency')
        selected_target_currency = request.form.get('target_currency')
        input_amount = float(request.form.get('amount'))

    conn = get_db_connection()
    rate_row = conn.execute(
        'SELECT rate FROM exchange_rates WHERE base_currency = ? AND target_currency = ?',
        (selected_base_currency, selected_target_currency)
    ).fetchone()

    conn.close()

    if rate_row:
        rate = rate_row['rate']
        result = calculate(input_amount, rate)
    else:  
        error_message = "Exchange rate not found for this pair."
        result = 0.00 # No rate found, so result is 0 or handle as per your requirement


    return render_template('index.html', result=result, selected_base_currency = selected_base_currency, selected_target_currency = selected_target_currency, input_amount=input_amount)


if __name__ == '__main__':
    app.run(debug=True)