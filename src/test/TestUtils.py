import re

import JsonSamples


def createPingBody():
    return (
        re.sub("\\s*", "", JsonSamples.pingRequest)
            .replace("replaceApplicationId", "1234567890")
            .replace("replaceRequestId", "09123231234")
            .replace("replaceRequestToken", "abcDefghiJkl01234")
    )
