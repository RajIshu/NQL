def MoreKeys(words):
    moreKeywords = ['from', 'into', 'where', 'all', 'a', 'an', 'in', 'to']
    # quantKeywords = ['all', 'a', 'an']
    
    keysGot = []

    for word in words:
        if word in moreKeywords:
            keysGot.append(word)

    return keysGot

