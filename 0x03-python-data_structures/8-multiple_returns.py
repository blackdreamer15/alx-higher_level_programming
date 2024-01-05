#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        return tuple((len(sentence), None))
    return tuple((len(sentence), sentence[0]))
