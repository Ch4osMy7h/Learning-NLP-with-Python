def percent(word, text):
    count = 0
    for w in text:
        if w == word:
            count = count + 1

    return '%.2f%%' % (count/len(text))