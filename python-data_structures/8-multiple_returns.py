#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        a0 = sentence[0]
        return (len(sentence), a0)
