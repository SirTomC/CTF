from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

hidden_flag = "<p style='color: white;'>Tommy{y0u_HaV3_f0uND_m3}</p>"

template = """
<!DOCTYPE html>
<html>
<head>
  <title>XSS Challenge</title>
</head>
<body style="background-color: white; color: black;">
  <h2>XSS Challenge</h2>
  <form method="GET">
    Enter your message: <input name="q">
    <button type="submit">Submit</button>
  </form>
  <hr>
  <h3>Your input:</h3>
  <div>{user_input}</div>

  <div>{flag}</div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    q = request.args.get("q", "")
    
    user_input = q
    
    return render_template_string(template.format(user_input=user_input, flag=hidden_flag))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
