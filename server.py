import paho.mqtt.publish as publish
from flask import *
app = Flask(__name__)

tran_data = ["enter", "up", "down", "left", "right", "f", "esc"]

@app.route("/")
def index():
    return "<h1 style='text-align:center'>It's Work</h1>"

@app.route("/post", methods=['POST'])
def post():
    data = request.form['data']
    channelid = request.form['channel']
    if data in tran_data:
        print("action: %s in channel: %s"%(data, channelid))
        publish.single(channelid, data, qos=0, hostname=<hostname>)
    else:
        pass
    return "post complate!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
