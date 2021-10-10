from typing import List
from flask import Flask,escape,request,render_template,redirect
from flask.helpers import url_for
from flask.wrappers import Response
import requests
from todo_app.flask_config import Config
from todo_app.data.session_items import TRELLO_BOARD, get_list, add_card, move_card, del_card
import os

app = Flask(__name__)
app.config.from_object(Config)
viewmodel=get_list()

@app.route('/', methods=['GET'])
def index():
    if request.method == "POST":
        if request.form['card'] == "AddCard":
            return redirect(url_for('addCard'))
        if request.form['card'] == "movecard":
            return redirect(url_for('movecard'))
    else:
        return render_template('index.html',items=viewmodel)

@app.route('/addcard',methods=['GET','POST'])
def addCard():
    if request.method == "POST":
        title =request.form["trello_title"]
        desc=request.form["trello_desc"]
        add_card(title,desc)
        return redirect('/')
    else:
        return render_template('add_card.html')

@app.route('/movecard/<cardid>/<destid>',methods=['GET','POST'])
def moveCard(cardid,destid):
    get=move_card(cardid,destid)
    if get[0] != 200:
        return render_template('error.html',Err=get[0],Errtext="Cannot Post Data")
    else:
        return redirect('/')
    
@app.route('/delcard/<cardid>',methods=['GET','DELETE'])
def delcard(cardid):
    get=del_card(cardid)
    if get[0] != 200:
        return render_template('error.html',Err=get[0],Errtext="Cannot Post Data")
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
