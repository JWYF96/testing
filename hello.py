from flask import Flask
import time
import redis

app = Flask(__name__)


@app.route("/<x>")
def hello_world(x):

    r = redis.Redis(host='localhost', port=6379, db=0)

    if r.exists(x) == 1:
        return r.get(x)
    else:
        result = int(x)+1
        time.sleep(5)
        r.set(x, result, ex=30)
        return fresult

