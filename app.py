from flask import Flask, request, jsonify

from DiscordCommands import isHighFive, isDefine
from DiscordUtils import verify, isPing, pong, isApplicationCommand

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>App is live</p>"


@app.route("/interactions/", methods=["POST"])
def outgoingWebhook():
    verify(request)
    requestType = request.json["type"]
    if isPing(requestType):
        return jsonify(pong())
    elif isApplicationCommand(requestType):
        commandName = request.json["data"]["name"]
        if isHighFive(commandName):
            userFrom = request.json["member"]["user"]["id"]
            userTo = request.json["data"]["target_id"]
            return jsonify({
                "type": 4,
                "data": {
                    "tts": False,
                    "content": f"High Five <@{userTo}>",
                    "embeds": [],
                    "allowed_mentions": {"parse": ["users"]}
                }
            })
        elif isDefine(commandName):
            print(request.json)
            pass
            # todo
