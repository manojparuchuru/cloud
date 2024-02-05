from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for user data (replace this with a database in a real application)
users_data = {}


@app.route('/')
def registration_page():
    return render_template('registration.html')


@app.route('/register', methods=['POST'])
def register_user():
    # Get user data from the registration form
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    email = request.form['email']

    # Store user data in memory (replace this with database storage)
    users_data[username] = {
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }

    # Redirect to the display page
    return redirect(url_for('display_info', username=username))


@app.route('/display/<username>')
def display_info(username):
    # Retrieve user data from memory (replace this with database retrieval)
    user_data = users_data.get(username, None)

    if user_data:
        return render_template('display_info.html', user_data=user_data)
    else:
        return "User not found"


@app.route('/login', methods=['POST'])
def login():
    # Get login credentials from the login form
    login_username = request.form['loginUsername']
    login_password = request.form['loginPassword']

    # Retrieve user data from memory (replace this with database retrieval)
    user_data = users_data.get(login_username, None)

    if user_data and user_data['password'] == login_password:
        return f"Login successful! User: {login_username}"
    else:
        return "Invalid login credentials"


if __name__ == '__main__':
    app.run(debug=True)

