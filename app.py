from flask import Flask
from flask import request
from flask import render_template
from positiongen import generate_positions

app = Flask(__name__)

positions = {
    'First Base':'',
    'Second Base':'',
    'Third Base':'',
    'Pitcher':'',
    'Short Stop':'',
    'Cather':'',
    'Right Field':'',
    'Left Field':'',
    'Center Field':''
}

@app.route('/')
def mainpage():
    return render_template('index.html',
    position_details=positions,
    team='')

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
