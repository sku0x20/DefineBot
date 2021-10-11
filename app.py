from flask import Flask, request, jsonify
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>App is live</p>"


@app.route("/interactions/", methods=["POST"])
def outgoingWebhook():
    verify()
    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })
    elif request.json["type"] == 2:
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


def verify():
    from nacl.signing import VerifyKey
    from nacl.exceptions import BadSignatureError

    # Your public key can be found on your application in the Developer Portal
    # PUBLIC_KEY = 'APPLICATION_PUBLIC_KEY'
    PUBLIC_KEY = 'fcb1d87bdcd3c00ecf45a9df8494d276bb00f2982517b5d4e7b19f5e563a8187'

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = request.data.decode("utf-8")

    try:
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
    except BadSignatureError:
        abort(401, 'invalid request signature')
