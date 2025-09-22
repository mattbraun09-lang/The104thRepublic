from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set the correct passcode here
CORRECT_PASSCODE = "HICOM6767"

@app.route('/')
def home():
    # Redirect to the login page by default
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the passcode from the form
        passcode = request.form.get('passcode')

        # Check if the entered passcode is correct
        if passcode == CORRECT_PASSCODE:
            # If correct, redirect to the protected page
            return redirect(url_for('protected'))
        else:
            # If incorrect, re-render the login page with an error message
            return render_template('login.html', error="Invalid passcode.")
    
    # Render the login page for GET requests
    return render_template('login.html')

@app.route('/protected')
def protected():
    return render_template('protected.html')

if __name__ == '__main__':
    app.run(debug=True)
