from flask import Flask, request, jsonify
from werkzeug.exceptions import abort

from DiscordUtils import verify, isPing, pong, isApplicationCommand

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>App is live</p>"


@app.route("/interactions/", methods=["POST"])
def outgoingWebhook():
    verify(request)
    if isPing(request):
        return jsonify(pong())
    elif isApplicationCommand(request):
        # print(request.json)
        return jsonify({
            "type": 4,
            "data": {
                "tts": False,
                "content": "Congrats on sending your command!",
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        })
