#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        tupl = (len(sentence), sentence[0])
    else:
        tupl = (len(sentence), 'None')
    return tupl
