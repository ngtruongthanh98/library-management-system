from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

# hello world route
@app.route('/', methods=['GET'])
def greeting():
  return 'Hello World'

@app.route('/shark', methods=['GET'])
def shark():
  return 'Shark'

## Game list, we will use DynamoDB

GAMES = [
  {
    'title': 'Bida',
    'genre': ' sports',
    'played': False
  },
  {
    'title': 'Bida',
    'genre': ' sports',
    'played': False
  },
  {   
    'title':'Evil Within',
    'genre':'horror',
    'played': False,
  },
  {   
    'title':'The last of us',
    'genre':'survival',
    'played': True,
  },
  {  
    'title':'Days gone',
    'genre':'horror/survival',
    'played': False,
  },
  {   
    'title':'Mario',
    'genre':'retro',
    'played': True,
  }
]

# The GET route handler
@app.route('/games', methods=['GET'])
def all_games():
  return jsonify({
    'games': GAMES,
    'status': 'success',

  })


if __name__ == '__main__':
  app.run(debug=True)