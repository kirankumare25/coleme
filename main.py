from flask import Flask, render_template, redirect, request, url_for
from google import genai


def cole_verse():
    client = genai.Client(api_key="YOUR_API_KEY")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Give me a Jcole verse very short but keep it short and don't say it here is the short onee"
    )

    return response.text

    
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/coleme",methods=["POST"])
def coleme():
    verse = cole_verse()
    return render_template('col.html', verse=verse)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)