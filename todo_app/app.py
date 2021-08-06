from flask import Flask,escape,request,render_template,redirect
from flask.helpers import url_for
from flask.wrappers import Response
import requests
from todo_app.flask_config import Config
from todo_app.data.session_items import add_card, getDoneCard,getTodoCard,move_card,getDoingCard


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form['card'] == "AddCard":
            return redirect(url_for('addCard'))
        if request.form['card'] == "MoveCard":
            return redirect(url_for('moveCard'))
    else:
        return render_template('index.html',items=getTodoCard(),doingitems=getDoingCard(),doneitems=getDoneCard())

@app.route('/addcard',methods=['GET','POST'])
def addCard():
    if request.method == "POST":
        title =request.form["trello_title"]
        desc=request.form["trello_desc"]
        add_card(title,desc)
        return redirect('/')
    else:
        return render_template('add_card.html')

@app.route('/movecard',methods=['GET','POST'])
def moveCard():
    if request.method == "POST":
        cardid =request.form["trello_id"]
        destid=request.form["movecard"]
        get=move_card(cardid,destid)
        if get[0] != 200:
            return render_template('error.html',Err=get[0],Errtext="Cannot Post Data")
        else:
            return redirect('/')
    else:
        return render_template('move_card.html',items=getTodoCard(),doingitems=getDoingCard(),doneitems=getDoneCard())

if __name__ == '__main__':
    app.run()
