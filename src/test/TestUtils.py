import re

import JsonSamples


def createPingBody():
    return (
        stringFromJsonSample(JsonSamples.pingRequest)
            .replace("replaceApplicationId", "1234567890")
            .replace("replaceRequestId", "09123231234")
            .replace("replaceRequestToken", "abcDefghiJkl01234")
    )


def stringFromJsonSample(jsonSample):
    return re.sub("\\s{2,}", "", jsonSample)
