from flask import Flask
app = Flask(__name__)

@app.route('/a')
def a():
    return 'I am route a'

@app.route('/a/a')
def aa():
    return 'I am route aa'

@app.route('/a/b')
def ab():
    return 'I am route ab'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
