import random
from api import catFact, jokes
# string = input('say something')

topic_dict = {'value': 0 , 'name':''}

def botlogic(string,topic):
    string = string.lower()
    phrase_list = string.split()
    switcher = {
        1: greeting(phrase_list),
        2: howDoYouDo(phrase_list),
        3: jokeOrCats(phrase_list),
        4: news_weather_resto(phrase_list),
        #5: startOver(phrase_list)
    }
    if noNoWordsDetector(phrase_list):
        response = noNoWordsDetector(phrase_list)
        animation = 'no'
        newTopic = topic
    else: response,animation, newTopic = switcher.get(topic)
    return response,animation, newTopic
    
def greeting(wordslist):
    emote = 'inlove'
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
    return response,emote,2


def howDoYouDo(wordslist):
    good = ['great','happy','good','ok']
    bad = ['not','sad','upset','bad','down']
    name = topic_dict['name']
    emote = 'crying'
    nextTopic = 3
    if any(x in wordslist for x in bad ):
        response = 'That\'s too bad , would you like me to cheer you up with a joke or a cat fact?'
        emote = 'crying'
    elif any(x in wordslist for x in good ):
        response = 'That\'s great! So what would you like to do?'\
            ' Hear a Joke or learn a new cat fact?'
        emote = 'excited'
    else:
        response = 'just asking how you\'re doing bruh'
        nextTopic = 2
    return response,emote,nextTopic

def jokeOrCats(wordslist):
    response = ''
    cats = ['cats','cat','kitten','kitty']
    joke = ['joke','jokes','funny','laugh']
    emote = 'laughing'
    nextTopic = 4
    if any(x in wordslist for x in cats):
        response = catFact()
        emote = 'dog'
    elif any(x in wordslist for x in joke):
        response = jokes()
    else: 
        response = 'its either cats or a joke'
        nextTopic = 3
    return response+'\n' 'So what would you like to do now?\
         \n Hear the latest news, find a good restaurant or get the weather?' \
         , emote, nextTopic

def news_weather_resto(wordslist):
    news = ['news']
    weather = ['weather','temp','rain', 'sunny', 'sun' ]
    resto = ['restaurant']
    if any(x in wordslist for x in news):
        response = 'all is good'
        emote = 'takeoff'
    elif any(x in wordslist for x in weather):
        response = 'all is rain'
        emote = 'takeoff'
    elif any(x in wordslist for x in resto):
        response = 'all is food'
        emote = 'takeoff'
    else:
        response = 'restaurant, weather or news, nobody is keeping you here '
        emote = 'money'
    return response, emote,4

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
        print(word)
        if word in noNoWords:
            return phrases[random.randint(0,len(phrases)-1)]

#print(botlogic(string,1))
#print(noNoWordsDetector(['fock','toot']))
