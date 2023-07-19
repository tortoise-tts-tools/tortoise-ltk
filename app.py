from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from tokenizer import VoiceBpeTokenizer

# Create an instance of the Flask app
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret_key'

# Create an instance of the SocketIO extension
socketio = SocketIO(app)

# Create an instance of the tokenizer
tokenizer = VoiceBpeTokenizer()

# Route to render the HTML page
@app.route('/')
def index():
    return '''
    <html>
    <head>
        <title>Token Count</title>
        <script src="https://cdn.socket.io/4.3.2/socket.io.min.js"></script>
        <script type="text/javascript">
            var socket = io();
            socket.on('token_count', function(data) {
                document.getElementById('token-count').innerHTML = 'Token Count: ' + data.token_count;
                document.getElementById('input-text').style.color = data.text_color;
            });
            function onInputChange() {
                var inputText = document.getElementById('input-text').value;
                socket.emit('text_change', { 'input_text': inputText });
            }
        </script>
    </head>
    <body>
        <textarea id="input-text" style="height:400px;width:100%;resize:vertical" oninput="onInputChange()"></textarea>
        <p id="token-count">Token Count: 0</p>
    </body>
    </html>
    '''

# Event handler for text change
@socketio.on('text_change')
def handle_text_change(data):
    input_text = data['input_text'].strip()
    tokens = tokenizer.encode(input_text)
    token_count = len(tokens)

    # Determine text color
    text_color = 'black'
    if len(input_text) >= 400:
        text_color = 'red'
    elif len(input_text) > 350:
        text_color = 'yellow'

    # Emit the token count and text color to all clients
    emit('token_count', {'token_count': token_count, 'text_color': text_color}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
