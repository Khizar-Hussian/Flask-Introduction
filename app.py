import os
import markdown
from flask import Flask

app = Flask(__name__)


# routing start heres
@app.route('/')
def index():
    """ Present some documentation Until project is complete"""
    with open('./README.md') as readme:
        return markdown.markdown(readme.read())


if __name__ == "__main__":
    app.run(debug=True)   