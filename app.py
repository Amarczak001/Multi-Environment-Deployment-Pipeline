from flask import Flask
app = Flask(__name__)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f'The result is {result}'

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
