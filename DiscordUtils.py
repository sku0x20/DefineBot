from flask import jsonify
from werkzeug.exceptions import abort

from DiscordEnums import InteractionType


def verify(requestParam):
    from nacl.signing import VerifyKey
    from nacl.exceptions import BadSignatureError

    # Your public key can be found on your application in the Developer Portal
    # PUBLIC_KEY = 'APPLICATION_PUBLIC_KEY'
    PUBLIC_KEY = 'fcb1d87bdcd3c00ecf45a9df8494d276bb00f2982517b5d4e7b19f5e563a8187'

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    signature = requestParam.headers["X-Signature-Ed25519"]
    timestamp = requestParam.headers["X-Signature-Timestamp"]
    body = requestParam.data.decode("utf-8")

    try:
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
    except BadSignatureError:
        abort(401, 'invalid request signature')


def isPing(typeParam):
    return InteractionType(typeParam) == InteractionType.PING


def isApplicationCommand(typeParam):
    return InteractionType(typeParam) == InteractionType.APPLICATION_COMMAND


def pong():
    return {
        "type": InteractionType.PING.value
    }
