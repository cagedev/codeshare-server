#!/usr/bin/env python
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, disconnect

async_mode = None

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins='*')

state = None


# HTTP Routes
@app.route('/client')
def client():
    """Checks authorization and returns broadcaster template"""
    return render_template('client.html', async_mode=socketio.async_mode)


@app.route('/viewer')
def viewer():
    """Returns viewer (unable to broadcast) template"""
    return render_template('viewer.html', async_mode=socketio.async_mode)


# SocketIO Routes
@socketio.on('connect', namespace='')
def ws_connect():
    global state
    print('Connected', request.sid)
    if state:
        emit('code_update', state, room=request.sid)
    emit('message', {'data': 'Connected', 'sid': request.sid}, broadcast=True)


@socketio.on('disconnect', namespace='')
def ws_disconnect():
    print('Disconnected', request.sid)
    emit('message', {'data': 'Disconnected',
                     'sid': request.sid}, broadcast=True)


@socketio.on('code_update', namespace='')
def update_code(message):
    global state
    state = message
    emit('code_update', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
