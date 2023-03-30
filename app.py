from flask import Flask
from flask import request
from flask import render_template
from positiongen import generate_positions

app = Flask(__name__)

default_positions = {
    'First Base':'',
    'Second Base':'',
    'Third Base':'',
    'Pitcher':'',
    'Short Stop':'',
    'Catcher':'',
    'Right Field':'',
    'Left Field':'',
    'Center Field':''
}

@app.route('/')
def mainpage():
    teamname = request.args.get('teamname', '')
    positions = request.args.get('positions', '').split(',')
    players = request.args.get('players', '').split(',')
    position_details = {} if request.args.get('positions') else default_positions
    for i, pos in enumerate(positions):
        position_details[pos] = players[i]
    return render_template('index.html',
    position_details=position_details,
    team=teamname)

@app.route('/generate', methods=['POST'])
def generate():
    positions = request.form.getlist('positions')
    players = request.form.getlist('players')
    team = request.form.get('team')
    innings = int(request.form.get('innings'))
    norandomize = True if request.form.get('norandomize') == 'on' else False
    keeporder = True if request.form.get('keeporder') == 'on' else False
    (order, position_map) = generate_positions(
        positions, players, innings, norandomize, keeporder)
    position_data = [[p]+pl for p,pl in position_map.items()]
    return render_template('generate.html', team=team, innings=innings, positions_details=position_data, order=order)
