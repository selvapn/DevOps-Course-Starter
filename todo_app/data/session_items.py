from flask import session,render_template
from flask.templating import Environment
from flask.wrappers import Response
from todo_app.flask_config import Config
import requests
import json
import os
class getCards:
    def __init__(self,id):
        self.url="https://api.trello.com/1/lists/"+id+"/cards/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN


    def getData(self):
        response = requests.get(self.url)
        data = response.text
        card=json.loads(data)
        return card

    def getTodoCards(self):
         return getCards.getData(self)

    def getDoingCards(self):
        return getCards.getData(self)

    def getDoneCards(self):
        return getCards.getData(self)

def add_card(card,desc):
    addurl="https://api.trello.com/1/cards?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN+"&id=610bec1beb3b0116846ba04a&idList=610beb5a99354405b1f4ec6f&name="+card+"&desc="+desc
    requests.post(addurl)

def move_card(cardid,dest):
    cardid=cardid.strip()
    if dest =="Move to Todo":
        destid=os.environ.get('TRELLO_TODO')
    elif dest == "Move to Doing":
        destid=os.environ.get('TRELLO_DOING')
    elif dest == "Move to Done":
        destid=os.environ.get('TRELLO_DONE')
    moveurl="https://api.trello.com/1/cards/"+cardid+"/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN+"&idList="+destid
    response = requests.put(moveurl)
    return response.status_code,response.text
