from flask import Flask, render_template_string, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 8))
        use_letters = 'letters' in request.form
        use_numbers = 'numbers' in request.form
        use_symbols = 'symbols' in request.form

        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))

    return render_template_string("""
    <h1>Password Generator 🔐</h1>
    <form method="post">
        Length: <input name="length" type="number" value="8"><br>
        <input type="checkbox" name="letters" checked> Letters<br>
        <input type="checkbox" name="numbers"> Numbers<br>
        <input type="checkbox" name="symbols"> Symbols<br>
        <button type="submit">Generate</button>
    </form>
    {% if password %}
        <h3>Your Password:</h3>
        <p><strong>{{ password }}</strong></p>
    {% endif %}
    """, password=password)
