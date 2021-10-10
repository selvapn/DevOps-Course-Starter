from flask import session,render_template
from flask.templating import Environment
from flask.wrappers import Response
#from todo_app.flask_config import Config
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
TRELLO_KEY = os.getenv('TRELLO_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
TRELLO_ID=os.environ.get('TRELLO_ID')
TRELLO_TODO=os.environ.get('TRELLO_TODO')
TRELLO_DOING=os.environ.get('TRELLO_DOING')
TRELLO_DONE=os.environ.get('TRELLO_DONE')
TRELLO_BOARD=os.environ.get('TRELLO_BOARD')

headers = {
   "Accept": "application/json"
}

query = {
   'key' :  TRELLO_KEY,
   'token' : TRELLO_TOKEN
}

def get_query(url):
    return requests.request("GET",url,headers=headers,params=query)


def get_list():
    url = "https://api.trello.com/1/boards/"+TRELLO_BOARD+"/cards/"
    response = get_query(url)
    data = response.json()
    return data

def get_cards(list_id):
    url= "https://api.trello.com/1/lists/"+list_id+"/cards"
    response = get_query(url)
    data=response.json()
    return data

def add_card(card,desc):
    addurl="https://api.trello.com/1/cards?key="+TRELLO_KEY+"&token="+TRELLO_TOKEN+"&id="+TRELLO_ID+"&idList="+TRELLO_TODO+"&name="+card+"&desc="+desc
    requests.post(addurl)

def move_card(cardid,dest):
    cardid=cardid.strip()
    if dest =="Move to Todo":
        destid=TRELLO_TODO
    elif dest == "Move to Doing":
        destid=TRELLO_DOING
    elif dest == "Move to Done":
        destid=TRELLO_DONE
    moveurl="https://api.trello.com/1/cards/"+cardid+"/?key="+TRELLO_KEY+"&token="+TRELLO_TOKEN+"&idList="+destid
    response = requests.put(moveurl)
    return response.status_code,response.text

def del_card(cardid):
    cardid=cardid.strip()
    delurl="https://api.trello.com/1/cards/"+cardid+"/?key="+TRELLO_KEY+"&token="+TRELLO_TOKEN
    response = requests.delete(delurl)
    return response.status_code,response.text