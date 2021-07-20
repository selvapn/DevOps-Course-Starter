from types import GetSetDescriptorType
from flask import Flask,escape,request,render_template,redirect
from flask.helpers import url_for
from flask.wrappers import Request
from todo_app.data.session_items import _DEFAULT_ITEMS, add_item,get_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
       return redirect(url_for('addItm'))
    else:
        return render_template('index.html',items=get_items())

@app.route('/additem',methods=['GET','POST'])
def addItm():
    if request.method == "POST":
        title =request.form["todo_title"]
        add_item(title)
        return redirect('/')
    else:
        return render_template('todo_item.html')
    

if __name__ == '__main__':
    app.run()
