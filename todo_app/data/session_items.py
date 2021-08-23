from flask import session,render_template
from flask.templating import Environment
from flask.wrappers import Response
from todo_app.flask_config import Config
import requests
import json
import os
class getCards:
    def __init__(self,item):
        self.item="https://api.trello.com/1/lists/"+item+"/cards/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN#

    def getData(self):
        response = requests.get(self.item)
        data = response.text
        cardname=json.loads(data)
        return cardname

    def getTodoCards(self):
         return getCards.getData(self)

    def getDoingCards(self):
        return getCards.getData(self)

    def getDoneCards(self):
        return getCards.getData(self)

def add_card(cardname,desc):
    addurl="https://api.trello.com/1/cards?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN+"&id=610bec1beb3b0116846ba04a&idList=610beb5a99354405b1f4ec6f&name="+cardname+"&desc="+desc
    requests.post(addurl)

def move_card(cardid,dest):
    cardid=cardid.strip()
    if dest =="Move to Todo":
        destid="610beb5a99354405b1f4ec6f"
    elif dest == "Move to Doing":
        destid="610beb5a99354405b1f4ec70"
    elif dest == "Move to Done":
        destid="610beb5a99354405b1f4ec71"
    moveurl="https://api.trello.com/1/cards/"+cardid+"/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN+"&idList="+destid
    response = requests.put(moveurl)
    return response.status_code,response.text
