from flask import Flask, render_template, send_file, make_response, request
from datetime import datetime
import sys
app = Flask(__name__)

days = None
template = "trial.html"
try:
    sys.argv[2]
    if sys.argv[2] > 0:
      days = int(sys.argv[2])
except IndexError:
    template = 'index.html'

bgColor="black"

if days is not None:
  gold = False
else:
  gold = True

print(gold)

if gold is True:
  mainColor="gold"
else:
  mainColor="white"


def getTrialTime():
    if template == "trial.html":
        return (secondsInADay*int(sys.argv[2])) + time.time()
    else:
        return 0


# Pages
@app.route('/')
def index():
    return render_template('index.html', mainColor=mainColor, bgColor=bgColor)
# Pages
@app.route('/redirect')
def redirect():
    return render_template('redirect.html')

@app.route('/manifest.json')
def manifest():
    return render_template('manifest.json', mimetype='application/json')

@app.route('/sw.js')
def serviceWorker():
    response = make_response(render_template('sw.js', mimetype='text/javascript'))
    response.content_type = 'text/javascript'
    return response

@app.route('/main.js')
def mainJS():
    return render_template('main.js', mimetype='text/javascript')

@app.route('/offline.html')
def offline():
    if gold is True:
      return render_template('gold.html', clientIp=request.remote_addr, serverIp = sys.argv[1], lastUpdated = datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    else:
      return render_template('trial.html', trialend=getTrialTime(), clientIp=request.remote_addr, serverIp = sys.argv[1], lastUpdated = datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# Icons
@app.route('/favicon.ico')
def favicon():
    return send_file('icons/favicon.ico', mimetype='image/x-icon')

@app.route('/144x144.png')
def icon():
    return send_file('icons/144x144.png', mimetype='image/png')

# @app.after_request
# def add_headers(response):
#     response.headers['Cache-Control'] = 'immutable, max-age=31536000'
#     return response

app.run(host=sys.argv[1], port=80)
