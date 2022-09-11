from flask import Flask, jsonify, request 
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
    'title': 'Identity V',
    'genre': ' horror',
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
@app.route('/games', methods=['GET', 'POST'])
def all_games():
  response_object = {'status': 'success'}
  if request.method == "POST":
    post_data = request.get_json()
    GAMES.append({
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played'),
    })
    response_object['message'] = 'Game Added!'
  else: 
    response_object['games'] = GAMES
  return jsonify(response_object)




if __name__ == '__main__':
  app.run(debug=True)