"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
from botlogic import botlogic, topic_dict


@route('/', method='GET')
def index():
    return template("chatbot.html")
@route('/intro', method='POST')
def intro():
    if request.get_cookie("visited"):
        botresponse = "Welcome back! Nice to see you again, please remind me your name"
    else:
        response.set_cookie("visited", "yes")
        botresponse=  "Hello there! Nice to meet you, what is your name"
    
    return json.dumps({"animation": 'excited', "msg": botresponse})


@route("/chat", method='POST')
def chat():
    global topic_dict
    if topic_dict['value'] is 0:
        topic_dict['value'] = 1
    print(topic_dict['name'])
    user_message = request.POST.get('msg')
    botresponse,animation, newTopic = botlogic(user_message, topic_dict['value'])
    topic_dict['value'] = newTopic
    return json.dumps({"animation": animation, "msg": botresponse})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
