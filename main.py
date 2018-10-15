
""""
Doe het volgende in Powershell om de webserver op te starten:

$env:FLASK_APP="main.py"
$env:FLASK_ENV="development"
python -m flask run
"""

from flask import Flask
app = Flask(__name__)

from flask import render_template

audiofiles = [
    'Lazy_Porch_Swing_Blues.mp3',
    'Swing_Theory.mp3'
]

@app.route("/")
def index():
    return render_template('audiofiles.html', audiofiles=audiofiles)

@app.route("/audioplayer/<filename>")
def audioplayer(filename):
    return render_template('audioplayer.html', filename=filename)
