# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR QUESTIONS 1 AND 2. DO NOT CHANGE ANY METHOD SIGNATURES OR THE RUNALL METHOD

from flask import Flask, request, jsonify
import json
from time import clock

app = Flask(__name__)


# IMPORTANT: DO NOT CHANGE THIS FUNCTION UNDER ANY CIRCUMSTANCES
@app.route('/runall', methods=['POST'])
def runall():
    q1inputs = request.data
    # q2inputs = request.args.get('q2inputs')
    q1inputs = json.loads(q1inputs)
    response = jsonify([[runq1(q1input) for q1input in q1inputs], []])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def runq1(q1input):
    start = clock()
    output = findbestprofit(q1input[0], q1input[1])
    end = clock()
    diff = end - start
    return output, diff


# Space for question 1
def findbestprofit(pricesarray, k):
    return -1


if __name__ == '__main__':
    app.run(port=8182)
