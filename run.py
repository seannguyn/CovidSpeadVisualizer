from flask import Flask, request, jsonify, render_template
from Grid import Grid
import json
from random import randrange
from flask_cors import CORS


app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route("/", methods=["GET"])
def connectedX():

    return render_template("connectedX.html",)


@app.route("/dummy", methods=["GET"])
def hello():

    return render_template("hello.html",)


@app.route("/randomizeNoSocialDistance", methods=["GET"])
def randomizeNoSocialDistance():

    # call random function
    randomGrid = Grid.randomInputStringAndCovidNoSocialDistance()

    virusPoints = randomGrid.split("|")[0].split("_")
    inputString = randomGrid.split("|")[1]

    gridInfo = {
        "covid": virusPoints,
        "inputString": inputString,
    }
    return jsonify(gridInfo)

@app.route("/randomizeSocialDistance", methods=["GET"])
def randomizeSocialDistance():

    # call random function
    randomGrid = Grid.randomInputStringAndCovidSocialDistance()

    virusPoints = randomGrid.split("|")[0].split("_")
    inputString = randomGrid.split("|")[1]

    gridInfo = {
        "covid": virusPoints,
        "inputString": inputString,
    }
    return jsonify(gridInfo)

@app.route('/findConnectedX', methods=['POST'])
def findMaxConnectedNode():

    bodyData = json.loads(str(request.data, encoding='utf-8'))

    grid = Grid(bodyData['gridRow'], bodyData['gridCol'], bodyData['inputString'], bodyData['xCovid'])

    Grid.findMaxConnectedCell(grid)

    return jsonify(grid.traversePath)


if __name__ == "__main__":
    app.run()
