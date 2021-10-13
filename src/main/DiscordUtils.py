import os

from werkzeug.exceptions import abort

from DiscordEnums import InteractionType


def verify(requestParam):
    from nacl.signing import VerifyKey
    from nacl.exceptions import BadSignatureError

    # Your public key can be found on your application in the Developer Portal
    # PUBLIC_KEY = 'APPLICATION_PUBLIC_KEY'
    PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
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
