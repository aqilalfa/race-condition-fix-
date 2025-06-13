from flask import Flask, request
from filelock import FileLock
import os

app = Flask(__name__)
STOCK_FILE = 'stock.txt'
LOCK_FILE = STOCK_FILE + '.lock'  # akan jadi "stock.txt.lock"

@app.route('/buy', methods=['POST'])
def buy():
    item = request.form.get('item', 'banana')
    qty = int(request.form.get('qty', '1'))

    lock = FileLock(LOCK_FILE)

    try:
        with lock:
            if not os.path.exists(STOCK_FILE):
                return "Stock file not found", 500

            with open(STOCK_FILE, 'r') as f:
                stock_data = f.read().strip()

            if not stock_data.isdigit():
                return "Stock file corrupted or unreadable", 500

            stock = int(stock_data)

            if stock < qty:
                return f"Insufficient stock! Available: {stock}", 400

            stock -= qty

            with open(STOCK_FILE, 'w') as f:
                f.write(str(stock))

            return f"Successfully bought {qty} {item}(s). Remaining: {stock}"

    except Exception as e:
        return f"Internal error: {e}", 500

if __name__ == '__main__':
    # Reset stock ke 10 SETIAP KALI server dijalankan
    with open(STOCK_FILE, 'w') as f:
        f.write('10')

    print("[INFO] Stock reset to 10.")
    app.run(debug=True, threaded=True)
