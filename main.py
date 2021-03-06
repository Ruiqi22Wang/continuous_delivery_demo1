from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting!"""
    return """
    <h1>IDS690 1st Individual Project</h1>
    <a href="https://github.com/Ruiqi22Wang/continuous_delivery_demo1">Click here to see my repo </a>
  """


@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
