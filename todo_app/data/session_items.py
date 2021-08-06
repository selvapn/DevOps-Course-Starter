from flask import session,render_template
from flask.wrappers import Response
from todo_app.flask_config import Config
import requests
import json

def getTodoCard():
    todourl="https://api.trello.com/1/lists/610beb5a99354405b1f4ec6f/cards/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN
    response = requests.get(todourl)
    data = response.text
    cardname=json.loads(data)
    return cardname

def getDoingCard():
    doingurl="https://api.trello.com/1/lists/610beb5a99354405b1f4ec70/cards/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN
    response = requests.get(doingurl)
    data = response.text
    cardname=json.loads(data)
    return cardname

def getDoneCard():
    doneurl="https://api.trello.com/1/lists/610beb5a99354405b1f4ec71/cards/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN
    response = requests.get(doneurl)
    data = response.text
    cardname=json.loads(data)
    return cardname

def add_card(cardname,desc):
    addurl="https://api.trello.com/1/cards?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN+"&id=610bec1beb3b0116846ba04a&idList=610beb5a99354405b1f4ec6f&name="+cardname+"&desc="+desc
    requests.post(addurl)

def move_card(cardid,dest):
    cardid=cardid.strip()
    if dest =="Todo":
        destid="610beb5a99354405b1f4ec6f"
    elif dest == "Doing":
        destid="610beb5a99354405b1f4ec70"
    elif dest == "Done":
        destid="610beb5a99354405b1f4ec71"
    moveurl="https://api.trello.com/1/cards/"+cardid+"/?key="+Config.TRELLO_KEY+"&token="+Config.TRELLO_TOKEN+"&idList="+destid
    response = requests.put(moveurl)
    return response.status_code,response.text
