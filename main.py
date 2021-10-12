import requests

from Word import Word

FREE_DICTIONARY_API = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"


def getWordFromJson(response):
    word = response[0]["word"]
    definition = response[0]["meanings"][0]["definitions"][0]["definition"]
    return Word(word, definition)


def getWordMeaning(wordStr):
    response = requests.get(FREE_DICTIONARY_API.format(word=wordStr))
    word = getWordFromJson(response.json())
    return word
