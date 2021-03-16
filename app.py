from flask import Flask, Response, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///chat.db'
app.config['SECRET_KEY']='mysecret'
db = SQLAlchemy(app)
socketio=SocketIO(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@socketio.on('send_message')
def handle_message(data, methods=['GET','POST']):
    socketio.emit('rec_msg', data)


if __name__ == '__main__':
    socketio.run(app,debug=True)

