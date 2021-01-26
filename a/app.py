from flask import Flask
app = Flask(__name__)

@app.route('/a')
def a():
    return 'I am route a'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
