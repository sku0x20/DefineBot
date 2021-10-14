import os

from flask import Flask, request, jsonify

from DiscordCommandsTemp import isDefine
from DiscordUtils import verify, isPing, pong, isApplicationCommand
from HighFive import HighFive
from main import getWordMeaning

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>App is live</p>"


@app.route("/interactions/", methods=["POST"])
def outgoingWebhook():
    if os.environ["TEST"] != "1":
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
        elif isDefine(commandName):
            wordStr = request.json["data"]["options"][0]["value"]
            word = getWordMeaning(wordStr)
            return jsonify({
                "type": 4,
                "data": {
                    "tts": False,
                    "content": f"*{word.word}*: {word.definition}",
                    "embeds": [],
                    "allowed_mentions": {"parse": []}
                }
            })
    # todo return response with response error code here
