import random
from api import catFact, jokes, getWeather, getNews
from restaurant import getRestaurant, resto_query
# string = input('say something')

topic_dict = {'value': 0 , 'name':''}

def switcher_func(string,topic):
    string = string.lower()
    phrase_list = string.split()
    switcher = {
        1: greeting(phrase_list, topic),
        2: howDoYouDo(phrase_list, topic),
        3: jokeOrCats(phrase_list, topic),
        4: news_weather_resto(phrase_list, topic),
        5: restaurant(phrase_list, topic),
        6: something(phrase_list,topic)
    }
    if noNoWordsDetector(phrase_list):
        response = noNoWordsDetector(phrase_list)
        animation = 'no'
        newTopic = topic
    else: response,animation, newTopic = switcher.get(topic)
    return response,animation, newTopic
    
def greeting(wordslist, topic):
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


def howDoYouDo(wordslist, topic):
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

def jokeOrCats(wordslist, topic):
    response = ''
    cats = ['cats','cat','kitten','kitty']
    joke = ['joke','jokes','funny','laugh']
    emote = 'laughing'
    nextTopic = 4
    outro = 'So what would you like to do now?\
         \n Hear the latest news, find a good restaurant or get the weather?' 
    if any(x in wordslist for x in cats):
        response = catFact() + outro
        emote = 'dog'
    elif any(x in wordslist for x in joke):
        response = jokes() + outro
    else: 
        response = 'its either cats or a joke'
        nextTopic = 3
    return response, emote, nextTopic

def news_weather_resto(wordslist, topic):
    # print('ping weather')
    news = ['news','info','events']
    weather = ['weather','temp','rain', 'sunny', 'sun' ]
    resto = ['restaurant','resturant','resto','food','hungry']
    followUp = [ 'else','nothing','done']
    next_topic = 4
    if any(x in wordslist for x in news):
        intro = 'here\'s today\'s headline from the New York Times: '
        outro = ' would you like to find a restaurant, get the weather or do something else?'
        response = intro + getNews()
        emote = 'takeoff'
    elif any(x in wordslist for x in weather):
        outro = ' Would you like to get the news, find a restaurant or do something else?'
        response = getWeather()
        print(response)
        emote = 'takeoff'
    elif any(x in wordslist for x in resto):
        response, emote, next_topic = restaurant(wordslist, 5)
    elif any(x in wordslist for x in followUp):
        response = 'well I\'m not really programmed to do anything else'
        emote = 'dancing'
        next_topic = 6
    else:
        response = 'restaurant, weather or news, nobody is keeping you here '
        emote = 'money'
    return response, emote, next_topic

def restaurant(wordslist, topic):
    # print('ping resto')
    global resto_query
    emote = 'money'
    next_topic = 5
    # print(resto_query)
    # print(resto_query['start'])
    if topic is not 5:
        pass
    else:
        if resto_query['start'] is False:
            response = 'how many people will you be dining with?'
            resto_query['start'] = True
        elif resto_query['amount_people'] is None:
            standard_resp = 'Do you keep kosher(yes or no)?'
            if isinstance(int(wordslist[0]), int):
                amount = int(wordslist[0])
                resto_query['amount_people'] = amount
                response = standard_resp
            elif isinstance(int(wordslist[-1]),int):
                amount =int(wordslist[-1])
                resto_query['amount_people'] = amount
                response = standard_resp
            else: response = 'please enter a whole number'
            # return response
        elif resto_query['kashrut'] is None:
            standard_resp = 'what style of food do you like(salad, bistro, fast-food)?'
            if 'yes' in wordslist:
                resto_query['kashrut'] = True
                response = standard_resp
            elif 'no' in wordslist:
                resto_query['kashrut'] = False
                response = standard_resp
            else: response = 'its a simple yes or no question'
        elif resto_query['style'] is None:
            next_topic = 4
            resto_query['style'] = wordslist[0]
            response = getRestaurant(resto_query)
        
        
        return response, emote, next_topic

def something(wordslist,topic):
    pass   


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
