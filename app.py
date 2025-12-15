from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password"><br>
  <button type="submit">Login</button>
</form>
<p>{{ message }}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simulated SQL injection vulnerability
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("[DEBUG] SQL:", query)

        if username == 'admin' and "' OR 1=1--" in password:
            message = "Flag: CTF{sql_injection_worked}"
        else:
            message = "Login failed"
    return render_template_string(template, message=message)

if __name__ == '__main__':
    app.run(debug=True)
