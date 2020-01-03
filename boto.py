"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
from botlogic import switcher_func, topic_dict


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    global topic_dict
    if topic_dict['value'] is 0:
        topic_dict['value'] = 1
    print(topic_dict['name'])
    user_message = request.POST.get('msg')
    botresponse,animation, newTopic = switcher_func(user_message, topic_dict['value'])
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
