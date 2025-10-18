
# ChatSync minimal Flask stub. For realtime features, extend with Flask-SocketIO.
from flask import Flask
app = Flask(__name__)
@app.route('/')
def i(): return 'ChatSync stub - implement with Flask-SocketIO for realtime'
if __name__ == '__main__': app.run(debug=True)
