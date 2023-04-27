# Baseball Position Generator

## Description
This is a web application that can populate positions for each inning and batting order.
It helps manager/coach of baseball teams (Little League, in particular) to distribute and rotate positions of the players, so that there will be less chaos during the game.

## Usage
You can put positions and players into the boxes and specify number of innings and team name and press `Generate!` button to produce a table that contains position sheet as well as batting order.

* Toggle `Preserve position for first inning` option to keep the positions for the first inning, and the positions are shifted for the following innings. Otherwise, positions are randomly generated, while avoiding the same player to be allocated over and over.
* Toggle `Preserve batting order` option to keep the batting order.
* You can pre-populate positions and players by providing URL parameters to the app. Accepted inputs are `teamname`: name of the team, `positions`: comma separated list of positions, and `players`: comma separated list of players

## Requirements
* `Python 3.8`
* `Pip`
* `virtualenv`

## Installation

With `virtualenv`:

```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Running tests

Run:

```sh
$ python -m unittest test_positiongen
```

## Running the application

### Running locally

Run the application using the built-in Flask server:

```sh
$ flask --app app run
```