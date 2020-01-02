import random
from api import catFact, jokes
# string = input('say something')

topic_dict = {'value':1, 'name':''}

def botlogic(string,topic):
    string = string.lower()
    phrase_list = string.split()
    switcher = {
        1: greeting(phrase_list),
        2: howDoYouDo(phrase_list),
        3: jokeOrCats(phrase_list),
        # 4: other,
    }
    response,animation, newTopic = switcher.get(topic)
    return response,animation, newTopic
    
def greeting(wordslist):
    emote = 'inlove'
    if noNoWordsDetector(wordslist):
        #print(bool(noNoWordsDetector(wordslist)))
        response = noNoWordsDetector(wordslist)
        emote = 'no'
        #print(response)
    else:
        if len(wordslist) == 1:
            name = wordslist[0]
        elif ('name' in wordslist):
            x = wordslist.index('name')
            if wordslist[x+1] is 'is':
                name = wordslist[x+2]
        elif (('its' in wordslist) or ('it\'s' in wordslist) ):
            name = wordslist[1]
        elif (('im' in wordslist) or ('i\'m' in wordslist)):
            name = wordslist[1]
        else:
            name = 'buddy'
        name = name.capitalize()
        response = ('Hey ' + name + ' how are you feeling today?' )
    print('name is ', topic_dict['name'])
    return response,emote,2


def howDoYouDo(wordslist):
    good = ['great','happy','good','ok']
    bad = ['not','sad','upset','bad','down']
    name = topic_dict['name']
    emote = 'crying'
    if noNoWordsDetector(wordslist):
        #print(bool(noNoWordsDetector(wordslist)))
        response = noNoWordsDetector(wordslist)
        emote = 'no'
    else:
        if any(x in wordslist for x in bad ):
            response = 'That\'s too bad , would you like me to cheer you up with a joke or a cat fact?'
            emote = 'crying'
        elif any(x in wordslist for x in good ):
            response = 'That\'s great! So what would you like to do?'\
                ' Hear a Joke or learn a new cat fact?'
            emote = 'excited'
        else:
            response = 'not sure bruh'
    return response,emote,3

def jokeOrCats(wordslist):
    response = ''
    cats = ['cats','cat','kitten','kitty']
    joke = ['joke','jokes','funny','laugh']
    emote = 'laughing'
    if any(x in wordslist for x in cats):
        response = catFact()
    elif any(x in wordslist for x in joke):
        response = jokes()
    else: response = 'its either cats or a joke'
    return response+'\n' 'So what would you like to do now?\
         \n Hear the latest news, find a good restaurant or get the weather?' \
         , emote,4



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
    phrases = [
        'don\'t make me wash your mouth with soap!',
        'your mother was a hamster and your father smells of elderberries',
        'it\'s ok, I farted on your pillow',
        'you lack manners almost as much as good looks',
        'were you not hugged enough as a child?',
        'it\'s ok, I forgive you',
        'oi! no fucking cursing here you fucking cuntface'
    ]
    for word in wordslist:
        if word in noNoWords:
            return phrases[random.randint(0,len(phrases))]

#print(botlogic(string,1))
#print(noNoWordsDetector(['fock','toot']))
