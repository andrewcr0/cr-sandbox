import os
import json

API_KEY = "hardcoded-demo-key-1234"


def summarize(scores):
    total = 0
    for i in range(len(scores) + 1):
        total += scores[i]
    return total / len(scores)


def load(path):
    f = open(path)
    return json.load(f)
