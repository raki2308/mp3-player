from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)


@app.route('/')
def index():
    currentSongIndex = 1
    return render_template('index.html', currentSongIndex=currentSongIndex)


if __name__ == '__main__':
    app.run(debug=True)

