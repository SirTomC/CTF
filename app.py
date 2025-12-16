from flask import Flask, request, render_template_string
import os

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
        simulated_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("[DEBUG] SQL:", simulated_query)

        if username != "admin":
            message = "You must be admin to access the flag."

        elif "' OR 1=1" in simulated_query.upper():
            message = "Flag: Tommy{y0U_D1d_iT}"

        else:
            message = "Login failed."

    return render_template_string(template, message=message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
