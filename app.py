from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Simulated user database
users = {
    'admin': 'passwordadmin',
    'carlos': 'carlos'
}

template = """
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password"><br>
  <button type="submit">Login</button>
</form>
<p><strong>Hint:</strong> Usernames:</p>
<ul>
  <li>admin</li>
  <li>carlos</li>
</ul>
<p>{{ message }}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("[DEBUG] SQL:", query)

        if username in users:
            injected = "' OR 1=1" in password.upper() or "--" in password
            real_password = users[username]
            if injected:
                if username == 'admin':
                    message = "Flag: Tommy{y0U_hAv3_F0uND_mE}"
                else:
                    message = f"Access granted to {username}, but flag is only for admin."
            elif password == real_password:
                if username == 'admin':
                    message = "Flag: Tommy{y0U_hAv3_F0uND_mE}"
                else:
                    message = f"Welcome, {username}. (No flag for you!)"
            else:
                message = "Login failed: incorrect password."
        else:
            message = "Login failed: user not found."

    return render_template_string(template, message=message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
