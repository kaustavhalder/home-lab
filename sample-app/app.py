from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/health')
def health():
    return "App is Healthy"


if __name__ == "__name__":
    app.run()
