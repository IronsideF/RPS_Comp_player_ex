from flask import render_template,request
from app import app
from models.player import *
from models.game import *

player_count = 0
comp_count = 0
draw_count = 0

@app.route('/rps')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def game():
    game = Game()
    player_1 = Player(request.form['name'], request.form['choice'])
    comp_player = game.generate_player()
    winning_player = game.play_game(player_1, comp_player)
    if winning_player == player_1:
        player_count += 1
    elif winning_player == comp_player:
        comp_count += 1
    else:
        draw_count += 1

    return render_template('result.html', winner=winning_player, player1=player_1, player2=comp_player, playercount=player_count, compcount=comp_count, drawcount=draw_count)

    