from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def fizzBuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


@app.route('/run', methods=['GET'])
def fetchFizzBuzz():
    num = int(request.args.get('num'))
    return jsonify(solution=fizzBuzz(num))


if __name__ == "__main__":
    app.run(debug=True)
