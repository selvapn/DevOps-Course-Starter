from flask import Flask,escape,request,render_template,redirect
from flask.helpers import url_for
from flask.wrappers import Response
import requests
from todo_app.flask_config import Config
from todo_app.data.session_items import add_card,move_card, getCards #, getDoneCard,getTodoCard,getDoingCard
import os

app = Flask(__name__)
app.config.from_object(Config)
todoCards=getCards(os.environ.get('TRELLO_TODO'))
doingCards=getCards(os.environ.get('TRELLO_DOING'))
doneCards=getCards(os.environ.get('TRELLO_DONE'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form['card'] == "AddCard":
            return redirect(url_for('addCard'))
        if request.form['card'] == "MoveCard":
            return redirect(url_for('moveCard'))
    else:
        return render_template('index.html',items=todoCards.getDoingCards(),doingitems=doingCards.getDoingCards(),doneitems=doneCards.getDoneCards())

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
    print("testing")
#    if request.method == "POST":
#        cardid =request.form["trello_id"]
#        destid=request.form["movecard"]
    print("card id ")
    get=move_card(cardid,destid)
    if get[0] != 200:
        return render_template('error.html',Err=get[0],Errtext="Cannot Post Data")
    else:
        return redirect('/')
    #else:

    return render_template('index.html',items=todoCards.getDoingCards(),doingitems=doingCards.getDoingCards(),doneitems=doneCards.getDoneCards())

    
if __name__ == '__main__':
    app.run()
