from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session handling

# Mock route for index
@app.route('/')
def index():
    dishes = [
        {"name": "Paneer Butter Masala", "description": "Delicious paneer cooked in butter", "price": 250},
        {"name": "Rajma Chawal", "description": "Comfort food of rajma and rice", "price": 150},
        {"name": "Aloo Paratha", "description": "Stuffed paratha with spicy potatoes", "price": 100}
    ]
    return render_template('index.html', dishes=dishes)


# Example route for login
@app.route('/login')
def login():
    session['user_id'] = 1  # Mock login for demonstration
    return redirect(url_for('index'))

# Example route for logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user_id from session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
