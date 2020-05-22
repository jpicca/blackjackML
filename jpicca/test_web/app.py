# Dependencies
import numpy as np
from flask_cors import CORS
from flask import Flask, jsonify
import pickle


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Basis for Gameplay
#################################################

# Load model policy file
policy_file = 'Q_policy'
fr = open(policy_file, 'rb')
policy = pickle.load(fr)
fr.close()

# Load win % file
winpct_file = 'win_pct'
fr = open(winpct_file, 'rb')
win_pct = pickle.load(fr)
fr.close()

# Template for dictionary to jsonify/return
final_dict = {

        'cards_dealt': 
            {
                'player': [],
                # First card in dealer list is the show card
                'dealer': []
            },
        'actions': 
            [
            # Action (0: Stay, 1: Hit, 2: Double Down, 3: Split)
             {'action':0,'winProb':0,'available':1},
             {'action':1,'winProb':0,'available':1},
             {'action':2,'winProb':0,'available':1},
             {'action':3,'winProb':0,'available':0},   
            ],
        'winProb': 42.5,
        'gameState': 
            {
                # Standard (0) = typical game, no split ongoing; Standard (1) = split game
                'standard': 0,
                'end': 0
            }
    }

# Other variables needed
# Have a second list & usable ace in player cards to handle splits if necessary
actionCount = 0
playerCards = [[],[]]
playerUseAce = [False, False]
dealerCards = []
dealerUseAce = False

def reset():

    # Reset actionCount, playerCards, playerUseAce, dealerCards, dealerUseAce
    return 0, [[],[]], [False,False], [], False

def makeStack():

    # Stuff here

def deal2Cards():

    # Stuff here for dealing

def giveCard():

    # Stuff here



#################################################
# Flask Routes
#################################################

# D3.js will navigate to this url based on user actions/inputs
# Flask will use arguments from these inputs to advance
# gameplay forward. It will then return jsonified data
# to the front-end so it can be visualized

@app.route("/<game>/<action>/<bet>")
def gamePlay(game,action,bet):

    # Determine if this is a new game

    # If new game, deal cards
    if (game == 'new'):

        # Stuff to set up new round

        return jsonify(final_dict)

    # Else take action input and perform proper processing
    else:

        # Manage ongoing game based on actions

        return jsonify(final_dict)

    

if __name__ == '__main__':
    app.run(debug=True)
