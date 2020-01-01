string = 'my name is jonathan'
def botlogic(string,status):
    phrase_list = string.split()
    switcher = {
        1: greeting(phrase_list),
        # 2: howDoYouDo,
        # 3: restOrBar,
        # 4: other,
    }
    response = switcher.get(status)
    return response
    
def greeting(wordslist):
    x = wordslist.index('name')
    if noNoWordsDetector(wordslist):
        response = noNoWordsDetector(wordslist)
    elif wordslist[x+1] == 'is':
        response = ('Hello ' + wordslist[x+2] )
    return response

def noNoWordsDetector(wordslist):
    noNoWords = {
        'fuck',
        'shit',
        'ass',
        'dick',
        'pussy',
        'tits',
        'fucking',
        'fucker',
    }
    for word in wordslist:
        if word in noNoWords:
            return 'dont make me wash your mouth with soap!'
        else: return False

print(botlogic(string,1))
