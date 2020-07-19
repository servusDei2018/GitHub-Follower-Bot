import flask
import threading

app = flask.Flask('Github Follower Bot')

# Flask configuration
host = {
  'ip': '0.0.0.0',
  'port': 3000
}

@app.route('/', methods=['GET','POST'])
def home():
  return 'pong'

def start():
  app.run(host=host['ip'], port=host['port'])

# thread = threading.Thread(target=start)
# thread.start()
