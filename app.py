from flask import (Flask, render_template, request, request_finished, make_response)
from  diaspora import  Diaspora, pyrustic_data
"""
python diaspora based not ruby :)
"""
from config import port, host
app = Flask(__name__)
@app.route("/")
def Landing():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(host=host,port=port)