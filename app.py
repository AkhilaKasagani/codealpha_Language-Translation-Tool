from flask import Flask, request
import requests

app = Flask(__name__)

# ✅ Stable API (MyMemory Translation API)
API_URL = "https://api.mymemory.translated.net/get"

html = """
<!DOCTYPE html>
<html>
<head>
    <title>API Translator</title>

    <style>
        body {{
            font-family: Arial;
            text-align: center;
            background: #f2f2f2;
            padding-top: 40px;
        }}

        .box {{
            background: white;
            width: 500px;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }}

        textarea {{
            width: 90%;
            height: 120px;
            padding: 10px;
        }}

        select, button {{
            padding: 10px;
            margin: 10px;
        }}

        #output {{
            color: green;
            font-size: 18px;
        }}
    </style>
</head>

<body>

<div class="box">

    <h2>🌐 API Translator (MyMemory)</h2>

    <form method="POST">
        <textarea name="text" placeholder="Enter text"></textarea>
        <br>

        <select name="source">
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="te">Telugu</option>
            <option value="ta">Tamil</option>
        </select>

        →

        <select name="target">
            <option value="te">Telugu</option>
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="ta">Tamil</option>
        </select>

        <br>

        <button type="submit">Translate</button>
    </form>

    <h3>Output:</h3>
    <div id="output">{output}</div>

</div>

</body>
</html>
"""

# 🔁 API FUNCTION
def translate_text(text, source, target):
    try:
        lang_pair = f"{source}|{target}"

        response = requests.get(API_URL, params={
            "q": text,
            "langpair": lang_pair
        })

        data = response.json()
        return data["responseData"]["translatedText"]

    except:
        return "API Error / Not reachable"

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    if request.method == "POST":
        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        if text.strip() != "":
            output = translate_text(text, source, target)

    return html.format(output=output)

if __name__ == "__main__":
    app.run(debug=True)