from flask import Flask

app = Flask(__name__)

# routing start heres
@app.route('/')
def index()