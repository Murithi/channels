from channels import Group
import threading
import random


def sendmsg(num):
    Group('safcom').send({'text': num})


t = 0


def periodic():
    global t
    n = random.randint(10, 200)
    sendmsg(str(n))
    t = threading.Timer(5, periodic)
    t.start()


def ws_message(message):
    global t
    print(message.content['text'])
    if (message.content['text'] == 'start'):
        periodic()
    else:
        t.cancel()


def ws_connect(message):
    Group('safcom').add(message.reply_channel)
    Group('safcom').send({'text': 'connected'})


def ws_disconnect(message):
    Group('safcom').send({'text': 'disconnected'})
    Group('safcom').discard(message.reply_channel)
