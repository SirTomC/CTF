from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

FLAG = "Tommy{y0u_HaV3_f0uND_m3}"

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
  <p>Hint: Dark mode is superior by far.</p>
  <hr>
  <h3>Your input:</h3>
  <div>{user_input}</div>

  <script>
    async function revealFlag() {{
      const bg = window.getComputedStyle(document.body).backgroundColor;
      if (bg !== "rgb(0, 0, 0)") {{
        return;
      }}
      const res = await fetch("/flag");
      const text = await res.text();
      const p = document.createElement("p");
      p.style.color = "white";
      p.textContent = text;
      document.body.appendChild(p);
    }}
    revealFlag();
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    q = request.args.get("q", "")
    return render_template_string(template.format(user_input=q))

@app.route("/flag")
def flag():
    return FLAG

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
