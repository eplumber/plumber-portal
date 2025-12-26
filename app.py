from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage (Resets if app restarts)
# In a real app, you would use a database (SQLite/Postgres)
database = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_action', methods=['POST'])
def login_action():
    # Simple hardcoded check based on your HTML placeholder
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == "admin" and password == "admin123":
        return redirect(url_for('dashboard'))
    else:
        return "Invalid Credentials <a href='/'>Try Again</a>"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', people=database)

@app.route('/add_new')
def add_new():
    return render_template('add.html')

@app.route('/save_person', methods=['POST'])
def save_person():
    person = {
        "name": request.form.get('name'),
        "phone": request.form.get('phone'),
        "cnic": request.form.get('cnic'),
        "exp": request.form.get('exp')
    }
    database.append(person)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
