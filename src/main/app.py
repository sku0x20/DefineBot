import os

from flask import Flask, request, jsonify

from Commands.Define import Define
from Commands.HighFive import HighFive
from DiscordUtils import verify, isPing, pong, isApplicationCommand

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>App is live</p>"


@app.route("/interactions/", methods=["POST"])
def outgoingWebhook():
    if os.environ.get("TEST", "0") != "1":
        verify(request)
    requestType = request.json["type"]
    if isPing(requestType):
        return jsonify(pong())
    elif isApplicationCommand(requestType):
        commandName = request.json["data"]["name"]
        if HighFive.isCommand(commandName):
            jsonBody = request.json
            response = HighFive().execute(jsonBody)
            return jsonify(response)
        elif Define.isCommand(commandName):
            jsonBody = request.json
            response = Define().execute(jsonBody)
            return jsonify(response)
    # todo return response with response error code here
