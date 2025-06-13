from flask import Flask, render_template, request, jsonify, session
import random
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    level = request.json.get('level')

    if level == 'easy':
        session['chances'] = 10
    elif level == 'hard':
        session['chances'] = 5
    else:
        return jsonify({'error': 'Invalid level'}), 400

    session['number'] = random.randint(1, 100)
    session['remaining'] = session['chances']

    return jsonify({'remaining': session['remaining']})

@app.route('/guess', methods=['POST'])
def guess_number():
    guess = int(request.json.get('guess'))
    number = session.get('number')
    remaining = session.get('remaining')

    if remaining <= 0:
        return jsonify({'result': 'lose', 'number': number})

    session['remaining'] -= 1

    if guess == number:
        return jsonify({'result': 'win'})
    elif session['remaining'] == 0:
        return jsonify({'result': 'lose', 'number': number})
    elif guess < number:
        return jsonify({'result': 'low', 'remaining': session['remaining']})
    else:
        return jsonify({'result': 'high', 'remaining': session['remaining']})

if __name__ == '__main__':
    app.run(debug=True)
