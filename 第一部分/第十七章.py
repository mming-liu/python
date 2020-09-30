from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello,World! asdajid"

app.run(port=8000)