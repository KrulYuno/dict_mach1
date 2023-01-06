from flask import Flask, render_template

import json

app     = Flask(__name__)

@app.route('/')
def root():
    return "/"

@app.route("/character")
def character():
    characters = dict()
    with open("data/characters.json") as file:
        characters  = json.load(file)

    return render_template("character.html", characters=characters)


if __name__ == "__main__":
    app.run()
